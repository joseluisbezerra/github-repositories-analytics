from github.client import GithubClient

from repository.parser import RepositoryParser
from repository.reports_generator import ReportsGenerator

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

    parser.add_argument(
        '--type',
        action='store',
        dest='file_type',
        default='csv',
        required=False,
        help='File type to export (CSV or HTML, default CSV)'
    )

    username = parser.parse_args().username
    file_type = parser.parse_args().file_type

    response = GithubClient.get_repositories_by_username(username)

    if response['status_code'] == 200:
        repositories = RepositoryParser.parse(response['body'])

        message = ReportsGenerator.build(file_type, repositories)

        print(message)
    else:
        print(response['body'])
