import logging

from django.http import Http404
from django.core.exceptions import MiddlewareNotUsed, ImproperlyConfigured
from django.conf import settings as django_settings

from errorstack import settings
from errorstack.handlers import logger

class ErrorStackMiddleware(object):

    def __init__(self):
        if settings.STACK_KEY is None:
            raise ImproperlyConfigured('ErrorStackMiddleware requires the '
                                       'ERRORSTACK_STACK_KEY setting.')
        if django_settings.DEBUG:
            raise MiddlewareNotUsed

    def process_exception(self, request, exception):
        if not settings.CATCH_404 and isinstance(exception, Http404):
            return

        logger.error('Unhandled exception', exc_info=True)
