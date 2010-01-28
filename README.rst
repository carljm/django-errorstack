=================
django-errorstack
=================

A Django reusable application for logging errors to the `ErrorStack`_
service.

.. _ErrorStack: http://www.errorstack.com/

Installation
============

Install from PyPI with ``easy_install`` or ``pip``::

    pip install django-errorstack

or get the `in-development version`_::

    pip install django-errorstack==tip

.. _in-development version: http://bitbucket.org/carljm/django-errorstack/get/tip.gz#egg=django_errorstack-tip

Dependencies
------------

``django-errorstack`` requires `Django`_ 1.0 or later.

.. _Django: http://www.djangoproject.com/

Usage
=====

To use ``django-errorstack`` in your Django project:

    1. Add ``'errorstack'`` to your ``INSTALLED_APPS`` setting.

    2. Set the `ERRORSTACK_STACK_KEY`_ setting.

    3. Add ``errorstack.middleware.ErrorStackMiddleware`` to the end
       of your ``MIDDLEWARE_CLASSES`` setting.

When ``DEBUG`` is False, all unhandled view exceptions will be logged
to ErrorStack. Error handling will otherwise proceed as it would
otherwise: ``django-errorstack`` does not disable or modify Django's
usual error handling.

Logging errors manually
-----------------------

You may want to log some errors to ErrorStack in your own code,
without raising an unhandled exception or displaying a 500 page to
your user.

``django-errorstack`` uses a named logger from the Python standard
library ``logging`` module. The name of the logger is defined by the
`ERRORSTACK_LOGGER_NAME` setting (defaults to "errorstack"). Assuming
you don't change the setting, you could log errors yourself like this::

    import logging

    logger = logging.getLogger("errorstack")

    try:
        #... some code that raises an exception
    except:
        logger.error("Something bad happpened.", exc_info=True)

This logger only sends errors or critical errors (not warnings or info
or debug messages) to ErrorStack.

Attaching the ErrorStack handler to your own logger
---------------------------------------------------

Your application may already use the stdlib ``logging`` module with
your own named loggers. If you want to attach the ErrorStack logger
handler to your own loggers, you can do the following::

    import logging

    from errorstack.handlers import errorstack_handler

    logger = logging.getLogger("my_logger")
    logger.addHandler(errorstack_handler)

Again, this handler only listens for errors or critical errors.

Settings
========

ERRORSTACK_STACK_KEY
--------------------

The key of the error stack you want to send errors to. This option is
required.

ERRORSTACK_CATCH_404
--------------------

Log ``Http404`` exceptions to ErrorStack if this is
``True``. ``False`` by default.

ERRORSTACK_LOGGER_NAME
----------------------

The logger name to use. Defaults to "errorstack".
