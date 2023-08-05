"""Common data for gitlab scripts
"""
import os

from gitlab import endpoints


def get(var) -> str:
    """Get an environmental variable
    """
    return os.environ[var]

ENDPOINT_URL = get('CI_API_V4_URL')
TOKEN = get('API_AUTH_TOKEN')

ENDPOINT = endpoints.GitLabEndpoint(ENDPOINT_URL, token=TOKEN)
