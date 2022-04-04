.. _ref_project_structure:

#################
Project Structure
#################

Most of the projects in the PyAnsys ecosystem ship in the form of a Python
library with other additional files. All these files form what it is called a
"project". A project can be uploaded to a repository to better track the changes
applied to it.


Naming Convention
=================

Large organizations providing Python packages follow a consistent naming
pattern. Ansys follows two naming conventions, depending on the nature of the project.

PyAnsys Library
---------------

- The project name is to be ``Py<project>``. For example, ``PyMAPDL`` is the
  project name for MAPDL and ``PyAEDT`` is the project name for AEDT.

- The repository name as hosted on GitHub should be all lowercase to follow
  GitHub community standards. For example, `pymapdl`_ and `pyaedt`_.

- The Python library name is to be in the format
  ``ansys-<product/service>-<feature>``. For example, `ansys-mapdl-core
  <https://pypi.org/project/ansys-mapdl-core/>`_ is the name for the core MAPDL
  library.

.. include:: diag/pyansys_namespace_diag.rst

The previous structure leads to the following namespace when executing the import
statement:

.. code:: python

   import ansys.product import library

Using long Python library names provides two primary advantages:

- `Namespace Packages`_ can be used to designate official Ansys packages
- Consistent branding and style can be applied to PyAnsys libraries


gRPC Interface Package
----------------------
Lower-level gRPC interface packages like `ansys-api-mapdl`_ should always be
named ``ansys-api-<product/service>`` and may contain an additional level:
``ansys-api-<product/service>-<secondlevel>``.

.. include:: diag/grpc_structure_diag.rst

The previous structure leads to the following namespace within the ``*.proto`` files:

