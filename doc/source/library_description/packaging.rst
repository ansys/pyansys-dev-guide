.. _packaging:

Packaging
#########

A Python package organizes and structures a Python library, which contains
several modules and assets such as examples or binary extensions. A Python
package offers an easy, reliable, and comprehensive way to distribute and
install a Python library on a variety of platforms and environments.

.. note::

   If you want to create a new PyAnsys project according to the guidelines
   presented in the following lines, consider using the `ansys-templates tool`_.


Python Scripts, Modules, Sub-packages, and Packages
---------------------------------------------------

It is important to understand the difference between Python scripts, modules,
sub-packages, and packages:

* ``Script``: Any Python file with logic source code.
* ``Module``: Any Python script hosted next to an ``__init__.py`` file.
* ``Sub-package``: Any directory containing various Python modules.
* ``Package``: Any directory containing Python modules and sub-packages.

The following structure is shown to better explain previous concepts:

.. code:: bash

    .
    ├── src
    │   └── package
    │       ├── subpackage_a
    │       │   ├── __init__.py
    │       │   └── module_c.py
    │       ├── __init__.py
    │       ├── module_a.py
    │       └── module_b.py
    ├── LICENSE
    ├── README.rst
    └── pyproject.toml


Namespace Packaging
-------------------
A PyAnsys library uses `namespace packaging`_.  Namespace packages allow you
to easily split sub-packages from a package into single, independent
distributions.

There are different approaches available for creating a namespace package. For
the ``ansys`` namespace, we use the `PEP 420`_ `native namespace packages`_
approach.

Therefore, the source directory of any `PyAnsys library` should look like this:

.. code:: bash

    .
    └── src
        └── ansys
            └── product
                └── library
                    └── __init__.py


Required Files
--------------

* ``README.rst`` file: Describes the purpose of the package.
  *The format of this file must be reStructuredText.*

* ``LICENSE`` file: Specifies copyrights and required authorization.

* ``pyproject.toml`` file: Provides package metadata and defines how the package
  is built. There are different build backends available, such as `setuptools`_,
  `poetry`_, and `flit`_.

* ``src/ansys/product/library/__init__.py`` file: Usually contains the
  version of the package in a variable named ``__version__``. The value of this
  variable can be parsed from the ``pyproject.toml`` file so that the version 
  is only specified in one location.


Additional Directories
----------------------

The following directories may be specified at the same level as the ``src/`` one:

* ``tests/``: Contains all unit tests for the package. It is
  likely that these tests take advantage of the `pytest`_ framework.

* ``doc/``: Contain all documentation files and examples on
  how to use the package.


Project File and Build System
------------------------------

The ``pyproject.toml`` file is the standardized build configuration file for Python
projects. It must contain at least a ``[build-system]`` section, which determines
how the project is built. Some commonly used packaging tools are `setuptools`_,
`poetry`_, and `flit`_. All three of these packaging tools are currently supported by
the ``pyansys-advanced`` template, which is included in the `ansys-templates tool`_.


Flit
^^^^

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
^^^^^^

Because of its ``poetry.lock`` file, Poetry provides strong dependency pinning. When
installing a package, poetry creates a virtual environment, thus ensuring an isolated
package development environment.

Nevertheless, it is possible to make Poetry ignore the `poetry.lock` file by running:

.. code:: bash

   poetry config virtualenvs.create false --local

Using `poetry`_ is popular because it:

* Supports pinning dependency versions via a ``poetry.lock`` file that can be 
  used for testing and CI
* Allows downstream packages to still consume a loose dependency specification
* Integrates with `dependabot`_ to update the pinned version

The ``[tool.poetry]`` section contains metadata and defines the project's
dependencies. For more information, see `poetry pyproject.toml documentation`_.


Setuptools
^^^^^^^^^^

Setuptools is a very well known build system in the Python ecosystem. It is used
in projects requiring a ``setup.py`` file and can be used in projects with a
``pyproject.toml`` file, although not all metadata in this second file
is fully supported yet.

The main advantage of this build system is the ability to create custom build
steps in the form of Python code.


Specifying Package Version
--------------------------

It is very common for packages to specify their current version in the
``__version__`` variable. This variable is usually declared in the
``__init__.py`` file included in the ``library`` directory.

However, it is also required to specify the version in the ``pyproject.toml`` or
``setup.py`` file. This leads to a duplicate declaration of the project's version,
which could lead to a potential mismatch between both.

Therefore, a good practice is to take advantage of the `importlib.metadata package`_
for parsing the version from package metadata. This guarantees that there is no mismatch
between both version declarations.


