from .base import *

DEBUG = False

ALLOWED_HOSTS = []

import django_heroku
django_heroku.settings(locals())