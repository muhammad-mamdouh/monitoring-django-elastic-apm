from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="1ZDUIHYgHDmOob3lpmtDWkr2Im6cp2UpUgdx5lMTXJipJGXByKdm8ZpYGREcJui3",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa F405
