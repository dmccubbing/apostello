import os
import channels.asgi
from apostello.loaddotenv import loaddotenv

if os.environ.get('DYNO_RAM') is None:
    loaddotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.dev")
channel_layer = channels.asgi.get_channel_layer()
