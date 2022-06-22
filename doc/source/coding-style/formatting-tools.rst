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

While `PEP 8`_ imposes a default line length of 79 characters, `black`_ has
a default line length of 88 characters.

The minimum `black`_ configuration for a PyAnsys project should look like this:

.. code-block:: toml

    [tool.black]
    line-length: "<length>"


Isort
-----
The goal of `isort`_  is to properly format ``import`` statements by making sure
that they follow the standard order: library, third-party libraries, and custom libraries.

When using `isort`_ with `black`_, it is important to properly configure both
tools so that no conflicts arise. To accomplish this, use the
``--porfile black`` flag in `isort`_.

.. code-block:: toml

   [tool.isort]
   profile = "black"
   force_sort_within_sections = true
   line_length = "<length>"
   default_section = "THIRDPARTY"
   src_paths = ["doc", "src", "tests"]


Flake8
------
The goal of `flake8` is to act as a `PEP 8`_ compliance checker. Again, if
this tool is being used with `black`_, it is important to make sure that no
conflicts arise.

The following configuration is the minimum one to set up `flake8`_ together with
`black`_.

The configuration for `flake8`_ must be specified in a ``.flake8`` file.

.. code-block:: toml

   [flake8]
   max-line-length = 88
   extend-ignore = E203

Flake8 has many options that can be set within the configuration file.
For more information, see this `Flake8 documentation topic
<https://flake8.pycqa.org/en/latest/user/options.html>`__.

The example configuration defines these options:

- ``exclude``
    Subdirectories and files to exclude when checking.

- ``select``
    Sequence of error codes that Flake8 is to report errors
    for. The set in the preceding configuration is a basic set of errors
    for checking and is not an exhaustive list.

    For a full list of error codes and their descriptions, see this `Flake8
    documentation topic <https://flake8.pycqa.org/en/3.9.2/user/error-codes.html>`__.

- ``count``
    Total number of errors to print when checking ends.

- ``max-complexity``
   Maximum allowed McCabe complexity value for a block of code.
    The value of 10 was chosen because it is a common default.

- ``statistics``
    Number of occurrences of each error or warning code
    to print as a report when checking ends.


Code coverage
-------------
Code coverage indicates the percentage of the codebase tested by the test
suite. Code coverage should be as high as possible to guarantee that every piece
of code has been tested.

For ``PyAnsys``, code coverage is done using `pytest-cov`_, a `pytest`_ plugin
that triggers the code coverage analysis once your test suite has executed.

Considering the layout presented in :ref:`Required Files`, the following
configuration for code coverage is the minimum one required for a ``PyAnsys``
project:

.. code-block:: toml

   [tool.coverage.run]
   source = ["ansys.<product>"]

   [tool.coverage.report]
   show_missing = true

Pre-commit
----------
To ensure that every commit you make is compliant with the code style
guidelines for PyAnsys, you can take advantage of `pre-commit`_ in your project.
Every time you stage some changes and try to commit them, `pre-commit`_ only
allows them to be committed if all defined hooks succeed.

The configuration for `pre-commit`_ must be defined in a
``.pre-commit-config.yaml`` file. The following lines present a minimum
`pre-commit`_ configuration that includes both code and documentation
formatting tools.


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

Installing ``pre-commit``
~~~~~~~~~~~~~~~~~~~~~~~~~
You can install ``pre-commit`` by running:

.. code-block:: bash

    python -m pip install pre-commit

Then, ensure that you install it as a ``Git hook`` by running:

.. code-block:: bash

    pre-commit install

Using ``pre-commit``
~~~~~~~~~~~~~~~~~~~~
One installed as described, ``pre-commit`` automatically triggers every time
that you try to commit a change. If any hook defined in `.pre-commit-config.yaml`
fails, you must fix the failing files, stage the new changes, and try to commit
them again.

If you want to manually run ``pre-commit``, you can run:

.. code-block:: bash

    pre-commit run --all-files --show-diff-on-failure

This command shows the current and expected style of the code if any of
the hooks fail.

Tox
---
You might consider using `tox`_ in your project. While this automation
tool is similar to `Make`_, it supports testing of your package in a temporary
virtual environment. Being able to test your package in isolation rather than in
"local" mode guarantees reproducible builds.

Configuration for `tox`_ is stored in a ``tox.ini`` file. The minimum
configuration for a PyAnsys ``py<product>-<library>`` project should be:


.. tabs::

    .. tab:: Tox with Flit

        .. include:: code/tox-flit.rst

    .. tab:: Tox with Poetry

        .. include:: code/tox-poetry.rst


This minimum configuration assumes that you have a ``requirements/`` directory that
contains ``requirements_tests.txt`` and ``requirements_doc.txt``. In
addition, the ``style`` environment must execute ``pre-commit``, which guarantees
the usage of this tool in your project.

Installing ``tox``
~~~~~~~~~~~~~~~~~~
You can install ``tox`` like any other Python package:

.. code-block:: bash

    python -m pip install tox


Using ``tox``
~~~~~~~~~~~~~

`tox`_ uses ``environments``, which are similar to ``Makefile`` rules,
to make it highly customizable. Descriptions follow of some of the most
widely used environments:

- ``tox -e style`` checks the code style of your project.
- ``tox -e py`` runs your test suite.
- ``tox -e doc`` builds the documentation of your project.

It is possible to run multiple environments by separating them with commas ``tox
-e <env-name0>,<env-name1>,...```.  To run all available environments, simply
run ``tox``.


.. LINKS AND REFERENCES

.. _black: https://black.readthedocs.io/en/latest/
.. _isort: https://pycqa.github.io/isort/
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _pre-commit: https://pre-commit.com/
.. _pytest: https://docs.pytest.org/en/latest/
.. _pytest-cov: https://pytest-cov.readthedocs.io/en/latest/
.. _tox: https://tox.wiki/en/latest/
.. _PEP 8: https://www.python.org/dev/peps/pep-0008/
.. _make: https://www.gnu.org/software/make/
