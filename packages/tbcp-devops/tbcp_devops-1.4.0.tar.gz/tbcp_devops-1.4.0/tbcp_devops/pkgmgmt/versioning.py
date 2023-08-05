""""""
import semver


def major(version: str) -> str:
    version = semver.VersionInfo.parse(version)
    changes_major = version.bump_major()

    return changes_major


def minor(version: str) -> str:
    version = semver.VersionInfo.parse(version)
    changes_monior = version.bump_minor()

    return changes_monior


def patch(version: str) -> str:
    version = semver.VersionInfo.parse(version)
    changes_patch = version.bump_patch()

    return changes_patch


def pre(version: str) -> str:
    version = semver.VersionInfo.parse(version)
    changes_pre = version.bump_prerelease()

    return changes_pre


def build(version: str) -> str:
    version = semver.VersionInfo.parse(version)
    changes_build = version.bump_build()

    return changes_build
