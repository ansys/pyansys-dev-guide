.. _content_writing:

Content writing
===============

Earlier sections of this guide are written primarily for PyAnsys developers. While this
section on content writing is invaluable to developers drafting documentation for their
Python client libraries, it is tailored to helping those who are new to both reviewing and
writing content for these libraries. The objective is for all PyAnsys documentation to be
clear, consistent, effective, and user-friendly.

This section provides these comprehensive subsections:

- :ref:`content_contrib_setup`: Describes PyAnsys libraries to those new to contributing
  content to PyAnsys documentation and explains how to set up a content development environment.
  In addition to providing essential information for new content contributors, this subsection
  includes links to many resources relevant to its creation and maintenance.

- :ref:`rst_files_writers`: Explains how reStructuredText (RST) files define the hierarchy
  of the documentation and provide manually authored content. This sub section also explains
  how you can see and reuse the formatting of any documentation page and summarizes the
  formatting rules to follow so that your contributions are rendered correctly.

- :ref:`py_files_writers`: Explains how docstrings in Python (PY) files provide
  descriptions for the Python objects that are used to interact with the library. In Python,
  a module is a PY file that contains Python objects, such as interfaces, classes, enums,
  functions, methods, parameters, properties, attributes, and constants. This subsection
  also explains how PY files are set up and summarizes the formatting rules for docstrings,
  code comments, and message strings.

- :ref:`examples_writers`: Explains how to provide downloadable scripts, which
  developers tend to seek out first and refer to most often. This subsection explains the
  Sphinx extensions that can be used to generate examples, how to use them, and how to
  format their source files.

- :ref:`content_how_tos`: Explains how to perform tasks associated with contributing
  to PyAnsys documentation, including how to review and create GitHub PRs (pull requests).
  As you become a more experienced contributor, this subsection and the
  `PyAnsys documentation resources <resources_writers_>`_ page are likely to be the content
  that you refer to most often.


.. toctree::
   :maxdepth: 3
   :hidden:

   content_contrib_setup/index
   rst_files_writers/index
   py_files_writers/index
   examples_writers/index
   content_how_tos/index
