How to create a package
#######################
Python packages are used to organize and structure a python project containing many modules and
all kind of assets such as unit tests or documentation.
They offer an easy, reliable and comprehensive way to distribute and install
python code on different platforms.


Namespace package
-----------------
PyAnsys libraries use the `namespace_packaging`_.
Namespace packages allow the user to easily split subpackages from a package into
single and independant distribution.

Three different approaches are currently supported to create a namespace package:
* `native namespace packages`_
* pkgutil-style namespace packages
* pkg_resources-style namespace packages

Required files
--------------
*README.rst file is used to describe the purpose of the package.
  *The format of this file must be reStructuredText.*

*LICENSE file to specify the copyrigths and required authorization.

*setup.py file to provide package main information.
  The presence of this file indicate that the package was likely created using disutils
  which is the python standard for building and distributing python package.

  This file contains package main information such as description, author, versions...
  This file gathers all namespace packages. It extract the version number from the ``_version.py``
  located in the source code.


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
  python -m twine upload -u __token__ -p PYPI_TOKEN --skip-existing dist/*

Then, for the next release upload, you can do it through the ci/cd workflow.
Create a secret in github setting.
Name it ``PYPI_TOKEN`` and assign it the token provided by Pypi.
This token will be reused in the ci/cd workflow used for the pacakge distribution.

Tag a release
-------------
In order to deploy a new pacakge on Pypi, you must tag a release.
As a reminder, PyAnsys library is following a trunk based development.
Consequently, the main version is always containing the last version of the package.
To tag the release, you must update your main local branch.

.. code::
  git checkout main
  git pull

Then, create the new release branch

.. code::
  git checkout -b release/0.1

Change the version number in the _version file.
Commit and push your changes.
Create the tag.

.. code::
  git commit -am "Increase version to 0.x.x" && git tag v0.x.x && git push --tags

Install a package
-----------------

.. code::
  py -m pip install --upgrade pip
  py -m pip install "SomePackage"


.. toctree::
   ansys
   LICENSE
   README.rst
   tests


.. _namespace_packaging: https://packaging.python.org/guides/packaging-namespace-packages/
.. _native_namespace_packages: https://packaging.python.org/guides/packaging-namespace-packages/#native-namespace-packages

