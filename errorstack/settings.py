from django.conf import settings

STACK_KEY = getattr(settings, 'ERRORSTACK_STACK_KEY', None)
CATCH_404 = getattr(settings, 'ERRORSTACK_CATCH_404', False)
LOGGER_NAME = getattr(settings, 'ERRORSTACK_LOGGER_NAME', 'errorstack')
