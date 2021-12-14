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
from os import path

from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
from sphinx.application import Sphinx

base_path = path.abspath(path.join(__file__, '../../..'))

# -- Project information -----------------------------------------------------
project = 'Sphinx Inplace'
copyright = '2021, Haoyu Pan'
author = 'panhaoyu.china@outlook.com'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'recommonmark',
    # 'numpydoc',
    'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en_US'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The homepage will be rendered independently.
# html_additional_pages = {'index': 'index.html'}

# Change the name of the generated home page for fear that it will cause interruption.
master_doc = 'contents'

add_module_names = False

# If you want to use to do plugin
# todo_include_todos = True

# recommonmark plugin supports both *.md and *.rst files.
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# show the docstring of class and the ``__init__`` method of the class.
autoclass_content = 'both'

# The order of generated documentation will be the same as the source code.
autodoc_member_order = 'bysource'

# The style
# html_style = 'css/style.css'

# show the author indicated by ``.. sectionauthor``
show_authors = True

source_parsers = {
    '.md': CommonMarkParser,
}


def setup(app: Sphinx):
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
    }, True)
    app.add_transform(AutoStructify)
