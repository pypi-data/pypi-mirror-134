import datetime

from collections import Counter

from gitrics import configuration

from gitrics.group.epics import gitricsGroupEpics
from gitrics.group.issues import gitricsGroupIssues

class gitricsGroupEpicsIssues:
    """
    gitricsGroupEpicsIssues is an abstraction of the GitLab Issue and GitLab Epic data objects specific to the requirements of the gitrics ecosystem.
    """

    def __init__(self, group_id: str = None, group: dict = None, epics: list = None, issues: list = None, date_start: str = None, date_end: str = None, token: str = configuration.GITLAB_TOKEN, version: str = configuration.GITLAB_API_VERSION):
        """
        Args:
            date_end (string): iso 8601 date value
            date_start (string): iso 8601 date value
            group (dict): key/values representing a Gitlab Group
            group_id (string): GitLab Group id
            epics (list): dictionaries of GitLab Epic
            issues (list): dictionaries of GitLab Issue
            token (string): GitLab personal access or deploy token
            version (string): GitLab API version as base url
        """

        # itialize epics
        groupEpics = gitricsGroupEpics(
            group_id=group_id,
            group=group,
            epics=epics,
            date_start=date_start,
            date_end=date_end,
            token=token,
            version=version
        )

        # extract group epics
        self.epics = groupEpics.epics
        self.epicsNested = groupEpics.nested

        # update class
        if self.epics:
            for e in self.epics:
                e.item = e.epic
                e.gitlab_type = "epic"
                delattr(e, "epic")

        # initialize issues
        groupIssues = gitricsGroupIssues(
            group_id=group_id,
            group=group,
            date_start=date_start,
            date_end=date_end,
            issues=issues,
            token=token,
            version=version
        )

        # extract group issues
        self.issues = groupIssues.issues
        self.issuesNested = groupIssues.nested

        # update class
        if self.issues:
            for i in self.issues:
                i.item = i.issue
                i.gitlab_type = "issue"
                delattr(i, "issue")

        # put all items together
        items = list()
        if self.epics: items = self.epics
        if self.issues: items = items + self.issues

        # dump epics and issue keys so items is always used
        delattr(self, "epics")
        delattr(self, "issues")

        # enrich items
        self.items = self.enrich(items)

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

    def enrich(self, items: list) -> list:
        """
        Enrich items for gitrics ecosystem.

        Args:
            items (list): classes of GitlabEpic or GitlabIssue

        Returns:
            A list of classes of GitlabEpic or GitlabIssue representing a GitLab Epic or Issue, respectively.
        """

        result = items

        # loop through items
        for item in items:

            # determine status based on timing
            item.status = self.determine_status(item.item)
            item.ownership = None

            # check for notes
            if item.notes:

                # assign ownership by participation
                item.ownership = [x[0] for x in Counter(d["author"]["id"] for d in item.notes).most_common(3)]

            # check for assignees
            if "assignees" in item.item and item.item["assignees"]:

                # add as assignees
                item.ownership = [d["id"] for d in item.item["assignees"]]

        return result
