PyAnsys Developer's Guide
#########################

This guide serves as the central document for:

- Ansys developers who want to create and "own" libraries.
- Anyone in the Python community who wants to contribute to a 
  library.
- Anyone who is interested in learning more about the PyAnsys 
  project and libraries.


Web-based documentation will be posted upon approval.

PDF version of this guide can be found in the release notes in `Releases
<https://github.com/pyansys/about/releases>`_.


Generate Documentation
----------------------
Generate this documentation locally by first installing the
requirements with:

.. code::

   pip install -r requirements_docs.txt

Then build (on Windows) with:

.. code::

   cd doc
   make.bat html

Or on Linux with:

.. code::

  make -C doc html


Contributing
------------
Feel free to contribute to this guide by creating a branch and
contributing directly, or forking and submitting a PR.  All PRs will
be reviewed before merge.
