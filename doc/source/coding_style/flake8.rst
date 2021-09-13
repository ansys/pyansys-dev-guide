.. _style-guide-enforcement:

Style Guide Enforcement
=======================
The following sections will describe the use of flake8 for `PEP8`_ style
enforcement. The PyAnsys libraries will be consistent with these basic
guidelines.

.. _PEP8: https://www.python.org/dev/peps/pep-0008/

Flake8
~~~~~~
`Flake8`_ is a python tool for enforcing code styling. It is a wrapper
around the following three tools: `PyFlakes`_, `pycodestyle`_, and
`Ned Batchelder's McCabe script`_. Flake8 runs all three tools at once,
checking the code against a variety of style rules, such as line length,
code complexity, whitespace, etc.

.. _Flake8: https://flake8.pycqa.org/en/latest/index.html
.. _PyFlakes: https://pypi.org/project/pyflakes/
.. _pycodestyle: https://pypi.org/project/pycodestyle/
.. _`Ned Batchelder's McCabe script`: https://github.com/PyCQA/mccabe

Configuring Flake8
------------------
Flake8 supports configuring a specific set of the style checks to
enforce. This configuration can be stored in your project in a
``setup.cfg``, ``tox.ini``, or ``.flake8`` file. The PyAnsys libraries
store the flake8 configuration in a ``.flake8`` file at the root of the
repository.

Here is an example of a ``.flake8`` configuration file from one the
PyAnsys libraries:

.. code::

    [flake8]
    exclude = venv, __init__.py, doc/_build
    select = W191, W291, W293, W391, E115, E117, E122, E124, E125, E225, E231, E301, E303, E501, F401, F403
    count = True
    max-complexity = 10
    max-line-length = 100
    statistics = True

Flake8 has many options that can be set within the configuration file.
A list of possible options can be found `here <https://flake8.pycqa.org/en/latest/user/options.html>`_.

The above example defines the following options:

- ``exclude``
    This denotes subdirectories ``venv`` and ``doc/_build``, along with all
    ``__init__.py`` files to be excluded from the check.

- ``select``
    This is a sequence of error codes that flake8 will report errors
    for. This set in the above configuration is a basic set of errors to
    check for and is not an exhaustive list. The error codes chosen above
    have the following descriptions:

    - W191: Indentation has tabs when only spaces are expected.
    - W291: Line contains trailing whitespace.
    - W293: Blank line contains tabs or spaces.
    - W391: There should only one blank line at the end of each file. This warning will occur when there are zero, two, or more than two blank lines.
    - E115: An indented block comment was expected but a non-indented block comment was found instead.
    - E117: Line is over-indented.
    - E122: Continuation line is not indented as far as it should be or is indented too far.
    - E124: Closing brackets do not match the indentation of the opening bracket.
    - E125: Continuation line is indented at the same level as the next logical line. It should be indented to one more level so as to distinguish it from the next line.
    - E225: Operator does not have one space both before and after it.
    - E231: Missing whitespace after the characters ``,``, ``;``, or ``:``.
    - E301: One blank line is expected but no blank line is found.
    - E303: Too many blank lines are found.
    - E501: Line too long. Based on the option ``max-line-length`` included in the configuration.
    - F401: Module import but not used.
    - F403: ``from module import *`` used.

    A full list of error codes and their descriptions can be found `here <https://flake8.pycqa.org/en/3.9.2/user/error-codes.html>`_.

- ``count``
    The total number of errors is printed at the end of the check.

- ``max-complexity``
    This sets the maximum allowed McCabe complexity value for a block of code.
    The value of 10 was chosen because it is a common default.

- ``max-line-length``
    This denotes the maximum line length for any one line of code.
    The `PEP8`_ standard advises a line length of 79. This is a bit
    limiting in some cases. In all cases, the maximum line length should
    not exceed 100.

    .. _PEP8: https://www.python.org/dev/peps/pep-0008/#maximum-line-length

- ``statistics``
    This enables the number of occurrences of each error or warning code
    to be printed as a report at the end of the check.