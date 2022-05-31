Testing
=======
Unit and integration testing is critical for the successful continuous
integration and delivery of any program or libraries belonging to the PyAnsys
project.

`Test Driven Development (TDD)`_ is the practice of writing unit tests before writing
production code. This has the benefit of knowing that each of the new lines of
code are working as soon as they're written. It's easier to track down problems
as only a small amount of code has been implemented since the execution of the
last test. Furthermore, all test cases do not have to be implemented at once but
rather gradually as the code evolves TDD has been created by Kent Beck in the
1990's as part of the Extreme Programming software development process

We recommend that you follow TDD when developing your PyAnsys project, and this
document contains examples and best practices to help you write them.

Testing Framework
-----------------
.. raw:: html
    
    <div align="center">
      <img width="50%"; src="https://docs.pytest.org/en/7.1.x/_static/pytest_logo_curves.svg">
    </div>

For consistency, PyAnsys tools and libraries should use either the `unittest
<https://docs.python.org/3/library/unittest.html>`_ or `pytest
<https://docs.pytest.org/>`_ frameworks for unit testing. This last framework is
recommended unless any contrain prevents you from using it in your project.  As
described in :ref:`Required Files`, unit tests should be placed in :ref:`The
\`\`tests/\`\` Directory` in the library's root directory.


Adding Testing Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Requirements for testing dependencies should be included either in :ref:`The
\`\`setup.py\`\` File`, :ref:`The \`\`pyproject.toml\`\` File` or in a
``requirements_tests.txt`` file. Notice that only ``pytest`` and ``pytest-cov``
need to be specified as third party dependencies since ``unittest`` is included
in `The Python Standard Library <https://docs.python.org/3/library/>`_.

.. tabs::

    .. tab:: Flit

        .. code-block:: toml

            [project.optional-dependencies]
            test = [
                "pytest",
                "pytest-cov",
            ]

    .. tab:: Poetry

        .. code-block:: toml

            [tool.poetry.group.test.dependencies]
            pytest = "*"
            pytest-cov = "*"

    .. tab:: Setuptools

        .. code-block:: python

            setup(
                name="ansys-<product>-<library>",
                ...,
                extras_require={
                    "test": ["pytest", "pytest-cov"],
                },
            )

    .. tab:: Requirements

        .. code-block:: text

            pytest
            pytest-cov


These dependencies can be installed using ``pip``:

.. tabs::

    .. tab:: From setup.py or pyproject.toml

        .. code-block:: text

            python -m pip install .[test]

    .. tab:: From requirements_tests.txt

        .. code-block:: text

            python -m pip install -r requirements_tests.txt


Organizing Test Files
~~~~~~~~~~~~~~~~~~~~~
Test files must be collected in :ref:`The \`\`tests/\`\` Directory`. To
guarantee that tests are run against the library source code, follow a ``src/``
layout as explained in :ref:`The \`\`src/\`\` Directory` section rather than
having your Python library source directly within the repository root directory. 

This helps you avoid testing the source of the repository and
rather the installed package. This helps to catch errors caused by files that
might be missed by the installer, including any C extensions or additional
internal packages.

Running Tests
-------------
Once you have installed ``pytest``, it is possible to execute the test suite by
running:

.. code-block:: text

    pytest -v tests/

Filtering Tests
~~~~~~~~~~~~~~~
It is also possible to run a subset of all available tests by taking advantage
of the ``keywords`` and ``markers`` flags:

**Filtering tests by keywords**

.. code-block:: text

    pytest -k '<name pattern>'
    pytest -k 'not <name pattern>'

**Filtering tests by markers**

.. code-block:: text

    pytest -m slow


Visit `Working with Custom Markers
<https://docs.pytest.org/en/latest/example/markers.html>`_ for more information
about filtering tests.

Testing Methodology
-------------------
You should consider three levels of testing for your PyAnsys library: unit,
integration, and functional testing.

* :ref:`Unit Testing` validates your library at the lowest possible level, isolating
  individual classes and methods without any communication with other libraries
  or services.

* :ref:`Integration Testing` validates that your library works in the context of an
  application or software stack. For example, if your library extends or wraps
  the functionality of an external service, you would need to test that service
  in conjunction with your library. On GitHub, the ideal approach for this would
  be to start your service via docker and test accordingly. You should still be
  testing at the individual class or method level, but you can now test how
  multiple libraries or services interact. This is mandatory for testing APIs and
  is preferred over mocking the service.

* :ref:`Functional Testing` should be used for validating workflows or long running
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
example, if you have a method that deserializes chunks, the associated test
file would be:

.. tabs:: 

    .. tab:: parse_chunks.py
    
        .. code-block:: python
           
            def parse_chunks(chunks):
                """Deserialize gRPC chunks into a numpy array.
        
                Parameters
                ----------
                chunks : generator
                    Generator from grpc.  Each chunk contains a bytes payload.
        
                dtype : np.dtype
                    Numpy data type to interpert chunks as.
        
                Returns
                -------
                array : np.ndarray
                    Deserialized numpy array.
        
                """
                arrays = []
                for chunk in chunks:
                    arrays.append(
                        np.frombuffer(chunk.payload, ANSYS_VALUE_TYPE[chunk.value_type])
                    )
        
                return np.hstack(arrays)
    
    .. tab:: test_parse_chunks.py
    
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

