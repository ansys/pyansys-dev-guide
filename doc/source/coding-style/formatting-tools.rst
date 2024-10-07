.. _code_style_tools:

Code style tools
================

There are many tools for checking code style. This section presents some of
the most popular ones in the Python ecosystem. A minimum configuration is
provided for each one so that you can easily include them in your PyAnsys project.

Most of the tools presented can be configured using :ref:`the
\`\`pyproject.toml\`\` file`. Avoiding dotfiles leads to a much
cleaner root project directory.

Black
-----

`Black`_ is the most popular code formatter in the Python community because it is
maintained by the Python Software Foundation. It allows for a minimum
configuration to ensure that the Python code format looks almost the same across
projects. 

While `PEP 8`_ imposes a default line length of 79 characters, Black has
a default line length of 88 characters.

The minimum Black configuration for a PyAnsys project should look like this:

.. code-block:: toml

    [tool.black]
    line-length = "<length>"


The ``isort`` tool
------------------

The goal of `isort`_  is to properly format ``import`` statements by making sure
that they follow the standard order:

#. Library
#. Third-party libraries
#. Custom libraries

When using `isort`_ with `Black`_, it is important to properly configure both
tools so that no conflicts arise. To accomplish this, use the
``--profile black`` flag in ``isort``.

.. code-block:: toml

   [tool.isort]
   profile = "black"
   force_sort_within_sections = true
   line_length = "<length>"
   src_paths = ["doc", "src", "tests"]

Flake8
------

The goal of `Flake8`_ is to act as a `PEP 8`_ compliance checker. Again, if
this tool is being used with `Black`_, it is important to make sure that no
conflicts arise.

The following configuration is the minimum one to set up Flake8 together with
Black.

The configuration for Flake8 must be specified in a ``.flake8`` file.

.. code-block:: toml

   [flake8]
   max-line-length = 88
   extend-ignore = 'E203'

Flake8 has many options that can be set within the configuration file.
For more information, see `Full Listing of Options and Their Descriptions
<https://flake8.pycqa.org/en/latest/user/options.html>`__ in the Flake8
documentation.

The example configuration defines these options:

- ``exclude``
    Subdirectories and files to exclude when checking.

- ``select``
    Sequence of error codes that Flake8 is to report errors
    for. The set in the preceding configuration is a basic set of errors
    for checking and is not an exhaustive list. For more information, see
    `Error/Violation Codes <https://flake8.pycqa.org/en/3.9.2/user/error-codes.html>`__
    in the Flake8 documentation.

- ``count``
    Total number of errors to print when checking ends.

- ``max-complexity``
    Maximum allowed McCabe complexity value for a block of code.
    The value of 10 was chosen because it is a common default.

- ``statistics``
    Number of occurrences of each error or warning code
    to print as a report when checking ends.


The ``Add-license-headers`` pre-commit hook
-------------------------------------------

The goal of the ``add-license-headers`` pre-commit hook is to add and update license headers
for files with `REUSE <https://reuse.software/>`_ software. By default, the hook runs on
PROTO files in any directory and on Python files in the ``src``, ``examples``, and ``tests`` directories.

You can find in the ``ansys/pre-commit-hooks`` repository, the `MIT.txt
<https://github.com/ansys/pre-commit-hooks/blob/main/src/ansys/pre_commit_hooks/assets/LICENSES/MIT.txt>`_ file
that is added to files.

For information on customizing the hook, in this same repository, see the
`README <https://github.com/ansys/pre-commit-hooks/blob/main/README.rst>`_ file.

Code coverage
-------------

Code coverage indicates the percentage of the codebase tested by the test
suite. Code coverage should be as high as possible to guarantee that every piece
of code has been tested.

For PyAnsys libraries, code coverage is done using `pytest-cov`_, a `pytest`_ plugin
that triggers code coverage analysis once your test suite has executed.

Considering the layout presented in :ref:`Required files`, the following
configuration for code coverage is the minimum one required for a PyAnsys
project:

.. code-block:: toml

   [tool.coverage.run]
   source = ["ansys.<product>"]

   [tool.coverage.report]
   show_missing = true

The ``pre-commit`` tool
-----------------------

To ensure that every commit you make is compliant with the code style
guidelines for PyAnsys, you can take advantage of `pre-commit`_ in your project.
Every time you stage some changes and try to commit them, ``pre-commit`` only
allows them to be committed if all defined hooks succeed.

You must define the configuration for ``pre-commit`` in a
``.pre-commit-config.yaml`` file. The following lines present a minimum
configuration that includes both code and documentation formatting tools.

