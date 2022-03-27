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
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Combustion Toolbox'
copyright = '2022, Alberto Cuadra Lara'
author = 'Alberto Cuadra Lara'

# The full version, including alpha/beta/rc tags
release = '0.9.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',   # for enumeration of objects stuff
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'nbsphinx',
    'sphinx_togglebutton',
    # 'sphinxcontrib.fulltoc', # for sidebar TOC
    'sphinxcontrib.matlab', # support for Matlab
    'sphinx.ext.napoleon',  # support for shorthand syntax
    'sphinx.ext.mathjax',   # LaTeX support
    'texext.math_dollar',   # lightweight LaTeX filter
    'ablog',
]

autodoc_default_options = {'members': True, 'show-inheritance': True}
autosummary_generate = True

matlab_keep_package_prefix = False

matlab_src_dir = os.path.dirname(os.path.abspath(__file__ + "/"))+"/../src" # ... from the point of view of the generated/sphinx folder
primary_domain = 'mat'
default_role = 'obj'

source_suffix = ['.rst', '.md']


# The master toctree document.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store', 'src']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

numfig = True
highlight_language = "matlab"
nitpicky = True