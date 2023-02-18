# -*- coding: utf-8 -*-
#
# pyOpenMS documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  1 15:50:55 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import subprocess
import glob
import shutil
import urllib.request
import contextlib
import sys

# import sys
# sys.path.insert(0, os.path.abspath('.'))
from platform import python_version_tuple
from sys import platform

sys.path.append(os.path.abspath("./_ext"))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_copybutton',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'notfound.extension',
    'sphinx_inline_tabs',
    'sphinx_search.extension',
    'glossary_warnings',
    'hoverxref.extension',
]

autosummary_generate = True
autosummary_imported_members = True
autodoc_docstring_signature = True

#configure tooltips
hoverxref_roles = ['term',]
hoverxref_role_types = {'term':'tooltip',}
#specific for pyopenms documentation
hoverxref_tooltip_lazy = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'pyOpenMS'
copyright = u'2023, OpenMS Team'
author = u'OpenMS Team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'2.8.0'
# The full version, including alpha/beta/rc tags.
release = u'2.8.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

html_favicon = '../assets/logo/OpenMS_transparent_background.png'
html_logo = '../assets/logo/OpenMS_transparent_background.png'

html_theme_options = {
    "navigation_with_keys": True,
    "light_css_variables": {
        "font-stack--monospace": "Consolas, monospace",
        "font-size--small": "90%",
        "toc-font-size": "87.5%",
        "color-announcement-background": "#bbbbbb",
        "color-announcement-text": "#ffffff"
    },
    "announcement": """
    <a style=\"text-decoration: none;\"
       href=\"https://mybinder.org/v2/gh/OpenMS/pyopenms-extra/master+ipynb?urlpath=lab/tree/docs/source/index.ipynb\">
       Try Online With Binder
    </a>
    """,
}
pygments_style = 'sas'

pygments_dark_style = 'rrt'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pyOpenMSdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'pyOpenMS.tex', u'pyOpenMS Documentation',
     u'OpenMS Team', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pyopenms', u'pyOpenMS Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'pyOpenMS', u'pyOpenMS Documentation',
     author, 'pyOpenMS', 'One line description of project.',
     'Miscellaneous'),
]


def setup(app):
    app.add_css_file('custom.css')
    app.add_js_file('piwik.js')
