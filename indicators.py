def ema(values, span):
    if not values:
        return 0.0
    alpha = 2.0 / (span + 1.0)
    result = float(values[0])
    for value in values[1:]:
        result = alpha * float(value) + (1.0 - alpha) * result
    return result


def sma(values):
    if not values:
        return 0.0
    return sum(values) / len(values)


def indicators(rows):
    closes = [float(r[4]) for r in rows]
    highs = [float(r[2]) for r in rows]
    lows = [float(r[3]) for r in rows]
    volumes = [float(r[5]) for r in rows]

    ema20 = []
    ema50 = []
    fast = []
    slow = []
    macd = []
    macd_signal = []
    rsi_values = []
    atr_values = []
    vol_ma = []

    e20 = closes[0]
    e50 = closes[0]
    f = closes[0]
    s = closes[0]
    signal = 0.0

    gains = []
    losses = []

    for i, close in enumerate(closes):
        if i > 0:
            delta = close - closes[i - 1]
            gains.append(max(delta, 0.0))
            losses.append(max(-delta, 0.0))

        e20 = (2 / 21) * close + (19 / 21) * e20
        e50 = (2 / 51) * close + (49 / 51) * e50
        f = (2 / 13) * close + (11 / 13) * f
        s = (2 / 27) * close + (25 / 27) * s

        m = f - s
        signal = (2 / 10) * m + (8 / 10) * signal

        if len(gains) >= 14:
            avg_gain = sum(gains[-14:]) / 14
            avg_loss = sum(losses[-14:]) / 14
            if avg_loss == 0:
                rsi = 100.0
            else:
                rs = avg_gain / avg_loss
                rsi = 100.0 - (100.0 / (1.0 + rs))
        else:
            rsi = 50.0

        if i == 0:
            tr = highs[i] - lows[i]
        else:
            prev = closes[i - 1]
            tr = max(
                highs[i] - lows[i],
                abs(highs[i] - prev),
                abs(lows[i] - prev)
            )

        if i >= 13:
            trs = []
            for j in range(i - 13, i + 1):
                if j == 0:
                    trs.append(highs[j] - lows[j])
                else:
                    prev = closes[j - 1]
                    trs.append(max(
                        highs[j] - lows[j],
                        abs(highs[j] - prev),
                        abs(lows[j] - prev)
                    ))
            atr = sum(trs) / 14
        else:
            atr = tr

        ema20.append(e20)
        ema50.append(e50)
        fast.append(f)
        slow.append(s)
        macd.append(m)
        macd_signal.append(signal)
        rsi_values.append(rsi)
        atr_values.append(atr)

        start = max(0, i - 19)
        vol_ma.append(sum(volumes[start:i + 1]) / (i - start + 1))

    result = []

    for i, row in enumerate(rows):
        result.append({
            "timestamp": row[0],
            "open": float(row[1]),
            "high": highs[i],
            "low": lows[i],
            "close": closes[i],
            "volume": volumes[i],
            "ema20": ema20[i],
            "ema50": ema50[i],
            "rsi": rsi_values[i],
            "macd": macd[i],
            "macd_signal": macd_signal[i],
            "atr": atr_values[i],
            "vol_ma": vol_ma[i],
        })

    return result
