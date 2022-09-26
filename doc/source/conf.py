"""Sphinx documentation configuration file for the pyansys developer's guide."""
from datetime import datetime

from ansys_sphinx_theme import (
    __version__,
    ansys_logo_white,
    ansys_logo_white_cropped,
    pyansys_logo_black,
    watermark,
)
from ansys_sphinx_theme.latex import generate_preamble

from sphinx_gallery.sorting import FileNameSortKey

# Project information
project = "PyAnsys Developer's Guide"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "Ansys Inc."
release = version = "0.3.dev0"

html_logo = pyansys_logo_black
html_theme = "ansys_sphinx_theme"

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

html_static_path = ["_static"]


html_css_files = [
    "css/ansys.css",
]


# Sphinx extensions
extensions = [
    "sphinx_copybutton",
    "sphinx_toolbox.collapse",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.graphviz",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinxcontrib.mermaid",
    "sphinx_design",
    'sphinx_gallery.gen_gallery',
]

# -- Sphinx Gallery Options ---------------------------------------------------
sphinx_gallery_conf = {
    # convert rst to md for ipynb
    "pypandoc": True,
    # path to your examples scripts
    "examples_dirs": ["examples"],  # ["../../examples/"],
    # path where to save gallery generated examples
    "gallery_dirs": ["_automodule/examples"],
    # Patter to search for example files
    "filename_pattern": r"\.py",
    # Remove the "Download all examples" button from the top level gallery
    "download_all_examples": False,
    # Sort gallery example by file name instead of number of lines (default)
    "within_subsection_order": FileNameSortKey,
    # directory where function granular galleries are stored
    "backreferences_dir": None,
    # Modules for which function level galleries are created.  In
    "doc_module": "examples",
    # "image_scrapers": ("pyvista", "matplotlib"),
    "image_scrapers": ("matplotlib"),
    "ignore_pattern": "flycheck*",
    "thumbnail_size": (350, 350),
}

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
exclude_patterns = [
    "packaging/diag/*",
    "packaging/code/*",
    "how-to/diag/*",
    "how-to/api/ansys_sphinx_theme.samples.Complex.abs.rst",
    "how-to/api/ansys_sphinx_theme.samples.Complex.imag.rst",
    "how-to/api/ansys_sphinx_theme.samples.Complex.real.rst",
]

# Fix excessive margins in mermaid output.
# See issue: https://github.com/mermaid-js/mermaid/issues/1800#issuecomment-741617143
mermaid_output_format = "png"
mermaid_params = ["--width", "2000", "--backgroundColor", "white"]

# Graphviz diagrams configuration
graphviz_output_format = "png"

# Generate section labels up to four levels deep
autosectionlabel_maxdepth = 4

# TODO: warning suppression is temporary till https://github.com/pyansys/dev-guide/issues/64
# gets fully implemented.
suppress_warnings = ["autosectionlabel.*"]

# Generate the LaTeX preamble
latex_additional_files = [watermark, ansys_logo_white, ansys_logo_white_cropped]
latex_elements = {"preamble": generate_preamble(html_title)}
