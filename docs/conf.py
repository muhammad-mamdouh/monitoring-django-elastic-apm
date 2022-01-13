# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
import django

if os.getenv("READTHEDOCS", default=False) == "True":
    sys.path.insert(0, os.path.abspath(".."))
    os.environ["DJANGO_READ_DOT_ENV_FILE"] = "True"
    # os.environ["USE_DOCKER"] = "no"
else:
    sys.path.insert(0, os.path.abspath("/app"))
os.environ["DATABASE_URL"] = "sqlite:///readthedocs.db"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

# -- Project information -----------------------------------------------------

project = "Coding Task"
copyright = """2021, Mohamed Mamdouh"""
author = "Mohamed Mamdouh"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# The theme to use for HTML and HTML Help pages.
html_theme = "alabaster"
