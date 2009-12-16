import logging
import logging.handlers

from errorstack import settings

if settings.STACK_KEY is None:
    raise ImproperlyConfigured('ErrorStackHandler requires the '
                               'ERRORSTACK_STACK_KEY setting.')

# This code modified from Python example at errorstack.com
class ErrorStackHandler(logging.handlers.HTTPHandler):
    def mapLogRecord(self, record):
        """ Define the values submitted to ErrorStack.com. """
        keys = ['name', 'msg', 'levelname', 'module', 'pathname', 'funcName',
                'lineno', 'args', 'exc_text', 'threadName', 'thread', 'process',
                'asctime']
        info = {}
        for key in keys:
            info[key] = record.__dict__.get(key, '')
        return info

errorstack_handler = ErrorStackHandler(
    "www.errorstack.com",
    "/submit?_s=%s&_r=json" % settings.STACK_KEY,
    "POST")
errorstack_handler.setLevel(logging.ERROR)

logger = logging.getLogger(settings.LOGGER_NAME)
logger.addHandler(errorstack_handler)
