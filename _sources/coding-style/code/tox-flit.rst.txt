.. code-block:: ini

    [tox]
    description = Default tox environments list
    envlist =
        style,{py310,py311,py312,py313}{,-coverage},doc
    skip_missing_interpreters = true
    isolated_build = true
    isolated_build_env = build
    
    [testenv]
    description = Checks for project unit tests and coverage (if desired)
    basepython =
        py39: python3.9
        py310: python3.10
        py311: python3.11
        py312: python3.12
        py313: python3.13
        py: python3
        {style,reformat,doc,build}: python3
    setenv =
        PYTHONUNBUFFERED = yes
        coverage: PYTEST_EXTRA_ARGS = --cov=ansys.product --cov-report=term --cov-report=xml --cov-report=html
    deps =
        -r{toxinidir}/requirements/requirements_tests.txt
    commands =
        pytest {env:PYTEST_MARKERS:} {env:PYTEST_EXTRA_ARGS:} {posargs:-vv}
    
    [testenv:style]
    description = Checks project code style
    skip_install = true
    deps =
        pre-commit
    commands =
        pre-commit install
        pre-commit run --all-files --show-diff-on-failure
    
    [testenv:doc]
    description = Check if documentation generates properly
    deps =
        -r{toxinidir}/requirements/requirements_doc.txt
    commands =
        sphinx-build -d "{toxworkdir}/doc_doctree" doc/source "{toxworkdir}/doc_out" --color -vW -bhtml

