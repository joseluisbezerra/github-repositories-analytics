import requests


class GithubClient():
    API_BASE_URL = 'https://api.github.com'
    ERROR_MESSAGE = 'Error while getting repositories'

    @classmethod
    def get_repositories_by_username(self, username: str) -> dict:
        response = requests.get(
            f'{self.API_BASE_URL}/users/{username}/repos'
        )

        return {
            'status_code': response.status_code,
            'body': response.json() if response.status_code == 200 else self.ERROR_MESSAGE  # noqa: E501
        }
