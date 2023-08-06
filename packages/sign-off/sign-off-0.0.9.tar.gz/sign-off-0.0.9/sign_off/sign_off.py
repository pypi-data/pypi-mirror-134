"""Pre-commit to add a signature line to commit messages."""

import argparse
import subprocess
import sys


def _get_git_vars() -> dict:
    git_vars_lines = (
        subprocess.check_output(["git", "var", "-l"], universal_newlines=True)
        .strip()
        .splitlines()
    )

    git_vars = {}
    for line in git_vars_lines:
        parts = line.split("=")
        git_vars[parts[0]] = "=".join(parts[1:])

    return git_vars


def _replace_vars_in_template(template: str) -> str:
    for key, value in _get_git_vars().items():
        if f"<{key}>" in template:
            if key in ["GIT_AUTHOR_IDENT", "GIT_COMMITER_IDENT"]:
                value = _strip_timestamp(value)
            template = template.replace(f"<{key}>", value)
    return template


def _strip_timestamp(text: str) -> str:
    """Remove timestamp that are added to end of some git vars.

    I'm not sure how fixed the format is (w/o timezone etc.), that's why this logic
    is a bit more complicated
    """
    parts = text.split()
    for _ in range(2):
        if parts[-1].lstrip("+-").isdigit():
            parts = parts[:-1]
    return " ".join(parts)


def _get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("commit_msg_filepath")
    parser.add_argument(
        "-t",
        "--template",
        default="\n\nSigned-off-by: <GIT_AUTHOR_IDENT>",
        help="Text to append as signature. Possible placeholders are all variables "
        + "shown by `git var -l`. (Timestamps are getting stripped.)",
    )
    parser.add_argument(
        "-s",
        "--skip-containing",
        default="Signed-off-by:",
        help="Do not add a signature, if the commit message contains this text. "
        + "Useful e.g. to avoid duplicate entries. "
        + 'Use empty string "" to always add the signature.',
    )
    return parser


def main(args=None):
    """Run logic to append signature to git commit message.

    (`args` are used for automated testing only.)
    """
    args = args or vars(_get_argparser().parse_args())
    print(args)
    with open(args["commit_msg_filepath"], "r+", encoding="utf-8") as commit_msg_file:
        msg = commit_msg_file.read().rstrip()
        if (
            args["skip_containing"]
            and _replace_vars_in_template(args["skip_containing"]) in msg
        ):
            return

        msg += _replace_vars_in_template(args["template"])
        commit_msg_file.seek(0, 0)
        commit_msg_file.write(msg)


if __name__ == "__main__":
    sys.exit(main())
