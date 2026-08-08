import requests

from config import Config
from services.cache_service import CacheService
from utils.logger import logger

from models.github_models import (
    GitHubProfile,
    Repository,
    Analysis
)


class GitHubService:
    """
    Handles all GitHub API operations.
    """

    @staticmethod
    def _get(endpoint: str):

        cached = CacheService.get(endpoint)

        if cached:

            logger.info(
                f"Cache Hit : {endpoint}"
            )

            return cached

        logger.info(
            f"GitHub Request : {endpoint}"
        )

        response = requests.get(
            Config.BASE_URL + endpoint,
            headers=Config.HEADERS,
            timeout=Config.REQUEST_TIMEOUT
        )

        if response.status_code == 404:
            raise Exception("GitHub user not found.")

        if response.status_code == 403:
            raise Exception("GitHub API rate limit exceeded.")

        response.raise_for_status()

        data = response.json()

        CacheService.save(
            endpoint,
            data
        )

        return data

    @staticmethod
    def get_profile(username: str):

        data = GitHubService._get(
            f"/users/{username}"
        )

        return GitHubProfile(

            name=data.get("name"),

            login=data["login"],

            bio=data.get("bio"),

            followers=data["followers"],

            following=data["following"],

            public_repos=data["public_repos"],

            created_at=data["created_at"],

            profile_url=data["html_url"]
        )

    @staticmethod
    def get_repositories(username: str):

        repos = GitHubService._get(
            f"/users/{username}/repos"
        )

        repository_list = []

        for repo in repos:

            repository_list.append(

                Repository(

                    name=repo["name"],

                    description=repo["description"],

                    language=repo["language"],

                    created_at=repo["created_at"],

                    updated_at=repo["updated_at"],

                    url=repo["html_url"]

                )

            )

        return repository_list

    @staticmethod
    def get_language_statistics(username: str):

        repos = GitHubService.get_repositories(
            username
        )

        stats = {}

        for repo in repos:

            if repo.language is None:
                continue

            stats[repo.language] = (
                stats.get(
                    repo.language,
                    0
                ) + 1
            )

        return stats

    @staticmethod
    def analyze_profile(username: str):

        profile = GitHubService.get_profile(
            username
        )

        repos = GitHubService.get_repositories(
            username
        )

        languages = GitHubService.get_language_statistics(
            username
        )

        return Analysis(

            profile=profile,

            repository_count=len(repos),

            language_statistics=languages,

            repositories=repos

        )