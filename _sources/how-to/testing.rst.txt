.. _testing:

Testing
=======

Unit testing and integration testing are critical for the successful continuous
integration (CI) and delivery of any library belonging to the PyAnsys
project.

In 1993, Kent Beck developed `Test Driven Development (TDD)`_ as part
of the Extreme Programming software development process. TDD is the practice
of writing unit tests before writing production code. The benefit of this practice
is that you know each new line of code is working as soon as it is written. It's
easier to track down problems because only a small amount of code has been implemented
since the execution of the last test. Furthermore, all test cases do not have to be
implemented at once but rather gradually as the code evolves.

You should follow TDD when developing your PyAnsys project. Examples
and best practices for unit tests follow.

Test framework
--------------
.. raw:: html
    
    <div align="center">
      <img width="30%"; src="https://docs.pytest.org/en/7.1.x/_static/pytest_logo_curves.svg">
    </div>

For consistency, PyAnsys tools and libraries should use either the `pytest`_ or
`unittest <https://docs.python.org/3/library/unittest.html>`_ framework
for unit testing. The ``pytest`` framework is recommended unless a constraint
in your project prevents you from using it. As described in :ref:`Required files`,
you should place unit tests in :ref:`The \`\`tests\`\` directory` in the library's
root directory.

Add testing dependencies
~~~~~~~~~~~~~~~~~~~~~~~~

Requirements for testing dependencies should be included in :ref:`The
\`\`setup.py\`\` file`, :ref:`The \`\`pyproject.toml\`\` file`, or a
``requirements_tests.txt`` file. Only ``pytest`` and `pytest-cov`_
must be specified as third-party dependencies because ``unittest`` is included
in `The Python Standard Library <https://docs.python.org/3/library/>`_.

.. tab-set::

    .. tab-item:: Flit

        .. code-block:: toml

            [project.optional-dependencies]
            test = [
                "pytest",
                "pytest-cov",
            ]

    .. tab-item:: Poetry

        .. code-block:: toml

            [tool.poetry.group.test.dependencies]
            pytest = "*"
            pytest-cov = "*"

    .. tab-item:: Setuptools

        .. code-block:: python

            setup(
                name="ansys-<product>-<library>",
                ...,
                extras_require={
                    "test": ["pytest", "pytest-cov"],
                },
            )

    .. tab-item:: Requirements

        .. code-block:: text

            pytest
            pytest-cov

You can use ``pip`` to install these testing dependencies:

.. tab-set::

    .. tab-item:: From setup.py or pyproject.toml

        .. code-block:: text

            python -m pip install .[test]

    .. tab-item:: From requirements_tests.txt

        .. code-block:: text

            python -m pip install -r requirements_tests.txt


Organize test files
~~~~~~~~~~~~~~~~~~~

You must place your test files in :ref:`The \`\`tests\`\` directory`. To
guarantee that tests are run against the library source code, follow a ``src``
layout as explained in :ref:`The \`\`src\`\` directory` rather than
having your Python library source located directly in the repository root directory. 

This helps you to achieve these objectives:

- Avoid testing the source of the repository rather than testing the installed package.
- Catch errors caused by files that might be missed by the installer, including any
  C extensions or additional internal packages.

Test execution
--------------

Once you have installed ``pytest``, you can execute the test suite with this command:

.. code-block:: text

    pytest -v tests/

Filter tests
~~~~~~~~~~~~

To run a subset of all available tests, you can taking advantage
of the ``keywords`` and ``markers`` flags:

**Filter tests by keywords**

.. code-block:: text

    pytest -k '<name pattern>'
    pytest -k 'not <name pattern>'

**Filter tests by markers**

.. code-block:: text

    pytest -m slow

For more information about filtering tests, see `Working with custom markers
<https://docs.pytest.org/en/latest/example/markers.html>`_ in the ``pytest``
documentation.

Testing methodology
-------------------

You should consider three levels of testing for your PyAnsys library: unit,
integration, and functional.

* :ref:`Unit testing` validates your library at the lowest possible level, isolating
  individual classes and methods without any communication with other libraries
  or services.

* :ref:`Integration testing` validates that your library works in the context of an
  app or software stack. For example, if your library extends or wraps
  the features of an external service, you must test that service
  in conjunction with your library. On GitHub, the ideal approach for this would
  be to start your service using `Docker`_ and then test accordingly. You should still be
  testing at the individual class or method level, but you can now test how
  multiple libraries or services interact. This is mandatory for testing APIs and
  is preferred over mocking the service.

