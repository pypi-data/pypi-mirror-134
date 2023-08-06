import logging

from .md_functions import load_markdown_files
from .api_calls import get_request, post_request, verify_authentication

logger = logging.getLogger("ghproject")


class GitHubAPI:
    """Create a project board with issues in a GitHub repository

    Parameters
    ----------
    repo_name : str
        Name of the repository
    repo_owner : str
        Name of the organization or GitHub user that owns the repository
    github_token : str
        GitHub Personal Access Token

    Examples
    --------
    >>> import os
    >>> from ghproject import GitHubAPI
    >>>
    >>> # Setup arguments
    >>> repo_name = "my_repository"
    >>> repo_owner = "username" # Github user name or organization name
    >>> token = os.environ["GITHUB_TOKEN"]
    >>> path_issues = "./md_files"
    >>> project_name = "My project"
    >>>
    >>> # Instantiate repo and call functions
    >>> repo = GitHubAPI(repo_name, repo_owner, token)
    >>> repo.load_markdown_files(path_issues)
    >>> repo.push_project(project_name)
    >>> repo.push_issues()
    >>> repo.add_issues_to_project(project_name)

    """

    def __init__(
        self,
        repo_name: str,
        repo_owner: str,
        github_token: str,
    ):
        """Initialize GitHubAPI parameters."""
        self.repo_name = repo_name
        self.repo_owner = repo_owner
        self.headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json",
        }
        self.base_url = (
            f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}"
        )
        verify_authentication(self.base_url, self.headers)

    def get_issues(self):
        """Get issues from GitHub repository"""
        url = f"{self.base_url}/issues"
        r = get_request(url, self.headers)
        self.issues = {issue["title"]: issue["id"] for issue in r}

    def get_projects(self):
        """Get projects from GitHub repository"""
        url = f"{self.base_url}/projects"
        r = get_request(url, self.headers)
        self.projects = {project["name"]: project["id"] for project in r}

    def load_markdown_files(self, path: str):
        """Import markdown files for uploading as issues.
        The first line of the markdown file will become the issue title (can be preceeded by a #), while
        the remainder of the markdown file will be converted into the issue body.

        Parameters
        ----------
        path : str
            Path to local directory with markdown files
        """
        self.markdown_issues = load_markdown_files(path=path)

    def push_project(
        self, project_name: str, columns: list = ["To do", "In progress", "Done"]
    ):
        """Push project to GitHub repository

        Parameters
        ----------
        project_name : str
            Name of the project
        columns : list, optional
            List of column names to be created in the project board, defaults to ["To do", "In progress", "Done"]

        """
        url = f"{self.base_url}/projects"

        # Check if project exists on GitHub
        self.get_projects()
        if bool(self.projects):
            if project_name in self.projects.keys():
                logger.warning(f"Project '{project_name}' already exists")
                return

        data = {"name": project_name}
        r = post_request(url, data, self.headers)
        id_project = r["id"]

        # Add columns to project board
        url = f"https://api.github.com/projects/{id_project}/columns"
        for column in columns:
            data = {"name": column}
            r = post_request(url, data, self.headers)
            if column == columns[0]:
                self.id_column = r["id"]
        logger.info(f"Created project {project_name} with columns {columns}")

    def push_issues(self):
        """Upload issues to GitHub repository

        Parameters
        ----------
        labels : list, optional
            List of issue labels, by default ["documentation"]
        """
        url = f"{self.base_url}/import/issues"

        # Load issue title, labels, and content
        for issue in self.markdown_issues:
            data = {
                "issue": {
                    "title": issue["title"],
                    "body": issue.content,
                    "closed": False,
                    "labels": issue["labels"],
                }
            }

            # Check if issue exists
            self.get_issues()
            if issue["title"] not in self.issues.keys():
                post_request(url, data, self.headers)
                logger.info(f"Issue '{issue['title']}' uploaded")
            else:
                logger.warning(f"Issue '{issue['title']}' already exists")

    def add_issues_to_project(self, project_name: str, column_name: str = None):
        """Add uploaded issues to project board

        Parameters
        ----------
        project_name : str
            name of the project board to add the issues to
        column_name : str, optional
            name of the column to add the issues to, defaults to first column
        """
        # Get column ids
        columns = self.get_columns(project_name)
        if not column_name and columns:
            column_name = list(columns.keys())[0]

        try:
            id_column = columns[column_name]
        except KeyError:
            logger.error(
                f"Cannot find {column_name} in the columns of the project board"
            )

        url = f"https://api.github.com/projects/columns/{id_column}/cards"

        # Only move issues if all uploaded issues are present on GitHub
        self.get_issues()
        issue_list = [issue["title"] for issue in self.markdown_issues]
        if set(issue_list).issubset(self.issues.keys()):
            issue_ids = [self.issues[name] for name in issue_list]
            for id in issue_ids:
                data = {"content_type": "Issue", "content_id": id}
                post_request(url, data, self.headers)
        else:
            logger.warning(
                "Cannot find all issues on GitHub, process could be delayed. Please try again."
            )

    def get_columns(self, project_name: str):
        """Get column names and id's from a project

        Parameters
        ----------
        project_name : str
            Name of the project board

        Returns
        -------
        dict
            Dictionary with [column_name:column_id] as [key:value]
        """
        self.get_projects()
        try:
            project_id = self.projects[project_name]
            url = f"https://api.github.com/projects/{project_id}/columns"
            r = get_request(url, self.headers)
            columns = {column["name"]: column["id"] for column in r}
            logger.info(
                f"Successfully retrieved column(s) {columns} from project '{project_name}'"
            )
            return columns
        except KeyError:
            logger.error(f"Cannot find project {project_name}")
            return None
