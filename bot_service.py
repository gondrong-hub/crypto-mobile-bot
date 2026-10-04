import time
import threading
from exchange import candles
from strategy import analyze
from paper import load_state, open_paper
from config import SYMBOLS, LOOP_SECONDS

_running = False
_thread = None


def bot_loop():
    global _running

    state = load_state()

    while _running:
        for symbol in SYMBOLS:
            if not _running:
                break

            try:
                df = candles(symbol)
                a = analyze(df)

                print(
                    f"{symbol} | {a['signal']} | "
                    f"Confidence: {a['confidence']}% | "
                    f"Price: {a['price']:.4f}"
                )

                if a["confidence"] >= 66:
                    open_paper(state, symbol, a)

            except Exception as e:
                print(symbol, "ERROR:", e)

        for _ in range(LOOP_SECONDS):
            if not _running:
                break
            time.sleep(1)


def start():
    global _running, _thread

    if _running:
        return False

    _running = True
    _thread = threading.Thread(target=bot_loop, daemon=True)
    _thread.start()
    return True


def stop():
    global _running
    _running = False
    return True


def is_running():
    return _running
