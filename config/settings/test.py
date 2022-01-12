"""
With these settings, tests run faster.
"""
import environ  # to avoid flake 8 * import check

from .base import *  # noqa

# GENERAL
# ------------------------------------------------------------------------------
env = environ.Env()
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="o&9-xt)9o3aj28&hs=1i_x1dpfos^@8rkz%r-w6qr86m*hrsdb",
)

# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"
