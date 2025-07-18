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
    ignore = []

    [tool.ruff.lint.pydocstyle]
    convention = "numpy"

    [tool.ruff.lint.isort]
    combine-as-imports = true
    force-sort-within-sections = true
    
    [tool.coverage.run]
    source = ["ansys.<product>"]

    [tool.coverage.report]
    show_missing = true

    [tool.pytest.ini_options]
    addopts = "--doctest-modules"

    [tool.pydocstyle]
    convention = "numpy"

Required ``pre-commit`` configuration
-------------------------------------

You can take advantage of `pre-commit`_ by including a
``.pre-commit-config.yaml`` file like this one in your project:

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
