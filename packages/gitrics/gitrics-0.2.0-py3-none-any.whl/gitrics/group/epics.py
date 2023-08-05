import datetime

import networkx as nx

from gitrics import configuration
from gitrics.epic import gitricsEpic
from gitrics.utilities import ci_lower_bound

from glapi.group import GitlabGroup

class gitricsGroupEpics(GitlabGroup):
    """
    gitricsGroupEpics is a collection of Gitlab Group Epics modified and enriched for gitrics ecosystem.
    """

    def __init__(self, group_id: str = None, group: dict = None, epics: list = None, date_start: str = None, date_end: str = None, token: str = configuration.GITLAB_TOKEN, version: str = configuration.GITLAB_API_VERSION):
        """
        Args:
            date_end (string): iso 8601 date value
            date_start (string): iso 8601 date value
            epics (list): dictionaries of GitLab Epic
            group (dictionary): key/value pair representing a GitLab Group
            group_id (string): GitLab Group id
            token (string): GitLab personal access, ci, or deploy token
            version (string): GitLab API version as base url
        """

        # initialize inheritance
        super(gitricsGroupEpics, self).__init__(
            group=group,
            id=group_id,
            token=token,
            version=version
        )

        # get epics
        if epics:
            self.epics = [gitricsEpic(epic=d) for d in epics]
        else:
            # try to get from api
            epics = self.extract_epics(
                date_end=date_end,
                date_start=date_start
            )

            # format result
            self.epics = [gitricsEpic(epic=d.epic) for d in epics] if epics else None

        # build tree
        self.nested = self.nest(self.epics) if self.epics else None

        # check for data
        if self.epics:

            # enrich epics
            for e in self.epics:

                # get notes
                e.notes = e.extract_notes()

                # generate subgraph
                sg = e.subgraph(self.nested)

                # prune lists to the nodes in the subgraph
                sg_epics = [d for d in self.epics if d.id in list(sum(list(sg.edges()), ()))]

                # update epic
                e.percent_complete = e.calculate_completion(sg_epics)
                e.nested = sg
                e.count_at_risk = len([d for d in e.issues if d.issue["health_status"] == "at_risk"]) if e.issues else 0
                e.count_on_track = len([d for d in e.issues if d.issue["health_status"] == "on_track"]) if e.issues else 0
                e.score_at_risk = ci_lower_bound(e.count_at_risk, len(e.issues)) if e.issues else 0
                e.score_on_track = ci_lower_bound(e.count_on_track, len(e.issues)) if e.issues else 0

            # generate maps of ids to scores
            atriskmap = { k.id: k.score_at_risk for k in self.epics }
            ontrackmap = { k.id: k.score_on_track for k in self.epics }

            # determine scoring ranks
            self.top_at_risk = [d for d in self.epics if d.score_at_risk == atriskmap[max(atriskmap, key=atriskmap.get)]]
            self.top_on_track = [d for d in self.epics if d.score_on_track == ontrackmap[max(ontrackmap, key=ontrackmap.get)]]

    def nest(self, epics: list) -> nx.DiGraph:
        """
        Nest epics by parent/child relationship.

        Args:
            epics: (list): GitlabEpic classes where each represents a GitLab Epic

        Returns:
            A networkx directional graph object representing a nested dictionary of parent/child relationships.
        """

        result = None

        # build tuples of parent nodes
        parents = [(d.epic["parent_id"], d.id) for d in epics if d.epic["parent_id"]]

        # build tuples of unlinked nodes
        # i.e. direct children of root
        unlinked = [(0, d.id) for d in epics if d.epic["parent_id"] is None]

        # check for nodes
        if len(parents + unlinked) > 0:

            # generate graph
            result = nx.DiGraph(parents + unlinked)

        return result
