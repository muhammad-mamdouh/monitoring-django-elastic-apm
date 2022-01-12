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
