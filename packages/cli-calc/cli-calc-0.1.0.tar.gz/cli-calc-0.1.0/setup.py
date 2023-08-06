# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cli_calc']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cli-calc',
    'version': '0.1.0',
    'description': 'Powerful yet easy command line calculator.',
    'long_description': '# cli-calc\n\n[![Build Status](https://github.com/nikolai.krusenstiern.de/cli-calc/workflows/test/badge.svg?branch=master&event=push)](https://github.com/nikolai.krusenstiern.de/cli-calc/actions?query=workflow%3Atest)\n[![codecov](https://codecov.io/gh/nikolai.krusenstiern.de/cli-calc/branch/master/graph/badge.svg)](https://codecov.io/gh/nikolai.krusenstiern.de/cli-calc)\n[![Python Version](https://img.shields.io/pypi/pyversions/cli-calc.svg)](https://pypi.org/project/cli-calc/)\n[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)\n\nPowerful yet easy command line calculator.\n\n\n## Features\n\n- Fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)\n\n\n## Installation\n\n```bash\npip install cli-calc\n```\n\nIn order to run it from anywhere: Add a symbolic link in ~/bin\n\n```bash\ncd ~/bin\nln -s ~/path/to/your/install/cli_calc/warpper.sh calc\n```\n\nThen use it anywhere. :-)\n\n```bash\ncalc\n```\n\n## Help\n\n```bash\nInput:\n    "q" for quit, "h" for help\n\n    "_float_" and/or "_int_" for last value\n    "pi", "tau" and "e" for pi, tau and Euler\n\n    "+f" to add display for fraction, "-f" to suppress display for fraction\n        Other letters are:\n        he(x), (o)ctal, (b)inary, (i)nteger,\n        (f)raction, (t)ruth, i(e)ee, ieee_bi(n), f(r)om_ieee\n        "float" is always visible\n\n    See https://docs.python.org/3/library/math.html, use without "math."\n        https://www.w3schools.com/python/python_operators.asp\n\n    Try "cos(_pi_/2)", XOR: "0xFF ^ 0b10", "2**8-1", "factorial(42)",\n        "help(math)"\n```\n\n## Example\n\nTry:\n\n```\ncos(_pi_/2)\n0xFF ^ 0b10\n2**8-1\nfactorial(42)\n```\n\n## License\n\n[MIT](https://github.com/nikolai.krusenstiern.de/cli-calc/blob/master/LICENSE)\n\n\n## Credits\n\nThis project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [d06993f12e3ffad79652a2aec86189dee92d94dd](https://github.com/wemake-services/wemake-python-package/tree/d06993f12e3ffad79652a2aec86189dee92d94dd). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/d06993f12e3ffad79652a2aec86189dee92d94dd...master) since then.\n',
    'author': None,
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nikolai.krusenstiern.de/cli-calc',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
