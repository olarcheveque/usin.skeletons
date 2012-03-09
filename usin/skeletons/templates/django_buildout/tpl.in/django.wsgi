#!${buildout:executable}
# vim: set filetype=python:

# -*- coding: utf-8 -*-

import setupenv
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'projects.${settings}'

application = django.core.handlers.wsgi.WSGIHandler()
