.. _ref_project_structure:

Project structure
=================

Most of the projects in the PyAnsys ecosystem ship in the form of a Python
library with other additional files. All these files form what it is called a
*project*. A project can be uploaded to a repository to better track the changes
applied to it.

Naming convention
=================

Large organizations providing Python packages follow a consistent naming
convention. Ansys follows two naming conventions, depending on the nature of the project.

PyAnsys library
---------------

- The project name is in the format ``Py<project>``. For example, ``PyAEDT`` is the
  project name for AEDT (Ansys Electronics Desktop) and ``PyMAPDL`` is the
  project name for MAPDL (an abbreviation for Mechanical APDL).

- The repository name as hosted on GitHub should be all lowercase to follow
  GitHub community standards. For example, `pyaedt`_ and `pymapdl`_.

- The Python library name is in the format ``ansys-<product/service>-<feature>``.
  For example, `ansys-mapdl-core <https://pypi.org/project/ansys-mapdl-core/>`_
  is the name for the core MAPDL library.

.. include:: diag/pyansys_namespace_diag.rst

The previous structure leads to the following namespace when executing the import
statement:

.. code:: python

   from ansys.product import library

Using long Python library names provides two primary advantages:

- `Namespace packages`_ can be used to designate official Ansys packages.
- Consistent branding and style can be applied to PyAnsys libraries.

gRPC interface package
----------------------
Lower-level gRPC interface packages like `ansys-api-mapdl`_ should always be
named ``ansys-api-<product/service>`` and may contain an additional level:
``ansys-api-<product/service>-<secondlevel>``.

.. include:: diag/grpc_structure_diag.rst

This structure leads to the following namespace within Protobuf (PROTO) files:

.. code::

   package ansys.api.<product/service>.v0;

Python libraries
================

A Python library is the formal way of distributing Python source code. It allows
for reuse and for specifying Python code dependencies. Guidelines in this section
are compliant with `Python Packaging Authority`_ (PyPA) and PyAnsys recommendations.

.. note::

   The best way to keep up to date with Python packaging is to check the `Python
   Packaging User Guide`_, maintained by the PyPA. PyAnsys guidelines are built
   on top of the PyPA guidelines.

Scripts, modules, subpackages, and packages
--------------------------------------------

To understand the structure of a Python Library, it is important to know
the difference between Python scripts, modules, subpackages, and packages.

* ``Script``: Any Python file with logic source code
* ``Module``: Any Python script hosted next to an ``__init__.py`` file
* ``Subpackage``: Any directory containing various Python modules
* ``Package``: Any directory containing Python modules and subpackages

Differences between a Python package and library
------------------------------------------------

Although the terms *package* and *library* are often used interchangeably, there is
a key difference between them. As shown in the following image, a Python package is
a collection of Python modules and subpackages, while a Python library is a collection
of Python packages.

.. include:: diag/python_library_diag.rst

Required files
==============

The structure of any PyAnsys library contains these directories and files:

.. include:: diag/pyproduct_library_structure_diag.rst

Descriptions follow for some of the directories in this structure:

- ``doc``: Contains files related to documentation, guidelines, and examples

- ``src``: Contains all Python modules and scripts that form the project

- ``tests``: Contains all unit tests for checking the integrity of the project

- ``setup.py`` or ``pyproject.toml``: Configures the project.

The ``doc`` directory
----------------------

Prior to distributing software, it is important to document it. Documenting software
consists of explaining how to install and use all functions, classes, and methods that
it ships with. The documentation should also include use case scenarios. 

A PyAnsys project typically has these documentation sections:

- ``Getting started``: Defines requirements and provides installation information
- ``User guide``: Explains how to use the software
- ``API reference``: Describes the source code
- ``Examples``: Provides use case scenarios that demonstrate the capabilities of the software
- ``Contribute``: Links to the *PyAnsys developer's guide* for overall guidance and supplies
  project-specific contribution information

Projects in the PyAnsys ecosystem take advantage of `Sphinx`_, a tool for
building documentation for Python-based projects. Sphinx requires a ``doc``
directory with a specific structure:

.. include:: diag/doc_structure_diag.rst

- ``_build``: Contains the rendered documentation in various formats, such as HTML
  and PDF.

- ``source``: Contains the RST files with the manually authored content. Folder
  and file names in this directory should use hyphens as space delimiters for search
  optimization of the generated HTML documentation.

- ``make.bat`` and ``Makefile``: Automates documentation cleaning and building
  commands. You use ``make.bat`` when running on Windows and ``Makefile``
  when running on macOS or Linux. For information on the required configuration for
  these files, see :ref:`Automation files`.

The ``source`` directory must contain at least these files:

- ``conf.py``: Python script that declares the `Sphinx`_ configuration.
  The minimum required configuration is explained in :ref:`The
  \`\`conf.py\`\` file`.
- ``index.rst``: Main index (landing) page for the overall documentation. Some
  projects reuse ``README.rst`` files in the main ``index.rst`` file.
  For more information, see :ref:`readme_files`. In newer projects, however, the ``index.rst``
  file uses a grid of cards to present the organization of the documentation in a visual manner.

You generally add any images or documents that you would like to include in a ``_static``
directory.

The ``src`` directory
----------------------

All the Python source code must be located in the ``src`` directory. This is where the
build system looks when generating the wheel and source distributions.

.. warning::

   The names of directories and files in the ``src`` directory cannot contain spaces or hyphens.
   Replace these characters with an underscore (``_``).

