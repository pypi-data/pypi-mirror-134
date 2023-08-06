# f4ratk

[![Version: PyPi](https://img.shields.io/pypi/v/f4ratk?cacheSeconds=2592000)](https://pypi.org/project/f4ratk/)
[![Python Version: PyPi](https://img.shields.io/pypi/pyversions/f4ratk?cacheSeconds=2592000)](https://pypi.org/project/f4ratk/)
[![License: AGPL](https://img.shields.io/badge/license-AGPL--3.0--only-informational.svg?cacheSeconds=31536000)](https://spdx.org/licenses/AGPL-3.0-only.html)
[![Build Status: Azure](https://img.shields.io/azure-devops/build/toroettg/f4ratk/1?cacheSeconds=86400)](https://dev.azure.com/toroettg/f4ratk/_build/latest?definitionId=1&branchName=main)
[![Coverage: Azure](https://img.shields.io/azure-devops/coverage/toroettg/f4ratk/1?cacheSeconds=86400)](https://dev.azure.com/toroettg/f4ratk/_build/latest?definitionId=1&branchName=main)
[![Downloads: PyPi](https://img.shields.io/pypi/dm/f4ratk?cacheSeconds=86400)](https://pypistats.org/packages/f4ratk)
[![Donate: Liberapay](https://img.shields.io/liberapay/patrons/f4ratk?logo=liberapay?cacheSeconds=2592000)](https://liberapay.com/f4ratk/donate)

A Fama/French Finance Factor Regression Analysis Toolkit.

The deployed project is provided at https://f4ratk.herokuapp.com.

## Here be dragons

This project is experimental: it does not provide any guarantees and its
results are not rigorously tested. It should not be used by itself as a
basis for decision‐making.

If you would like to join, please see [CONTRIBUTING] for guidelines.

## Features

The following lists some main use cases, this software can assist you.

- Analyze stock quotes of a ticker symbol.
- Analyze arbitrary performance data from file.
- Display historic factor returns.
- Estimate excess returns based on regression results.

## Quickstart

### Installation

Obtain the latest released version of f4ratk using pip:

`pip install -U f4ratk`

### Usage

Run the program to see an interactive help. Note that each listed
command also provides an individual help.

`f4ratk --help`

```lang-none
Usage: f4ratk [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --verbose  Increase output verbosity.
  --about        Display program information and exit.
  --help         Show this message and exit.

Commands:
  convert    Convert files to the 'file' command format.
  file       Analyze a CSV file.
  history    Display historic factor returns.
  portfolio  Analyze a portfolio file.
  ticker     Analyze a ticker symbol.

```

Adjust the program arguments according to your problem.
Then run your regression analysis similar to the following.

#### Examples

```lang-sh
f4ratk ticker USSC.L US USD
f4ratk file ./input.csv DEVELOPED EUR PRICE --frequency=MONTHLY

```

## License

This project is licensed under the GNU Affero General Public License
version 3 (only). See [LICENSE] for more information and [COPYING]
for the full license text.

[CONTRIBUTING]: https://codeberg.org/toroettg/f4ratk/src/branch/main/CONTRIBUTING.md
[LICENSE]: https://codeberg.org/toroettg/f4ratk/src/branch/main/LICENSE
[COPYING]: https://codeberg.org/toroettg/f4ratk/src/branch/main/COPYING
