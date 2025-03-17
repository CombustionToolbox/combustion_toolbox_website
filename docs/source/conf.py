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

sys.path.append('sphinxext')
from github_linkcode import github_linkcode_resolve

# Correct path for autodoc
sys.path.insert(0, os.path.abspath(os.path.join('..', '..', '..')))

# tell Sphinx matlab extension where to find matlab code.
matlab_src_dir = os.path.abspath('../..')

# -- Project information -----------------------------------------------------

project = 'Combustion Toolbox'
project_acronym = 'CT'
copyright = '2022-2025, Alberto Cuadra Lara'
author = 'Alberto Cuadra Lara'

# The full version, including alpha/beta/rc tags
url = 'https://github.com/CombustionToolbox/combustion_toolbox/releases/latest'
r = requests.get(url)
release = r.url.split('/')[-1]
# release = 'v1.0.03'

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
    'sphinxcontrib.matlab',    # support for MATLAB
    'sphinx.ext.linkcode',     # to link code to the repository
    # 'sphinx.ext.viewcode',     # view source code (local files)
    'sphinx.ext.napoleon',     # support for shorthand syntax
    'sphinx.ext.mathjax',      # LaTeX support
    'texext.math_dollar',      # lightweight LaTeX filter
    'sphinx_toolbox.collapse', # collapse long sections
    'sphinx_copybutton',
    'sphinx_design',
    # "sphinxext.opengraph",
    # "sphinx_inline_tabs",
    'sphinxcontrib.bibtex',    # support for bibtex
]

myst_enable_extensions = [
    'colon_fence',
    'substitution',
]

myst_substitutions = {
    'author': author,
    'version': release,
    'copyright': 'Copyright © 2022-2025',
    'project': project,
    'affiliation': 'Grupo de Mecánica de Fluidos, Universidad Carlos III, Av. Universidad 30, 28911, Leganés, Spain',
}

# Other settings
myst_heading_anchors = 4
bibtex_bibfiles = ['refs.bib']
bibtex_reference_style = 'author_year'

default_role = 'obj'
numfig = True
highlight_language = 'matlab'
sd_fontawesome_latex = True

source_suffix = ['.rst', '.md']

nitpicky = True
nitpick_ignore = [
    ('mat:obj', 'struct'),
    ('mat:obj', 'str'),
    ('mat:obj', 'float'), ('mat:obj', 'double'),
    ('mat:obj', 'cell'),
    ('mat:obj', 'cell or struct'),
    ('mat:obj', 'any'),
    ('mat:obj', 'none'),
    ('mat:obj', 'bool'),
    ('mat:obj', 'function'),
    ('mat:obj', 'file'),
    ('mat:obj', 'obj'),
    ('mat:obj', 'object'),
    ('mat:obj', 'char'),
    ('mat:obj', 'empty'),
    ('mat:class', 'matlab.apps.AppBase'),
    ('mat:class', 'handle'), ('mat:class', 'matlab.mixin.Copyable'), 
    ('mat:obj', 'Database'), ('mat:func', 'Database'), ('mat:class', 'combustiontoolbox.databases.Database'), ('mat:class', 'Database'),
    ('mat:obj', 'NasaDatabase'), ('mat:func', 'NasaDatabase'), ('mat:class', 'combustiontoolbox.databases.NasaDatabase'), ('mat:class', 'NasaDatabase'),
    ('mat:obj', 'BurcatDatabase'), ('mat:func', 'BurcatDatabase'), ('mat:class', 'combustiontoolbox.databases.BurcatDatabase'), ('mat:class', 'BurcatDatabase'),
    ('mat:obj', 'Elements'), ('mat:func', 'Elements'), ('mat:class', 'combustiontoolbox.core.Elements'), ('mat:class', 'Elements'),
    ('mat:obj', 'Species'), ('mat:func', 'Species'), ('mat:class', 'combustiontoolbox.core.Species'), ('mat:class', 'Species'),
    ('mat:obj', 'ChemicalSystem'), ('mat:func', 'ChemicalSystem'), ('mat:class', 'combustiontoolbox.core.ChemicalSystem'), ('mat:class', 'ChemicalSystem'),
    ('mat:obj', 'Mixture'), ('mat:func', 'Mixture'), ('mat:class', 'combustiontoolbox.core.Mixture'), ('mat:class', 'Mixture'),
    ('mat:obj', 'EquilibriumSolver'), ('mat:func', 'EquilibriumSolver'), ('mat:class', 'combustiontoolbox.equilibrium.EquilibriumSolver'), ('mat:class', 'EquilibriumSolver'),
    ('mat:obj', 'ShockSolver'), ('mat:func', 'ShockSolver'), ('mat:class', 'combustiontoolbox.shockdetonation.ShockSolver'), ('mat:class', 'ShockSolver'),
    ('mat:obj', 'DetonationSolver'), ('mat:func', 'DetonationSolver'), ('mat:class', 'combustiontoolbox.shockdetonation.DetonationSolver'), ('mat:class', 'DetonationSolver'),
    ('mat:obj', 'RocketSolver'), ('mat:func', 'RocketSolver'), ('mat:class', 'combustiontoolbox.rocket.RocketSolver'), ('mat:class', 'RocketSolver'),
    ('mat:func', 'solve'), 
    ('mat:func', 'solveArray'),
    ('mat:func', 'report')
]
    
