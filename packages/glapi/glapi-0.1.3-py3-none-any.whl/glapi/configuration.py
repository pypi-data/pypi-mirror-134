import os

# GITLAB
GITLAB_API_VERSION = os.environ["GITLAB_API_VERSION"] if "GITLAB_API_VERSION" in os.environ else "https://gitlab.com/api/v4"
GITLAB_PAGINATION_PER_PAGE = int(os.environ["GITLAB_PAGINATION_PER_PAGE"]) if "GITLAB_PAGINATION_PER_PAGE" in os.environ else 100
GITLAB_PROJECT_SIMPLE = os.environ["GITLAB_PROJECT_SIMPLE"] if "GITLAB_PROJECT_SIMPLE" in os.environ else True
GITLAB_PROJECT_PERSONAL_ONLY = os.environ["GITLAB_PROJECT_PERSONAL_ONLY"] if "GITLAB_PROJECT_PERSONAL_ONLY" in os.environ else False
GITLAB_PROJECT_USER_ACCESS = int(os.environ["GITLAB_PROJECT_USER_ACCESS"]) if "GITLAB_PROJECT_USER_ACCESS" in os.environ else 30
GITLAB_PROJECT_USER_MEMBERSHIP = os.environ["GITLAB_PROJECT_USER_MEMBERSHIP"] if "GITLAB_PROJECT_USER_MEMBERSHIP" in os.environ else False
GITLAB_PROJECT_VISIBILITY = os.environ["GITLAB_PROJECT_VISIBILITY"] if "GITLAB_PROJECT_VISIBILITY" in os.environ else "public"
GITLAB_TOKEN = os.environ["GITLAB_TOKEN"] if "GITLAB_TOKEN" in os.environ else None

# TIME
DATE_ISO_8601 = "%Y-%m-%d"
