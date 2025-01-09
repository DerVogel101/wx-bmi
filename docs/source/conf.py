# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath('../../layout'))
sys.path.insert(0, os.path.abspath('../..'))

project = 'wx-bmi'
copyright = '2025, DerVogel101 & KyattsuNoTsume'
author = 'DerVogel101 & KyattsuNoTsume'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.todo',
        'sphinx.ext.viewcode',
        'sphinx.ext.napoleon',
        'sphinx.ext.autosummary',
        'sphinx.ext.autodoc.typehints'
]

templates_path = ['_templates']
exclude_patterns = [".vscode", "__pycache__", ".idea"]

autodoc_default_options = {
    'undoc-members': True,
    'private-members': True,
}

todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
