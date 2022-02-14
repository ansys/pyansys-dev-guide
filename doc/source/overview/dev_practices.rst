.. _development_practices:

Development Practices
=====================

This section explains how development is conducted in PyAnsys
repositories. Please follow the practices outlined here when
contributing directly to PyAnsys libraries.


General Development Procedures
------------------------------

To submit new code to a PyAnsys, first `fork <https://docs.github.com/en/get-started/quickstart/fork-a-repo>`_
the repository (for example, `PyMAPDL <https://github.com/pyansys/pymapdl>`_)
and then clone the forked repository to your local environment. Next, create a new branch based on the
`Branch Naming Conventions Section <#branch-naming-conventions>`__ in
your local repository.

Next, add your new feature and commit it locally. Be sure to commit
often as it is often helpful to revert to past commits, especially if
your change is complex. Also, be sure to test often. See the `Testing
Section <#testing>`__ below for automating testing.

When you are ready to submit your code, create a pull request by
following the steps in `Creating a New Pull Request <#creating-a-new-pull-request>`__.

Be sure to review these topics:

#. `Branching Section <#Branching Model>`__
#. Testing standards.
#. Documentation standards. See :ref:`api_documentation`.
#. Code quality standards. See :ref:`coding_style`.


Guidelines
~~~~~~~~~~

Consider the following general coding paradigms when contributing:

1. Follow the `Zen of Python <https://www.python.org/dev/peps/pep-0020/>`__.
   As silly as the core Python developers are sometimes, there's much to
   be gained by following the basic guidelines listed in PEP 20.
   Without repeating them here, focus on making your additions
   intuitive, novel, and helpful for users.

   When in doubt, ``import this``.

2. **Document it**. Include a docstring for any function, method, or
   class added. Follow the `numpydocs docstring
   <https://numpydoc.readthedocs.io/en/latest/format.html>`_
   guidelines, and always provide an example of simple use cases for
   new features.

3. **Test it**. Because Python is an interpreted language, if it's not
   tested, it's probably broken. At the minimum, include unit tests
   for each new feature within the ``tests`` directory. Ensure that
   each new method, class, or function has reasonable (>80%) coverage.

Additionally, do not include any data sets for which a license
is not available or commercial use is prohibited.

Licensing
~~~~~~~~~

All contributed code will be licensed under the MIT License found in
the repository. If you did not write the code yourself, it is your
responsibility to ensure that the existing license is compatible and
included in the contributed files. You must obtain permission from the
original author to relicense the code.

See :ref:`license_file` for more details.


Branching Model
---------------
This project has a branching model that enables rapid development of
features without sacrificing stability and closely follows the
`Trunk Based Development <https://trunkbaseddevelopment.com/>`_ approach.

Descriptions follow for the main features of the branching model.

- The `main` branch is the primary development branch. All features,
  patches, and other branches should be merged here. While all pull
  requests (PRs) should pass all applicable CI (Continuous Integration)
  checks, this branch might be functionally unstable if changes have
  introduced unintended side-effects or bugs that were not caught through
  unit testing.
- There will be one or many `release/` branches based on minor
  releases (for example, ``release/0.2``) that contain a stable version
  of the code base that is also reflected on PyPI. Hotfixes from
  `fix/` branches should be merged both to main and to these
  branches. When creating a new patch release is necessary, these
  release branches will have their ``__version__.py`` updated and be
  tagged with a patched semantic version (for example, ``0.2.1``). This
  triggers CI to push to PyPi and allow us to rapidly push hotfixes
  for past versions without having to worry about untested features.
- When a minor release candidate is ready, a new ``release`` branch will
  be created from ``main`` with the next incremented minor version
  (for example, ``release/0.2``), This ``release`` branch will be thoroughly
  tested. When deemed stable, it will be tagged with the version (``0.2.0``
  in this case) and merged with ``main`` if any changes were pushed to it.
  Feature development then continues on ``main`` and any hotfixes will now
  be merged with this release. Older release branches should not be deleted
  so they can be patched as needed.

.. _release_procedures:

Release Procedures
------------------

Major and Minor
~~~~~~~~~~~~~~~
Procedures follow for major and minor releases.

#. Create a new branch from the `main` branch with name
   ``release/MAJOR.MINOR`` (for example, ``release/0.2``).

#. Locally run all tests as outlined in :ref:`testing` and ensure all
   are passing.

#. Locally test and build the documentation with link checking to make
   sure no links are outdated. Be sure to run ``make clean`` to ensure no
   results are cached.

    .. code::

        cd doc
        make clean  # deletes the sphinx-gallery cache
        make html -b linkcheck

#. After building the documentation, open the local build and examine
   the examples for any obvious issues.

#. Update the version numbers in
   ``ansys/<product>/<library>/_version.py`` and commit it.  Push the
   branch to GitHub and create a new PR for this release that merges
   it to ``main``. Development to ``main`` should be limited while
   effort is focused on the release.

#. The community and Ansys developers must now functionally test the
   new release. It is best to locally install this branch and use it in
   production. Any bugs identified should have their hotfixes pushed to
   this release branch.

