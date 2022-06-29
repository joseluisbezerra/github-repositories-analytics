from github.client import GithubClient
from repository.parser import RepositoryParser

import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        "main.py",
        description="Lists all repositories of a Github user."
    )

    parser.add_argument(
        "username",
        help="Valid github username.",
        type=str
    )

    username = parser.parse_args().username

    response = GithubClient.get_repositories_by_username(username)

    if response['status_code'] == 200:
        RepositoryParser.parse(response['body'])
    else:
        print(response['body'])
