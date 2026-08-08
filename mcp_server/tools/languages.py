from services.github_service import GitHubService


def github_languages(username: str):
    """
    Get language statistics of repositories.
    """

    return GitHubService.get_language_statistics(username)