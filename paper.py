import json
import os
from config import PAPER_BALANCE, RISK_PER_TRADE

STATE_FILE = "paper_state.json"

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {
        "balance": PAPER_BALANCE,
        "positions": {},
        "trades": []
    }

def save_state(s):
    with open(STATE_FILE, "w") as f:
        json.dump(s, f, indent=2)

def open_paper(state, symbol, signal):
    if symbol in state["positions"] or signal["signal"] == "WAIT":
        return False

    risk_money = state["balance"] * RISK_PER_TRADE
    distance = abs(signal["price"] - signal["sl"])

    if distance <= 0:
        return False

    qty = risk_money / distance

    state["positions"][symbol] = {
        "side": signal["signal"],
        "entry": signal["price"],
        "sl": signal["sl"],
        "tp": signal["tp"],
        "qty": qty
    }

    save_state(state)
    return True

def close_paper(state, symbol, price):
    if symbol not in state["positions"]:
        return None

    pos = state["positions"][symbol]
    side = pos["side"]
    entry = pos["entry"]
    qty = pos["qty"]
    sl = pos["sl"]
    tp = pos["tp"]

    reason = None
    exit_price = price

    if side == "LONG":
        if price <= sl:
            reason = "SL"
            exit_price = sl
        elif price >= tp:
            reason = "TP"
            exit_price = tp

        if reason:
            pnl = (exit_price - entry) * qty

    elif side == "SHORT":
        if price >= sl:
            reason = "SL"
            exit_price = sl
        elif price <= tp:
            reason = "TP"
            exit_price = tp

        if reason:
            pnl = (entry - exit_price) * qty

    else:
        return None

    if reason is None:
        return None

    state["balance"] += pnl

    trade = {
        "symbol": symbol,
        "side": side,
        "entry": entry,
        "exit": exit_price,
        "qty": qty,
        "pnl": pnl,
        "reason": reason
    }

    state["trades"].append(trade)
    del state["positions"][symbol]
    save_state(state)

    return trade

def status(state):
    return state