* :ref:`Functional testing` should be used for validating workflows or long-running
  examples. Assume that you have a library that wraps a CAD service. You
  would validate that you can create complex geometry while directly interfacing
  with the service. Functional tests are great at discovering edge cases that are
  not normally found at the unit or integration level. However, functional testing
  should be limited to only a handful of examples because these tend to be long
  running and difficult to validate.

Each PyAnsys project should have all three levels of testing implemented in its
testing framework. Consider implementing functional tests as examples within
your project's documentation examples. This lets you write helpful
user-facing tests while accomplishing functional testing.

Unit testing
~~~~~~~~~~~~
Unit testing tests at the lowest possible level, isolated
from other applications or libraries. For Python tool libraries like
`ansys-tools-protoc-helper`_, unit testing is sufficient to get high coverage
(> 80%) of your library while actually testing the library.

.. _ansys-tools-protoc-helper: https://github.com/ansys/ansys-tools-protoc-helper

These tests should be written to test a single method in isolation. For example,
the following ``parse_chunks.py`` file has a method that deserializes chunks. The
associated ``test_parse_chunks_py`` file tests this method in isolation.

.. note:: 
    This example assumes that you do not have a ``serialize_chunks`` function in your
    library. If you did, you could exclude it from the ``test_parse_chunks.py`` file.

.. tab-set:: 

    .. tab-item:: parse_chunks.py
    
        .. code-block:: python
        
           def parse_chunks(chunks):
               """Deserialize gRPC chunks into a Numpy array.

               Parameters
               ----------
               chunks : generator
                   Generator from gRPC. Each chunk contains a bytes payload.

               dtype : np.dtype
                   Numpy data type to interpret chunks as.

               Returns
               -------
               array : np.ndarray
                   Deserialized Numpy array.

               """
               arrays = []
               for chunk in chunks:
                   arrays.append(np.frombuffer(chunk.payload, ANSYS_VALUE_TYPE[chunk.value_type]))
        
                return np.hstack(arrays)
    
    .. tab-item:: test_parse_chunks.py
    
        .. code-block:: python
        
            from ansys.api.mapdl.v0 import ansys_kernel_pb2 as anskernel
            import numpy as np
            import pytest
        
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

Integration testing
~~~~~~~~~~~~~~~~~~~

This section explains :ref:`Wrapped service methods` and how to
:ref:`Test using remote method invocation`. 

Wrapped service methods
+++++++++++++++++++++++

Any PyAnsys library that provides features by wrapping a gRPC interface
should include tests of the gRPC methods exposed by the PROTO files and wrapped
by the Python library. They would not be expected to test the features of
the server but rather the APIs exposed by the server. For example, if testing
the ``GetNode`` gRPC method, then your integration test would test the wrapped
Python function. If the Python library wraps this gRPC method with a
``get_node`` method, your test would be implemented within the
``tests/test_nodes.py`` file.

