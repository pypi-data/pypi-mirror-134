# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['torchdemon']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.0,<2.0.0', 'torch>=1.10.1,<2.0.0']

setup_kwargs = {
    'name': 'torchdemon',
    'version': '0.0.1',
    'description': 'Inference server for RL',
    'long_description': "# torchdemon\n\n[![PyPI](https://img.shields.io/pypi/v/torchdemon?style=flat-square)](https://pypi.python.org/pypi/torchdemon/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/torchdemon?style=flat-square)](https://pypi.python.org/pypi/torchdemon/)\n[![PyPI - License](https://img.shields.io/pypi/l/torchdemon?style=flat-square)](https://pypi.python.org/pypi/torchdemon/)\n[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)\n\n\n---\n\n**Documentation**: [https://jacknurminen.github.io/torchdemon](https://jacknurminen.github.io/torchdemon)\n\n**Source Code**: [https://github.com/jacknurminen/torchdemon](https://github.com/jacknurminen/torchdemon)\n\n**PyPI**: [https://pypi.org/project/torchdemon/](https://pypi.org/project/torchdemon/)\n\n---\n\nInference server for RL\n\n## Installation\n\n```sh\npip install torchdemon\n```\n\n## Development\n\n* Clone this repository\n* Requirements:\n  * [Poetry](https://python-poetry.org/)\n  * Python 3.7+\n* Create a virtual environment and install the dependencies\n\n```sh\npoetry install\n```\n\n* Activate the virtual environment\n\n```sh\npoetry shell\n```\n\n### Testing\n\n```sh\npytest\n```\n\n### Documentation\n\nThe documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings\n of the public signatures of the source code. The documentation is updated and published as a [Github project page\n ](https://pages.github.com/) automatically as part each release.\n\n### Releasing\n\nTrigger the [Draft release workflow](https://github.com/jacknurminen/torchdemon/actions/workflows/draft_release.yml)\n(press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.\n\nFind the draft release from the\n[GitHub releases](https://github.com/jacknurminen/torchdemon/releases) and publish it. When\n a release is published, it'll trigger [release](https://github.com/jacknurminen/torchdemon/blob/master/.github/workflows/release.yml) workflow which creates PyPI\n release and deploys updated documentation.\n\n### Pre-commit\n\nPre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality\n checks to make sure the changeset is in good shape before a commit/push happens.\n\nYou can install the hooks with (runs for each commit):\n\n```sh\npre-commit install\n```\n\nOr if you want them to run only for each push:\n\n```sh\npre-commit install -t pre-push\n```\n\nOr if you want e.g. want to run all checks manually for all files:\n\n```sh\npre-commit run --all-files\n```\n\n---\n\nThis project was generated using the [wolt-python-package-cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter) template.\n",
    'author': 'Jack Nurminen',
    'author_email': 'jack.nurminen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://jacknurminen.github.io/torchdemon',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
