"""
Working with Git Repositories

- Checking if there are any changes
- Get a diff of changes

Refernences:
- https://gitpython.readthedocs.io/en/stable/tutorial.html#meet-the-repo-type
- https://gitpython.readthedocs.io/en/stable/tutorial.html#initializing-a-repository
"""

from tbcp_devops.scmgmt.repository import Repository
from ._defaults import *
from ._errors import *


class Remotes(Repository):
    """"""

    def list_remote(self) -> list:
        """Return the remote values of the current repository"""
        list_remotes = []
        for remote in self.repo.remotes:
            list_remotes.append({"url": format(remote.url), "name": format(remote.name)})

        return list_remotes

    def set_new_remote_origin(self, remote_url, remote_name="origin"):
        """Create a new remote"""

        return self.repo.create_remote(remote_name, url=remote_url)

    def pull_from_remote(self):
        """Pull from remote repo"""

        return self.repo.remotes.origin.pull()

    def push_to_remote(self):
        """Push changes"""
        return self.repo.remotes.origin.push()

    def delete_remote(self, remote_name="origin"):
        """Delete a remote"""
        # Reference a remote by its name as part of the object
        # print(f'Remote name: {repo.remotes.origin.name}')
        # print(f'Remote URL: {repo.remotes.origin.url}')

        return self.repo.delete_remote(remote_name)
