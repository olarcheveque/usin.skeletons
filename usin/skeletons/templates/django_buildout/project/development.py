# -*- coding: utf-8 -*-

from project.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

#INTERNAL_IPS = ('127.0.0.1',)
#INSTALLED_APPS += ('debug_toolbar',)
#MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

AUTH_PASSWORD_REQUIRED = False
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
