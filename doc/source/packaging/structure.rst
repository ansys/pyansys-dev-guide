.. ref_project_structure::

#################
Project Structure
#################

Most of the projects in the PyAnsys ecosystem ship in the form of a Python
package. This is the formal way of distributing Python-based projects.

The guide presented in this page is compliant with the `Python Packaging
Authority`_ and `PyAnsys`_ recommendations.

.. note::

   The best way to keep up to date with Python packaging is to check the `Python
   Packaging User Guide`_, maintained by the `Python Packaging Authority`_ (PyPA).
   PyAnsys guidelines are built on top of PyPA guidelines.


.. TODO: Explain the difference between Package and Library?
   Package: only holds modules
   Library: a collection of packages


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
