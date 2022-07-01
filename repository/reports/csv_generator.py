from models.repository import Repository

from typing import Iterable
import csv
import os


class CSVGenerator():

    @classmethod
    def build(cls, repositories: Iterable[Repository]) -> None:
        filename = 'files/repositories.csv'

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w', encoding='UTF8', newline='') as csv_file:
            writer = csv.writer(csv_file)

            header = repositories[0].as_dict().keys()

            writer.writerow(header)

            rows = [
                repository.as_dict().values() for repository in repositories
            ]

            writer.writerows(rows)
