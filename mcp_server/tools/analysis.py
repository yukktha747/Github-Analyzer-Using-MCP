from services.github_service import GitHubService

def analyze_profile(username: str):
    """
    Analyze GitHub profile.
    """

    return GitHubService.analyze_profile(username)
