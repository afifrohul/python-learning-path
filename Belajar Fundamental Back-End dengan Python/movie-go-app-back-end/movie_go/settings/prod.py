import os
import sys

from .common import *

from loguru import logger

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.loguru import LoguruIntegration

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    '127.0.0.1',
    '34.128.96.165'
]

# =========================
# SENTRY
# =========================

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),

    integrations=[
        DjangoIntegration(),

        LoguruIntegration(
            level="INFO",
            event_level="ERROR",
        ),
    ],

    traces_sample_rate=1.0,
    send_default_pii=True,
)

# =========================
# LOGURU
# =========================

logger.remove()

# Console log
logger.add(
    sys.stdout,
    level="INFO",
)

# Error log file
logger.add(
    "logs/error.log",
    rotation="500 MB",
    level="ERROR",
    backtrace=True,
    diagnose=True,
)

# App log file
logger.add(
    "logs/app.log",
    rotation="1 day",
    level="INFO",
)