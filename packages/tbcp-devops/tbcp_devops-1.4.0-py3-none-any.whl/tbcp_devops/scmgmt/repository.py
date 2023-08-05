"""
Working with Git Repositories

- Checking if there are any changes
- Get a diff of changes

Refernences:
- https://gitpython.readthedocs.io/en/stable/tutorial.html#meet-the-repo-type
- https://gitpython.readthedocs.io/en/stable/tutorial.html#initializing-a-repository
"""

import git
from git.refs.head import HEAD
from git.repo.base import Repo
from ._defaults import *
from ._errors import *


class Repository:
    """"""

    def __init__(self, repo_dir=DEF_REPO_PATH) -> None:
        """Gets the repository instance inherited by super()

        Default: repo_dir = './'
        """
        try:
            self.repo = git.Repo(str(repo_dir))
        except git.InvalidGitRepositoryError as error:
            print(ERR_INVALID_REPO + format(error))
            raise
        except git.GitCommandError as error:
            print(ERR_GIT_COMMAND + format(error))
            raise
        except git.GitCommandNotFound as error:
            print(ERR_GIT_COMMAND_NOT_FOUND + format(error))
            raise
        except git.GitError as error:
            print(ERR_GIT + format(error))
            raise

    def get_repo(self) -> Repo:
        return self.repo

    def init_repo(self, path: str, bare=False) -> Repo:

        Repo.init(path, bare=bare)
        new_repo = git.Repo(str(path))

        return new_repo

    def is_repo_bare(self) -> bool:
        """Return True if Repository Type is Bare"""

        return bool(self.repo.bare)

    def get_description(self) -> str:
        """Return the description of the current repository"""

        return str(self.repo.description)

    def add_description(self, description: str, top=False) -> None:
        """"""

        position = "r+" if top else "a+"
        with open(self.repo.common_dir + "/description", position) as f:
            f.write(description + "\n")

    def set_description(self, description: str, overwrite: bool) -> None:
        """"""

        if overwrite:
            with open(self.repo.common_dir + "/description", "w") as f:
                f.write(description + "\n")

    def has_separate_working_tree(self) -> bool:
        """Return boolean if the repository has a separate working tree"""

        return bool(self.repo.has_separate_working_tree())

    def get_repository_dir(self) -> str:
        """Return a list of known directories of the repository"""

        common = str(self.repo.common_dir)
        working_tree = str(self.repo.working_tree_dir)
        working_dir = str(self.repo.working_dir)
        git_repo = str(self.repo.git_dir)

        if common is working_dir or git_repo and not self.has_separate_working_tree():
            return common
        elif common is not working_tree and self.has_separate_working_tree():
            return working_tree

    # def get_alternates(self) -> list:
    #     """List Alternates"""
    #     return self.repo.alternates

    # def get_cmd_wrapper_type(self):
    #     """Provide Git Command Wrapper Type"""
    #     return format(self.repo.GitCommandWrapperType)

    def get_head(self) -> HEAD:
        """Return the head of the current repository"""
        return self.repo.head

    def pull(self) -> None:
        """"""
        self.repo.git.pull("origin", self.repo.head)

    def push(self, from_head="origin") -> None:
        self.repo.git.push("--set-upstream", from_head, self.repo.head)

    # def clone(self, remote_repo, local_path='./'):
    #     """Clone a Repository"""
    #     self.remote_repo = remote_repo
    #     self.local_path = local_path

    #     self._clone_from_url(self.remote_repo, self.local_path )
    #     self._clone_from_local(self.remote_repo, self.local_path)

    # def _clone_from_url(self, repo_url, repo_path):
    #     """Check out via HTTPS or clone via ssh (will use default keys)"""
    #     self.repo_url = repo_url
    #     self.repo_path = repo_path

    #     self.repo_instance.clone_from(self.repo_url, self.repo_path)

    # def _clone_from_local(self, repo_path, new_path):
    #     """Load existing local repo, Create a copy of the existing repo"""
    #     self.repo_path = repo_path
    #     self.new_path = new_path

    #     local_repo = self.repo_instance(self.repo_path)
    #     local_repo.clone(self.new_path)
