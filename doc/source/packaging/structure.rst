.. ref_project_structure::

#################
Project Structure
#################

Most of the projects in the PyAnsys ecosystem ship in the form of a Python
Package. This is the formal way of distributing Python-based projects.

The guide presented in this page is compliant with the `Python Packaging
Authority`_ and the `PyAnsys`_ recommendations.

.. note::

   The best way to keep up-to-date with Python Packaging is to check the `Python
   Packaging User Guide`_, maintained by the `Python Packaging Authority`_ (PyPA).
   PyAnsys guidelines are build on top of PyPA ones.


.. TODO: Explain the difference between Package and Library?
   Package: only holds modules
   Library: a collection of packages


PyAnsys Project Required Files
==============================

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

The following directories can be identified in previous structure:

- ``doc/`` is devoted to store any piece of information related to documentation,
  guidelines and examples.

- ``src/`` is used to collect all the Python modules and scripts that form
  the project.

- ``tests/`` stores all the unit tests whose purpose is to check the integrity
  of the project.


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
