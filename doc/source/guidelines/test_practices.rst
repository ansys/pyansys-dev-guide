.. _testing:

Testing
=======
Unit and integration testing is critical for the successful continuous
integration and delivery of any program or libraries belonging to the PyAnsys
project.

`Test driven development`_ is the practice of writing unit tests before writing
production code. This has the benefit of knowing that each of the new lines of
code are working as soon as they're written. It's easier to track down problems
as only a small amount of code has been implemented since the execution of the
last test. Furthermore, all test cases do not have to be implemented at once
but rather gradually as the code evolves TDD has been created by Kent Beck in
the 1990's as part of the Extreme Programming software development process

We recommend that you follow TDD when developing your PyAnsys project, and
this document contains examples and best practices to help you write them.


Testing Methodology
-------------------
You should consider three levels of testing for your PyAnsys library: unit,
integration, and functional testing.

**Unit** testing validates your library at the lowest possible level, isolating
individual classes and methods without any communication with other libraries
or services.

**Integration** testing validates that your library works in the context of an
application or software stack. For example, if your library extends or wraps
the functionality of an external service, you would need to test that service
in conjunction with your library. On GitHub, the ideal approach for this would
be to start your service via docker and test accordingly. You should still be
testing at the individual class or method level, but you can now test how
multiple libraries or services interact. This is mandatory for testing APIs and
is preferred over mocking the service.

**Functional** testing should be used for validating workflows or long running
examples. For example, if you have a library that wraps a CAD service, you
would validate that you can create complex geometry while directly interfacing
with the service. Functional tests are great at discovering edge cases that are
not normally found at the unit or integration level, but functional testing
should be limited to only a handful of examples as these tend to be long
running and difficult to validate.

Each PyAnsys project should have all three levels of testing implemented in its
testing framework. Consider implementing functional tests as examples within
your project's documentation examples. This will allow you to write helpful
user-facing tests while accomplishing functional testing.


Unit Testing
~~~~~~~~~~~~
Unit testing tests at the lowest possible level isolated
from other applications or libraries. For Python tool libraries like
`ansys-tools-protoc-helper`_, unit testing is sufficient to get high coverage
(> 80%) of your library while actually testing the library.

.. _ansys-tools-protoc-helper: https://github.com/ansys/ansys-tools-protoc-helper

These tests should be written to test a single method in isolation. For
example, if you have a method that deserializes chunks:

.. code:: python
   
    def parse_chunks(chunks):
        """Deserialize gRPC chunks into a numpy array

        Parameters
        ----------
        chunks : generator
            generator from grpc.  Each chunk contains a bytes payload

        dtype : np.dtype
            Numpy data type to interpert chunks as.

        Returns
        -------
        array : np.ndarray
            Deserialized numpy array.

        """
        arrays = []
        for chunk in chunks:
            arrays.append(np.frombuffer(chunk.payload, ANSYS_VALUE_TYPE[chunk.value_type]))

        return np.hstack(arrays)

Your ``test_parse_chunks.py`` would then be:

.. code:: python


    import pytest
    import numpy as np
    from ansys.api.mapdl.v0 import ansys_kernel_pb2 as anskernel

    from ansys.mapdl.core.common_grpc import parse_chunks

    DEFAULT_CHUNKSIZE = 256*1024  # 256 kB


    @pytest.fixture()
    def sample_array():
        """Generate a non-trivial (n x 3) float array."""
        sz = np.random.randint(100000, 200000)
        array = np.random.random((sz, 3)).astype(np.float64)
        assert array.nbytes > DEFAULT_CHUNKSIZE
        return array


    def serialize_chunks(array):
        """Serialize an array into chunks."""
        # convert to raw
        raw = array.tobytes()
        value_type = 5  # float64

        i = 0
        while True:
            piece = raw[i:i + DEFAULT_CHUNKSIZE]
            i += DEFAULT_CHUNKSIZE
            length = len(piece)
            if length == 0:
                break
            yield anskernel.Chunk(payload=piece, size=length, value_type=value_type)


    def test_deserialize_chunks(sample_array):
        parsed_array = parse_chunks(serialize_chunks(sample_array))
        parsed_array = parsed_array.reshape(-1, 3)
        assert np.allclose(sample_array, parsed_array)