The structure of the ``src`` directory determines the namespace of the PyAnsys
library. A namespace allow you to easily split subpackages from a package into
single, independent distributions.

There are different approaches available for creating a namespace.
Ansys namespaces use the `native namespace packages`_ from
`PEP 420`_.

Therefore, the source directory of any PyAnsys library must look like this:

.. include:: diag/src_structure_diag.rst

The ``tests`` directory
------------------------

To guarantee the integrity of a PyAnsys project, a good test suite is required.
PyAnsys projects use the `pytest`_ framework.

A good practice is to emulate the structure of the ``src/ansys/product/library``
directory, although this is not always necessary.

.. include:: diag/tests_structure_diag.rst

Notice the use of ``tests_*`` when creating child directories within the
``tests`` directory. For unit testing files, names use the ``test_*.py`` prefix.
This is the preferred way of naming directories and files in the
``tests`` directory.

The ``AUTHORS`` file
--------------------

You use the ``AUTHORS`` file to specify the authorship of the repository. The
Ansys Legal department has defined its format. You can add external contributors
to this file on demand. Make sure that you adapt the project name on your
specific repository's ``AUTHORS`` file.

.. include:: code/authors_code.rst


.. _ref_changelog_file:

The ``CHANGELOG.md`` file
-------------------------

You use the ``CHANGELOG.md`` file to collect new features, fixed bugs, documentation
improvements, and new contributors. It provides a summary of the latest
enhancements to the project.

.. literalinclude:: code/changelog_file.md
   :language: markdown

The ``CODE_OF_CONDUCT.md`` file
-------------------------------

You use the ``CODE_OF_CONDUCT.md`` to specify how users, developers, and maintainers
are to behave while working in the project. PyAnsys projects usually adopt the *Contributor
Covenant Code of Conduct*, which is very popular across open source projects.

.. literalinclude:: code/code_of_conduct_file.md
   :language: markdown

The ``CONTRIBUTING.md`` file
----------------------------
You use the ``CONTRIBUTING.md`` file to provide a quick entry-point for developers
who are willing to contribute to the project. It usually provides references to
this information:

- Where the source code of the project is hosted.
- Which steps must be followed to install the software in "development" mode.
- Ways of contributing to the source code.

Ideally, the ``CONTRIBUTING.md`` file for a PyAnsys project should link
to the `PyAnsys developer's guide <https://docs.pyansys.com/>`_ for overall
guidance.

.. literalinclude:: code/contributing_file.md
   :language: markdown

The ``CONTRIBUTORS.md`` file
----------------------------

You use the ``CONTRIBUTORS.md`` file to list the contributors to the repository. Its
purpose is to credit the authors for their individual contributions and provide a
record of authorship for the codebase. Provide first and last names and
links to GitHub usernames.

.. literalinclude:: code/contributors_file.md
   :language: markdown

The ``LICENSE`` file
--------------------

The ``LICENSE`` file provides the legal framework for the software. PyAnsys projects
must use the `MIT License`_. Here is the template:

.. include:: code/license_mit_code.rst

.. caution::

   Just because a software does not ship with a ``LICENSE`` file, it does not mean
   it is free or open source. If you need to use unlicensed software, contact
   its development team so that they can provide you with the correct license.

The ``README`` file
--------------------

Each PyAnsys library must have a ``README`` file in the root directory.

The preferred format of this file is `reStructuredText Markup Syntax`_,
although you can also use `Markdown Syntax`_. While Markdown syntax has better
GitHub support, you can reuse ReStructuredText (RST) files within Sphinx documentation.
For more information, see :ref:`readme_files`.

The ``README`` file should at the minimum contain these elements:

- PyAnsys library title
- General description
- Installation instructions (using ``pip install`` and ``git clone``) but only if the library
  reuses ``README`` file content in its documentation

.. note::
   While older projects tend to reuse content in their ``README.rst`` files in the
   main ``index.rst`` files in their ``doc/source`` directories, newer projects do not.
   Instead, they provide a bulleted list with documentation links and descriptions in
   their ""README`` files. In the main ``index.rst`` files for their documentation,
   they then use a grid of cards to visually explain and link to documentation sections.
   This keeps the ``README`` file focused on why you might want to explore the
   library and lets you quickly view documentation sections of interest.

The ``README.rst`` file is also reused within the project file metadata. It is
usually included in the ``long-description`` field.

The ``pyproject.toml`` file
---------------------------

`PEP 518`_ introduced the use of a project file named ``pyproject.toml``.
This file is mandatory because it allows `pip`_ to resolve the
requirements for building the library. The following tabs expose the ``[build-system]`` section
for build-system backend tools commonly used in the Python ecosystem:

.. include:: code/pyproject_code.rst

The ``setup.py`` file
---------------------

For a long time, Python developers used the ``setup.py`` file to build and
distribute their libraries. Unlike a static ``pyproject.toml`` file, the
``setup.py`` file is a Python script. This means that Python code is interpreted
when building the library. This approach supports customizing the build
process but can also introduce security issues.

.. note::

   The ``setup.py`` file is only compatible with `Setuptools`_, which is why
   you should consider using a ``pyproject.toml`` file instead.

While you can use a ``setup.cfg`` file to specify the metadata and packages, the ``setup.py``
file must also be present. For more information, see these pages in the Setuptools
documentation:

* `Building and Distributing Packages with Setuptools`_
* `Configuring setuptools using setup.cfg files`_

As a minimum configuration for a PyAnsys project, you can use this ``setup.py``
template:

.. include:: code/setup_file_code.rst