#. When the branch is deemed as stable for public release, the PR is merged
   to `main` branch, which is then tagged with a `MAJOR.MINOR.0` release.
   The release branch will not be deleted.

   Tag the release with:

    .. code::

	git tag v<MAJOR.MINOR.0>
        git push origin --tags

#. Create a list of all changes for the release. It is often helpful
   to see the differences from the last tag and the ``main`` branch
   using `GitHub's compare feature`_ tool.  Be sure to acknowledge new
   contributors by their GitHub username and place mentions where
   appropriate if a specific contributor is to be thanked for a new
   feature.

#. Place your release notes from the previous in the release section within the GitHub repository. See
   `GitHub Releases`_

.. _GitHub Releases: https://docs.github.com/en/github/administering-a-repository/releasing-projects-on-github/managing-releases-in-a-repository
.. _GitHub's compare feature: https://github.com/pyansys/pymapdl/compare


Patch Release Steps
~~~~~~~~~~~~~~~~~~~
Patch releases are for critical and important bug fixes that cannot or
should not wait until a minor release. These are the steps for a patch release:

1. Push the necessary bug fixes to the applicable release branch.
   This will generally be the latest release branch (`release/MAJOR.MINOR`).

2. Update ``__version__.py`` with the next patch increment
   (`MAJOR.MINOR.PATCH`), commit it, and open a PR to merge with the
   release branch. This gives the developers and community
   an opportunity to validate and approve the bug fix release.  Any
   additional hotfixes should be outside of this PR.

3. When approved, merge with the release branch, but not `main` as
   there is no reason to increment the version of the `main` branch.
   Then, create a tag from the release branch with the applicable
   version number (see above for the correct steps).

4. If deemed necessary, add a release notes page.


.. _testing:

Testing
-------
Unit testing is critical for the sucessful continious integration and testing of
any program or libraries belonging to the PyAnsys project.

There are generally two types of libraries part of the PyAnsys project: those
that interface or wrap functionality of a different Ansys product, service, or
application, or tools those that provide functionality. Both types of libraries
should be tested, but the tests written will depend on the purpose of the library.
For example, a library that is wrapping a gRPC interface would include tests of
the gRPC methods exposed by the proto files and wrapped by the Python library. They would not be expected to test the functionality of the server.

For example, if testing the gRPC method ``GetNode``:

.. code::

   message Node
   {
     int32      id = 1;
     double     x = 2;
     double     y = 3;
     double	z = 4;
   }

   message NodeRequest {
     int32		num = 1;
   }

   message NodeResponse {
     Node		node = 1;
   }

  service SomeService{

     rpc GetNode(NodeRequest)				returns (NodeResponse);
     // other methods
   }

Then your unit test would test the wrapped python function (for example,
``get_node``).  For example the ``get_node`` method might be implemented as:

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

Your test would be implemented (within ``tests/test_nodes.py``):

.. code::

   def test_get_node(srv):
       srv.clear()

       node_index = 1
       node_coord = 0, 10, 20
       srv.create_node(node_index, node_coord*)
       assert srv.get_node(node_index) == node_coord

The goal of the unit test should be to test the wrapping of the interface rather
than the product or service itself. In the case of ``GetNode``, this method
should have already been tested when designing and developing the service.


Testing Framework
~~~~~~~~~~~~~~~~~
For consistency, PyAnsys tools and libraries should use either the `unit test
<some link>`_ or `pytest <some link>`_ frameworks for unit testing. As described
in :ref:`repo_dir_struct`, unit tests should be placed into the ``tests``
directory in the root directory of the library::

   tests/
       test_basic.py
       test_advanced.py

Furthermore, any testing dependencies requirements should be included when using ``setup.py`` within a ``requirements_tests.txt`` file that is installed via::

.. code::

   pip install -r requirements_tests.txt

Or included in ``pyproject.toml``. For example, when using the `filt
<missing_link>`_ build system::

   [project.optional-dependencies]
   test = [
       "pytest>=2.7.3",
       "pytest-cov",
   ]

And then installed via::

   pip install .[test]

When using ``pytest``, test via::

   pytest

.. note::
   Note that it is preferable to cd into the testing directory and run unit
   testing there because you will be testing the installed library (generally in
   development mode ``pip install -e .``) rather than the source within the
   uninstalled "local" source. This catches files that might be missed by the
   installer, including any C extensions or additional internal packages.


Coverage
~~~~~~~~
Given that Python is an interpreted language, developers of Python libraries should
aim to have high coverage for their libraries as only syntax errors can be caught
during the almost trivial compile time. Coverage is defined as parts of the
executable and usable source that are tested by unit tests. You can use the ``pytest-cov`` library to view the coverage for your library. For example::

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
the coverage of a Python library. Consequently, achieving 80-90% coverage is often sufficient.
For parts of your library that are difficult or impossible to test,
consider using ``# pragma: no cover`` at the end of the method definition, branch,
or line to denote that part of the code cannot be reasonably tested.  For
example, if part of your module performs a simple ``import`` test of
``matplotlib`` and raises an error when the library is not installed, it is not
reasonable to attempt to test this and assume full coverage:

