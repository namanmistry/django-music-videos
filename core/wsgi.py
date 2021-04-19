"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from pathlib import Path

sys.path.append('D:/django video songs/core')
sys.path.append('D:/django video songs/core/core')

# Add project directory to the sys.path
path_home = str(Path(__file__).parents[1])
path = 'D:/django video songs/core'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()
