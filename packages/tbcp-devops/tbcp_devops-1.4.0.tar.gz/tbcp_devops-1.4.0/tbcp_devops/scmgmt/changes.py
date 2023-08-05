"""
Working with Git Repositories

- Checking if there are any changes
- Get a diff of changes

Refernences:
- https://gitpython.readthedocs.io/en/stable/tutorial.html#meet-the-repo-type
- https://gitpython.readthedocs.io/en/stable/tutorial.html#initializing-a-repository
"""

from tbcp_devops.scmgmt.commits import Commits
from ._defaults import *
from ._errors import *


class Changes(Commits):
    """"""

    def stage_files(self, list_files="all") -> None:
        """"""
        if list_files == "all":
            self.repo.git.add(all=True)
        elif isinstance(list_files, list) and list_files != [""]:
            self.repo.git.add(list_files)

    def has_changed_files(self) -> bool:
        """Return True if the repository has changed files"""
        return bool(self.repo.is_dirty(untracked_files=True))

    def lists_changed_files(self, where="unstaged") -> bool:
        """Return True if the repository has changed files"""
        if where == "unstaged":
            return [item.a_path for item in self.repo.index.diff(None)]
        elif where == "staged":
            return [item.a_path for item in self.repo.index.diff(self.repo.head.commit)]

    def lists_untracked_files(self) -> list:
        """Provide a list of the files to stage"""
        return list(self.repo.untracked_files)

    def get_diff(self) -> str:
        """Return the difference since the last commit"""
        return self.repo.git.diff(self.repo.head.commit.tree)
