from models.repository import Repository

from typing import Iterable

from dominate import (
    document,
    tags
)

import os


class HTMLGenerator():

    @classmethod
    def build(cls, repositories: Iterable[Repository]) -> None:
        doc = document(title='Github Repositories Analytics')

        with doc.head:
            tags.meta(charset="utf-8")
            tags.meta(
                name='viewport',
                content='width=device-width, initial-scale=1'
            )

            tags.link(
                rel='stylesheet',
                href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css',  # noqa: E501
                integrity='sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC',  # noqa: E501
                crossorigin='anonymous'
            )

        with doc:
            with tags.main(cls='flex-shrink-0').add(tags.div(cls='container')):
                tags.h1('Repositories list', cls='mt-3')

                with tags.table(cls='table table-hover mt-3'):
                    with tags.thead().add(tags.tr()):
                        for title in repositories[0].as_dict().keys():
                            tags.th(title.capitalize(), scope='col')

                    with tags.tbody():
                        for repository in repositories:
                            tags.tr(
                                tags.th(repository.id, scope='row'),
                                tags.td(repository.name),
                                tags.td(repository.stars)
                            )

        filename = 'files/repositories.html'

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w') as html_file:
            html_file.write(doc.render())
