Packaging
#########
Python packages are used to organize and structure a Python library containing several modules and assets such as examples or binary extensions.
They offer an easy, reliable and comprehensive way to distribute and install
Python libraries on a variety of platforms and environments.

Namespace Packaging
-------------------
PyAnsys libraries use the `namespace packaging`_.
Namespace packages allow the user to easily split subpackages from a package into
a single and an independent distribution.

Three different approaches are currently available to create a namespace package:

* `native namespace packages`_
* pkgutil-style namespace packages
* pkg_resources-style namespace packages

Required files
--------------

* README.rst file is used to describe the purpose of the package.
  *The format of this file must be reStructuredText.*

* LICENSE file to specify the copyrigths and required authorization.

* setup.py file to provide package main information.
  The presence of this file indicate that the package was likely created using disutils
  which is the Python standard for building and distributing python package.


Setup File
----------
The `setup.py`_ file is the build script for ``setuptools``. It exposes dynamic metadata and contains
package's main information such as description, author, and version.
In this file, the ``setuptools`` module will be used to configure the metadata as opposed to ``distutils``,

.. code:: python

  import setuptools
  setuptools.setup(...)

This file gathers all namespace packages and files that must be included in the distributed
package.

.. code:: python

  packages = []
  for package in setuptools.find_namespace_packages(include='ansys*'):
      if package.startswith('ansys.tools.example_coverage'):
          packages.append(package)


It also extracts the version number from the ``_version.py`` located in the ``ansys/<product>/library`` directory of the source code.


Generate the Package and Upload it on PyPI
------------------------------------------

The first time you want to upload a package on PyPI under the `ansys <https://pypi.org/user/ansys/>`_ account, you must perform the following
process manually:

Create the python package.

.. code::

  python setup.py sdist

Verify the distribution's long description rendering with ``twine``.

.. code::

  pip install twine
  twine check dist/*

Upload the package to PyPI using ``twine`` using the upload token generated for the ``ansys`` PyPI account.  Contact alexander.kaszynski@ansys.com for the token.

.. code::

  python -m twine upload -u __token__ -p <TOKEN_FOR_PYPI> --skip-existing dist/*

Then, for the next release upload, you can do it through the CI/CD workflow after generating a token just for this package.
Create a `secret`_ in GitHub settings.
Name it ``PYPI_TOKEN`` and assign it the token provided by PyPI.
This token will be reused in the CI/CD workflow handling the package distribution.

Tag a Release
-------------
In order to deploy a new package on PyPI, you must tag a release under a release branch.  The PyAnsys project is follows the `trunk-based development`_ source-control branching model, where the main development branch is always in a releasable state.
To tag the release, you must update your main local branch.

.. code::

  git checkout main
  git pull

Then, create the new release branch

.. code::

  git checkout -b release/MAJOR.MINOR

Bump the version number in the ``_version`` file to ``MAJOR.MINOR.PATCH``.
Commit and push your changes and then create the tag:

.. code::

  git commit -am "Increase version to v<MAJOR.MINOR.PATCH>"
  git tag v<MAJOR.MINOR.PATCH>
  git push --tags

Finally, following this tag creation, the workflow responsible for the distribution
will be automatically triggered.

Install a package
-----------------

.. code::

  pip install ansys.<product>.<library>

Here is the minimal content of your python project to create a package complying with the above standards.

.. code::

   ansys/<product>/<library>/__init__.py
   LICENSE
   README.rst
   setup.py
   tests/


.. _namespace packaging: https://packaging.python.org/guides/packaging-namespace-packages/
.. _native namespace packages: https://packaging.python.org/guides/packaging-namespace-packages/#native-namespace-packages
.. _trunk-based development: https://trunkbaseddevelopment.com/
.. _secret: https://docs.github.com/en/actions/reference/encrypted-secrets
.. _setup.py: https://packaging.python.org/tutorials/packaging-projects/#configuring-metadata
