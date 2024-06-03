from fastapi import Depends
from fastapi.routing import APIRouter
from .schemas import RepositorySchema
from .dependencies import get_github_client
from github import Github

router = APIRouter(tags=['GitHub'])


@router.get(
    "/get-repositories",
    summary="Get all repositories",
    description="Get all repositories",
    response_model=list[RepositorySchema]
)
def get_repositories(github_client: Github = Depends(get_github_client)):
    user = github_client.get_user()
    repos = user.get_repos()
    response = []

    for repo in repos:
        colaborators = repo.get_collaborators()
        repository_schema = RepositorySchema(
            name=repo.name,
            created_at=repo.created_at,
            stargazers_count=repo.stargazers_count,
            colaborators_count=colaborators.totalCount
        )
        response.append(repository_schema)

    return response
