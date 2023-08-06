#!/usr/bin/env python
import habitmove.schema as schema
import habitmove.habits as habits
import habitmove.repetitions as rep
import habitmove.nomie as nomie
from habitmove.nomiedata import NomieImport

import click
from . import __version__


def migrate(data: NomieImport):
    db = schema.migrate("output.db")
    if not db:
        raise ConnectionError

    if data.trackers is not None:

        habitlist = habits.migrate(db, data.trackers)

        if data.events is not None:
            rep.migrate(db, habitlist, data.events)

    db.commit()
    db.close()


@click.command()
@click.version_option(version=__version__)
@click.argument("inputfile")
def main(inputfile):
    data = nomie.get_data(inputfile)
    migrate(data)


if __name__ == "__main__":
    main()
