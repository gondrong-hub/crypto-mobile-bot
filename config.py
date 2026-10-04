import os
from dotenv import load_dotenv

load_dotenv()

SYMBOLS = ["BTC/USDT", "ETH/USDT", "SOL/USDT"]
TIMEFRAME = os.getenv("TIMEFRAME", "15m")
PAPER_BALANCE = float(os.getenv("PAPER_BALANCE", "1000"))
RISK_PER_TRADE = float(os.getenv("RISK_PER_TRADE", "0.01"))
LOOP_SECONDS = int(os.getenv("LOOP_SECONDS", "60"))

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
