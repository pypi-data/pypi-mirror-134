from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
from ._defaults import *


def create_dataset(commits: list):
    formated_commits = []
    list_of_dates = []

    for commit in commits:
        commited_date = datetime.utcfromtimestamp(commit["committed_date"]).strftime("%Y-%m-%d")
        list_of_dates.append(commited_date)
        list_of_dates = list(dict.fromkeys(list_of_dates))

    for day in list_of_dates:
        formated_commits.append({"date": day, "added": [], "fixed": [], "changed": [], "maintained": []})

    for day in formated_commits:

        for commit in commits:
            commited_date = datetime.utcfromtimestamp(commit["committed_date"]).strftime("%Y-%m-%d")
            type_of = str(commit["message"]["header"]["type"]).upper()
            scope = str(commit["message"]["header"]["scope"])
            description = str(commit["message"]["header"]["description"])
            breaking = str(commit["message"]["header"]["breaking"])

            if commited_date == day["date"]:

                if type_of.lower() in DEF_COMMIT_TYPES_ADDED:
                    day["added"].append(
                        {"type": type_of, "scope": scope, "description": description, "breaking": breaking}
                    )
                elif type_of.lower() in DEF_COMMIT_TYPES_FIXED:
                    day["fixed"].append(
                        {"type": type_of, "scope": scope, "description": description, "breaking": breaking}
                    )
                elif type_of.lower() in DEF_COMMIT_TYPES_CHANGED:
                    day["changed"].append(
                        {"type": type_of, "scope": scope, "description": description, "breaking": breaking}
                    )
                elif type_of.lower() in DEF_COMMIT_TYPES_MAINTAINED:
                    day["maintained"].append(
                        {"type": type_of, "scope": scope, "description": description, "breaking": breaking}
                    )

    return formated_commits


def create_changelog(dataset: list):
    env = Environment(loader=FileSystemLoader("tbcp_devops/pkgmgmt/templates"), autoescape=select_autoescape(["md"]))

    template = env.get_template("CHANGELOG.j2")
    output_from_parsed_template = template.render(days=dataset)

    with open("CHANGELOG", "w") as fh:
        fh.write(output_from_parsed_template)
