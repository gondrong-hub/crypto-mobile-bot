from urllib.parse import urlencode
from urllib.request import Request, urlopen
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send(text):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = urlencode({
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }).encode("utf-8")

    request = Request(url, data=data, method="POST")
    with urlopen(request, timeout=15):
        pass