.. tab-set::

    .. tab-item:: gRPC code

        .. code-block:: rust
        
           message Node
           {
             int32      id = 1;
             double     x = 2;
             double     y = 3;
             double     z = 4;
           }
        
           message NodeRequest {
             int32      num = 1;
           }
        
           message NodeResponse {
             Node       node = 1;
           }
        
          service SomeService {
        
             rpc GetNode(NodeRequest)  returns (NodeResponse);
             // other methods
           }

    .. tab-item:: Python code

        .. code-block:: python
        
           from ansys.product.service.v0 import service_pb2
        
           def get_node(self, index):
               """Get the coordinates of a node for a given index.
        
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


    .. tab-item:: Unit test

        .. code-block:: python
        
           def test_get_node(srv):
               srv.clear()
        
               node_index = 1
               node_coord = 0, 10, 20
               srv.create_node(node_index, node_coord*)
               assert srv.get_node(node_index) == node_coord

The goal of the unit test should be to test the API rather than the product or
service. The ``GetNode`` gRPC method should have already been tested when
designing and developing the service.

Test using remote method invocation
+++++++++++++++++++++++++++++++++++

For a Remote Method Invocation (RMI)-like method, it is only
necessary to test the method with a basic case and potentially with any edge
cases. A RMI-like API might send and receive strings that are executed on the
server using a custom API or language only available within the context of the
service.

For example, if a method has a RMI service definition named ``SendCommand()`` and
a Python wrapping named ``send_command``, your code and the example test would look
like this:

.. tab-set::

    .. tab-item:: gRPC code

        .. code-block:: rust
        
           message SendCommand()

    .. tab-item:: Python code

        .. code-block:: python
        
            def send_command(command):
                """Run a command on the remote server.

                Parameters
                ----------
                command : str
                    Command to run on the remote server.
                """

    .. tab-item:: Unit test
    
        .. code-block:: python
        
           def test_send_command(srv):
               output = srv.send_command("CREATE,1")
               assert "Created 1" in output

Note that this test only validates that the ``"CREATE,1"`` command has been
received, executed, and sent back to the client. It does not validate all
commands. Running such a test is necessary only if there are edge cases, which
include characters that cannot be streamed or use long-running commands.

Functional testing
~~~~~~~~~~~~~~~~~~

Functional testing should test the Python library using scripts or examples
that are expected to be executed by the user. Unlike unit or integration
testing, functional tests are testing the library as a whole by calling
several methods to accomplish a task. You should run these tests only after unit
and integration testing is complete. Ideally, you should run them outside the
``pytest`` framework while building documentation with `Sphinx-Gallery <Sphinx_ext_sphinx_gallery_>`_.

.. note::
   Functional tests should not contribute to global library coverage. Testing
   should always be done on individual functions or methods.

Test code coverage
------------------

Because Python is an interpreted language, syntax errors can only be
caught during the almost trivial compile times. Thus, developers of Python libraries
should aim to have high coverage for their libraries. Coverage is defined as parts
of the executable and usable source that are tested by unit tests. You can use
the `pytest-cov`_ library to view the coverage for your library.

Configure code coverage
~~~~~~~~~~~~~~~~~~~~~~~

If you do not configure code coverage properly, the resulting report does
not show the real scope covered by the test suite.

Assuming that a ``PyAnsys`` project follows :ref:`The \`\`src\`\` directory` layout,
you must pass the following flag when :ref:`executing tests <Test execution>`:

.. code-block:: text

    pytest --cov=ansys.<product>.<library> --cov-report=term tests/

This command tells ``pytest-cov`` to look for source code in the
``src/ansys/<product>`` directory and generate a terminal report for all tests
located in :ref:`The \`\`tests\`\` directory`.

While 100% coverage is ideal, the law of diminishing returns applies to
the coverage of a Python library. Consequently, achieving 80-90% coverage is
often sufficient. For parts of your library that are difficult or impossible
to test, consider using ``# pragma: no cover`` at the end of the method
definition, branch, or line to denote that part of the code cannot be
reasonably tested. For example, if part of your module performs a simple
``import`` test of ``matplotlib`` and raises an error when the library is not
installed, it is not reasonable to attempt to test this and assume full
coverage:

.. code:: python

   try:
       import matplotlib
   except ImportError:  # pragma: no cover
       raise ImportError("Install matplotlib to use this feature.")

You should only avoid coverage of parts of your library where you cannot
reasonably test without an extensive testing suite or setup. Most methods and
classes, including edge cases, can be reasonably tested. Even parts of your code
that raise errors like ``TypeError`` or ``ValueError`` when users input the
wrong data type or value can be reasonably tested.

Enforce code coverage
~~~~~~~~~~~~~~~~~~~~~

One way of enforcing unit test coverage with a project on GitHub is to use
``codecov.io`` to enforce minimum patch (and optionally project) coverage. Because
this app is already available to the `Ansys GitHub organization`_, you can simply
add a ``codecov.yml`` file to the root directory of your repository. This example
file provides a sample configuration:

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

Using a ``codecov.yml`` file requires that each PR has a patch coverage of 90%, meaning that 90% of any
source added to the repository (unless ignored) must be covered by unit tests.

Test using GitHub Actions
-------------------------

Effective CI/CD assumes that unit testing is developed during feature
development or bug fixes. However, given the limited scope of the local
development environment, it is often not possible to enforce testing on
multiple platforms, or even to enforce unit testing in general. However, with the proper
automated CI/CD, such testing can still occur and be enforced automatically.

`GitHub Actions`_ is the preferred automated CI/CD platform for running Python
library unit tests for PyAnsys. It can be used immediately by cloning the
project `template <https://github.com/ansys/template/>`_.

.. literalinclude:: code/tests.yml     
   :language: yaml
