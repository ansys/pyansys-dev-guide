.. _testing:

Testing
-------
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

.. _Test driven development: https://en.wikipedia.org/wiki/Test-driven_development

We recommend that you follow TDD when developing your PyAnsys project, and
this document contains examples and best practices to help you write them.


Sample gRPC Method Test
~~~~~~~~~~~~~~~~~~~~~~~
There are generally two types of libraries part of the PyAnsys project:

* those that interface or wrap functionality of a different Ansys product,
  service, or application
* tools those that provide functionality Both types of Python libraries should
  be tested, but the tests written will depend on the purpose of the
  library. For example, a library that is wrapping a gRPC interface would
  include tests of the gRPC methods exposed by the proto files and wrapped by
  the Python library. They would not be expected to test the functionality of
  the server.

For example, if testing the gRPC method ``GetNode``:

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

Then your unit test would test the wrapped python function (for example,
``get_node``).  You might implement the ``get_node`` method with:

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

The goal of the unit test should be to test the wrapping of the
interface rather than the product or service itself. In the case of
``GetNode``, this method should have already been tested when designing and
developing the service.


Remote Method Invocation Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In the case of a Remote Method Invocation (RMI)-like method, it is only necessary
to test the method with a basic case and potentially with any edge cases.

RMI Service Definition:

.. code::

   message SendCommand()


Python wrapping:

.. code:: python

   def send_command(command):
       """Run a command on the server.

       Parameters
       ----------
       command : str
           Command to run on the remote server.

Example test:

.. code:: python

   def test_send_command(srv):
       output = srv.send_command("CREATE,1")
       assert "Created 1" in output

Note that this test only validates the command ``"CREATE,1"`` has been
received, executed, and sent back to the client. It does not validate all
commands, but nor is it necessary to do this unless there are edge cases
(e.g. characters that cannot be streamed or dealing with long running
commands).


Testing Framework
~~~~~~~~~~~~~~~~~
For consistency, PyAnsys tools and libraries should use either the `unittest
<https://docs.python.org/3/library/unittest.html>`_ or `pytest
<https://docs.pytest.org/>`_ frameworks for unit testing. As described in
:ref:`repo_dir_struct`, unit tests should be placed into the ``tests``
directory in the root directory of the library::

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
   direction rather than having your Python library source directly within the
   repository root directory. This helps you avoid testing the source of the
   repository and rather the installed package. This helps to catch errors
   caused by files that might be missed by the installer, including any C
   extensions or additional internal packages.


Coverage
~~~~~~~~
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


Unit Testing Within CI/CD
~~~~~~~~~~~~~~~~~~~~~~~~~
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

**Sample Workflow**

The following sections describe the usage of a simple GitHub workflow for a
PyAnsys library:

**Setup**

Include the job name when it should be run at the top of the workflow ``.yml``::

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

**Job Description**

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

**Running the Tests**

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


If you are using ``setup.py``, your installation step is:


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


Files Layout
~~~~~~~~~~~~
PyAnsys libraries should use ``unittest`` or ``pytest`` libraries to run
individual unit tests contained within a ``tests`` directory in the root of the
project. The specific test files for your project should at a minimum include:

.. code::

   requirements_tests.py
   tests/
     test_<filename>.py
     conftest.py

**Requirements File**
The requirements file contains a list of all the libraries that must be
installed to run ``pytest``.  No assumption should be made regarding the state
of the virtual


.. _poetry: https://python-poetry.org
.. _codecov.io: https://app.codecov.io/gh/pyansys
