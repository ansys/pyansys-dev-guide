Manage Protobuf definitions
===========================

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

Here is an example of a nightly build pipeline publishing the Python stub package:

.. code-block:: yml

    name: Nightly dev release
  
    on:
      schedule: # UTC at 0300
        - cron: "0 5 * * *"
      workflow_dispatch:
          
    env:
      MAIN_PYTHON_VERSION: '3.10'
    
    jobs:
    nightly-release:
        name: Nightly release package
        if: github.ref == 'refs/heads/main'
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@v3
    
        - name: Append date to version tags
            run: |
            PACKAGE_DATE=$(date +'%Y%m%d%H%M')
            sed -i "1s/.$/$PACKAGE_DATE/" ansys/api/<api-name>/VERSION
        - name: Set up Python
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
            python -c "import ansys.api.<api-name>.v0; print('Successfully imported ansys.api.<api-name>.v0')"
            python -c "from ansys.api.<api-name> import __version__; print(__version__)"

        - name: Upload to PyPI
            run: |
            pip install twine
            twine upload --skip-existing ./**/*.whl
            twine upload --skip-existing ./**/*.tar.gz
            env:
            TWINE_USERNAME: PAT
            TWINE_PASSWORD: ${{ secrets.PYANSYS_PyPI_PAT }} 
            TWINE_REPOSITORY_URL: https://pkgs.dev.azure.com/pyansys/_packaging/pyansys/PyPI/upload
    
        - name: Upload packages
            uses: actions/upload-artifact@v3
            with:
            name: ansys-api-<api-name>-packages
            path: dist/
            retention-days: 7

PyPI packages follow semantic versioning while gRPC Protobuf API versions typically follow a simplified ``v*``
versioning pattern. It is not expected to synchronize the PyPI package version with the Protobuf API version.
There is no methodology to correlate the PyPI package version with exposed gRPC API versions included within
the package.


Consuming the API package within Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the API package has been published to PyPI, a reference can be included within
the client library build dependencies.

Example ``poetry`` configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: toml

    [tool.poetry.dependencies]
    python = ">=3.7,<4.0"
    ansys-api-<api-name> = {version = "==*.*.*", source = "PyPI"}

The stub imports follow a standard pattern. For each API service, there is a ***_pb2
module that defines all messages within a specific service file and
a ``*_pb2_grpc`` module that defines a ``Stub`` class that encapsulates all service methods.

Example gRPC imports within the wrapping client library
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
