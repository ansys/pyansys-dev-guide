from datetime import datetime

# Project information
project = 'PyAnsys Developers Guide'
copyright = f'{datetime.now().year}, ANSYS'
author = 'ANSYS, Inc.'
release = version = '0.1.dev0'

html_logo = 'https://docs.pyansys.com/_static/pyansys-logo-black-cropped.png'
html_theme = 'pyansys_sphinx_theme'

html_theme_options = {
    "github_url": "https://github.com/pyansys/about",
    "show_prev_next": False
}

# Sphinx extensions
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'


master_doc = 'index'

latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc,
     f'pyansys_dev_guide_v{version}.tex',
     "PyAnsys Developer's Guide",
     author,
     'manual'),
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
