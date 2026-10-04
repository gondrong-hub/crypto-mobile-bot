from indicators import indicators


def analyze(rows):
    x = indicators(rows)
    r = x[-1]

    score_long = 0
    score_short = 0

    if r["ema20"] > r["ema50"]:
        score_long += 1
    elif r["ema20"] < r["ema50"]:
        score_short += 1

    if r["rsi"] > 55:
        score_long += 1
    elif r["rsi"] < 45:
        score_short += 1

    if r["macd"] > r["macd_signal"]:
        score_long += 1
    elif r["macd"] < r["macd_signal"]:
        score_short += 1

    if r["volume"] > r["vol_ma"]:
        if r["close"] > r["ema20"]:
            score_long += 1
        elif r["close"] < r["ema20"]:
            score_short += 1

    if score_long >= 3 and score_long > score_short:
        signal = "LONG"
        confidence = int(50 + score_long * 8)
    elif score_short >= 3 and score_short > score_long:
        signal = "SHORT"
        confidence = int(50 + score_short * 8)
    else:
        signal = "WAIT"
        confidence = 50

    atr = float(r["atr"])
    price = float(r["close"])

    if signal == "LONG":
        sl = price - 1.5 * atr
        tp = price + 3.0 * atr
    elif signal == "SHORT":
        sl = price + 1.5 * atr
        tp = price - 3.0 * atr
    else:
        sl = None
        tp = None

    return {
        "signal": signal,
        "confidence": min(confidence, 90),
        "price": price,
        "rsi": float(r["rsi"]),
        "ema20": float(r["ema20"]),
        "ema50": float(r["ema50"]),
        "macd": float(r["macd"]),
        "atr": atr,
        "sl": sl,
        "tp": tp
    }
