""""""
import semver
from ..scmgmt._defaults import *
from .files_folders import *
from tbcp_devops.scmgmt.commits import Commits


def bump_version_from_package(pkg_file: str, pkg_tool: str, repo_dir=DEF_REPO_PATH) -> str:

    version = get_version_from_toml(file_path=pkg_file, package=pkg_tool)
    version = semver.VersionInfo.parse(version)

    repo = Commits(repo_dir)
    commit = repo.get_recent_commit()
    versioning = str(commit["message"]["header"]["versioning"])

    if versioning.lower() == "major":
        new_version = version.bump_major()
    elif versioning.lower() == "minor":
        new_version = version.bump_minor()
    elif versioning.lower() == "patch":
        new_version = version.bump_patch()

    return new_version
