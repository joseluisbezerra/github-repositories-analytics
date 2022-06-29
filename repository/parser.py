from models.repository import Repository


class RepositoryParser():

    @classmethod
    def parse(cls, repositories):
        for repository in repositories:
            instance = Repository(
                id=repository['id'],
                name=repository['name'],
                stars=repository['stargazers_count']
            )

            print(instance)
