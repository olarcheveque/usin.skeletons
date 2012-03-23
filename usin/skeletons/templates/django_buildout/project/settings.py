# -*- coding: utf-8 -*-

import os
from conf import *
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as DEFAULT_TEMPLATE_CONTEXT_PROCESSORS 

PROJECT_ROOT = os.path.join(os.path.dirname(__file__))
SITE_ROOT = os.path.join(os.path.dirname(PROJECT_ROOT))

ROOT_URLCONF = 'project.urls'

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'south',
)


STATIC_ROOT = os.path.join(SITE_ROOT, 'www_static')
STATIC_URL = '/static/'
#STATICFILES_DIRS = (
#    os.path.join(PROJECT_ROOT, 'static'),
#)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

ADMIN_TOOLS_INDEX_DASHBOARD = 'project.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'project.dashboard.CustomAppIndexDashboard'
