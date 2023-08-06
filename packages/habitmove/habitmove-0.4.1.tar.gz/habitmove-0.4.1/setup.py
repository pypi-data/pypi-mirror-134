# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['habitmove']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0,<9.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=0.23,<0.24']}

entry_points = \
{'console_scripts': ['habitmove = habitmove.cli:main']}

setup_kwargs = {
    'name': 'habitmove',
    'version': '0.4.1',
    'description': 'migrate nomie data to loop habits tracker',
    'long_description': '# habitmove\n\nTakes habit in one habit-tracking application and transforms them ready to use for another.\n\nCurrently can take an export of nomie habits in json format and convert it to be importable in Loop Habit Tracker.\nPlans for reverse migration are on the roadmap, and ultimately this tool ideally understands more and more habit formats to prevent app lock-in.\n\nConfirmed working for nomie version 5.6.4 and Loop Habit Tracker version 2.0.2 and 2.0.3. \nPresumably works for other nomie 5.x versions and other Loop 2.x versions as well, \nbut that is untested.\n\n## Installation\n\nInstallation can be accomplished through *pip*:\n\n```bash\npip install habitmove\n```\n\nRequirements:\n\n`habitmove` requires at least Python 3.7. \nIt has only been tested on GNU/Linux (amd64) though it should work on other platforms.\n\n## Usage \n\nRun as a cli utility `habitmove` currently takes a single argument: the nomie database `.json` file to import habits from.\n\nInvoked like: `habitmove nomie-export.json`.\n\nThe output as a Loop Habit Tracker database will be written to `output.db` in the present working directory.\n\nCan also take an existing Loop Habit database (exported from the application), \nand add the nomie exported habits and checkmarks to it.\nSimply put the exported Loop database in the same directory and call it `output.db`, \nit will not (should not™️) overwrite anything.\nIf there are any duplicated habits however, \nit will add duplications of the existing repetitions into the database.\n\n## Development\n\nTo enable easy development on the app, \ninstall [poetry](https://python-poetry.org/) and let it do all dependency management for you by doing:\n\n```bash\npoetry install\npoetry run habitmove <nomie-json>\n```\n\nTo see a set up more closely resembling the final cli environment, \nwith its libraries loaded as environmental dependencies enter the poetry shell:\n\n```bash\npoetry shell \n```\n\nThe package can eventually also be used as a library to load nomie data to work with in Python,\nor to move data into Loop Habit Tracker.\nTake a look at the `Parser` and `Transformer` interfaces respectively.\n\nTo run tests for the app, simply invoke `pytest` through `poetry run pytest` or from within the `poetry shell`.\nTo run larger scale test automation, make sure you habe nox installed and run `poetry run ` or again through the shell.\n\nYou can exclude integration tests that take longer and inspect the complete database output of the program through the parameters `-m "not e2e"` for both `pytest` and `nox` (which also does it automatically).\n',
    'author': 'Marty Oehme',
    'author_email': 'marty.oehme@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://git.martyoeh.me/Marty/habit-migrate',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
