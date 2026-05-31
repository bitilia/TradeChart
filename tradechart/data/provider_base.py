"""Abstract base class for market-data providers."""

from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd

from tradechart.data.models import MarketData


def to_utc_index(df: pd.DataFrame) -> pd.DataFrame:
    """Normalise a DataFrame's DatetimeIndex to UTC-aware in-place and return it."""
    if df.index.tz is None:
        df.index = df.index.tz_localize("UTC")
    else:
        df.index = df.index.tz_convert("UTC")
    return df


class BaseProvider(ABC):
    """Every data provider must implement this interface."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable provider name."""

    @abstractmethod
    def fetch(self, ticker: str, duration: str) -> MarketData:
        """Fetch OHLCV data. Must raise on failure."""
