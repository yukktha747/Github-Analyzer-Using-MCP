from pydantic import BaseModel
from typing import Optional, Dict, List


class GitHubProfile(BaseModel):
    name: Optional[str]
    login: str
    bio: Optional[str]
    followers: int
    following: int
    public_repos: int
    created_at: str
    profile_url: str


class Repository(BaseModel):
    name: str
    description: Optional[str]
    language: Optional[str]
    created_at: str
    updated_at: str
    url: str


class Analysis(BaseModel):
    profile: GitHubProfile
    repository_count: int
    language_statistics: Dict[str, int]
    repositories: List[Repository]
