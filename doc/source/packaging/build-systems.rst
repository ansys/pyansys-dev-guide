.. _ref_build_system:

Build system
============

The build system is a fundamental tool for packaging Python
libraries. It generates distribution files that can be shared with
users and developers. 

Artifacts
=========

The build system allows maintainers to generate artifacts for their Python
libraries. Here, `artifacts` refers to both wheel and source files:

- Wheel files have a WHL extension.
- Source files have a TAR.GZ or ZIP extension.

These are the files that you upload to `PyPI`_ when releasing a new version of a
PyAnsys project.

.. warning::

   Not all files are included by default in the source distribution. A ``MANIFEST.in``
   file is required at the root of the project to specify additional
   files. For more information, see `Controlling files in the distribution <https://setuptools.pypa.io/en/latest/userguide/miscellaneous.html>`_
   in the Setuptools documentation. 

The interaction between the maintainer and the build system is performed using a
build system tool. This tool provides both a frontend and a backend. The maintainers
trigger the frontend, which then calls the backend to read the
project directory and generate the artifacts.

.. include:: diag/build_system_diag.rst

PEP 517 and PEP 518
===================

For a long time, the ``setup.py`` file was the only way of specifying the
project structure, metadata, and installation workflow that `pip`_ was to follow.
However, having to execute a Python file when installing a Python package
introduced the following problems:

- It was not possible to know which dependencies required the ``setup.py`` file
  to be properly executed.

- The default Python package installer, `pip`_, expected `Setuptools <setuptools_repo_>`_
  to be the default build system tool, excluding others like `Flit`_ and `Poetry`_.

These problems led to the acceptance of `PEP 517`_ and `PEP 518`_.

PEP 517
-------

PEP 517 allows Python developers to specify the build-backend tool for
generating artifacts. The earlier image shows the most popular backends:

- Setuptools, while very popular, lacks the ability to declare build-time dependencies
  and is difficult to extend.
- Flit is a lightweight build system tool for Python.
- Poetry focuses on dependency management and environment isolation.

PEP 517 introduced the ``build-backend`` key inside the
``[build-system]`` table in the ``pyproject.toml`` file.

PEP 518
-------

In addition to the ``setup.py`` file, PEP 518 includes a project file named
``pyproject.toml``. Its main goal is to specify build-time dependencies.
However, some build-system tools like Flit or Poetry are able to specify all
project metadata inside the ``pyproject.toml`` file and eliminate the need to use
the ``setup.py`` file.

To specify the build-time requirements, the ``[build-system]`` table must be
declared in the ``pyproject.toml`` file. Within it, the ``requires`` key is
assigned to a list of strings, which are the build-time requirements.

The combination of PEP 517 and PEP 518 leads to the following syntax in a
``pyproject.toml`` file:

.. code:: toml

   [build-system]
   requires = ["flit"] # Defined by PEP 518
   build-backend = "flit_core.api" # Defined by PEP 517

Build-backend tools
===================

This section lists some of the most popular build systems in the
Python ecosystem. Although all of them achieve the same goal, there are a few
differences regarding their capabilities and the way of specifying project
metadata.

.. TODO: Include links to each build system allowed metadata fields

Setuptools
----------

`Setuptools <setuptools_repo_>`_ has been a part of the Python ecosystem for a long time. Unless
you require high control over your project's installation steps, you should use
Flit or Poetry.

If you do not need a dynamic installation process, you can consider using a
``setup.cfg`` file. However, the ``setup.py`` file is still required. The ``setup.cfg`` file
should have a call to the ``setup`` function to act as the entry point of the
build backend system.

All of these `setuptools metadata fields`_ are valid and must be
specified either in the ``setup.py`` or ``setup.cfg`` file.

Flit
----

`Flit`_ is a modern and lightweight build system that requires developers
to manage virtual environments on their own. Developers must:

* Create a virtual environment and activate it.
* Install the package in editable mode.

Flit is the default tool for creating a new PyAnsys project when using the
`Ansys templates <Ansys_templates_>`_.

The ``[project]`` section specifies the project's metadata and required dependencies.
For more information, see `The pyproject.toml config file <flit pyproject.toml guidelines_>`_
in the Flit documentation.

Poetry
------

`Poetry`_ has a ``poetry.lock`` file, which provides strong dependency pinning. When
installing a package, Poetry creates a virtual environment, thus ensuring an isolated
package development environment.

Nevertheless, it is possible to make Poetry ignore the ``poetry.lock`` file with this
command:

.. code:: bash

   poetry config virtualenvs.create false --local

Using Poetry is popular because it offers these features:

* Supports pinning dependency versions using a ``poetry.lock`` file that can be
  used for testing and CI
* Allows downstream packages to still consume a loose dependency specification
* Integrates with `dependabot`_ to update the pinned version

The ``[tool.poetry]`` section contains metadata and defines project
dependencies. For more information, see `The pyproject.toml file <poetry pyproject.toml documentation_>`_
in the Poetry documentation.
