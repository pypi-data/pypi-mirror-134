"""
Helps to search for files and directories
"""
import os
import toml
import json


def read_gitignore(dir_path="./"):
    """List all files and directories in the given .gititnore file"""
    file_lines = []

    with open(f"{dir_path}.gitignore", encoding="UTF-8") as ignore_file:
        lines = ignore_file.readlines()
        for line in lines:
            if not line.startswith("#"):
                line = str(line).rstrip("\n")
                file_lines.append(line)

    return file_lines


def list_folder(dir_path="./"):
    """List all files and direcotires in the given path"""

    ignored_lists = [".git", "tests", "test", "env", ".env", "venv", ".venv"] + read_gitignore()
    matches = []
    extensions = []
    for element in os.listdir(dir_path):
        if element not in ignored_lists and not element.startswith("."):
            matches.append(element)
            ext = element.split(".")
            if ext[-1] != element:
                extensions.append(ext[-1])

    matches = list(dict.fromkeys(matches))
    extensions = list(dict.fromkeys(extensions))

    return {"matches": matches, "extensions": extensions}


def get_version_from_toml(file_path: str, package: str) -> str:
    toml_file = toml.load(file_path)

    if package.lower() == "poetry":
        version = toml_file["tool"]["poetry"]["version"]
    else:
        version = toml_file["version"]

    return version


def get_version_from_json(file_path: str, package: str) -> str:
    f = open(file_path)
    json_file = json.load(f)

    if package.lower() == "npm":
        version = json_file["version"]
    else:
        version = json_file["version"]

    f.close()

    return version
