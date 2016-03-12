# -*- coding: utf-8 -*-
# Copyright (c) 2014 Raphaël Barrois
# This code is distributed under the two-clause BSD License.

try:  # pragma: no cover
    import django
    django_loaded = True
except ImportError:  # pragma: no cover
    django_loaded = False
    django = None


if django_loaded:
    from django.conf import settings
    if not settings.configured:
        settings.configure(
            DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3'}},
            INSTALLED_APPS=['tests.django_test_app'],
            MIDDLEWARE_CLASSES=[],
        )
    django.setup()
