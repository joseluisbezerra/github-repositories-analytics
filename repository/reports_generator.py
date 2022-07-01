from typing import Iterable

from models.repository import Repository

from repository.reports.csv_generator import CSVGenerator
from repository.reports.html_generator import HTMLGenerator


REPORT_TYPES = {
    'HTML': HTMLGenerator,
    'CSV': CSVGenerator
}


class ReportsGenerator():

    @classmethod
    def build(cls, type: str, repositories: Iterable[Repository]) -> str:
        type = type.upper()

        if type in REPORT_TYPES.keys():
            REPORT_TYPES[type].build(repositories)

            return 'Report file created successfully in /files'

        return "Invalid report type"
