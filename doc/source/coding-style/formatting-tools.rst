.. _code_style_tools:

Code style tools
================

There are many tools for checking code style. This section presents some of
the most popular ones in the Python ecosystem. A minimum configuration is
provided for each one so that you can easily include them in your PyAnsys project.

Most of the tools presented can be configured using :ref:`the
\`\`pyproject.toml\`\` file`. Avoiding dotfiles leads to a much
cleaner root project directory.

Ruff
----

`Ruff`_ is a Python linter and code formatter written in Rust. It aims to be 
orders of magnitude faster than alternative tools while integrating more 
functionality behind a single, common interface. Ruff can therefore be used 
to replace the previously preferred alternatives that were `Flake8`_ 
(natively re-implementing its popular plugins), `Black`_ and `isort`_.

It is actively developed, used in major open-source projects, and offers the following 
features and advantages:

- Can be installed via ``pip install ruff``

- ``pyproject.toml`` support

- Python 3.7 to 3.13 compatibility

- Built-in caching, to avoid re-analyzing unchanged files

- Over 800 built-in rules

- Editor integrations for VS Code or PyCharm

A minimum Ruff configuration for a PyAnsys project (to be included in the ``pyproject.toml``)
may look like this:

.. code-block:: toml

    [tool.ruff]
    line-length = 100
    fix = true

    [tool.ruff.format]
    quote-style = "double"
    indent-style = "space"

    [tool.ruff.lint]
    select = [
        "E",    # pycodestyle, see https://docs.astral.sh/ruff/rules/#pycodestyle-e-w
        "D",    # pydocstyle, see https://docs.astral.sh/ruff/rules/#pydocstyle-d
        "F",    # pyflakes, see https://docs.astral.sh/ruff/rules/#pyflakes-f
        "I",    # isort, see https://docs.astral.sh/ruff/rules/#isort-i
        "N",    # pep8-naming, see https://docs.astral.sh/ruff/rules/#pep8-naming-n
        "PTH",  # flake8-use-pathlib, https://docs.astral.sh/ruff/rules/#flake8-use-pathlib-pth
        "TD",   # flake8-todos, https://docs.astral.sh/ruff/rules/#flake8-todos-td
    ]
    ignore = [
        "TD003", # Missing issue link in TODOs comment
    ]

    [tool.ruff.lint.pydocstyle]
    convention = "numpy"

    [tool.ruff.lint.isort]
    combine-as-imports = true
    force-sort-within-sections = true

Linting and formatting rules shall be added step by step when migrating a project to Ruff, 
gradually resolving the triggered errors. For more information about configuring Ruff, as 
well as a complete description of the available rules and settings, please refer to the 
`tool's documentation <https://docs.astral.sh/ruff/configuration/>`__.


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
    
    - repo: https://github.com/astral-sh/ruff-pre-commit
      rev: vX.Y.Z
      hooks:
      - id: ruff
      - id: ruff-format
    
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
