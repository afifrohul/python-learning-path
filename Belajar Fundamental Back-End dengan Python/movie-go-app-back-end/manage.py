#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from loguru import logger
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.loguru import LoguruIntegration

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_go.settings.dev')

    logger.remove()  # hapus handler bawaan
    logger.add(sys.stdout, level="INFO")  # log ke console
    logger.add("logs/error.log",
            rotation="500 MB",  # rotasi file jika mencapai 500 MB)
            level="ERROR",  # hanya log level error
            backtrace=True,
            diagnose=True)  #
    logger.add("logs/app.log",
            rotation="1 day",  # rotasi harian
            level="INFO") # hanya log level info
    
    sentry_sdk.init(
        dsn=os.getenv("SENTRY_DSN"),
        integrations=[
            DjangoIntegration(),
            LoguruIntegration(
                level="INFO",        # Minimum level for breadcrumbs
                event_level="ERROR"  # Minimum level to create a Sentry event
            ),
        ],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # If you wish to send personal data like user IDs
        send_default_pii=True
    )

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

   

if __name__ == '__main__':
    main()