This assumes that you do not have a ``serialize_chunks`` function within your
library. If you did, you could exclude it from ``test_parse_chunks.py``


Integration Testing
~~~~~~~~~~~~~~~~~~~
This subsections explains :ref:`Wrapped Service Methods` and :ref:`Remote Method
Invocation Testing`. 

Wrapped Service Methods
+++++++++++++++++++++++
Any PyAnsys library that provides functionality by wrapping a gRPC interface
should include tests of the gRPC methods exposed by the proto files and wrapped
by the Python library. They would not be expected to test the functionality of
the server, but rather the APIs exposed by the server. For example, if testing
the gRPC method ``GetNode``, then your integration test would test the wrapped
Python function.  If the Python library wraps this gRPC method with a
``get_node`` method, your test would be implemented within
``tests/test_nodes.py``:


.. tabs::

    .. tab:: gRPC Code

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

    .. tab:: Python Code

        .. code-block:: python
        
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


    .. tab:: Unit Test

        .. code-block:: python
        
           def test_get_node(srv):
               srv.clear()
        
               node_index = 1
               node_coord = 0, 10, 20
               srv.create_node(node_index, node_coord*)
               assert srv.get_node(node_index) == node_coord

The goal of the unit test should be to test the API rather than the product or
service itself. In the case of ``GetNode``, this method should have already
been tested when designing and developing the service.


Remote Method Invocation Testing
++++++++++++++++++++++++++++++++
In the case of a Remote Method Invocation (RMI)-like method, it is only
necessary to test the method with a basic case and potentially with any edge
cases. A RMI-like API might send and receive strings that are executed on the
server using a custom API or language only available within the context of the
service.

For example, if a method has a RMI service definition named ``SendCommand()`` and
a Python wrapping ``send_command``, the example test would be:

.. tabs::

    .. tab:: gRPC Code

        .. code-block:: rust
        
           message SendCommand()

    .. tab:: Python Code

        .. code-block:: python
        
           def send_command(command):
               """Run a command on the server.
        
               Parameters
               ----------
               command : str
                   Command to run on the remote server.
        
               """

    .. tab:: Unit Test
    
        .. code-block:: python
        
           def test_send_command(srv):
               output = srv.send_command("CREATE,1")
               assert "Created 1" in output

Note that this test only validates that the command ``"CREATE,1"`` has been
received, executed, and sent back to the client. It does not validate all
commands, but doing this is necessary only if there are edge cases, which
include characters that cannot be streamed or using long-running commands.


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



Testing Code Coverage
---------------------
Given that Python is an interpreted language, developers of Python libraries
should aim to have high coverage for their libraries as only syntax errors can
be caught during the almost trivial compile time. Coverage is defined as parts
of the executable and usable source that are tested by unit tests. You can use
the `pytest-cov <https://pytest-cov.readthedocs.io/>`_ library to view the
coverage for your library.


Configuring Code Coverage
~~~~~~~~~~~~~~~~~~~~~~~~~
Code coverage must be properly configured, otherwise the resultant report will
not be showing the real scope covered by the test suite.

Assuming that a ``PyAnsys`` project follows :ref:`The \`\`src/\`\` Directory` layout,
the following flag needsto be passed when :ref:`Running Tests`:

.. code-block:: text

    pytest --cov=ansys.<product>.<library> --cov-report=term tests/

Previous command indicates ``pytest-cov`` to look for source code in the
``src/ansys/<product>`` directory and generate a terminal report for all tests
located in :ref:`The \`\`tests/\`\` Directory`.


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

You should only avoid coverage of parts of your library where you cannot
reasonably test without an extensive testing suite or setup.  Most methods and
classes, including edge cases, can be reasonably tested. Even parts of your code
that raise errors like ``TypeError`` or ``ValueError`` when users input the
wrong data type or value can be reasonably tested.

Code Coverage Enforcement
~~~~~~~~~~~~~~~~~~~~~~~~~
One way of enforcing unit test coverage with a project on GitHub is to use the
codecov.io to enforce minimum patch (and optionally project) coverage. As this
application is already available to the `PyAnsys Organization
<https://github.com/pyansys>`_, simply add a ``codecov.yml`` file to the root
directory of your repository:

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
Notice previous example file is only a sample configuration.


Testing Using GitHub Actions
----------------------------
Effective CI/CD assumes that unit testing is developed during feature
development or bug fixes. However, given the limited scope of the local
development environment, it is often not possible to enforce testing on
multiple platforms, or even unit testing in general. However, with the right
automated CI/CD, such testing can still occur and be enforced automatically.

`GitHub Actions`_ is the preferred automated CI/CD platform for running Python
library unit tests for PyAnsys, and it can be used immediately by cloning the
project `template <https://github.com/pyansys/template/>`_. If you are
unfamiliar with GitHub Actions, see `GitHub Actions`_ for an overview.


.. literalinclude:: code/tests.yml     
   :language: yaml


.. _GitHub Actions: https://github.com/features/actions
.. _Test Driven Development (TDD): https://en.wikipedia.org/wiki/Test-driven_development
.. _codecov.io: https://app.codecov.io/gh/pyansys
.. _poetry: https://python-poetry.org