.. code-block:: yaml

    repos:
    
    - repo: https://github.com/psf/black
      rev: X.Y.Z
      hooks:
      - id: black
    
    - repo: https://github.com/pycqa/isort
      rev: X.Y.Z
      hooks:
      - id: isort
    
    - repo: https://github.com/PyCQA/flake8
      rev: X.Y.Z
      hooks:
      - id: flake8
    
    - repo: https://github.com/codespell-project/codespell
      rev: vX.Y.Z
      hooks:
      - id: codespell
    
    - repo: https://github.com/pycqa/pydocstyle
      rev: X.Y.Z
      hooks:
      - id: pydocstyle
        additional_dependencies: [toml]
        exclude: "tests/"

    - repo: https://github.com/ansys/pre-commit-hooks
      rev: v0.2.4
      hooks:
      - id: add-license-headers

Install ``pre-commit``
~~~~~~~~~~~~~~~~~~~~~~

You can install ``pre-commit`` by running this command:

.. code-block:: bash

    python -m pip install pre-commit

Then, ensure that you install it as a ``Git hook`` by running this command:

.. code-block:: bash

    pre-commit install

Use ``pre-commit``
~~~~~~~~~~~~~~~~~~

One installed as described, ``pre-commit`` automatically triggers every time
that you try to commit a change. If any hook defined in the ``.pre-commit-config.yaml``
file fails, you must fix the failing files, stage the new changes, and try to commit
them again.

If you want to manually run ``pre-commit``, run this command:

.. code-block:: bash

    pre-commit run --all-files --show-diff-on-failure

If any of the hooks fail, this command shows the current and expected style of the code.

The ``tox`` tool
----------------

You might consider using `tox`_ in your project. While this automation
tool is similar to `Make`_, it supports testing of your package in a temporary
virtual environment. Being able to test your package in isolation rather than in
"local" mode guarantees reproducible builds.

Configuration for ``tox`` is stored in a ``tox.ini`` file. Here is the minimum
configuration for a PyAnsys ``py<product>-<library>`` project:

.. tab-set::

    .. tab-item:: Tox with Flit

        .. include:: code/tox-flit.rst

    .. tab-item:: Tox with Poetry

        .. include:: code/tox-poetry.rst

This minimum configuration assumes that you have a ``requirements`` directory that
contains ``requirements_tests.txt`` and ``requirements_doc.txt`` files. In
addition, the ``style`` environment must execute ``pre-commit``, which guarantees
the usage of this tool in your project.

Install ``tox``
~~~~~~~~~~~~~~~

You can install ``tox`` like any other Python package:

.. code-block:: bash

    python -m pip install tox

Use ``tox``
~~~~~~~~~~~

The ``tox`` tool uses ``environments``, which are similar to ``Makefile`` rules,
to make it highly customizable. Descriptions follow of some of the most
widely used environments:

- ``tox -e style``: Checks the code style of your project.
- ``tox -e py``: Runs your test suite.
- ``tox -e doc``: Builds the documentation of your project.

It is possible to run multiple environments by separating them with commas:

``tox -e <env-name0>,<env-name1>,...``

To run all available environments, simply type ``tox``.


The ``pre-commit.ci`` tool
--------------------------

The goal of the `pre-commit.ci <https://pre-commit.ci/>`_ tool is to run the same hooks as the
``pre-commit`` tool, but in a CI environment. This tool is useful for
checking the code style of your project in a CI environment.

Although the PyAnsys ecosystem also has its own ``code-style`` action (see
`Code style action <https://actions.docs.ansys.com/version/stable/style-actions/index.html#code-style-action>`_),
the `pre-commit.ci`_ tool provides some additional features:

- It is free for public projects.
- It is compatible with any CI provider.
- It ensures that hook versions are up to date.
- Any changes performed by the hooks are committed back to the repository.
- It reduces CI run times by caching the hooks used.

To use the `pre-commit.ci`_ tool, you must have a ``.pre-commit-config.yaml`` file for your repository. Next,
you should request the `PyAnsys Core team <pyansys_core_email_>`_ to enable the `pre-commit.ci`_ tool for your
repository.

.. note::

    The `pre-commit.ci`_ tool is not available for private repositories.

The PyAnsys ecosystem strongly recommends using the `pre-commit.ci`_ tool in your project. It is a
great way to ensure that your code is compliant with the code style guidelines set by the PyAnsys ecosystem.

Using ``pre-commit.ci`` with conventional commits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are using `conventional commits <https://www.conventionalcommits.org/en/v1.0.0/>`_ in your project,
via the `check PR title <https://actions.docs.ansys.com/version/stable/style-actions/index.html#pull-request-title-action>`_,
it is important to ensure that the commit messages are compliant with the conventional commits standard.

Use the following configuration in your ``.pre-commit-config.yaml`` file to be compliant:

.. code-block:: yaml

    ci:
        autofix_commit_msg: 'chore: auto fixes from pre-commit hooks'
        autoupdate_commit_msg: 'chore: pre-commit automatic update'
        autoupdate_schedule: weekly

    repos:
        # Your repository-specific configurations here
