# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['testudo']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0',
 'funcy>=1.16,<2.0',
 'legion-utils>=0.2.7,<0.3.0',
 'logzero>=1.7.0,<2.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'pyyaml>=6.0,<7.0',
 'typeguard>=2.13.2,<3.0.0',
 'types-pyyaml>=6.0.1,<7.0.0']

entry_points = \
{'console_scripts': ['testudo = testudo.cli:main']}

setup_kwargs = {
    'name': 'testudo',
    'version': '0.1.7',
    'description': 'A wrapper for commands to be run as periodic tasks while reporting on their results/errors to legiond. Intended to be integrated with supervisord, should work well with systemd in theory.',
    'long_description': '# Testudo\n\nA wrapper for commands to be run as periodic tasks while reporting on their results/errors to legiond. Intended to be integrated with supervisord, should work well with systemd in theory.\n\n## Setup & Usage\n\n### Installation\n\nTODO\n\n### Configuration\n\nTODO\n\n### Usage\n\nThe key reference for using `testudo` is:\n\n```bash\ntestudo --help\n```\n\n## Development\n\n### Standards\n\n- Be excellent to each other\n- Code coverage must be at 100% for all new code, or a good reason must be provided for why a given bit of code is not covered.\n  - Example of an acceptable reason: "There is a bug in the code coverage tool and it says its missing this, but its not".\n  - Example of unacceptable reason: "This is just exception handling, its too annoying to cover it".\n- The code must pass the following analytics tools. Similar exceptions are allowable as in rule 2.\n  - `pylint --disable=C0103,C0111,W1203,R0903,R0913 --max-line-length=120 testudo`\n  - `flake8 --max-line-length=120 ...`\n  - `mypy --ignore-missing-imports --follow-imports=skip --strict-optional ...`\n- All incoming information from users, clients, and configurations should be validated.\n- All internal arguments passing should be typechecked whenever possible with `typeguard.typechecked`\n\n### Development Setup\n\nUsing [poetry](https://python-poetry.org/) install from inside the repo directory:\n\n```bash\npoetry install\n```\n\nThis will set up a virtualenv which you can always activate with either `poetry shell` or run specific commands with `poetry run`. All instructions below that are meant to be run in the virtualenv will be prefaced with `(testudo)$ `\n\n#### IDE Setup\n\n**Sublime Text 3**\n\n```bash\ncurl -sSL https://gitlab.com/-/snippets/2066312/raw/master/poetry.sublime-project.py | poetry run python\n```\n\n#### Development\n\n### Testing\n\nAll testing should be done with `pytest` which is installed with the `dev` requirements.\n\nTo run all the unit tests, execute the following from the repo directory:\n\n```bash\n(testudo)$  pytest\n```\n\nThis should produce a coverage report in `/path/to/dewey-api/htmlcov/`\n\nWhile developing, you can use [`watchexec`](https://github.com/watchexec/watchexec) to monitor the file system for changes and re-run the tests:\n\n```bash\n(testudo)$ watchexec -r -e py,yaml pytest\n```\n\nTo run a specific test file:\n\n```bash\n(testudo)$ pytest tests/unit/test_cli.py\n```\n\nTo run a specific test:\n\n```bash\n(testudo)$ pytest tests/unit/test_cli.py::test_cli_basics\n```\n\nFor more information on testing, see the `pytest.ini` file as well as the [documentation](https://docs.pytest.org/en/stable/).\n',
    'author': 'Eugene Kovalev',
    'author_email': 'eugene@kovalev.systems',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/legion-robotnik/testudo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
