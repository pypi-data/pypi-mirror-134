"""
Working with Git Branches

- Listing branches
- Creating branches
- Switching branches

Refernences:
- https://gitpython.readthedocs.io/en/stable/tutorial.html#switching-branches
"""

from .repository import Repository


class Branches(Repository):
    """Inherits the self.repo instance"""

    def get_branch(self) -> str:
        """return the current active git branch of the repository"""

        return str(self.repo.active_branch)

    def list_branches(self) -> list:
        """return a list of all available git branches of the repository"""

        list_branches = []
        for branch in self.repo.branches:
            list_branches.append(str(branch))

        return list_branches

    def is_branch(self, branch) -> bool:
        """checks if the specified branch name is an existing branch in the repository"""

        return bool(branch in self.repo.branches)

    def create_branch(self, branch_name: str) -> None:
        """creates a new git branch, optionally allows checkout"""

        self.repo.create_head(branch_name)

    def checkout_branch(self, branch_name: str) -> None:
        """"""
        self.repo.git.checkout(branch_name)
