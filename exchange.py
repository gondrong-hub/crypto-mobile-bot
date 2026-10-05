import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from config import TIMEFRAME


def candles(symbol, limit=150):
    symbol = symbol.replace("/", "")
    interval = TIMEFRAME

    url = "https://api1.binance.com/api/v3/klines"
    query = urlencode({
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    })

    request = Request(f"{url}?{query}")
    with urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))
