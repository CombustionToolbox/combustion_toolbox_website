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
import requests

# sys.path.append('sphinxext')
# from sphinxext.github_linkcode import github_linkcode_resolve

# sys.path.insert(0, os.path.abspath(os.path.join('..', '..', '..')))

# tell Sphinx matlab extension where to find matlab code.
matlab_src_dir = os.path.abspath(os.path.join('..', '..'))

# -- Project information -----------------------------------------------------

project = 'Combustion Toolbox'
copyright = '2022, Alberto Cuadra Lara'
author = 'Alberto Cuadra Lara'

# The full version, including alpha/beta/rc tags
url = 'https://github.com/AlbertoCuadra/combustion_toolbox/releases/latest'
r = requests.get(url)
release = r.url.split('/')[-1]


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',   # for enumeration of objects stuff
    # 'sphinx.ext.autosummary',
    'nbsphinx',
    'sphinx_togglebutton',
    # 'sphinxcontrib.fulltoc', # for sidebar TOC
    'sphinxcontrib.matlab', # support for Matlab
    # 'github',
    # 'sphinx.ext.linkcode',
    'sphinx.ext.napoleon',  # support for shorthand syntax
    'sphinx.ext.mathjax',   # LaTeX support
    'texext.math_dollar',   # lightweight LaTeX filter
    'sphinx_toolbox.collapse', # collapse long sections
]

# Other settings
default_role = 'obj'
numfig = True
highlight_language = "matlab"

source_suffix = ['.rst', '.md']

nitpicky = True
nitpick_ignore = [
    ('mat:obj', 'struct'),
    ('mat:obj', 'str'),
    ('mat:obj', 'float'),
    ('mat:obj', 'cell'),
    ('mat:obj', 'cell or struct'),
    ('mat:obj', 'any'),
]

def linkcode_resolve(domain, info):
    return github_linkcode_resolve(
            domain=domain,
            info=info,
            allowed_module_names=['src'],
            github_org_id='combustion_toolbox',
            github_repo_id='combustion_toolbox_website',
            branch='master',
            source_prefix='')

# Autodoc settings

autodoc_default_options = {'members': True, 'show-inheritance': True}
autosummary_generate = True
# remove path in function names
add_module_names = False

# Matlab domain settings

matlab_keep_package_prefix = False
primary_domain = 'mat'



# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store', 'source']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_space = ' '
html_title = project + html_space + release

html_css_files = [
    'css/style.css',
]

html_theme_options = {
    "light_logo": "img/logo_CT.svg",
    "dark_logo": "img/logo_CT.svg",
}