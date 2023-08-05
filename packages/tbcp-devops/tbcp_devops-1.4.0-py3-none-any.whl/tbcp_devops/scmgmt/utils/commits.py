import re
from typing import Dict
from .._defaults import *


def get_header(row_header: str):

    if ":" in row_header:
        header_split = row_header.split(":")
        header_left = header_split[0].lstrip().rstrip()

        breaking = bool("!" in header_left)

        description = header_split[-1].lstrip().rstrip()

        if "(" in header_left and ")" in header_left:
            scope = re.search("\(+[a-zA-Z 0-9]*\)+", header_left)
            scope = scope.group().replace("(", "").replace(")", "")

            type_of = header_left.replace("(" + scope + ")", "")
        else:
            scope = ""

            type_of = header_left
    else:
        type_of = "chore"
        scope = ""
        breaking = False
        description = row_header

    versioning = get_type_of_commit(type_of=type_of, breaking=breaking)

    return {"type": type_of, "scope": scope, "description": description, "breaking": breaking, "versioning": versioning}


def get_footer(row_footer: str):

    breaking = bool("BREAKING" in row_footer)

    return {"description": row_footer, "breaking": breaking}


def get_body(row_body: str):

    breaking = bool("BREAKING" in row_body)

    return {"description": row_body, "breaking": breaking}


def message_parser(message: str) -> str:

    row_of_commit = message.lstrip().rstrip().split("\n\n")
    if len(row_of_commit) >= 1:
        header = get_header(row_of_commit[0])
        row_of_commit.remove(row_of_commit[0])
        if row_of_commit:
            footer = get_footer(row_of_commit[-1])
            row_of_commit.remove(row_of_commit[-1])

            body = get_body(row_of_commit)

            if row_of_commit:
                return {"header": header, "body": body, "footer": footer, "text": message}

            return {"header": header, "footer": footer, "text": message}
        else:
            return {"header": header, "text": message}


def commit_converter(commit):
    """Convert given Commit Instance in structered Object"""
    return {
        "hexsha": str(commit.hexsha),
        "summary": str(commit.summary),
        "message": message_parser(str(commit.message)),
        "parents": str(commit.parents),
        "author": {"name": str(commit.author.name), "email": str(commit.author.email)},
        "committer": {
            "name": str(commit.committer.name),
            "email": str(commit.committer.email),
        },
        "authored_datetime": str(commit.authored_datetime),
        "authored_date": int(commit.authored_date),
        "committed_date": int(commit.committed_date),
        "count": int(commit.count()),
        "size": int(commit.size),
    }


def message_builder(type_of: str, description: str, breaking=False, breaking_msg="", scope="", bodies=[""], footer=""):
    """"""
    # Commits MUST be prefixed with a type, which consists of a noun, feat, fix, etc.,
    # followed by the OPTIONAL scope,
    # OPTIONAL !, and REQUIRED terminal colon and space.
    #
    # Breaking changes MUST be indicated in the type/scope prefix of a commit, or as an entry in the footer.
    #
    # If included as a footer, a breaking change MUST consist of the uppercase text BREAKING CHANGE,
    # followed by a colon, space, and description,
    # e.g., BREAKING CHANGE: environment variables now take precedence over config files.
    breaking_sign = "!" if breaking else ""
    #
    # The type `feat` MUST be used when a commit adds a new feature to your application or library.
    # The type `fix` MUST be used when a commit represents a bug fix for your application.
    #
    # Types other than feat and fix MAY be used in your commit messages, e.g., docs: updated ref docs.
    type_of = type_of if type_of.lower() in DEF_COMMIT_TYPES else ""
    #
    # A scope MAY be provided after a type.
    # A scope MUST consist of a noun describing a section of the codebase surrounded by parenthesis, e.g., fix(parser):
    scope = "(" + scope + ")" if scope else ""
    #
    # A description MUST immediately follow the colon and space after the type/scope prefix.
    # The description is a short summary of the code changes, e.g., fix: array parsing issue when multiple spaces were contained in string.
    #
    # A longer commit body MAY be provided after the short description, providing additional contextual information about the code changes.
    # The body MUST begin one blank line after the description.
    #
    # A commit body is free-form and MAY consist of any number of newline separated paragraphs.
    body = []
    if isinstance(bodies, str) and bodies:
        body = "\n\n" + bodies
    elif isinstance(bodies, list) and len(bodies) == 1:
        body = "\n\n" + str(bodies[0])
    elif isinstance(bodies, list) and len(bodies) > 1:
        for sep_body in bodies:
            body.append("\n\n" + sep_body + "\n")
    #
    # If included in the type/scope prefix, breaking changes MUST be indicated by a ! immediately before the :.
    # If ! is used, BREAKING CHANGE: MAY be omitted from the footer section,
    # and the commit description SHALL be used to describe the breaking change.
    breaking_msg = "\n\nBREAKING CHANGE: " if breaking and footer else ""
    #
    # One or more footers MAY be provided one blank line after the body.
    # Each footer MUST consist of a word token, followed by either a :<space> or <space># separator,
    # followed by a string value (this is inspired by the git trailer convention).
    #
    # A footer’s token MUST use - in place of whitespace characters,
    # e.g., Acked-by (this helps differentiate the footer section from a multi-paragraph body).
    # An exception is made for BREAKING CHANGE, which MAY also be used as a token.
    #
    # A footer’s value MAY contain spaces and newlines,
    # and parsing MUST terminate when the next valid footer token/separator pair is observed.
    footer_space = "\n\n" if not breaking else ""
    footer = footer_space + footer if footer else ""

    row_header = type_of + scope + breaking_sign + ": " + description
    row_body = body
    rwo_footer = breaking_msg + footer

    message = " ".join(filter(None, [row_header, row_body, rwo_footer]))

    return message


def get_type_of_commit(type_of: str, breaking: bool) -> str:
    type_of = str(type_of).lower()
    breaking = bool(breaking)

    if not breaking:
        if type_of in DEF_VERSIONING_MINOR:
            versioning = "minor"

        elif type_of in DEF_VERSIONING_PATCH:
            versioning = "patch"

        else:
            versioning = "none"
    else:
        versioning = "major"

    return versioning
