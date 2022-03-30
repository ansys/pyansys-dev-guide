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

The structure of any PyAnsys library contains the following files and
directories:

.. include:: diagrams/pyproduct_library_structure_diagram.rst

Descriptions follow for some of the directories in the structure:

- ``doc/`` contains files related to documentation, guidelines, and examples.

- ``src/`` contains all Python modules and scripts that form the project.

- ``tests/`` contains all unit tests for checking the integrity of the project.

- ``setup.py`` or ``pyproject.toml`` is known as the project's file.


The ``doc/`` Directory
----------------------

When distributing software it is important to document it. Documenting software
means giving guidelines on how to install and use it but also which functions,
methods and/or classes does it ship with. Case scenarios and examples are also
be considered documentation. 

It is recommended to have the following sections in a PyAnsys project
documentation:

- ``Getting Started`` section explains requirements and installation details.
- ``User Guide`` section explains how to use the software.
- ``API Reference`` section contains source code documentation.
- ``Examples`` section case scenarios demonstrating the capabilities of the software.
- ``Contributing`` section can be linked to generic PyAnsys contributing guidelines. 

Projects in the PyAnsys ecosystem take advantage of `Sphinx`_, a tool used for
building documentation for Python-based projects. A ``doc/`` directory making
use of `Sphinx`_ requires the following structure, as shown by figure
:numref:`doc structure diagram`:


.. include:: diagrams/doc_structure_diagram.rst

- ``_build`` contains the rendered documentation in various formats: HTML,
  PDF...

- ``source`` contains the RST files which will be rendered when building the
  documentation.

- ``make.bat`` and ``Makefile`` are used to automate cleaning and building
  commands. The ``make.bat`` is intended to be used by Windows users while
  ``Makefile`` is devised for MacOS/Linux ones.

The ``source/`` directory needs to contain at least the following files:

- ``conf.py`` is a Python script used to declare the configuration of `Sphinx`_.
- ``index.rst`` is the index page of the documentation. Try to reuse the
  ``README.rst`` file in here to avoid duplication.

In case you would like to include images or documents, it is recommended to add
those in the ``_static/`` directory.


The ``src/`` Directory
----------------------

All the Python source code must be located in this directory. This is where the
build system will look when generating the wheel and source distributions.

.. warning::

   Folders inside the ``src/`` cannot contain spaces or hypens. Replace these
   symbols by using the underscore '_'.

The structure of the ``src/`` directory determines the namespace of the PyAnsys
library. Namespace allow you to easily split sub-packages from a package into
single, independent distributions.

There are different approaches available for creating a namespace package. For
the ansys namespace, we use the `PEP 420`_ `native namespace packages`_ approach.

Therefore, the source directory of any PyAnsys library must look like the one
exposed by figure :numref:`src structure diagram`:

.. include:: diagrams/src_structure_diagram.rst


The ``tests/`` Directory
------------------------

To guarantee the integrity of a PyAnsys project, a good test suite is required.
PyAnsys projects use the `pytest`_ testing framework.

A good practice is to emulate the structure of the ``src/ansys/product/library``
directory although it is not always necessary.

.. include:: diagrams/tests_structure_diagram.rst

Notice the usage of ``tests_*/`` when creating new directories inside the
``tests/`` one. On the other hand, unit testing files are named using the
``test_*.py`` prefix. This is the preferred way of naming directories and files
inside the ``tests/`` directory.


The ``LICENSE`` File
--------------------

The ``LICENSE`` file provides the legal framework for the software. The
recommended license for `PyAnsys`_ projects is `MIT License`_. A template for
this license is provided below:

.. include:: resources/license_mit.rst

.. note::

   Just because a software does not ship with a LICENSE file, it does not mean
   it is free or open source. If you require from using this software, contact
   its development team so they can provide you with the right license.


The ``README.rst`` File
-----------------------





.. REFERENCES & LINKS

.. _`MIT License`: https://opensource.org/licenses/MIT
.. _`PEP 420`: https://peps.python.org/pep-0420/
.. _`native namespace packages`: https://packaging.python.org/en/latest/guides/packaging-namespace-packages/#native-namespace-packages
.. _`PyAnsys`: https://docs.pyansys.com/
.. _`Python Packaging User Guide`: https://packaging.python.org/en/latest/
.. _`Python Packaging Authority`: https://www.pypa.io/en/latest/
.. _`pytest`: https://docs.pytest.org/en/latest/
.. _`Sphinx`: https://www.sphinx-doc.org/en/master/
