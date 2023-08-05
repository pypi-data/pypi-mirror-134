# mypy: ignore-errors

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.abspath(".."))

version = Path("../sec_cik_mapper/_version.py").read_text(encoding="utf-8")
about = {}
exec(version, about)

# -- Project information -----------------------------------------------------

project = "SEC CIK Mapper 🗺"
copyright = "2022, Jad Chaar"
author = "Jad Chaar"

release = about["__version__"]

# -- General configuration ---------------------------------------------------

extensions = ["sphinx.ext.autodoc", "sphinx_autodoc_typehints", "m2r2"]

autodoc_member_order = "groupwise"

master_doc = "index"
source_suffix = [".rst", ".md"]

html_sidebars = {
    "**": ["about.html", "localtoc.html", "relations.html", "searchbox.html"]
}

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "alabaster"
html_theme_options = {
    "description": "Generate mappings between SEC identifiers using Python",
    "github_user": "jadchaar",
    "github_repo": "sec-cik-mapper",
    "github_banner": True,
    "show_related": False,
    "show_powered_by": False,
}

html_static_path = []

html_show_sourcelink = False
html_show_copyright = True
html_show_sphinx = False
