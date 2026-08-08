from services.github_service import GitHubService


def github_profile(username: str):

    """
    Fetch GitHub profile information.
    """

    return GitHubService.get_profile(username)