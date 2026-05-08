#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from loguru import logger

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dico_event.settings')
    logger.remove()  # hapus handler bawaan
    logger.add(sys.stdout, level="INFO")  # log ke console
    logger.add("logs/error.log",
            rotation="500 MB",  # rotasi file jika mencapai 500 MB)
            level="ERROR",  # hanya log level error
            backtrace=True,
            diagnose=True)  #
    logger.add("logs/application.log",
            rotation="1 day",  # rotasi harian
            level="INFO") # hanya log level info
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
