import datetime

from collections import Counter

import networkx as nx

from glapi.group import GitlabGroup
from glapi.user import GitlabUser

from gitrics import configuration
from gitrics.group.epics import gitricsGroupEpics
from gitrics.group.issues import gitricsGroupIssues

class gitricsGroup(GitlabGroup):
    """
    gitricsGroup is an abstraction of the GitLab Group data object specific to the requirements of the gitrics ecosystem.
    """

    def __init__(self, id: str = None, group: dict = None, epics: list = None, issues: list = None, users: list = None, date_start: str = None, date_end: str = None, token: str = configuration.GITLAB_TOKEN, version: str = configuration.GITLAB_API_VERSION):
        """
        Args:
            date_end (string): iso 8601 date value
            date_start (string): iso 8601 date value
            group (dict): key/values representing a Gitlab Group
            epics (list): dictionaries of GitLab Epic
            id (string): GitLab Group id
            issues (list): dictionaries of GitLab Issue
            token (string): GitLab personal access or deploy token
            users (list): dictionaries of GitLab User
            version (string): GitLab API version as base url
        """

        # initialize inheritance
        super(gitricsGroup, self).__init__(
            group=group,
            id=id,
            token=token,
            version=version
        )

        # initialize epics
        self.epics = gitricsGroupEpics(
            group_id=id,
            group=group,
            epics=epics,
            date_start=date_start,
            date_end=date_end,
            token=token,
            version=version
        )

        # update class
        if self.epics.epics:
            for e in self.epics.epics:
                e.gitlab_type = "epic"

        # initialize issues
        self.issues = gitricsGroupIssues(
            group_id=id,
            group=group,
            date_start=date_start,
            date_end=date_end,
            issues=issues,
            token=token,
            version=version
        )

        # update class
        if self.issues.issues:
            for i in self.issues.issues:
                i.gitlab_type = "issue"

        # get users
        self.users = self.extract_users()

    def determine_status(self, item: dict) -> str:
        """
        Determine human-readable opinionated status based on start/end/due dates and state.

        Args:
            item (dictionary): key/value pairs representing a GitLab Epic or Issue

        Returns:
            A string representing a status related to start/end time.
        """

        result = "ongoing"
        now = datetime.datetime.now()

        # opened
        if item["state"] == "opened":

            # ending date
            if "end_date" in item or "due_date" in item:

                # normalize between data types
                edate = item["end_date"] if "end_date" in item else item["due_date"]

                # end/due date in the past
                if edate and datetime.datetime.strptime(edate, configuration.DATE_ISO_8601) < now:
                    result = "past due"

            # starting date
            if "start_date" in item or "due_date" in item:

                # normalize between data types
                sdate = item["start_date"] if "start_date" in item else item["due_date"]

                # start date in the future
                if sdate and datetime.datetime.strptime(sdate, configuration.DATE_ISO_8601) > now:
                    result = "upcoming"

        # closed
        else:
            result = "complete"

        return result

    def determine_ownership(self, item) -> list:
        """
        Determine opinionated ownership based on formal assignment via GitLab or highest note (comments) count.

        Args:
            item (enum): gitricsEpic || GitlabIssue

        Returns:
            A list of dictionaries where each is a GitlabUser.
        """

        result = None
        ids = list()
        subitem = item.epic if hasattr(item, "epic") else item.issue

        # check for notes
        if item.notes:

            # assign ownership by participation
            ids = [x[0] for x in Counter(d["author"]["id"] for d in item.notes).most_common(3)]

        # check for assignees
        if "assignees" in subitem and subitem["assignees"]:

            # add as assignees
            ids = [d["id"] for d in subitem["assignees"]]

        # replace ids with full user objects
        result = [d for d in self.users if d.id in ids]

        return result

    def tabulate_nest(self, items) -> dict:
        """
        Generate tabular-formatted data under level 1 nodes.

        Args:
            items (enum): gitricsEpics || gitricsIssues

        Returns:
            A dictionary where keys represent leve-1 nodes in the graph and corresponding values are lists of dictionaries of each descendant in order of nest.
        """

        result = None

        # check for graph in object
        if items.nested:

            # determine if epics or issues
            is_epics = hasattr(items, "epics")

            # get subitems
            subitems = items.epics if is_epics else items.issues

            result = [
                [x for x in subitems if x.id == d[1]][0]
                for d in list(items.nested.edges()) if d[0] == 0
            ]

            # add descendants
            for item in result:
                item.descendants = [
                    [x for x in subitems if x.id == d][0] for d in
                    list(nx.descendants(items.nested, item.id))
                ]

        return result
