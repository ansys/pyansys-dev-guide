PyAnsys Developer's Guide
#########################

This guide serves as the central document for:

- Ansys developers who want to create and "own" libraries
- Anyone in the Python community who wants to contribute to a 
  library
- Anyone who is interested in learning more about the PyAnsys 
  project and libraries


Web-based documentation is posted upon approval.

A PDF version of this guide can be found in the release notes in `Releases
<https://github.com/pyansys/about/releases>`_.


Generate Documentation
----------------------
To generate this documentation locally, you can install the requirements into
your Python environment with:

.. code::

   pip install -r requirements_docs.txt

or if you want to configure and activate Python virtual environment with the
required packages:

.. code::
    
   configure_venv

Then, depending on your operating system, generate the documentation.

On Windows, generate with:

.. code::

   cd doc
   make.bat html

On Linux, generate with:

.. code::

  make -C doc html


Contributing
------------
To contribute to this guide, either create a branch and
contribute directly or fork and submit a pull request.  All 
pull requests are reviewed before they can be merged.
