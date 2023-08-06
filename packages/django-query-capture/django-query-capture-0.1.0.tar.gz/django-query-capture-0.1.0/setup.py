# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_query_capture']

package_data = \
{'': ['*']}

install_requires = \
['Django==3.2.11', 'rich>=10.14.0,<11.0.0', 'typer[all]>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['django-query-capture = '
                     'django_query_capture.__main__:app']}

setup_kwargs = {
    'name': 'django-query-capture',
    'version': '0.1.0',
    'description': 'Awesome `django-query-capture` is a Python cli/package created with https://github.com/TezRomacH/python-package-template',
    'long_description': '# django-query-capture\n\n<div align="center">\n\n[![Build status](https://github.com/ashekr/django-query-capture/workflows/build/badge.svg?branch=master&event=push)](https://github.com/ashekr/django-query-capture/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/django-query-capture.svg)](https://pypi.org/project/django-query-capture/)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/ashekr/django-query-capture/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/ashekr/django-query-capture/blob/master/.pre-commit-config.yaml)\n[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/ashekr/django-query-capture/releases)\n[![License](https://img.shields.io/github/license/ashekr/django-query-capture)](https://github.com/ashekr/django-query-capture/blob/master/LICENSE)\n![Coverage Report](assets/images/coverage.svg)\n\n</div>\n\n## Installation\n\n```bash\npip install -U django-query-capture\n```\n\nor install with `Poetry`\n\n```bash\npoetry add django-query-capture\n```\n\n## 🛡 License\n\n[![License](https://img.shields.io/github/license/ashekr/django-query-capture)](https://github.com/ashekr/django-query-capture/blob/master/LICENSE)\n\nThis project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/ashekr/django-query-capture/blob/master/LICENSE) for more details.\n\n\n## Very first steps\n\n### Initialize your code\n\n1. Initialize `git` inside your repo:\n\n```bash\ncd django-query-capture && git init\n```\n\n2. If you don\'t have `Poetry` installed run:\n\n```bash\nmake poetry-download\n```\n\n3. Initialize poetry and install `pre-commit` hooks:\n\n```bash\nmake install\nmake pre-commit-install\n```\n\n4. Run the codestyle:\n\n```bash\nmake codestyle\n```\n\n### Poetry\n\nWant to know more about Poetry? Check [its documentation](https://python-poetry.org/docs/).\n\n### Makefile usage\n\n[`Makefile`](https://github.com/ashekr/django-query-capture/blob/master/Makefile) contains a lot of functions for faster development.\n\n<details>\n<summary>1. Download and remove Poetry</summary>\n<p>\n\nTo download and install Poetry run:\n\n```bash\nmake poetry-download\n```\n\nTo uninstall\n\n```bash\nmake poetry-remove\n```\n\n</p>\n</details>\n\n<details>\n<summary>2. Install all dependencies and pre-commit hooks</summary>\n<p>\n\nInstall requirements:\n\n```bash\nmake install\n```\n\nPre-commit hooks coulb be installed after `git init` via\n\n```bash\nmake pre-commit-install\n```\n\n</p>\n</details>\n\n<details>\n<summary>3. Codestyle</summary>\n<p>\n\nAutomatic formatting uses `pyupgrade`, `isort` and `black`.\n\n```bash\nmake codestyle\n\n# or use synonym\nmake formatting\n```\n\nCodestyle checks only, without rewriting files:\n\n```bash\nmake check-codestyle\n```\n\n> Note: `check-codestyle` uses `isort`, `black` and `darglint` library\n\nUpdate all dev libraries to the latest version using one comand\n\n```bash\nmake update-dev-deps\n```\n\n</details>\n<details>\n<summary>4. Code security</summary>\n<p>\n\n```bash\nmake check-safety\n```\n\nThis command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.\n\n```bash\nmake check-safety\n```\n\n</p>\n</details>\n\n<details>\n<summary>5. Type checks</summary>\n<p>\n\nRun `mypy` static type checker\n\n```bash\nmake mypy\n```\n\n</p>\n</details>\n\n<details>\n<summary>6. Tests with coverage badges</summary>\n<p>\n\nRun `pytest`\n\n```bash\nmake test\n```\n\n</p>\n</details>\n\n<details>\n<summary>7. All linters</summary>\n<p>\n\nOf course there is a command to ~~rule~~ run all linters in one:\n\n```bash\nmake lint\n```\n\nthe same as:\n\n```bash\nmake test && make check-codestyle && make mypy && make check-safety\n```\n\n</p>\n</details>\n\n<details>\n<summary>8. Docker</summary>\n<p>\n\n```bash\nmake docker-build\n```\n\nwhich is equivalent to:\n\n```bash\nmake docker-build VERSION=latest\n```\n\nRemove docker image with\n\n```bash\nmake docker-remove\n```\n\nMore information [about docker](https://github.com/ashekr/django-query-capture/tree/master/docker).\n\n</p>\n</details>\n\n<details>\n<summary>9. Cleanup</summary>\n<p>\nDelete pycache files\n\n```bash\nmake pycache-remove\n```\n\nRemove package build\n\n```bash\nmake build-remove\n```\n\nDelete .DS_STORE files\n\n```bash\nmake dsstore-remove\n```\n\nRemove .mypycache\n\n```bash\nmake mypycache-remove\n```\n\nOr to remove all above run:\n\n```bash\nmake cleanup\n```\n\n</p>\n</details>\n\n## 📃 Citation\n\n```bibtex\n@misc{django-query-capture,\n  author = {AsheKR},\n  title = {Awesome `django-query-capture` is a Python cli/package created with https://github.com/TezRomacH/python-package-template},\n  year = {2022},\n  publisher = {GitHub},\n  journal = {GitHub repository},\n  howpublished = {\\url{https://github.com/ashekr/django-query-capture}}\n}\n```\n\n## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)\n\nThis project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)\n',
    'author': 'AsheKR',
    'author_email': 'tech@ashe.kr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ashekr/django-query-capture',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
