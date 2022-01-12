"""
With these settings, tests run faster.
"""

from .base import *  # noqa

# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"