This assumes that you do not have a ``serialize_chunks`` function within your
library. If you did, you could exclude it from ``test_parse_chunks.py``


Integration Testing - Wrapped Service Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Any PyAnsys library that provides functionality by wrapping a gRPC interface
should include tests of the gRPC methods exposed by the proto files and wrapped
by the Python library. They would not be expected to test the functionality of
the server, but rather the APIs exposed by the server. For example, if testing
the gRPC method ``GetNode``:

.. code::

   message Node
   {
     int32      id = 1;
     double     x = 2;
     double     y = 3;
     double     z = 4;
   }

   message NodeRequest {
     int32              num = 1;
   }

   message NodeResponse {
     Node               node = 1;
   }

  service SomeService{

     rpc GetNode(NodeRequest)  returns (NodeResponse);
     // other methods
   }

Then your integration test would test the wrapped Python function.  If the
Python library wraps this gRPC method with a ``get_node`` method:

.. code:: python

   from ansys.product.service.v0 import service_pb2

   def get_node(self, index):
       """Return the coordinates of a node for a given index.

       Parameters
       ----------
       index : int
           Index of the node.

       Returns
       -------
       tuple
           Coordinates of the node.

       Examples
       --------
       >>> from ansys.product.service import SomeService
       >>> srv = SomeService()
       >>> srv.create_node(1, 4.5, 9.0, 3.2)
       >>> node = srv.get_node(1)
       >>> node
       (4.5, 9.0, 3.2)

       """
       resp = service_pb2.GetNode(index=index)
       return resp.x, resp.y, resp.z

Your test would be implemented within ``tests/test_nodes.py``:

.. code:: python

   def test_get_node(srv):
       srv.clear()

       node_index = 1
       node_coord = 0, 10, 20
       srv.create_node(node_index, node_coord*)
       assert srv.get_node(node_index) == node_coord

The goal of the unit test should be to test the API rather than the product or
service itself. In the case of ``GetNode``, this method should have already
been tested when designing and developing the service.



Integration Testing - Remote Method Invocation Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In the case of a Remote Method Invocation (RMI)-like method, it is only
necessary to test the method with a basic case and potentially with any edge
cases. A RMI-like API might send and receive strings that are executed on the
server using a custom API or language only available within the context of the
service.

For example, if a method has a RMI service definition of:

.. code::

   message SendCommand()


and a Python wrapping:

.. code:: python

   def send_command(command):
       """Run a command on the server.

       Parameters
       ----------
       command : str
           Command to run on the remote server.

       """

Your example test would be:

.. code:: python

   def test_send_command(srv):
       output = srv.send_command("CREATE,1")
       assert "Created 1" in output

Note that this test only validates that the command ``"CREATE,1"`` has been
received, executed, and sent back to the client. It does not validate all
commands, but doing this is necessary only if there are edge cases, which
include characters that cannot be streamed or using long-running
commands.


Functional Testing
~~~~~~~~~~~~~~~~~~
Functional testing should test the Python library using scripts or examples
that are expected to be executed by the user. Unlike unit or integration
testing, these functional tests are testing the library as a whole by calling
several methods to accomplish a task. These tests should only be run after unit
and integration testing is complete, and they should be run outside the
``pytest`` framework and ideally while building documentation with
`sphinx-gallery`_.

.. note::
   Functional tests should not contribute to global library coverage. Testing
   should always be done on individual function or methods.

.. _sphinx-gallery: https://sphinx-gallery.github.io/


