"""
Working with Git Commits object

Reference:
- https://gitpython.readthedocs.io/en/stable/tutorial.html#the-commit-object
- https://gitpython.readthedocs.io/en/stable/tutorial.html#understanding-objects
"""

from datetime import datetime
from operator import itemgetter
from ._defaults import *
from .utils.commits import *
from .branches import Branches


class Commits(Branches):
    """Inherits the self.repo instance"""

    def commit(
        self,
        type_of: str,
        description: str,
        breaking=False,
        breaking_msg="",
        scope="",
        bodies=[""],
        footer="",
    ) -> None:
        """"""

        message = message_builder(
            type_of=type_of,
            description=description,
            breaking=breaking,
            breaking_msg=breaking_msg,
            scope=scope,
            bodies=bodies,
            footer=footer,
        )
        self.repo.git.commit(m=message)

    def get_recent_commit(self) -> dict:
        """Return the latest commit of the repository"""

        return commit_converter(self.repo.head.commit)

    def get_commits(self, branch="--all", max_count=-1, since="", skip=0) -> list:
        """"""

        since = "" if since else False
        list_of_commits = []

        for commit in self.repo.iter_commits(branch, max_count=max_count, since=since, skip=skip):
            list_of_commits.append(commit_converter(commit))

        return list_of_commits

    def get_days_committed(self):

        dates = []
        all_commits = self.get_commits()

        for commit in all_commits:
            committed_date = commit["committed_date"]
            dates.append(datetime.utcfromtimestamp(committed_date).strftime("%Y-%m-%d"))

        dates = list(dict.fromkeys(dates))

        return dates

    def sort_commits(self, commits=[""], by="date"):
        return sorted(commits, key=itemgetter(by))

    def get_commit_by_hash(self, hexsha: str):
        """"""

        commit_of_hexsha = {""}
        for commit in self.get_commits():
            if hexsha == commit["hexsha"]:
                commit_of_hexsha = commit

        return commit_of_hexsha
