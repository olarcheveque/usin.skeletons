#!${buildout:executable}
# vim: set filetype=python:

# -*- coding: utf-8 -*-

import os
import sys

sys.path[0:0] = (os.path.dirname(__file__), )

import setupenv
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.${settings}'

application = django.core.handlers.wsgi.WSGIHandler()