Testing Framework
-----------------
For consistency, PyAnsys tools and libraries should use either the `unittest
<https://docs.python.org/3/library/unittest.html>`_ or `pytest
<https://docs.pytest.org/>`_ frameworks for unit testing. As described in
:ref:`Required Files for a PyAnsys Project`, unit tests should be placed in the ``tests``
directory in the library's root directory::

   tests/
       test_basic.py
       test_advanced.py

Furthermore, any requirements for testing dependencies should be included when
using ``setup.py`` within a ``requirements_tests.txt`` file that is installed
via::

   pip install -r requirements_tests.txt

An alternative is to include requirements for dependencies in the
``pyproject.toml`` file. For example, when using the `poetry`_ build system::

   [tool.poetry.group.test.dependencies]
       pytest>="2.7.3"
       pytest-cov = "*"

And then installed via::

   pip install .[test]

When using ``pytest``, test via::

   pytest

.. note::
   We recommend that you place the source of your library within the ``src``
   directory rather than having your Python library source directly within the
   repository root directory. This helps you avoid testing the source of the
   repository and rather the installed package. This helps to catch errors
   caused by files that might be missed by the installer, including any C
   extensions or additional internal packages.


Files Layout
~~~~~~~~~~~~
PyAnsys libraries should use ``unittest`` or ``pytest`` libraries to run
individual unit tests contained within a ``tests`` directory in the root of the
project.  The specific test files for your project should at a minimum include:

.. code::

   requirements_tests.py
   tests/
     test_<filename>.py
     conftest.py

Requirements File
~~~~~~~~~~~~~~~~~
The requirements file contains a list of all the libraries that must be
installed to run ``pytest``.  No assumption should be made regarding the state
of the virtual


Coverage
--------
Given that Python is an interpreted language, developers of Python libraries
should aim to have high coverage for their libraries as only syntax errors can
be caught during the almost trivial compile time. Coverage is defined as parts
of the executable and usable source that are tested by unit tests. You can use
the `pytest-cov <https://pytest-cov.readthedocs.io/>`_ library to view the
coverage for your library. For example::

  $ pytest --cov numpydoc_validation
   ============================= test session starts ==============================
   platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
   rootdir: /home/user/python/numpydoc_validation
   plugins: cov-3.0.0
   collected 1 item

   tests/test_validate.py .                                                 [100%]

   ---------- coverage: platform linux, python 3.8.10-final-0 -----------
   Name                               Stmts   Miss  Cover
   ------------------------------------------------------
   numpydoc_validation/__init__.py        2      0   100%
   numpydoc_validation/_validate.py      69      0   100%
   ------------------------------------------------------
   TOTAL                                 71      0   100%

While 100% coverage is ideal, the law of diminishing returns often applies to
the coverage of a Python library. Consequently, achieving 80-90% coverage is
often sufficient.  For parts of your library that are difficult or impossible
to test, consider using ``# pragma: no cover`` at the end of the method
definition, branch, or line to denote that part of the code cannot be
reasonably tested.  For example, if part of your module performs a simple
``import`` test of ``matplotlib`` and raises an error when the library is not
installed, it is not reasonable to attempt to test this and assume full
coverage:

.. code:: python

   try:
       import matplotlib
   except ImportError:  # pragma: no cover
       raise ImportError("Install matplotlib to use this feature.")

.. note::
   You should only avoid coverage of parts of your library where you cannot
   reasonably test without an extensive testing suite or setup.  Most methods
   and classes, including edge cases, can be reasonably tested. Even parts of
   your code that raise errors like ``TypeError`` or ``ValueError`` when users
   input the wrong data type or value can be reasonably tested.

Code Coverage Enforcement
~~~~~~~~~~~~~~~~~~~~~~~~~
One way of enforcing unit test coverage with a project on GitHub is to use the
codecov.io to enforce minimum patch (and optionally project) coverage. As this
application is already available to the `PyAnsys Organization
<https://github.com/pyansys>`_, simply add the following to the root directory
of your repository:

**/codecov.yml**

