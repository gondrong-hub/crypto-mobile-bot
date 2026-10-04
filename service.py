import time
from bot_service import start, is_running

start()

while is_running():
    time.sleep(5)
