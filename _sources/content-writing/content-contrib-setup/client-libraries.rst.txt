.. _client_libs:

Client libraries
=================

A client library is a collection of code specific to one programming language
that makes it easier to write scripts to access APIs programmatically. A
client library provides support for underlying services, including connection
management, asynchronous request processing, and exception handling. Its
high-level API abstractions are easier to understand and can be more
easily integrated with your codebase.

PyAnsys client libraries are collections of Python code that break apart
large monolithic Ansys desktop products into subsets by features, with the
expectation of compatibility and reusability across the entire Ansys
portfolio. For more information, see :ref:`componentizing`. In addition
to Ansys product wrappers, the PyAnsys ecosystem provides Python tools and
software utilities.

While installing a Python library depends on both the library and the
underlying services that it supports, most are installed in only a few steps
from the `Python Package Index <Python_Package_Index_>`_ (PyPI) using `pip <pip_>`_,
a package manager for installing Python packages:

#. Open a terminal or command prompt.
#. Install ``pip`` if it is not already installed on your system.
#. If you are using a `virtual environment <venv_>`_, activate it.
#. Run the command to install the library, ``pip install <library-name>``, where
   ``<library-name>`` is the name of the library.

To easily set up your PyAnsys development environment and install PyAnsys libraries
from one central source, you should use the **Ansys Python Manager**. From this app,
you can install a selected Python version (which includes ``pip``), create and
automatically activate a virtual environment, and install all or selected PyAnsys libraries.
You can also launch a console in your virtual environment to run commands from. For more
information, see :ref:`Ansys_Python_Manager`, which explains how to set up your content
development environment.
