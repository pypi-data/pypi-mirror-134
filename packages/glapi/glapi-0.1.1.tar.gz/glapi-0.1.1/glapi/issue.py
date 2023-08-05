from glapi import configuration
from glapi.connection import GitlabConnection

class GitlabIssue:
    """
    GitlabIssue is a GitLab Issue.
    """

    def __init__(self, id: str = None, issue: dict = None, token :str = configuration.GITLAB_TOKEN, version: str = configuration.GITLAB_API_VERSION):
        """
        Args:
            id (string): GitLab Issue id
            issue (dict): key/values representing a Gitlab Issue
            token (string): GitLab personal access or deploy token
            version (string): GitLab API version as base url
        """
        self.connection = GitlabConnection(
            token=token,
            version=version
        )
        self.issue = issue if issue else self.connection.query("issues/%s" % self.id)["data"]
        self.id = self.issue["id"] if self.issue else None

    def extract_notes(self) -> list:
        """
        Extract issue-specific note data (comments).

        Returns:
            A list of dictionaries where each represents a GtiLab Note.
        """

        result = None

        # check connection params
        if self.id and self.connection.token and self.connection.version:

            # query api
            result = self.connection.paginate(
                endpoint="issues/%s/notes" % self.id
            )

        return result
