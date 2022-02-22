.. _packaging:

Packaging
#########
A Python package organizes and structures a Python library, which contains several
modules and assets such as examples or binary extensions. A Python package
offers an easy, reliable, and comprehensive way to distribute and install
a Python library on a variety of platforms and environments.

Namespace Packaging
-------------------
A PyAnsys library uses `namespace packaging`_.
Namespace packages allow a user to easily split subpackages from a package into
single, independent distributions.

There are different approaches available for creating a namespace package. For the
``ansys`` namespace, we use the `PEP 420`_ `native namespace packages`_ approach.

Required Files
--------------

* README.rst file: Describes the purpose of the package.
  *The format of this file must be reStructuredText.*

* LICENSE file: Specifies copyrights and required authorization.

* pyproject.toml file: Provides package information.
  This file provides the package metadata, and defines how it is built.
  There are different build backends available, such as `setuptools`_,
  `poetry`_ and `flit`_.


Project Configuration File
--------------------------

The ``pyproject.toml`` file is the standardized build configuration file for Python
projects. It needs to at least contain a ``[build-system]`` section, which determines
how the project is built. Some commonly used packaging tools are `setuptools`_,
`poetry`_, or `flit`_.

We use `poetry`_ as a default choice in the `PyAnsys template`_, for the following reasons:
* it supports pinning dependency versions, which we use for testing / CI
* downstream packages can still consume a loose dependency specification
* it integrates with `dependabot`_ to update the pinned version

Feel free to use any one of the packaging tools mentioned above that best suits
your needs. The advantage of `flit`_ is its simplicity, while `setuptools`_ is most useful
when custom build steps need to be implemented as Python code.

To use `poetry`_ as a packaging tool, the ``pyproject.toml`` should contain

.. code:: toml

  [build-system]
  requires = ["poetry-core>=1.0.0"]
  build-backend = "poetry.core.masonry.api"

The ``[tool.poetry]`` section contains metadata, and defines the project's dependencies. Refer to the
`poetry pyproject.toml documentation`_ for details.

Since poetry cannot automatically determine a package's version, we instead specify it in the ``[tool.poetry]``
section, and add code to ``__init__.py`` which obtains the version from the installation metadata:

.. code:: python

  try:
      import importlib.metadata as importlib_metadata
  except ModuleNotFoundError:
      import importlib_metadata

  __version__ = importlib_metadata.version(__name__.replace(".", "-"))


Where supported, we aim to put all tooling-related configuration into ``pyproject.toml``.
For example, it can also be used to configure the code formatter `black`_ or the static
type checker `mypy`_.

.. note::

  When using `setuptools`_ as a build backend, providing the metadata in ``pyproject.toml`` is not yet fully supported.
  Instead, it also requires a ``setup.cfg`` and / or ``setup.py`` file.


Generate the Package and Upload It on PyPI
------------------------------------------

The first time that you want to upload a package on PyPI under the `ansys <https://pypi.org/user/ansys/>`_
account, you must perform the following process manually.

Create the python package.

.. code::

  pip install build
  python -m build

Verify the distribution's long description rendering with ``twine``.

.. code::

  pip install twine
  twine check dist/*

Upload the package to PyPI using ``twine`` and the upload token generated for the ``ansys`` PyPI account.
Contact alexander.kaszynski@ansys.com for the token.

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
.. _flit: https://flit.readthedocs.io
.. _dependabot: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates
.. _PyAnsys template: https://github.com/pyansys/template
.. _poetry pyproject.toml documentation: https://python-poetry.org/docs/pyproject/
.. _black: https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file
.. _mypy: https://mypy.readthedocs.io/en/stable/config_file.html#the-mypy-configuration-file
.. _trunk-based development: https://trunkbaseddevelopment.com/
.. _secret: https://docs.github.com/en/actions/reference/encrypted-secrets
.. _setup.py: https://packaging.python.org/tutorials/packaging-projects/#configuring-metadata