# Define routine to link functions to their files on GitHub
def linkcode_resolve(domain, info):
    return github_linkcode_resolve(
            domain=domain,
            info=info,
            allowed_module_names=[],
            github_org_id='CombustionToolbox',
            github_repo_id='combustion_toolbox',
            branch='master')
            # source_prefix='')

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = False
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'autodoc_member_order': 'groupwise',
    'show-inheritance': True,
    'autoclass_content': 'class',
    'private-members': True
}

autosummary_generate = True

# remove path in function names
add_module_names = False

# Matlab domain settings
matlab_short_links = True
matlab_auto_link = "all"
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
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store', '_static']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ['_static']

html_space = ' '
html_title = project + html_space + release

# Define favicon (relative to the path)
html_favicon = '_static/img/favicon.ico'

html_show_sphinx = True

html_css_files = [
    'css/style.css',
]

# templates_path = ["_templates"]
# html_additional_pages = {
#    "index": "landing_page.html"
# }

html_theme_options = {
    "announcement": '<a class="no-underline"; href="https://www.researchgate.net/publication/371351094_Combustion_Toolbox_An_open-source_thermochemical_code_for_gas-and_condensed-phase_problems_involving_chemical_equilibrium"; target="_blank"> The preprint of the Combustion Toolbox v1.1.0 article is now available on ResearchGate!</a>',
    "sidebar_hide_name": True,
    'light_logo': 'img/logo_CT_version.svg',
    'dark_logo': 'img/logo_CT_version_dark.svg',
    'footer_icons': [
        {
            'name': 'Email',
            'url': 'mailto:acuadra@ing.uc3m.es',
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
                <path d="M464 64C490.5 64 512 85.49 512 112C512 127.1 504.9 141.3 492.8 150.4L275.2 313.6C263.8 322.1 248.2 322.1 236.8 313.6L19.2 150.4C7.113 141.3 0 127.1 0 112C0 85.49 21.49 64 48 64H464zM217.6 339.2C240.4 356.3 271.6 356.3 294.4 339.2L512 176V384C512 419.3 483.3 448 448 448H64C28.65 448 0 419.3 0 384V176L217.6 339.2z"/>
                </svg>
            """,
        },
        {
            'name': 'GitHub',
            'url': 'https://github.com/CombustionToolbox/combustion_toolbox',
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
        },
    ],
    
    "navigation_with_keys": True,
    
    "light_css_variables": {
        "color-announcement-background": "#afe9ddff",
        "color-announcement-text": "#008080ff",
        "color-brand-primary": "#577A95",
        "color-brand-content": "#577A95",
        "color-problematic": "#1f8782",
        # "color-background-primary": "#0a192fff",
        # "color-background-secondary": "#172a46ff",
        "color-foreground-primary": "#323232ff",
        # "color-foreground-secondary": "#697796ff",
        # "color-background-hover": "#bac5e54a",
        # "color-sidebar-caption-text": "#44a79dff",
        # "color-background-item": "#44a79dff",
        # "sd-color-info": "#3493a3",
        # "color-code-foreground": "#172a46ff",
        # "color-code-background": "rgb(0 0 0 / 0%)",
        # "color-background-border": "rgb(0 0 0 / 0%)",
        # "color-background-item": "#44a79dff",
        # "color-foreground-muted": "#bac5e54a",
        # "color-card-background": "#172a46ff",
        # "color-highlight-on-target": "#bac5e54a",
        # "color-admonition-title--caution": "#ecb365ff",
        # "color-admonition-title-background--caution": "#ffffc02b",
        "color-inline-code-background": "#5fbcd399",
        "sd-color-info": "#264653ff",
        "sd-color-light": "rgb(0 0 0 / 0%)",
        "sd-color-light-text": "#323232ff",
    },
    
    "dark_css_variables": {
        "color-announcement-background": "#ecb365ff",
        "color-announcement-text": "#0a192fff",
        "color-brand-primary": "#bac5e5ff",
        "color-brand-content": "#44a79dff",
        "color-problematic": "#44a79dff",
        "color-background-primary": "#0a192fff",
        "color-background-secondary": "#172a46ff",
        "color-foreground-primary": "#bac5e5ff",
        "color-foreground-secondary": "#697796ff",
        "color-background-hover": "#bac5e54a",
        "color-sidebar-caption-text": "#44a79dff",
        "color-background-item": "#44a79dff",
        "sd-color-info": "#3493a3",
        "color-code-foreground": "#697796ff",
        "color-code-background": "rgb(0 0 0 / 0%)",
        "color-background-border": "rgb(0 0 0 / 0%)",
        "color-background-item": "#44a79dff",
        "color-foreground-muted": "#bac5e54a",
        "color-card-background": "#172a46ff",
        "color-highlight-on-target": "#bac5e54a",
        "color-admonition-title--caution": "#ecb365ff",
        "color-admonition-title-background--caution": "#ffffc02b",
        "color-inline-code-background": "#44475aff",
        "sd-color-info": "#44a79dff",
        "sd-color-light": "rgb(0 0 0 / 0%)",
        "sd-color-light-text": "#bac5e5ff",
    },
}

# Code block styling
pygments_style = "friendly"
pygments_dark_style = "material"

# Settings sphintext-opengraph
# ogp_site_url = "https://combustion-toolbox-website.readthedocs.io/"
# ogp_image = "http://example.org/image.png"
# ogp_description_length = 300
# ogp_type = "article"

# ogp_custom_meta_tags = [
#     '<meta property="og:ignore_canonical" content="true" />',
# ]

####################################################################################
# LaTeX configuration
####################################################################################

FLAG_UPDATE_SVG = False

# Set the directory where the SVG files are located
dir_path = '_static/img/'

# Traverse the directory tree recursively and find all SVG files
if FLAG_UPDATE_SVG:
    import cairosvg

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.svg'):
                # Generate the name of the corresponding PDF file
                pdf_file = os.path.splitext(os.path.join(root, file))[0] + '.pdf'
                # Convert the SVG file to PDF using CairoSVG
                cairosvg.svg2pdf(url=os.path.join(root, file), write_to=pdf_file)

# Set compiler
latex_engine = 'pdflatex'
latex_use_xindy = False

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '10pt'

# latex_additional_files = [
#     '_static/latex-note.png',
#     '_static/latex-warning.png',
# ]

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
  ('index_latex',
   'combustiontoolbox.tex',
   'Combustion Toolbox',
   'Alberto Cuadra Lara',
   'manual')
  ]

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_toplevel_sectioning = "section"

# If false, no module index is generated.
latex_domain_indices = False

# LaTeX preamble

_PREAMBLE = r"""
\usepackage[]{geometry}
\geometry{bindingoffset=0.45in,textheight=7.25in,hdivide={0.5in,*,0.75in},vdivide={1in,7.25in,1in},papersize={7.5in,9.25in}}
\usepackage{amsmath}
\usepackage[breaklinks]{hyperref}
\usepackage{graphicx}
\usepackage[english]{babel}
\renewcommand{\bibname}{References}
"""

latex_elements = {
    'preamble': _PREAMBLE,
    'releasename': 'Release',
    'title': r'Combustion Toolbox',
#    'pointsize':'12pt', # uncomment for 12pt version
}