# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['f4ratk',
 'f4ratk.analyze',
 'f4ratk.cli',
 'f4ratk.file',
 'f4ratk.portfolio',
 'f4ratk.portfolio.reader',
 'f4ratk.ticker',
 'f4ratk.web',
 'f4ratk.web.mail']

package_data = \
{'': ['*']}

modules = \
['COPYING']
install_requires = \
['PyYAML==6.0',
 'appdirs==1.4.4',
 'click==8.0.3',
 'importlib_metadata==4.10.0',
 'pandas-datareader==0.10.0',
 'pandas==1.3.5',
 'requests-cache==0.9.0',
 'scipy==1.7.3',
 'statsmodels==0.13.1',
 'xlrd==2.0.1']

extras_require = \
{'server': ['flask==2.0.2', 'flask-caching==1.10.1', 'marshmallow==3.14.1'],
 'server-engine': ['gunicorn==20.1.0']}

entry_points = \
{'console_scripts': ['f4ratk = f4ratk.cli.commands:main',
                     'f4ratk-server = f4ratk.web.server:main']}

setup_kwargs = {
    'name': 'f4ratk',
    'version': '2022.1',
    'description': 'A Fama/French Finance Factor Regression Analysis Toolkit.',
    'long_description': "# f4ratk\n\n[![Version: PyPi](https://img.shields.io/pypi/v/f4ratk?cacheSeconds=2592000)](https://pypi.org/project/f4ratk/)\n[![Python Version: PyPi](https://img.shields.io/pypi/pyversions/f4ratk?cacheSeconds=2592000)](https://pypi.org/project/f4ratk/)\n[![License: AGPL](https://img.shields.io/badge/license-AGPL--3.0--only-informational.svg?cacheSeconds=31536000)](https://spdx.org/licenses/AGPL-3.0-only.html)\n[![Build Status: Azure](https://img.shields.io/azure-devops/build/toroettg/f4ratk/1?cacheSeconds=86400)](https://dev.azure.com/toroettg/f4ratk/_build/latest?definitionId=1&branchName=main)\n[![Coverage: Azure](https://img.shields.io/azure-devops/coverage/toroettg/f4ratk/1?cacheSeconds=86400)](https://dev.azure.com/toroettg/f4ratk/_build/latest?definitionId=1&branchName=main)\n[![Downloads: PyPi](https://img.shields.io/pypi/dm/f4ratk?cacheSeconds=86400)](https://pypistats.org/packages/f4ratk)\n[![Donate: Liberapay](https://img.shields.io/liberapay/patrons/f4ratk?logo=liberapay?cacheSeconds=2592000)](https://liberapay.com/f4ratk/donate)\n\nA Fama/French Finance Factor Regression Analysis Toolkit.\n\nThe deployed project is provided at https://f4ratk.herokuapp.com.\n\n## Here be dragons\n\nThis project is experimental: it does not provide any guarantees and its\nresults are not rigorously tested. It should not be used by itself as a\nbasis for decision‐making.\n\nIf you would like to join, please see [CONTRIBUTING] for guidelines.\n\n## Features\n\nThe following lists some main use cases, this software can assist you.\n\n- Analyze stock quotes of a ticker symbol.\n- Analyze arbitrary performance data from file.\n- Display historic factor returns.\n- Estimate excess returns based on regression results.\n\n## Quickstart\n\n### Installation\n\nObtain the latest released version of f4ratk using pip:\n\n`pip install -U f4ratk`\n\n### Usage\n\nRun the program to see an interactive help. Note that each listed\ncommand also provides an individual help.\n\n`f4ratk --help`\n\n```lang-none\nUsage: f4ratk [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  -v, --verbose  Increase output verbosity.\n  --about        Display program information and exit.\n  --help         Show this message and exit.\n\nCommands:\n  convert    Convert files to the 'file' command format.\n  file       Analyze a CSV file.\n  history    Display historic factor returns.\n  portfolio  Analyze a portfolio file.\n  ticker     Analyze a ticker symbol.\n\n```\n\nAdjust the program arguments according to your problem.\nThen run your regression analysis similar to the following.\n\n#### Examples\n\n```lang-sh\nf4ratk ticker USSC.L US USD\nf4ratk file ./input.csv DEVELOPED EUR PRICE --frequency=MONTHLY\n\n```\n\n## License\n\nThis project is licensed under the GNU Affero General Public License\nversion 3 (only). See [LICENSE] for more information and [COPYING]\nfor the full license text.\n\n[CONTRIBUTING]: https://codeberg.org/toroettg/f4ratk/src/branch/main/CONTRIBUTING.md\n[LICENSE]: https://codeberg.org/toroettg/f4ratk/src/branch/main/LICENSE\n[COPYING]: https://codeberg.org/toroettg/f4ratk/src/branch/main/COPYING\n",
    'author': 'Tobias Röttger',
    'author_email': 'dev@roettger-it.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://codeberg.org/toroettg/f4ratk',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
