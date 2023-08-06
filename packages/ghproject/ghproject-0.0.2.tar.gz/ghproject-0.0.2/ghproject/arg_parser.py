import os
import argparse


def create_parser():
    """Create a CLI argument parser

    Returns
    -------
    args
        defined arguments for CLI
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.MetavarTypeHelpFormatter,
    )

    parser.add_argument(
        "--repo", type=str, required=True, help="name of the GitHub repository"
    )
    parser.add_argument(
        "--path", type=str, required=True, help="path to the folder with markdown files"
    )
    parser.add_argument(
        "--owner",
        type=str,
        required=True,
        help="GitHub username or organization name",
    )
    parser.add_argument(
        "--project",
        default="DCC Support",
        type=str,
        help="name of the project board, default is DCC Support",
    )
    parser.add_argument(
        "--token",
        default=os.environ["GITHUB_TOKEN"],
        type=str,
        help="GitHub Personal Access Token, default is environment variable GITHUB_TOKEN",
    )
    parser.add_argument(
        "--columns",
        type=str,
        nargs="+",
        default=["To do", "In progress", "Done"],
        help="column names in project board, default is 'To do' 'In progress' 'Done' (provide without commas)",
    )
    parser.add_argument(
        "--issue_column",
        type=str,
        help="project board column to add issues to, default is first element in list columns",
    )
    parser.add_argument("--loglevel", default="WARNING", type=str, help="loglevels")

    args = parser.parse_args()

    return args
