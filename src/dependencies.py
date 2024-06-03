from github import Github
import os
from dotenv import load_dotenv

load_dotenv()


def get_github_client() -> Github:
    return Github(os.getenv('GITHUB_TOKEN'))