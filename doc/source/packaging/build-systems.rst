.. _ref_build_system:

############
Build System
############

The build system is a fundamental tool when it comes to packaging Python
libraries. It allows to generate distribution files which can be shared with
users and developers. 


The Build System
================

The build-system allows maintainers to generate artifacts for their Python
libraries. The word artifacts refers to both wheel and source files:

- ``Wheel files`` have the ``*.whl`` file extension.
- ``Source files`` have the ``*.tar.gz`` or ``*.zip`` extension.

These are the files to be uploaded to `PyPI`_ when releasing a new version of a
PyAnsys project.

.. warning::

   Not all files are included by default in the source distribution. A
   `MANIFEST.in`_ is required at the root of the project to specify additional
   files.


The interation between the maintainer and the build-system is performed using a
build-system tool. This tool provides a frontend and a backend. The maintainers
trigger the frontend which then calls the backend. Then the backend reads the
project directory and generates the artifacts, as :numref:`build system diagram`:

.. include:: diagrams/build_system_diagram.rst


The PEP 517 and PEP 518
=======================

For a long time, the ``setup.py`` file was the only way of specifying the
project structure, metadata and installation workflow to be followed by `pip`_.
However, having to execute a Python file when installing a Python package
introduced the following problems:

- It was not possible to know which dependencies required the ``setup.py`` file
  to be properly executed.

- The default Python package installer, `pip`_, expected `setuptools`_ to be the
  default build system tool, excluding others like `flit`_ and `poetry`_.

Previous reasons lead to the acceptance of the `PEP 517`_ and `PEP 518`_.


PEP 517
-------

The `PEP 517` allowed Python developers to specify the build-backend tool to
generate the artifacts. As seen in :numref:`build system diagram` figure, the
most popular backends are provided by:

- `Setuptools`_ very popular but lacks from build time dependency declaration
  and it is difficult to extend.
- `Flit`_ is a lightweight build system tool for Python.
- `Poetry`_ focuses on dependency management and environment isolation.

The `PEP 517` introduced the ``build-backend`` key inside the
``[build-system]`` table in the ``pyproject.toml``.


PEP 518
-------

In addition to the ``setup.py`` file, a new project file named
``pyproject.toml`` file was specified by the `PEP 518`_. The main goal of this
file was to specify build time dependencies. However, some build system tools
like `flit`_ or `poetry`_ are able to specify all the project metadata inside
the ``pyproject.toml`` file and eliminate the usage of the ``setup.py``.

To specify the build time requirements, the ``[build-system]`` table needs to be
declared in the ``pyproject.toml`` file. Within it, the ``requires`` key is
assigned to a list of strings, each one of those being the build time
requirements.

The combination of `PEP 517`_ and `PEP 518`_ leads to the following syntax in te
``pyproject.toml`` files:

.. code:: toml

   [build-system]
   requires = ["flit"] # Defined by PEP 518
   build-backend = "flit_core.api" # Defined by PEP 517


Build-backend Tools
===================

This section collects some of the most popular build systems available in the
Python ecosystem. Although all of them achieve the same goal, there are a few
differences regarding their capabilities and the way of specifying project
metadata.

.. TODO: Include links to each build system allowed metadata fields

Setuptools
----------

`Setuptools`_ has been around for a long time in the Python ecosystem. Unless
you require from a high control over the installation steps of your project,
`flit`_ and `poetry`_ should be used.

If you do not need from a dynamic installation process, you may consider using a
``setup.cfg`` file. However, the ``setup.py`` is still required. This file
should have a call to the ``setup()`` function to act as the entry point of the
build backend system.

All the following `setuptools metadata fields`_ are valid ones. These need to be
specified either in the ``setup.py`` or ``setup.cfg``.


Flit
----

Flit is a modern and lightweight build system that requires developers
to manage virtual environments on their own. Developers must:

* Create a virtual environment and activate it.
* Install the package in editable mode.

Flit is the default tool for creating a new ``pyansys`` project when using the
`ansys-templates tool`_.

The ``[project]`` section specifies the project's metadata and required
dependencies. For more information, see `flit pyproject.toml
guidelines`_.


Poetry
------

Because of its ``poetry.lock`` file, Poetry provides strong dependency pinning. When
installing a package, poetry creates a virtual environment, thus ensuring an isolated
package development environment.

Nevertheless, it is possible to make Poetry ignore the ``poetry.lock`` file by running:

.. code:: bash

   poetry config virtualenvs.create false --local

Using `poetry`_ is popular because it:

* Supports pinning dependency versions via a ``poetry.lock`` file that can be
  used for testing and CI
* Allows downstream packages to still consume a loose dependency specification
* Integrates with `dependabot`_ to update the pinned version

The ``[tool.poetry]`` section contains metadata and defines the project's
dependencies. For more information, see `poetry pyproject.toml documentation`_.


.. _MANIFEST.in: https://packaging.python.org/en/latest/guides/using-manifest-in/
.. _PyPI: https://pypi.org/
.. _pip:
.. _flit: https://flit.pypa.io/en/latest/
.. _poetry: https://python-poetry.org/
.. _poetry pyproject.toml documentation: https://python-poetry.org/docs/pyproject/
.. _setuptools: https://pypi.org/project/setuptools/
.. _setuptools metadata fields: https://setuptools.pypa.io/en/latest/userguide/declarative_config.html#declarative-config
.. _flit pyproject.toml guidelines: https://flit.readthedocs.io/en/latest/pyproject_toml.html
.. _dependabot: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates
.. _ansys-templates tool: https://github.com/pyansys/ansys-templates
