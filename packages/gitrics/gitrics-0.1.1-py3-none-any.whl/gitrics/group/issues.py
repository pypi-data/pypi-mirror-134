import datetime

import networkx as nx

from gitrics import configuration

from glapi.group import GitlabGroup
from glapi.issue import GitlabIssue

class gitricsGroupIssues(GitlabGroup):
    """
    gitricsGroupIssues is a collection of Gitlab Group Issues modified and enriched for gitrics ecosystem.
    """

    def __init__(self, group_id: str = None, group: dict = None, issues: list = None, date_start: str = None, date_end: str = None, token: str = configuration.GITLAB_TOKEN, version: str = configuration.GITLAB_API_VERSION):
        """
        Args:
            date_end (string): iso 8601 date value
            date_start (string): iso 8601 date value
            issues (list): dictionaries of GitLab Issue
            group (dictionary): key/value pair representing a GitLab Group
            group_id (string): GitLab Group id
            token (string): GitLab personal access, ci, or deploy token
            version (string): GitLab API version as base url
        """

        # initialize inheritance
        super(gitricsGroupIssues, self).__init__(
            group=group,
            id=group_id,
            token=token,
            version=version
        )

        # get issues
        if issues:
            items = [GitlabIssue(issue=d) for d in issues]
        else:
            # try to get from api
            data = self.extract_issues(
                date_end=date_end,
                date_start=date_start
            )

            # format result
            items = [GitlabIssue(issue=d.issue) for d in data] if data else None

        # check for data
        if items:

            # get notes
            for i in items:
                i.notes = i.extract_notes()

            # enrich
            self.issues = self.enrich(items)

            # build network
            self.nested = self.nest(self.issues)

        else:
            self.issues = items
            self.nested = None

        # check for issues
        if self.nested:

            # calculate degree centrality
            degreecentralitymap = nx.degree_centrality(self.nested)

            # remove root node
            degreecentralitymap.pop(0)

            # get max value
            max_block_centrality = max(degreecentralitymap, key=degreecentralitymap.get)

            # update individual issues with score
            for i in self.issues:
                i.score_degree_centrality = degreecentralitymap[i.id] if i.id in degreecentralitymap else 0

            # get any nodes with max value
            # sort by nest level which assumes that nodes with an even score that the higher in the tree the more of a blocker it is
            self.top_blockers = sorted([
                d for d in self.issues
                if d.score_degree_centrality > 0 and
                degreecentralitymap[d.id] == degreecentralitymap[max_block_centrality]
            ], key=lambda d: nx.descendants(self.nested, d.id), reverse=True)

        else:
            self.top_blockers = None

    def enrich(self, issues: list) -> list:
        """
        Enrich with data for gitrics ecosystem.

        Args:
            issues (list): GitlabIssue classes where each represents a GitLab Issue

        Returns:
            A list of dictionaries where each represents an enriched GitLab Issue.
        """

        if issues:

            # loop through issues
            for issue in issues:

                # get links
                links = self.connection.query(
                    endpoint="projects/%s/issues/%s/links" % (
                        issue.issue["project_id"],
                        issue.issue["iid"]
                    )
                )["data"]

                # check if issue has links
                if len(links) > 0:

                    # update self
                    issue.has_links = True

                    # loop through links
                    for link in links:

                        # check attribute
                        if not hasattr(issue, link["link_type"]): setattr(issue, link["link_type"], list())

                        # add id to issue link type attribute
                        ids = getattr(issue, link["link_type"])
                        ids.append((link["id"], link["link_updated_at"]))

                        # set attribute
                        setattr(issue, link["link_type"], ids)

                else:

                    # update self
                    issue.has_links = False

        return issues

    def nest(self, issues: list) -> dict:
        """
        Nest issues by parent/child link relationship (relates_to, blocks, is_blocked_by).

        Args:
            issues: (list): GitlabIssue classes where each represents a GitLab Issue

        Returns:
            A directional network representing the link relationship.
        """

        result = None

        # build tuples for blocking nodes
        blockers = [
            x for y in [
                [(d.id, i[0]) for i in d.blocks]
                for d in issues
                if hasattr(d, "blocks")
            ] for x in y
        ]

        # build tuples of blockers which are unblocked themselves
        # i.e. these nodes are direct children of the root
        unblocked_blockers = [
            (0, d.id) for d in issues
            if not hasattr(d, "is_blocked_by") and hasattr(d, "blocks")
        ]

        # build tuples for complete unlinked issues
        # i.e. nodes are direct children of the root
        unlinked = [(0, d.id) for d in issues if not d.has_links]

        # combine list
        links = blockers + unblocked_blockers + unlinked

        # check for links
        if len(links) > 0:

            # generate graph
            result = nx.DiGraph(links)

        return result
