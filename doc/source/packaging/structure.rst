.. _ref_project_structure:

#################
Project Structure
#################

Most of the projects in the PyAnsys ecosystem ship in the form of a Python
library with other additional files. All these files form what it is called a
"project". A project can be uploaded to a repository to better track the changes
applied to it. The high-level structure of a PyAnsys project is exposed in
figure :numref:`high level pyansys structure`.

.. include:: diagrams/ansys_project_diagram.rst

Python Libraries
================

A Python library is the formal way of distributing Python source code. It allows
to reuse and specify Python code dependencies. The guide presented in this page
is compliant with the `Python Packaging Authority`_ and PyAnsys recommendations.

.. note::

   The best way to keep up to date with Python packaging is to check the `Python
   Packaging User Guide`_, maintained by the `Python Packaging Authority`_ (PyPA).
   PyAnsys guidelines are built on top of PyPA guidelines.


Scripts, Modules, Sub-packages, and Packages
--------------------------------------------

To understand the structure of a Python Library, it is important to know
the difference between Python scripts, modules, sub-packages, and packages.

* ``Script``: Any Python file with logic source code.
* ``Module``: Any Python script hosted next to an ``__init__.py`` file.
* ``Sub-package``: Any directory containing various Python modules.
* ``Package``: Any directory containing Python modules and sub-packages.


Differences Between a Python Package and Library
------------------------------------------------

Although both terms are used interchangeably, there is a key difference between
them: a Python package is a collection of Python modules and sub-packages while
a Python Library is a collection of Python packages. Figure :numref:`python pkg
lib diagram` exposes this.

.. include:: diagrams/python_library_diagram.rst


Required Files for a PyAnsys Project
====================================

The fundamental PyAnsys Library structure is composed by the following files and
directories:

.. code:: bash

    pyproduct_library/
    │
    ├── doc/
    │   ├── make.bat
    │   ├── Makefile
    │   └── source/
    │       ├── index.rst
    │       └── conf.py
    │               
    ├── src/
    │   └── ansys/
    │       └── product/
    │           └── library/
    │               └── __init__.py
    │               
    ├── tests/
    │   └── test_*.py
    │               
    ├── LICENSE
    ├── README.rst
    ├── pyproject.toml
    └── setup.py (optional)

Descriptions follow for some of the directories in the structure:

- ``doc/`` contains files related to documentation, guidelines, and examples.

- ``src/`` contains all Python modules and scripts that form the project.

- ``tests/`` contains all unit tests for checking the integrity of the project.


The ``doc/`` Directory
----------------------


The ``src/`` Directory
----------------------


The ``tests/`` Directory
------------------------


The ``LICENSE`` File
--------------------


The ``README.rst`` File
-----------------------





.. REFERENCES & LINKS

.. _`Python Packaging User Guide`: https://packaging.python.org/en/latest/
.. _`Python Packaging Authority`: https://www.pypa.io/en/latest/
