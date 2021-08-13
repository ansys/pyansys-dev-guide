from pyansys_sphinx_theme import __version__

# Project information
project = 'pyansys_sphinx_theme'
copyright = '2021, ANSYS'
author = 'PyAnsys Open Source Developers'
release = version = __version__

# optionally use the default pyansys logo
html_logo = 'https://docs.pyansys.com/_static/pyansys-logo-black-cropped.png'

html_theme = 'pyansys_sphinx_theme'

# specify the location of your github repo
html_theme_options = {
    "github_url": "https://github.com/pyansys/pyansys-sphinx-theme",
    "show_prev_next": False
}

# Sphinx extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
]

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

