"""Sphinx documentation configuration file for the PyAnsys developer's guide."""

from datetime import datetime
import os

from ansys_sphinx_theme import (
    __version__,
    ansys_favicon,
    ansys_logo_white,
    ansys_logo_white_cropped,
    pyansys_logo_black,
    watermark,
)
from ansys_sphinx_theme.latex import generate_preamble
import pyvista
from sphinx_gallery.sorting import FileNameSortKey

# Project information
project = "PyAnsys developer's guide"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "Ansys Inc."
release = version = datetime.now().strftime("%Y-%m-%d")

html_theme = "ansys_sphinx_theme"
html_favicon = ansys_favicon
html_context = {
    "github_user": "pyansys",
    "github_repo": "dev-guide",
    "github_version": "main",
    "doc_path": "doc/source",
}

html_theme_options = {
    "logo": "pyansys",
    "github_url": "https://github.com/ansys/dev-guide",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "use_edit_page_button": True,
    "additional_breadcrumbs": [
        ("PyAnsys", "https://docs.pyansys.com/"),
    ],
    "icon_links": [
        {
            "name": "Contribute",
            "url": "https://dev.docs.pyansys.com/how-to/contributing.html",
            "icon": "fa fa-wrench",
        },
    ],
    "use_meilisearch": {
        "api_key": os.getenv("MEILISEARCH_PUBLIC_API_KEY", ""),
        "index_uids": {
            "pyansys-dev-guide": "PyAnsys dev guide",
        },
    },
}

# necessary for proper breadcrumb title
html_short_title = html_title = project

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
    "sphinx_gallery.gen_gallery",
]

# -- Sphinx Gallery Options ---------------------------------------------------
sphinx_gallery_conf = {
    # path to your examples scripts
    "examples_dirs": ["../../examples"],  # ["../../examples/"],
    # path where to save gallery generated examples
    "gallery_dirs": ["examples"],
    # Pattern to search for example files
    "filename_pattern": r"\.py",
    # Remove the "Download all examples" button from the top level gallery
    "download_all_examples": False,
    # Remove sphinx configuration comments from code blocks
    "remove_config_comments": True,
    # Sort gallery example by file name instead of number of lines (default)
    "within_subsection_order": FileNameSortKey,
    # directory where function granular galleries are stored
    "backreferences_dir": None,
    # Modules for which function level galleries are created.  In
    "doc_module": "dev-guide",
    "image_scrapers": ("pyvista", "matplotlib"),
}

# Ensure that offscreen rendering is used for docs generation
# Preferred plotting style for documentation
pyvista.BUILDING_GALLERY = True
pyvista.OFF_SCREEN = True

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/dev", None),
    "grantami-bomanalytics": (
        "https://bomanalytics.grantami.docs.pyansys.com/version/stable",
        None,
    ),
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
    "how-to/api/ansys_sphinx_theme.examples.samples.Complex.abs.rst",
    "how-to/api/ansys_sphinx_theme.examples.samples.Complex.imag.rst",
    "how-to/api/ansys_sphinx_theme.examples.samples.Complex.real.rst",
    "links.rst",
]

# make rst_epilog a variable, so you can add other epilog parts to it
rst_epilog = ""

# Read link all targets from file
with open("links.rst") as f:
    rst_epilog += f.read()

# Fix excessive margins in mermaid output.
# See issue: https://github.com/mermaid-js/mermaid/issues/1800#issuecomment-741617143
mermaid_output_format = "png"
mermaid_params = ["--width", "2000", "--backgroundColor", "white"]

# Graphviz diagrams configuration
graphviz_output_format = "png"

# Generate section labels up to four levels deep
autosectionlabel_maxdepth = 4

# TODO: warning suppression is temporary till https://github.com/ansys/dev-guide/issues/64
# gets fully implemented.
suppress_warnings = ["autosectionlabel.*"]

# Generate the LaTeX preamble
latex_additional_files = [watermark, ansys_logo_white, ansys_logo_white_cropped]
latex_elements = {"preamble": generate_preamble(html_title)}

# Linkcheck configuration
linkcheck_ignore = [
    "https://pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi",  # Private URL hosting PyAnsys packages
    "https://github.com/ansys-internal/.*",  # Private URL
    "https://myapps.microsoft.com/signin/8f67c59b-83ac-4318-ae96-f0588382ddc0?tenantId=34c6ce67-15b8-4eff-80e9-52da8be89706",  # Join Ansys GitHub account
    "https://myapps.microsoft.com/signin/42c0fa04-03f2-4407-865e-103af6973dae?tenantId=34c6ce67-15b8-4eff-80e9-52da8be89706",  # Join Ansys internal GitHub account
]

# Linkcheck ignore broken anchors
linkcheck_anchors_ignore = [
    # these anchors are picked by linkcheck as broken but they are not.
    "38-comments-and-docstrings",
]

linkcheck_anchors_ignore_for_url = ["https://github.com/ansys/ansys-api-template"]
