README File
###########
Each PyAnsys project should have a README file in the root directory. 
To create this file, use either `reStructuredText Markup Syntax`_ to 
create a file named ``README.rst`` or `Markdown Syntax`_ to create a file 
named ``README.md``

While Markdown syntax has better GitHub support, text in RST files can 
be reused within Sphinx documentation, which avoids duplicating any 
auto-generated Sphinx pages. For example, see `pyansys-sphinx-theme index.rst`_.

.. _pyansys-sphinx-theme index.rst: https://github.com/pyansys/pyansys-sphinx-theme/blob/main/doc/source/index.rst
.. _reStructuredText Markup Syntax: https://docutils.sourceforge.io/rst.html
.. _Markdown Syntax: https://www.markdownguide.org/basic-syntax/


The README file should at the minimum contain these elements:

- PyAnsys library title
- General description
- Installation directions (via ``pip install`` and ``git clone``)
- Basic usage
- Links to the full documentation

The README file is also reused within the ``long_description`` in
the package's ``setup.py`` file.
