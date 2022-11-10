gRPC API Packages
=================

Protobuf service definitions provide the API specification for underlying
server implementations so that each consuming client library has a clear
contract for gRPC data messages. Ideally, the ``.proto`` files have a single
repository established as the source of truth, organized by API version
increment as the API definition expands and changes. Because most client
libraries are custom implementations enhancing the developer experience
when consuming the service, releasing the Protobuf definitions
publicly gives full flexibility to developers to operate at the abstraction
layer they choose.

Maintain API definition repository
----------------------------------

Because the Protobuf definition of the service is language agnostic, the repository
containing the Protobuf files can be created within the top-level
`Ansys GitHub organization <https://github.com/ansys/>`_.
Every update of the Protobuf files follows a standard
pull request process as a sanity check for API definition accuracy. Language-
specific packages can be generated for each merge or on a set cadence.

Managing Protobuf definitions for Python clients
------------------------------------------------

Within Ansys, and more specifically in the PyAnsys environment, most client libraries
have a dedicated Python package containing the needed ``.proto`` files compiled as
Python source code. These are typically consumed by the PyAnsys client libraries
for being able to communicate with their respective services.

For example, `PyMAPDL <https://github.com/pyansys/pymapdl>`_ consumes the
``ansys-api-mapdl`` package, which is build in the following
`ansys-api-mapdl repository <https://github.com/ansys/ansys-api-mapdl>`_.

How to build an ``ansys-api-<service>`` repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `Ansys GitHub organization`_ has a dedicated template repository for creating
these ``.proto`` file repositories and the needed files to generate the Python API
packages to be consumed by the PyAnsys clients.

In order to set up an API repository as ``ansys-api-mapdl``, there is a template
repository available known as `ansys-api-template <https://github.com/ansys/ansys-api-template>`_.
Follow the instructions on the `Expected usage <https://github.com/ansys/ansys-api-template#expected-usage>`_
section to understand how to use the template repository.

Building Python stub classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add a Python project definition to the API repository that can be consumed by
the Pythonic client of the service this API repository refers to.

A common tool to help build Python stub classes is available and maintained
within Ansys:

`ansys-tools-protoc-helper <https://github.com/ansys/ansys-tools-protoc-helper/>`_

Here is an example of how to include this tool in the ``pyproject.toml`` file as a build dependency:

.. code-block:: toml

    [build-system]
    requires = ["setuptools >= 42.0.0", "wheel", "ansys_tools_protoc_helper"]

The following basic Python steps for building a project can be executed locally or within a
build pipeline:

.. code-block:: python

    pip install -U pip
    pip install build
    python -m build

Publishing Python API package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PyPI is the common package manager where API packages are released.

Here is an example of a workflow pipeline for building and publishing the Python stub package.
In this example, the ``ansys-api-geometry`` workflow is shown. However, this workflow can be
easily copied and adapted. Only the ``PYTHON_PACKAGE_IMPORT`` environment variable
would have to be changed:

.. code-block:: yaml

    name: GitHub CI

    on:
      pull_request:
      push:
        tags:
          - "*"
        branches:
          - main

    env:
      MAIN_PYTHON_VERSION: '3.10'
      PYTHON_PACKAGE_IMPORT: 'ansys.api.geometry.v0'

    jobs:
      build:
        name: Build package
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v3

          - name: Setup Python
            uses: actions/setup-python@v4
            with:
              python-version: ${{ env.MAIN_PYTHON_VERSION }}

          - name: Install build requirements
            run: |
              pip install -U pip
              pip install build

          - name: Build
            run: python -m build
    
          - name: Install
            run: pip install dist/*.whl
    
          - name: Test import
            run: |
              mkdir tmp
              cd tmp
              python -c "import ${{ env.PYTHON_PACKAGE_IMPORT }}; print('Successfully imported ${{ env.PYTHON_PACKAGE_IMPORT }}')"
              python -c "from  import __version__; print(__version__)"
    
          - name: Upload packages
            uses: actions/upload-artifact@v3
            with:
              name: ansys-api-package
              path: dist/
              retention-days: 7
    
      release:
        name: Release package
        if: github.event_name == 'push' && contains(github.ref, 'refs/tags')
        needs: [build]
        runs-on: ubuntu-latest
        steps:
          - name: Set up Python
            uses: actions/setup-python@v4
            with:
              python-version: ${{ env.MAIN_PYTHON_VERSION }}

          - uses: actions/download-artifact@v3

          - name: Display structure of downloaded files
            run: ls -R

          - name: Upload to Public PyPi
            run: |
              pip install twine
              twine upload --skip-existing ./**/*.whl
              twine upload --skip-existing ./**/*.tar.gz
            env:
              TWINE_USERNAME: __token__
              TWINE_PASSWORD: ${{ secrets.PYPI_TOKEN }} 

          - name: Release
            uses: softprops/action-gh-release@v1
            with:
              generate_release_notes: true
              files: |
                ./**/*.whl
                ./**/*.tar.gz
                ./**/*.pdf

