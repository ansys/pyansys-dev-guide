.. _ref_build_system:

############
Build system
############

The build system is a fundamental tool for packaging Python
libraries. It generates distribution files that can be shared with
users and developers. 


Artifacts
=========

The build system allows maintainers to generate artifacts for their Python
libraries. Here, `artifacts` refers to both wheel and source files:

- ``Wheel files`` have the ``*.whl`` file extension.
- ``Source files`` have the ``*.tar.gz`` or ``*.zip`` extension.

These are the files to upload to `PyPI`_ when releasing a new version of a
PyAnsys project.

.. warning::

   Not all files are included by default in the source distribution. A
   `MANIFEST.in`_ is required at the root of the project to specify additional
   files.


The interaction between the maintainer and the build system is performed using a
build system tool. This tool provides both a frontend and a backend. The maintainers
trigger the frontend, which then calls the backend to read the
project directory and generate the artifacts, as :numref:`build system diag` shows.

.. include:: diag/build_system_diag.rst


PEP 517 and PEP 518
===================

For a long time, the ``setup.py`` file was the only way of specifying the
project structure, metadata, and installation workflow that `pip`_ was to follow.
However, having to execute a Python file when installing a Python package
introduced the following problems:

- It was not possible to know which dependencies required the ``setup.py`` file
  to be properly executed.

- The default Python package installer, `pip`_, expected `setuptools`_ to be the
  default build system tool, excluding others like `flit`_ and `poetry`_.

These problems led to the acceptance of `PEP 517`_ and `PEP 518`_.


PEP 517
-------

`PEP 517`_ allows Python developers to specify the build backend tool for
generating artifacts. The previous :numref:`build system diag` diagram shows the
most popular backends:

- `Setuptools`_ , while very popular, lacks the ability to declare build time dependencies
  and is difficult to extend.
- `Flit`_ is a lightweight build system tool for Python.
- `Poetry`_ focuses on dependency management and environment isolation.

`PEP 517` introduced the ``build-backend`` key inside the
``[build-system]`` table in the ``pyproject.toml``.


PEP 518
-------

In addition to the ``setup.py`` file, `PEP 518`_ includes a project file named
``pyproject.toml``. The main goal of this file is to specify build time dependencies.
However, some build system tools like `flit`_ or `poetry`_ are able to specify all
project metadata inside the ``pyproject.toml`` file and eliminate usage of the 
``setup.py`` file.

To specify the build time requirements, the ``[build-system]`` table must be
declared in the ``pyproject.toml`` file. Within it, the ``requires`` key is
assigned to a list of strings, which are the build time
requirements.

The combination of `PEP 517`_ and `PEP 518`_ leads to the following syntax in a
``pyproject.toml`` file:

.. code:: toml

   [build-system]
   requires = ["flit"] # Defined by PEP 518
   build-backend = "flit_core.api" # Defined by PEP 517


Build backend tools
===================

This section lists some of the most popular build systems in the
Python ecosystem. Although all of them achieve the same goal, there are a few
differences regarding their capabilities and the way of specifying project
metadata.

.. TODO: Include links to each build system allowed metadata fields

Setuptools
----------

`Setuptools`_ has been a part of the Python ecosystem for a long time. Unless
you require high control over your project's installation steps, you should use
`flit`_ or `poetry`_.

If you do not need a dynamic installation process, you can consider using a
``setup.cfg`` file. However, the ``setup.py`` file is still required. The ``setup.cfg`` file
should have a call to the ``setup`` function to act as the entry point of the
build backend system.

All of these `setuptools metadata fields`_ are valid and must be
specified either in the ``setup.py`` or ``setup.cfg`` file.


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

Nevertheless, it is possible to make Poetry ignore the ``poetry.lock`` file with:

.. code:: bash

   poetry config virtualenvs.create false --local

Using `poetry`_ is popular because it:

* Supports pinning dependency versions via a ``poetry.lock`` file that can be
  used for testing and CI
* Allows downstream packages to still consume a loose dependency specification
* Integrates with `dependabot`_ to update the pinned version

The ``[tool.poetry]`` section contains metadata and defines project
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
