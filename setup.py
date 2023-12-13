"""Manage package and distribution."""
import subprocess
from typing import List

from setuptools import setup


def find_version() -> str:
    """Parse rt version based on the git tag.

    :return: Version of the package.
    :rtype: str
    """
    try:
        cmd: List[str] = ["git", "describe", "--tags", "--always", "HEAD"]
        gitversion: str = subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode().strip()
        if all(char.isdigit() or char == "." for char in gitversion):
            return gitversion
        build: List[str] = gitversion.split("-")
        return f"{build[0]}.post{build[1]}"
    except IndexError:
        cmde: List[str] = ["git", "rev-list", "--count", "HEAD"]
        commits_count: str = (
            subprocess.check_output(cmde, stderr=subprocess.DEVNULL).decode().strip()
        )
        return f"0.0.dev{commits_count}"
    except subprocess.CalledProcessError:
        return "0.0.dev0"


setup(version=find_version())
