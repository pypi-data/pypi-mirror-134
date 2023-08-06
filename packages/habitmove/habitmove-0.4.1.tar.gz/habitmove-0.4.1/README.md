# habitmove

Takes habit in one habit-tracking application and transforms them ready to use for another.

Currently can take an export of nomie habits in json format and convert it to be importable in Loop Habit Tracker.
Plans for reverse migration are on the roadmap, and ultimately this tool ideally understands more and more habit formats to prevent app lock-in.

Confirmed working for nomie version 5.6.4 and Loop Habit Tracker version 2.0.2 and 2.0.3. 
Presumably works for other nomie 5.x versions and other Loop 2.x versions as well, 
but that is untested.

## Installation

Installation can be accomplished through *pip*:

```bash
pip install habitmove
```

Requirements:

`habitmove` requires at least Python 3.7. 
It has only been tested on GNU/Linux (amd64) though it should work on other platforms.

## Usage 

Run as a cli utility `habitmove` currently takes a single argument: the nomie database `.json` file to import habits from.

Invoked like: `habitmove nomie-export.json`.

The output as a Loop Habit Tracker database will be written to `output.db` in the present working directory.

Can also take an existing Loop Habit database (exported from the application), 
and add the nomie exported habits and checkmarks to it.
Simply put the exported Loop database in the same directory and call it `output.db`, 
it will not (should not™️) overwrite anything.
If there are any duplicated habits however, 
it will add duplications of the existing repetitions into the database.

## Development

To enable easy development on the app, 
install [poetry](https://python-poetry.org/) and let it do all dependency management for you by doing:

```bash
poetry install
poetry run habitmove <nomie-json>
```

To see a set up more closely resembling the final cli environment, 
with its libraries loaded as environmental dependencies enter the poetry shell:

```bash
poetry shell 
```

The package can eventually also be used as a library to load nomie data to work with in Python,
or to move data into Loop Habit Tracker.
Take a look at the `Parser` and `Transformer` interfaces respectively.

To run tests for the app, simply invoke `pytest` through `poetry run pytest` or from within the `poetry shell`.
To run larger scale test automation, make sure you habe nox installed and run `poetry run ` or again through the shell.

You can exclude integration tests that take longer and inspect the complete database output of the program through the parameters `-m "not e2e"` for both `pytest` and `nox` (which also does it automatically).
