import requests
from config import TIMEFRAME


def candles(symbol, limit=150):
    symbol = symbol.replace("/", "")
    interval = TIMEFRAME

    url = "https://api1.binance.com/api/v3/klines"
    response = requests.get(
        url,
        params={
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        },
        timeout=20
    )
    response.raise_for_status()

    return response.json()
