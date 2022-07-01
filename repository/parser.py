from models.repository import Repository
from typing import (
    Iterable,
    Dict,
    List
)


class RepositoryParser():

    @classmethod
    def parse(cls, response: Iterable[Dict]) -> List[Repository]:
        repositories = []

        for item in response:
            repository = Repository(
                id=item['id'],
                name=item['name'],
                stars=item['stargazers_count']
            )

            repositories.append(repository)

        return repositories