.. code:: yaml

   comment:
     layout: "diff"
     behavior: default

   coverage:
     status:
       project:
         default:
           # basic
           # target: 50%
           threshold: 0%
           # advanced
           if_not_found: success
           if_ci_failed: error
           if_no_uploads: error
       patch:
         default:
           # basic
           target: 90%
           if_not_found: success
           if_ci_failed: error
           if_no_uploads: error

This requires that each PR has a patch coverage of 90%, meaning that 90% of any
source added to the repository (unless ignored) must be covered by unit tests.

.. note::
   This is only a sample configuration.


Unit Testing on GitHub via CI/CD
--------------------------------
Effective CI/CD assumes that unit testing is developed during feature
development or bug fixes. However, given the limited scope of the local
development environment, it is often not possible to enforce testing on
multiple platforms, or even unit testing in general. However, with the right
automated CI/CD, such testing can still occur and be enforced automatically.

`GitHub Actions`_ is the preferred automated CI/CD platform for running Python
library unit tests for PyAnsys, and it can be used immediately by cloning the
project `template <https://github.com/pyansys/template/>`_. If you are
unfamiliar with GitHub Actions, see `GitHub Actions`_ for an overview.

.. _GitHub Actions: https://github.com/features/actions

The following sections describe the usage of a simple GitHub workflow for a
PyAnsys library:

Setup
~~~~~
Include the job name when it should be run at the top of the workflow
``.yml``::

   name: Unit Testing

   on:
     pull_request:
     workflow_dispatch:
     push:
       tags:
         - "*"
       branches:
         - main

Take note that this workflow runs on all pull requests and on demand with
``workflow_dispatch``. On commits, this workflow runs only on tags and on the
``main`` branch.  This ensures that CI/CD is not run twice on every commit for
each PR, which may saturate available build or testing machines.


Job Description
~~~~~~~~~~~~~~~
PyAnsys libraries should run on the currently supported versions of Python on
both Windows and Linux (and ideally on Mac OS). Therefore, it is necessary to
also test on both Linux and Windows for these versions of Python. Use the
``matrix`` run strategy for the job with both the latest images of Windows and
Linux::

   jobs:
     unit_tests:
       name: Unit testing
       runs-on: ${{ matrix.os }}
       strategy:
         matrix:
           os: [windows-latest, ubuntu-latest]
           python-version: ['3.7', '3.8', '3.9', '3.10']


Running the Tests
~~~~~~~~~~~~~~~~~
Each virtual machine within GitHub Actions starts in a fresh state with no
software or source downloaded or installed. Therefore, you must clone the
repository using the ``checkout`` action, set up Python, and install the
necessary testing dependencies.

.. code::

   steps:
     - uses: actions/checkout@v2
     - name: Set up Python ${{ matrix.python-version }}
       uses: actions/setup-python@v1
       with:
         python-version: ${{ matrix.python-version }}


If you are using ``setup.py``, install with:


.. code:: yaml

     - name: Install the library
       run: |
         pip install .
         pip install -r requirements_test.txt


If you are using ``pyproject.toml`` with the `poetry`_ build system, install
with:

.. code:: yaml

   - name: Install the library and dependencies
     run: |
       pip install poetry
       poetry install


Run the unit tests via ``pytest`` with:

.. code:: yaml

   - name: Test and show coverage
     working-directory: tests
     run: pytest --cov ansys.product.library

.. note::
   Replace ``ansys.product.library`` with your library name. This should match
   how it would be imported within Python. For example, rather than
   ``ansys-product-library``, use ``ansys.product.library``.

Optionally, though highly recommended, upload your unit test coverage to
`codecov.io`_ with:

.. code:: yaml

   - uses: codecov/codecov-action@v2
     name: 'Upload coverage to Codecov'

.. _Test driven development: https://en.wikipedia.org/wiki/Test-driven_development
.. _codecov.io: https://app.codecov.io/gh/pyansys
.. _poetry: https://python-poetry.org