.. code::

   package ansys.api.<product/service>.v0;


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
lib diag` exposes this.

.. include:: diag/python_library_diag.rst


Required Files for a PyAnsys Project
====================================

The structure of any PyAnsys library contains the following files and
directories:

.. include:: diag/pyproduct_library_structure_diag.rst

Descriptions follow for some of the directories in the structure:

- ``doc/`` contains files related to documentation, guidelines, and examples.

- ``src/`` contains all Python modules and scripts that form the project.

- ``tests/`` contains all unit tests for checking the integrity of the project.

- ``setup.py`` or ``pyproject.toml`` is known as the project's file.


The ``doc/`` Directory
----------------------

When distributing software it is important to document it. Documenting software
means giving guidelines on how to install and describing all functions,
methods, and classes that it ships with. Case scenarios and examples should also
be part of the documentation. 

A PyAnsys project should have the following documentation sections:

- ``Getting Started``: Defines requirements and provides installation information
- ``User Guide``: Explains how to use the software
- ``API Reference``: Describes the source code
- ``Examples``: Provides use case scenarios that demonstrate the capabilities of the software
- ``Contributing``: Supplies project-specific contribution guides and can link to general PyAnsys contribution guidelines

Projects in the PyAnsys ecosystem take advantage of `Sphinx`_, a tool used for
building documentation for Python-based projects. A ``doc/`` directory making
use of `Sphinx`_ requires the following structure, as shown by figure
:numref:`doc structure diag`:


.. include:: diag/doc_structure_diag.rst

- ``_build`` contains the rendered documentation in various formats: HTML,
  PDF...

- ``source`` contains the RST files which will be rendered when building the
  documentation.

- ``make.bat`` and ``Makefile`` are used to automate cleaning and building
  commands. The ``make.bat`` is intended to be used by Windows users while
  ``Makefile`` is devised for MacOS/Linux ones.

The ``source/`` directory must contain at least these files:

- ``conf.py`` is a Python script used to declare the configuration of `Sphinx`_.
- ``index.rst`` is the index page of the documentation. In this file, try to reuse the
  ``README.rst`` file to avoid duplication.

If you would like to include images or documents, add them in the ``_static/``
directory.


The ``src/`` Directory
----------------------

All the Python source code must be located in this directory. This is where the
build system will look when generating the wheel and source distributions.

.. warning::

   Folders inside the ``src/`` cannot contain spaces or hyphens. Replace these
   symbols by using the underscore '_'.

The structure of the ``src/`` directory determines the namespace of the PyAnsys
library. Namespace allow you to easily split sub-packages from a package into
single, independent distributions.

There are different approaches available for creating a namespace package. For
the ansys namespace, we use the `PEP 420`_ `native namespace packages`_ approach.

Therefore, the source directory of any PyAnsys library must look like the one
exposed by figure :numref:`src structure diag`:

.. include:: diag/src_structure_diag.rst


The ``tests/`` Directory
------------------------

To guarantee the integrity of a PyAnsys project, a good test suite is required.
PyAnsys projects use the `pytest`_ testing framework.

A good practice is to emulate the structure of the ``src/ansys/product/library``
directory although it is not always necessary.

.. include:: diag/tests_structure_diag.rst

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

Each PyAnsys library should have a ``README.rst`` file in the root directory.

The preferred format of this file is `reStructuredText Markup Syntax`_ or a
although `Markdown Syntax`_ can be used too.  While Markdown syntax has better
GitHub support, text in RST files can be reused within Sphinx documentation.
This avoids duplication between the ``README.rst`` and the main ``index.rst`` in
the ``doc/source/`` directory.

The ``README.rst`` file should at the minimum contain these elements:

- PyAnsys library title
- General description
- Installation directions (via ``pip install`` and ``git clone``)
- Basic usage
- Links to the full documentation

The ``README.rst`` file is also reused within the project file metadata. It is
usually included in the ``long-description`` field.


The ``pyproject.toml`` File
---------------------------

The `PEP 518`_ introduced the usage of a new project file called
``pyproject.toml``. More information about this file can be found in the
REF-TO-BUILD-SYSTEMS-TOML section.

This file is mandatory as it  allows ``pip`` to resolve the requirements for
building the library. The following tabs expose the ``[build-system]`` section
for some of the most popular build-system backend tools in the Python ecosystem:


.. tabs::

   .. tab:: setuptools

      .. code:: toml

          [build-system]
          requires = ["setuptools", "wheel"]
          build-backend = "setuptools.build_meta"

   .. tab:: flit

      .. code:: toml

          # Refer to https://dev.docs.pyansys.com/packaging/build-systems#flit
          [build-system]
          requires = ["flit_core>=3.2,<4"]
          build-backend = "flit_core.buildapi"


   .. tab:: poetry

      .. code:: toml

          # Refer to https://dev.docs.pyansys.com/packaging/build-systems#poetry
          [build-system]
          requires = ["poetry"]
          build-backend = "poetry.masonry.api"


The ``setup.py`` File
---------------------

For a long time, the ``setup.py`` has been the usual way of building and
distributing Python libraries. As opposite to the static ``pyproject.toml``
file, ``setup.py`` is Python script. This means that Python code is interpreted
when building the library. This allows to customize the building process but
also may introduced security issues.

.. tip::

   Consider using a ``pyproject.toml`` file instead of a ``setup.py`` when
   possible.


The ``setup.py`` file is only compatible with `Setuptools`_. A ``setup.cfg`` can
also be used for specifying the metadata and packages, but the ``setup.py`` file
must be present too. More information about its usage can be found in the
following links:

* `Building and Distributing Packages with Setuptools`_
* `Configuring setuptools using setup.cfg files`_

As a minimum configuration for PyAnsys projects, the following ``setup.py``
template can be used:


.. include:: resources/setup_file_template.rst


.. REFERENCES & LINKS

.. _MIT License: https://opensource.org/licenses/MIT
.. _PEP 420: https://peps.python.org/pep-0420/
.. _native namespace packages: https://packaging.python.org/en/latest/guides/packaging-namespace-packages/#native-namespace-packages
.. _Namespace Packages: https://packaging.python.org/guides/packaging-namespace-packages/
.. _PyAnsys: https://docs.pyansys.com/
.. _Python Packaging User Guide: https://packaging.python.org/en/latest/
.. _Python Packaging Authority: https://www.pypa.io/en/latest/
.. _pytest: https://docs.pytest.org/en/latest/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _PyMAPDL: https://github.com/pyansys/pymapdl
.. _PyAEDT: https://github.com/pyansys/PyAEDT
.. _ansys-api-mapdl: https://pypi.org/project/ansys-api-mapdl/
.. _reStructuredText Markup Syntax: https://docutils.sourceforge.io/rst.html
.. _Markdown Syntax: https://www.markdownguide.org/basic-syntax/
.. _PEP 518: https://peps.python.org/pep-0518/
.. _Building and Distributing Packages with Setuptools: https://setuptools.pypa.io/en/latest/setuptools.html
.. _Configuring setuptools using setup.cfg files: https://setuptools.pypa.io/en/latest/userguide/declarative_config.html
.. _setuptools: https://setuptools.pypa.io/en/latest/index.html