.. code:: python

   try:
       import matplotlib
   except ImportError:  # pragma: no cover
       raise ImportError("Install matplotlib to use this feature.")

.. note::
   You should only avoid coverage of parts of your library where you cannot
   reasonably test without an extensive testing suite or setup.  Most methods
   and classes, including edge cases, can be reasonable tested. Even parts of
   your code that raise errors like ``TypeError`` or ``ValueError`` when users
   input the wrong data type or value.


Unit Testing within CI/CD
~~~~~~~~~~~~~~~~~~~~~~~~~
Effective CI/CD assumes that unit testing is developed during feature
development or bug fixes. However, given the limited scope of the local
development environment, it is often not possible to enforce testing on multiple
platforms, or even, unit testing in general. However, with the right automated
CI/CD, such testing can still occur and be enforced automatically.

`GitHub Actions <gh actions link>`_ is the preferred automated CI/CD platform
for running Python library unit tests for PyAnsys, and can be employed
immediately by closing the project `template <link to
github.com/pyansys/template>`_. If you are unfamiliar with GitHub Actions, see: `missing link <missing_link>`_ for an overview.

**Sample Workflow**

The following sections describe the usage of a simple GitHub workflow for a
PyAnsys library:

**Setup**

Include the name and when your job should be run at the top of the workflow ``.yml``::

   name: Unit Testing

   on:
     pull_request:
     workflow_dispatch:
     push:
       tags:
         - "*"
       branches:
         - main

Take note that this workflow runs on all pull requests and on demand
with ``workflow_dispatch``. On commits, this workflow runs only on tags and
on the ``main`` branch.  This ensures that CI/CD is not run twice on every
commit for each PR, which may saturate available build or testing machines.

**Job Description**

PyAnsys libraries should run on the currently supported versions of Python on both Windows and Linux (and ideally on Mac OS). Therefore, it is necessary to also test on both Linux and Windows for these versions of Python. Use the ``matrix`` run strategy for the job with both the latest images of Windows and Linux::

   jobs:
     unit_tests:
       name: Unit testing
       runs-on: ${{ matrix.os }}
       strategy:
         matrix:
           os: [windows-latest, ubuntu-latest]
           python-version: ['3.7', '3.8', '3.9', '3.10']

**Running the Tests**

Each virtual machine within GitHub actions starts in a fresh state with no
software or source installed or downloaded. Therefore, you must clone the repository using the ``checkout`` action, set up Python, and install the necessary testing dependencies.

    steps:
      - uses: actions/checkout@v2

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v1
        with:
          python-version: ${{ matrix.python-version }}

If you are using ``setup.py``, your installation step is::

      - name: Install the library
        run: |
          pip install .
          pip install -r requirements_test.txt

If you are using ``pyproject.toml`` with the ``flit`` build system, your
installation step is::

      - name: Install the library and dependencies
        run: |
          pip install flit
          flit install

Run the unit tests via ``pytest`` with::

      - name: Test and show coverage
        working-directory: tests
        run: pytest --cov ansys.product.library

.. note::
   Replace ``ansys.product.library`` with your library name. This should match how it
   would be imported within Python. For example, rather than
   ``ansys-product-library`` use ``ansys.product.library``.

Optionally, though highly recommended, upload your unit test coverage to
`codecov.io`_ with::

      - uses: codecov/codecov-action@v2
        name: 'Upload coverage to Codecov'

See the following section regarding the usage of `codecov.io`_.


Code Coverage Enforcement
~~~~~~~~~~~~~~~~~~~~~~~~~
One way of enforcing unit test coverage with a project on GitHub is to use the
`codecov.io CI Bot`_ to enforce minimum patch (and optionally project)
coverage. As this application is already available to the `PyAnsys Organization
<https://github.com/pyansys>`_, simply add the following to the root directory
of your repository:

**/codecov.yml**

::

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

This requires that each PR has a patch coverage of 90%, meaning that 90% of any source added to the repository (unless ignored) must be covered by unit tests.

.. note::
   This is only a sample configuration.

Test-Driven Development
~~~~~~~~~~~~~~~~~~~~~~~




Remote Method Invocation Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In the case of a Remote Method Invocation (RMI)-like method, it is only necessary
to test the method with a basic case and potentially with any edge cases.

RMI Service Definition:

.. code::

   message SendCommand()


Python Wrapping

.. code::

   def send_command(command):
       """Run a command on the server.

       Parameters
       ----------
       command : str
           Command to run on the remote server. Should be in the form of





Files Layout
~~~~~~~~~~~~
PyAnsys libraries should use ``unittest`` or ``pytest`` libraries to run individual
unit tests contained within a ``tests`` directory in the root of the project.  The
specific test files for your project should at a minimum include:

.. code::

   requirements_tests.py
   tests/
     test_<filename>.py
     conftest.py

**Requirements File**
The requirements file contains a list of all the libraries that must be installed to
run ``pytest``.  No assumption should be made regarding the state of the virtual
