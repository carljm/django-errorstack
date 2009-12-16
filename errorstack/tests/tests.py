import datetime
import os

from django.conf import settings as django_settings

if not django_settings.configured:
    django_settings.configure(
        DATABASE_ENGINE='sqlite3',
        INSTALLED_APPS=(
            'errorstack',
        ),
    )

from django.test import TestCase

__all__ = []

# TODO!
