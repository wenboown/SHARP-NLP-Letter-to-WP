# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'SUPPLEMENTARY MATERIAL: Are language deficits associated with psychosis risk universal? Automated analyses of spoken language in Mandarin-speaking youths at clinical high risk for psychosis, by Agurto et al.'
copyright = '2022 IBM, Bo Wen'
author = """Carla Agurto, Raquel Norel, Bo Wen, Yanyan Wei, Dan Zhang, Zarina Bilgrami, Xiaolu Hsi, Tianhong Zhang, Ofer Pasternak, Huijun Li, Matcheri Keshavan, Larry J. Seidman, Susan Whitfield-Gabrieli, Martha E. Shenton, Margaret A. Niznikiewicz, Jijun Wang, Guillermo Cecchi, Cheryl M. Corcoran, William S. stone."""


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx_rtd_theme"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