.. code:: python

  try:
      import importlib.metadata as importlib_metadata
  except ModuleNotFoundError:
      import importlib_metadata

  __version__ = importlib_metadata.version(__name__.replace(".", "-"))


Extra Tools Configuration
-------------------------

There are plenty of tools in the Python ecosystem that enable developers to
write clean code according to different coding style guidelines. Some of these
tools are `black`_, `isort`_, `flake8`_, and `mypy`_.

Some of these tools can be configured. This configuration might be specified in
custom files required by the tool or in the ``pyproject.toml`` file, thus reducing the
number of files in the project directory.

.. note::

  When using `setuptools`_ as a build backend, providing the metadata in
  the ``pyproject.toml`` file is not yet fully supported.  Instead, it also 
  requires a ``setup.cfg`` file, ``setup.py`` file, or both files.

In the `pyansys template`, all these configurations are included by default in
the ``.pre-commit-config.yaml`` file because ``pre-commit`` is not able to parse the
``pyproject.toml`` file nor the ``setup.py`` file.


Generate the Package and Upload It on PyPI
------------------------------------------

The first time that you want to upload a package on PyPI under `ansys <https://pypi.org/user/ansys/>`_
account, you must perform the following process manually.

Create the python package.

.. code::

  pip install build
  python -m build

If using flit or poetry, you can also run:

.. code::

   flit build
   poetry build

Verify the distribution's long description rendering with ``twine``.

.. code::

  pip install twine
  twine check dist/*


Upload the package to PyPI using ``twine`` and the upload token generated for
the ``ansys`` PyPI account.  As soon as the package has been released for the
first time, it is possible to create an independent token dedicated to this
package.  This way the token stored in the GitHub secrets and used in the
release's workflow is only related to that specific package.  This limits the
exposure to any potential token security flaws.  Contact
alexander.kaszynski@ansys.com for the token.

.. code::

  python -m twine upload -u __token__ -p <TOKEN_FOR_PYPI> --skip-existing dist/*

For the next release upload, you can do it through the CI/CD workflow after generating a token just for this package.
Create a `secret`_ in GitHub settings.
Name it ``PYPI_TOKEN`` and assign it the token provided by PyPI.
This token will be reused in the CI/CD workflow handling the package distribution.

Tag a Release
-------------
To deploy a new package on PyPI, you must tag a release under a release branch. The PyAnsys project
follows the `trunk-based development`_ source-control branching model, where the main development
branch is always in a releasable state.

To tag the release, update your main local branch.

.. code::

  git checkout main
  git pull

Then, create a release branch.

.. code::

  git checkout -b release/MAJOR.MINOR

Bump the version number in the ``_version`` file to ``MAJOR.MINOR.PATCH``.

Commit and push your changes and then create the tag.

.. code::

  git commit -am "Increase version to v<MAJOR.MINOR.PATCH>"
  git tag v<MAJOR.MINOR.PATCH>
  git push --tags

Following this tag creation, the workflow responsible for the distribution
will be automatically triggered.

Install a Package
-----------------
Install a package with:

.. code::

  pip install ansys-<product>-<library>

To create a package complying with the above standards, here is the minimal content of your PyAnsys library:

.. code::

   ansys/<product>/<library>/__init__.py
   LICENSE
   README.rst
   pyproject.toml
   tests/


.. _namespace packaging: https://packaging.python.org/guides/packaging-namespace-packages/
.. _native namespace packages: https://packaging.python.org/guides/packaging-namespace-packages/#native-namespace-packages
.. _PEP 420: https://www.python.org/dev/peps/pep-0420/
.. _setuptools: https://setuptools.pypa.io
.. _poetry: https://python-poetry.org/docs/
.. _flit pyproject.toml guidelines: https://flit.readthedocs.io/en/latest/pyproject_toml.html
.. _flit: https://flit.readthedocs.io
.. _dependabot: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates
.. _ansys-templates tool: https://github.com/pyansys/pyansys-templates
.. _poetry pyproject.toml documentation: https://python-poetry.org/docs/pyproject/
.. _black: https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file
.. _mypy: https://mypy.readthedocs.io/en/stable/config_file.html#the-mypy-configuration-file
.. _trunk-based development: https://trunkbaseddevelopment.com/
.. _secret: https://docs.github.com/en/actions/reference/encrypted-secrets
.. _setup.py: https://packaging.python.org/tutorials/packaging-projects/#configuring-metadata
.. _importlib.metadata package: https://docs.python.org/3/library/importlib.metadata.html
.. _isort: https://github.com/PyCQA/isort
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _pytest: https://docs.pytest.org/en/latest/
