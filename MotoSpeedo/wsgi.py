"""
WSGI config for MotoSpeedo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import time
import traceback
import signal
import sys


from django.core.wsgi import get_wsgi_application
sys.path.append('/var/www/vhosts/motospeedo')
sys.path.append('/var/www/vhosts/motospeedo/MotoSpeedoAPI/venv/lib/python3.4/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MotoSpeedo.settings")

try:
    application = get_wsgi_application()
except Exception:
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)
