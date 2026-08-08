from services.github_service import GitHubService

def github_repositories(username: str):
    """
    Return all repositories.
    """
    return GitHubService.get_repositories(username)