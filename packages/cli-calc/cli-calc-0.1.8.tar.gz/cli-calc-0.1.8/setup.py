# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cli_calc']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cli-calc',
    'version': '0.1.8',
    'description': 'Powerful yet easy command line calculator.',
    'long_description': '![](https://github.com/cruisen/cli-calc/blob/main/assets/images/Cli-Calc.png)\n\n# cli-calc\n\n[![test](https://github.com/cruisen/cli-calc/actions/workflows/test.yml/badge.svg)](https://github.com/cruisen/cli-calc/actions/workflows/test.yml)\n[![codecov](https://codecov.io/gh/cruisen/cli-calc/branch/main/graph/badge.svg?token=i9nYZL3MM3)](https://codecov.io/gh/cruisen/cli-calc)\n[![Python Version](https://img.shields.io/pypi/pyversions/cli-calc.svg)](https://pypi.org/project/cli-calc/)\n[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)\n\nPowerful yet easy command line calculator.\n\n## Example Usage\n\n```\ncos(pi/2)\n0xFF ^ 0b10\n2**8-1\nfactorial(42)\n```\n\n# Installation\n\n```bash\npip install cli-calc\n```\n\n[pypi cli-calc](https://pypi.org/project/cli-calc/).\n\n## Configuration\n\nIn order to run it from anywhere: Add a symbolic link in ~/bin\n\n```bash\ncd ~/bin\nln -s ~/path/to/your/install/cli_calc/warpper.sh calc\n```\n\nThen use it anywhere. :-)\n\n```bash\ncalc\n```\n\n## Help\n\n```bash\ncalc\nh\nInput:\n    "q" for quit, "h" for help\n\n    "_float_" and/or "_int_" for last value\n    "pi", "tau" and "e" for pi, tau and Euler\n\n    "+f" to add display for fraction, "-f" to suppress display for fraction\n        Other letters are:\n        he(x), (o)ctal, (b)inary, (i)nteger,\n        (f)raction, (t)ruth, i(e)ee, ieee_bi(n), f(r)om_ieee\n        "float" is always visible\n\n    See https://docs.python.org/3/library/math.html, use without "math."\n        https://www.w3schools.com/python/python_operators.asp\n\n    Try "cos(pi/2)", XOR: "0xFF ^ 0b10", "2**8-1", "factorial(42)",\n        "help(math)"\n```\n\n## Warning\n\nUse of [eval](https://docs.python.org/3/library/functions.html#eval) is evil.\n\nHowever some precautions are taken.\n\n\n# Features\n\n* Fully typed with annotations and checked with mypy.\n* [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)\n\n## Tools\n\n### Style and type annotations\n* [pylint](https://pylint.org/)\n* [isort](https://pycqa.github.io/isort/)\n* [black](https://black.readthedocs.io/en/stable/)\n  * [wemake](https://wemake-python-stylegui.de/en/latest/)\n* [flake8](https://flake8.pycqa.org/en/latest/)\n  * [nitpick](https://nitpick.readthedocs.io/en/latest/)\n\n### Testing and CT\n* [pytest](https://docs.pytest.org/)\n\n### Build and publish to pypi\n* [git-bump.ksh](https://github.com/cruisen/cli-calc/blob/69430ce5e71bc2544390f36122a8d05756518199/dev-tools/git-bump.ksh)\n  * [poetry build](https://python-poetry.org/docs/cli/#build)\n  * [poetry publish](https://python-poetry.org/docs/cli/#publish)\n\n### Development Environment\n* [poetry](https://python-poetry.org/)\n* [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html)\n* [git](https://git-scm.com/)\n* [github](https://github.com/)\n  * [gh](https://github.com/cli/cli)\n* [Markdown](https://www.markdownguide.org/basic-syntax/)\n\n### Documentation\n* [sphinx](https://www.sphinx-doc.org/en/master/)\n* [doc8](https://github.com/pycqa/doc8)\n\n\n# License\n\n[MIT](https://github.com/cruisen/cli-calc/blob/master/LICENSE)\n\n\n## Credits\n\nThis project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [d06993f12e3ffad79652a2aec86189dee92d94dd](https://github.com/wemake-services/wemake-python-package/tree/d06993f12e3ffad79652a2aec86189dee92d94dd). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/d06993f12e3ffad79652a2aec86189dee92d94dd...master) since then.\n',
    'author': 'Nikolai von Krusenstiern',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cruisen/cli-calc',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