PyPI packages follow semantic versioning while gRPC Protobuf API versions typically follow a simplified ``v*``
versioning pattern. It is not expected to synchronize the PyPI package version with the Protobuf API version.
There is no methodology to correlate the PyPI package version with exposed gRPC API versions included within
the package.

As it may be seen in the ``release`` section of the previous workflow, once the Python API package is compiled
it is uploaded to the public PyPI. In order to do so, it is necessary to have access to the ``PYPI_TOKEN`` for
this Python package. Please contact the PyAnsys Core team at
`pyansys.core@ansys.com <mailto:pyansys.core@ansys.com>`_ in order to get the needed credentials.

If the repository cannot be uploaded to the public PyPI yet, but your Python client library needs to consume this
Python API package, it can also be uploaded to the private PyAnsys PyPI. Email the PyAnsys Core
team at `pyansys.core@ansys.com`_ for the required ``PYANSYS_PYPI_PRIVATE_PAT`` password.

In this last case, the workflow section ``Upload to Public PyPi`` should be replaced by this one:

.. code-block:: yaml

    - name: Upload to Private PyPi
        run: |
          pip install twine
          twine upload --skip-existing ./**/*.whl
          twine upload --skip-existing ./**/*.tar.gz
        env:
          TWINE_USERNAME: PAT
          TWINE_PASSWORD: ${{ secrets.PYANSYS_PYPI_PRIVATE_PAT }} 
          TWINE_REPOSITORY_URL: https://pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi/upload


Consuming the API package within Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the API package has been published to PyPI, a reference can be included within
the client library build dependencies.

Example ``poetry`` configuration
++++++++++++++++++++++++++++++++

.. code-block:: toml

    [tool.poetry.dependencies]
    python = ">=3.7,<4.0"
    ansys-api-<api-name> = "==*.*.*"

Example ``flit`` configuration
++++++++++++++++++++++++++++++

.. code-block:: toml

    dependencies = [
        ansys-api-<api-name>==*.*.*,
        ...
    ]

Using the API package within the Python client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The stub imports follow a standard pattern. For each API service, there is a ``*_pb2``
module that defines all messages within a specific service file and
a ``*_pb2_grpc`` module that defines a ``Stub`` class that encapsulates all service methods.

Example gRPC imports within the wrapping client library
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python

    from ansys.api.geometry.v0.designs_pb2 import (
        ExportDesignRequest,
        NewDesignRequest,
        SaveAsDocumentRequest,
    )
    from ansys.api.geometry.v0.designs_pb2_grpc import DesignsStub

The best practice is to create a Pythonic client library that organizes the service methods
in a user-friendly manner. At a minimum, this library should act as a facade layer wrapping the
service calls so that the Pythonic API can have a consistent abstraction, independent of
underlying implementations.

For each client library release, only a single gRPC API version should be wrapped
to maintain a consistent API abstraction expectation for the supporting server instances.

Public vs private Python API package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Making these ``.proto`` files repositories public or private is up to the owner of each repository.

In terms of intellectual property (IP) concerns, the ``.proto`` files are typically not an
issue since they do not expose any critical service logic or knowledge - and in most cases
the APIs being exposed through the ``.proto`` files are already exposed through other
mechanisms publicly.

Thus, the general recommendation is to make these repositories public as soon as possible. The
main reasons behind are:

* Private Python package dependencies usually involve workarounds when setting up the
  workflow. It is best to keep the workflows as standard and simple as possible. That
  implies making all its dependencies public - including this API Python package.

* The API Python package generated eventually has to be uploaded to the public PyPI, so
  that it can be consumed by its corresponding Python client library (when it is publicly released).
  So, better make it public sooner than later if there are no issues with it.

* Once the Python API package is publicly released to PyPI, there is no reason behind keeping the
  repository private since all users which consume the Python API package have direct access
  to the ``.proto`` files that are in the repository.

However, before making any repository public with the `Ansys GitHub organization`_, please review
the `Ansys open-source guide documentation <https://supreme-invention-8c3992a9.pages.github.io/index.html>`_
to verify that the repository is compliant with all the needed requirements.
