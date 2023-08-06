##############################################################################
# Copyright (C) 2020 - 2022 Tobias Röttger <dev@roettger-it.de>
#
# This file is part of f4ratk.
#
# f4ratk is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License version 3
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
##############################################################################

from datetime import date, timedelta
from os import PathLike
from typing import Optional

from pandas import DataFrame, read_csv
from pandas_datareader.famafrench import FamaFrenchReader
from pandas_datareader.fred import FredReader
from pandas_datareader.yahoo.daily import YahooDailyReader
from requests_cache import CachedSession

from f4ratk.directories import cache


def _cached_session() -> CachedSession:
    cache_duration = timedelta(days=14)
    cache_location = str(cache.file(name='requests'))

    session = CachedSession(
        cache_name=cache_location, backend='sqlite', expire_after=cache_duration
    )
    session.remove_expired_responses()

    session.headers.update(
        {
            # Workaround, see https://github.com/pydata/pandas-datareader/issues/867
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                ' AppleWebKit/537.36 (KHTML, like Gecko)'
                ' Chrome/91.0.4472.124 Safari/537.36'
            )
        }
    )

    return session


_session = _cached_session()


def fama_french_reader(returns_data: str) -> FamaFrenchReader:
    return FamaFrenchReader(symbols=returns_data, session=_session, start='1920')


def yahoo_reader(
    ticker_symbol: str, start: Optional[date], end: Optional[date]
) -> YahooDailyReader:
    return YahooDailyReader(
        symbols=ticker_symbol,
        start=start if start else '1970',
        end=end,
        session=_session,
    )


def fred_reader(
    exchange_symbol: str, start: Optional[date], end: Optional[date]
) -> FredReader:
    return FredReader(
        symbols=exchange_symbol,
        start=start if start else '1970',
        end=end,
        session=_session,
    )


class CsvFileReader:
    _HEADER = ('Dates', 'Returns')

    def __init__(self, path: PathLike):
        self._path = path

    def read(self) -> DataFrame:
        return read_csv(self._path, parse_dates=True, index_col=0, names=self._HEADER)
