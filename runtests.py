#!/usr/bin/env python

from os.path import dirname, abspath
import sys

from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        INSTALLED_APPS=(
            'errorstack',
        ),
        ERRORSTACK_STACK_KEY='',
    )

def runtests(*test_args):
    if not test_args:
        test_args = ['errorstack']
    parent = dirname(dirname(dirname(abspath(__file__))))
    sys.path.insert(0, parent)
    from django.test.simple import run_tests
    failures = run_tests(test_args, verbosity=1, interactive=True)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
