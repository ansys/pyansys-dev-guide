.. _content_writing:

Content writing
===============

Earlier sections of this guide are written primarily for PyAnsys developers by PyAnsys
developers. This section is written for anyone who wants to contribute new or revise
existing content in the documentation for a PyAnsys library. The goal is to
provide content contributors with the information that they need to write clear, consistent,
effective, and user-friendly content in the order in which they need to know it.

Comprehensive information on content writing is organized as follows:

- :ref:`content_contrib_setup`: Describes PyAnsys libraries, explains how to set up a
  content development environment, and provides links to many resources relevant to
  creating and maintaining PyAnsys documentation.

- :ref:`rst_files_writers`: Explains how reStructuredText (RST) files define the hierarchy
  of the documentation and provide manually authored content. This section also describes
  how to view and reuse the formatting of any documentation page and summarizes the
  formatting rules to follow so that your content contributions are rendered correctly.

- :ref:`py_files_writers`: Explains how docstrings in Python (PY) files provide
  descriptions for the Python objects that are used to interact with a PyAnsys library. This
  section also explains how PY files are set up and summarizes the formatting rules
  for docstrings, code comments, and message strings.

- :ref:`examples_writers`: Explains the Sphinx extensions that PyAnsys developers are
  using to generate the examples in the "Examples" section of their PyAnsys documentation
  and how to format the source files so that the content in the renders correctly.

- :ref:`content_how_tos`: Explains how to perform tasks associated with contributing
  to PyAnsys documentation, including how to review and create GitHub PRs (pull requests).
  As you become a more experienced contributor, this subsection and the :ref:`resources_writers`
  page are likely to be the content that you refer to most often.


.. toctree::
   :maxdepth: 3
   :hidden:

   content-contrib-setup/index
   rst-files-writers/index
   py-files-writers/index
   examples-writers/index
   content-how-tos/index
