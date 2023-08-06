import os

from packaging import version

from . import _version

__version__ = _version.get_versions()["version"]


def _add_new_version_tag_to_git(shift: str = "minor"):
    major_version = version.Version(__version__).major
    minor_version = version.Version(__version__).minor

    add_tag = True
    if shift == "major":
        major_version += 1
        minor_version = 0
    elif shift == "minor":
        minor_version += 1
    else:
        add_tag = False

    if add_tag:
        git_tag_command = f"git tag v{major_version}.{minor_version+1}"
        print(git_tag_command)
        os.system(git_tag_command)
