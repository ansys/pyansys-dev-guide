How to create a package
#######################
Python packages are used to organize and structure a python project containing many modules and
all kind of assets such as unit tests or documentation files.
They offer an easy, reliable and comprehensive way to distribute and install
python code on different platforms.

Namespace package
-----------------
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
  which is the python standard for building and distributing python package.


Setup.py
--------
  `setup.py`_ is the build script for setuptools. It exposes dynamic metadata and contains
  package's main information such as description, author, versions...
  In this file ``setuptools`` module will be used to configurate the metadata.

.. code::
  import setuptools
  setuptools.setup(...)

  This file gathers all namespace packages and files that must be included in the distributed
  package.

.. code::

  packages = []
  for package in setuptools.find_namespace_packages(include='ansys*'):
      if package.startswith('ansys.tools.example_coverage'):
          packages.append(package)


  It also extracts the version number from the ``_version.py`` located close to the source code.


Generate the package and upload it on Pypi
------------------------------------------

The first time you want to upload a package on Pypi, you must perform the following
process manually.

Create the python package.

.. code::

  python setup.py sdist

Verify the distribution's long description rendering with twine.

.. code::

  pip install twine
  twine check dist/*

Upload the package to Pypi using twine.

.. code::

  python -m twine upload -u __token__ -p TOKEN_FOR_PYPI --skip-existing dist/*

Then, for the next release upload, you can do it through the ci/cd workflow.
Create a `secret`_ in github settings.
Name it ``PYPI_TOKEN`` and assign it the token provided by Pypi.
This token will be reused in the ci/cd workflow handling the package distribution.

Tag a release
-------------
In order to deploy a new package on Pypi, you must tag a release.
As a reminder, PyAnsys library is following the `trunk-based development`_ source-control branching model.
Consequently, the main version is always up to date.
To tag the release, you must update your main local branch.

.. code::

  git checkout main
  git pull

Then, create the new release branch

.. code::

  git checkout -b release/0.x.x

Change the version number in the _version file.
Commit and push your changes.
Create the tag.

.. code::

  git commit -am "Increase version to 0.x.x" && git tag v0.x.x && git push --tags

Finally, following this tag creation, the workflow responsible for the distribution
will be automatically triggered.

Install a package
-----------------

.. code::

  py -m pip install --upgrade pip
  py -m pip install "SomePackage"

Here is the minimal content of your python project to create a package complying with the standard
mentionned above.

.. toctree::

   ansys
   LICENSE
   README.rst
   setup.py
   tests


.. _namespace packaging: https://packaging.python.org/guides/packaging-namespace-packages/
.. _native namespace packages: https://packaging.python.org/guides/packaging-namespace-packages/#native-namespace-packages
.. _trunk-based development: https://trunkbaseddevelopment.com/
.. _secret: https://docs.github.com/en/actions/reference/encrypted-secrets
.. _setup.py: https://packaging.python.org/tutorials/packaging-projects/#configuring-metadata
