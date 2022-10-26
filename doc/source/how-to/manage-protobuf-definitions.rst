Manage Protobuf Definitions
===========================

Protobuf service definitions provide the API specification for underlying
server implementations, so that each consuming client library has a clear
contract for gRPC data messages. Ideally, the proto files have a single
repository established as the source of truth for the .proto files,
organized by API version increment as the API definition expands and changes.
Since most client libraries are custom implementations enhancing the developer
experience when consuming the service, releasing the Protobuf definitions
publicly gives full flexibility to the developer to operate at the abstraction
layer they choose to do so.

Maintain API definition repository
----------------------------------

The Protobuf definition of the service is language agnostic, so the repository
containing the protobuf files can be created within the top-level Ansys
GitHub organization. Every update of the protobuf files will go through
a standard pull request process. Language specific packages are generated
for each merge or on a regular cadence.

Managing proto definitions for Python clients
---------------------------------------------

Building Python stub classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The API repository will need a python project definition that can be utilized
within the CI/CD build pipeline.

A common tool to help build python stub classes is available and maintained
within Ansys:

`ansys-tools-protoc-helper <https://github.com/ansys/ansys-tools-protoc-helper/>`_

Example inclusion within pyproject.toml build dependency configuration:

.. code-block:: toml

    [build-system]
    requires = ["setuptools >= 42.0.0", "wheel", "ansys_tools_protoc_helper"]

Basic python project build step that can be executed locally or within a
build pipeline:

.. code-block:: python

    pip install -U pip
    pip install build
    python -m build

Publishing Python API package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PyPi is the common package manager where API packages are released.

Example nightly build pipeline publishing the python stub package:

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
        - name: Upload to PyPi
            run: |
            pip install twine
            twine upload --skip-existing ./**/*.whl
            twine upload --skip-existing ./**/*.tar.gz
            env:
            TWINE_USERNAME: PAT
            TWINE_PASSWORD: ${{ secrets.PYANSYS_PYPI_PAT }} 
            TWINE_REPOSITORY_URL: https://pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi/upload
    
        - name: Upload packages
            uses: actions/upload-artifact@v3
            with:
            name: ansys-api-<api-name>-packages
            path: dist/
            retention-days: 7


Consuming the API package within Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the api package has been published to pypi, a reference can be included within
the client library build dependencies.

Example poetry configuration:

.. code-block:: toml

    [tool.poetry.dependencies]
    python = ">=3.7,<4.0"
    ansys-api-<api-name> = {version = "==*.*.*", source = "pypi"}

The stub imports follow a standard pattern. For each API service, there is a ***_pb2
module which defines all of the messages defined within that specific service file and
a ***_pb2_grpc module that defines a Stub class that encapsulates all service methods.

Example grpc imports within the wrapping client library:

.. code-block:: python

    from ansys.api.geometry.v0.designs_pb2 import (
        ExportDesignRequest,
        NewDesignRequest,
        SaveAsDocumentRequest,
    )
    from ansys.api.geometry.v0.designs_pb2_grpc import DesignsStub

The best practice is to create a pythonic client library that organizes the service methods
in a very user-friendly manner and at a minimum acts as a facade layer wrapping the
service calls so that the pythonic API can have a consistent abstraction, independent of
underlying implementations.
