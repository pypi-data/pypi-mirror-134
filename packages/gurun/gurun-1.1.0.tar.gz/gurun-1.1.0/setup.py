# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gurun', 'gurun.cv', 'gurun.gui']

package_data = \
{'': ['*']}

extras_require = \
{'cv': ['opencv-python>=4.5.4,<5.0.0'],
 'full': ['opencv-python>=4.5.4,<5.0.0',
          'PyAutoGUI>=0.9.41,<0.10.0',
          'mss>=6.1.0,<7.0.0'],
 'gui': ['opencv-python>=4.5.4,<5.0.0',
         'PyAutoGUI>=0.9.41,<0.10.0',
         'mss>=6.1.0,<7.0.0']}

setup_kwargs = {
    'name': 'gurun',
    'version': '1.1.0',
    'description': 'Task automation framework',
    'long_description': '# gurun\n\n<div align="center">\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/gabrielguarisa/gurun/blob/master/.pre-commit-config.yaml)\n[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/gabrielguarisa/gurun/releases)\n[![License](https://img.shields.io/github/license/gabrielguarisa/gurun)](https://github.com/gabrielguarisa/gurun/blob/master/LICENSE)\n\nTask automation framework\n\n</div>\n\n## Installation\n\nFull installation:\n\n```bash\npip install gurun[full]\n```\n\nInstalling only the main framework components:\n\n```bash\npip install gurun\n```\n\nYou can also install component dependencies separately. Thus, we have the cv (computer vision) version and the gui version:\n\n```bash\npip install gurun[cv] \npip install gurun[gui]\n```\n\n## Development\n### Setting up a development environment\n\nIf you don\'t have a local development environment, you can follow these steps to set one up.\n\nFirst, if you have not already, install [poetry](https://python-poetry.org/):\n\n```bash\npip install poetry\n```\n\nNow, initialize poetry and [pre-commit](https://pre-commit.com/) hooks:\n\n```bash\nmake install && make install-pre-commit\n```\n\n### Running tests\n\nYou can run the tests with:\n\n```bash\nmake tests\n```\n\nThis will run the tests with [pytest](https://docs.pytest.org/en/latest/) and show information about the coverage.\n\n### Formatting the code\n\nTo format the code, you can use the command:\n\n```bash\nmake formatting\n```\n\nThis will run the [black](https://github.com/psf/black), [isort](https://github.com/PyCQA/isort) and )[pyupgrade](https://github.com/asottile/pyupgrade) commands.\n\nIf you want to just check the formatting, use the command:\n\n```bash\nmake check-formatting\n```\n\n### Releasing a new version\n\nTo release a new version, you need to follow these steps:\n\n1. Update the version with `poetry version <version>` and commit the changes. This project follows [Semantic Versioning](http://semver.org/), so the version number should follow the format `<major>.<minor>.<patch>`. Alternatively, you can also use the version as `major` or `minor` or `patch`, and the version number will be automatically incremented.\n\n2. Create a Github release with the new version number.\n\n3. (Optional) Publish the new version to PyPI with `poetry publish --build`.\n',
    'author': 'Gabriel Guarisa',
    'author_email': 'gabrielguarisa@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gabrielguarisa/gurun',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7.12,<3.11',
}


setup(**setup_kwargs)
