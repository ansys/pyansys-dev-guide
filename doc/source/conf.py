"""Sphinx documentation configuration file for the pyansys developer's guide."""
from datetime import datetime

from pyansys_sphinx_theme import __version__
from pyansys_sphinx_theme import pyansys_logo_black

# Project information
project = "PyAnsys Developer's Guide"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "Ansys Inc."
release = version = "0.3.dev0"

html_logo = pyansys_logo_black
html_theme = "pyansys_sphinx_theme"

html_theme_options = {
    "github_url": "https://github.com/pyansys/dev-guide",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "additional_breadcrumbs": [
        ("PyAnsys", "https://docs.pyansys.com/"),
    ],
}

# necessary for proper breadcrumb title
html_short_title = html_title = project

# Sphinx extensions
extensions = [
    "sphinx_copybutton",
    "sphinx_toolbox.collapse",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.graphviz",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinxcontrib.mermaid",
    "sphinx_tabs.tabs",
]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/dev", None),
    "grantami-bomanalytics": ("https://grantami.docs.pyansys.com", None),
    # "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    # "numpy": ("https://numpy.org/devdocs", None),
    # "matplotlib": ("https://matplotlib.org/stable", None),
    # "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    # "pyvista": ("https://docs.pyvista.org/", None),
}

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        f"pyansys_dev_guide_v{version}.tex",
        "PyAnsys Developer's Guide",
        author,
        "manual",
    ),
]


# # -- Options for manual page output ------------------------------------------

# # One entry per manual page. List of tuples
# # (source start file, name, description, authors, manual section).
# man_pages = [
#     (master_doc, 'ansys.mapdl.core', 'ansys.mapdl.core Documentation',
#      [author], 1)
# ]


# # -- Options for Texinfo output ----------------------------------------------

# # Grouping the document tree into Texinfo files. List of tuples
# # (source start file, target name, title, author,
# #  dir menu entry, description, category)
# texinfo_documents = [
#     (master_doc, 'ansys.mapdl.core', 'ansys.mapdl.core Documentation',
#      author, 'ansys.mapdl.core', 'Pythonic interface to MAPDL using gRPC',
#      'Engineering Software'),
# ]

# Include numerical references for the figures
numfig = True

# Do not include the following patterns as documentation source files.
# See issue: https://github.com/sphinx-doc/sphinx/issues/1668
exclude_patterns = ["packaging/diagrams/*", "packaging/resources/*"]
