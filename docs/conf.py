# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

from wxee import __version__  # noqa: E402


# -- Project information -----------------------------------------------------

project = "wxee"
copyright = "2021, Aaron Zuspan"
author = "Aaron Zuspan"
version = __version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "nbsphinx",
    "sphinx_rtd_theme",
]

autosummary_generate = True
autodoc_member_order = "bysource"

# Automatically add a Binder and Github link to all notebook example pages
nbsphinx_prolog = """
{% set docname = env.doc2path(env.docname, base=None) %}
|Colab| |Github|

.. |Github| image:: https://img.shields.io/badge/Open%20in-Github-green.svg
   :target: https://github.com/aazuspan/wxee/blob/main/docs/{{ docname }}

.. |Colab| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/aazuspan/wxee/blob/main/docs/{{ docname }}
"""

nbsphinx_epilog = """
{% set docname = env.doc2path(env.docname, base=None) %}

.. note::
   This page was auto-generated from a Jupyter notebook. For full functionality, download the
   notebook from `Github <https://github.com/aazuspan/wxee/blob/main/docs/{{ docname }}>`_ and run it in a local Python environment.
"""

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]  # , sphinx_autosummary_accessors.templates_path]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

autodoc_mock_imports = ["ee", "rasterio", "tqdm", "joblib", "plotly"]


# Workaround to make Plotly graphs appear in Jupyter notebooks.
# https://github.com/spatialaudio/nbsphinx/issues/572#issuecomment-853389268
mathjax_path = (
    "https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
)
mathjax2_config = {
    "tex2jax": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "processEscapes": True,
        "ignoreClass": "document",
        "processClass": "math|output_area",
    }
}
