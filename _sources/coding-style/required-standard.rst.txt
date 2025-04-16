Required standards
==================

This page collects the required standards for any ``PyAnsys`` project. The
individual configurations for the tools presented in :ref:`Code style tools` and
:ref:`Documentation style tools` are combined together.

The following lines should be included in :ref:`The \`\`pyproject.toml\`\` file`
to indicate the configuration of the different code and documentation style tools.

Required ``pyproject.toml`` file configuration
----------------------------------------------

.. code-block:: toml

    [tool.black]
    line-length = "<length>"

    [tool.isort]
    profile = "black"
    force_sort_within_sections = true
    line_length = "<length>"
    src_paths = ["doc", "src", "tests"]

    [tool.coverage.run]
    source = ["ansys.<product>"]

    [tool.coverage.report]
    show_missing = true

    [tool.pytest.ini_options]
    addopts = "--doctest-modules"

    [tool.pydocstyle]
    convention = "numpy"

Required flake8 configuration
-----------------------------

The following ``.flake8`` file is also required:

.. code-block:: toml

   [flake8]
   max-line-length = 88
   extend-ignore = 'E203'

Required ``pre-commit`` configuration
-------------------------------------

You can take advantage of `pre-commit`_ by including a
``.pre-commit-config.yaml`` file like this one in your project:

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

GitHub CI/CD integration
------------------------

Finally, you can :ref:`Test using GitHub actions` and
create a ``style.yml`` workflow file in the ``.github/workflows``
directory:

.. code-block:: yaml

    name: Style
    
    on:
      pull_request:
      push:
        tags:
          - "*"
        branches:
          - main
    
    jobs:
      style:
        name: Code & Doc
        runs-on: ubuntu-latest
    
        steps:
          - uses: actions/checkout@v3
          - name: Setup Python
            uses: actions/setup-python@v4
            with:
              python-version: '3.10'
          - name: Install requirements
            run: |
              python -m pip install -U pip pre-commit
    
          - name: Run pre-commit
            run: |
              pre-commit run --all-files --show-diff-on-failure
