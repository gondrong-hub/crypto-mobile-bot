[app]
android.accept_sdk_license = True
title = Crypto Mobile Bot
package.name = cryptomobilebot
package.domain = org.cryptomobile
source.dir = .
source.include_exts = py,json,txt
version = 1.0
requirements = python3==3.11.9,kivy,python-dotenv
orientation = portrait
services = bot:service.py:foreground:sticky
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0
