.. _style-guide-enforcement:

Style Guide Enforcement
=======================
The following sections will describe the use of flake8 for `PEP8`_ style
enforcement and the minimum standards expected. The PyAnsys libraries
will be consistent with these basic guidelines.

.. _PEP8: https://www.python.org/dev/peps/pep-0008/

Flake8
~~~~~~
`Flake8`_ is a python tool for enforcing code styling. It is a wrapper
around the following three tools: `PyFlakes`_, `pycodestyle`_, and
`Ned Batchelder's McCabe script for complexity`_. Flake8 runs all three tools at once,
checking the code against a variety of style rules, such as line length,
code complexity, whitespace, etc.

.. _Flake8: https://flake8.pycqa.org/en/latest/index.html
.. _PyFlakes: https://pypi.org/project/pyflakes/
.. _pycodestyle: https://pypi.org/project/pycodestyle/
.. _`Ned Batchelder's McCabe script for complexity`: https://github.com/PyCQA/mccabe

Configuring Flake8
------------------
Flake8 supports configuring a specific set of style rules to
enforce. This configuration can be stored in your project in a
``setup.cfg``, ``tox.ini``, or ``.flake8`` file. The PyAnsys libraries
store the flake8 configuration in a ``.flake8`` file at the root of the
repository.

Here is an example of a ``.flake8`` configuration file from one of the
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
A list of possible options can be found `here <https://flake8.pycqa.org/en/latest/user/options.html>`__.

The above configuration defines the following options:

- ``exclude``
    This denotes subdirectories ``venv`` and ``doc/_build``, along with all
    ``__init__.py`` files to be excluded from the check.

- ``select``
    This is a sequence of error codes that flake8 will report errors
    for. The set in the above configuration is a basic set of errors to
    check for and is not an exhaustive list. The error codes chosen above
    have the following descriptions:

    - W191: Indentation has tabs when only spaces are expected.
    - W291: Line contains trailing whitespace.
    - W293: Blank line contains tabs or spaces.
    - W391: There should be only one blank line at the end of each file. This warning will occur when there are zero, two, or more than two blank lines.
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
    - F401: Module imported but not used.
    - F403: ``from module import *`` used.


    A full list of error codes and their descriptions can be found `here <https://flake8.pycqa.org/en/3.9.2/user/error-codes.html>`__.

- ``count``
    The total number of errors is printed at the end of the check.

- ``max-complexity``
    This sets the maximum allowed McCabe complexity value for a block of code.
    The value of 10 was chosen because it is a common default.

- ``max-line-length``
    This denotes the maximum line length for any one line of code.
    The `PEP8`_ standard advises a line length of 79. Since this is a bit
    limiting in some cases, a maximum line length of 100 is suggested.

- ``statistics``
    This enables the number of occurrences of each error or warning code
    to be printed as a report at the end of the check.

Running Flake8
--------------
First, to install flake8, run:

.. code::

    python -m pip install flake8

Then, flake8 can be run from inside your project directory by executing:

.. code::

    flake8 .

This will use the configuration defined in the ``.flake8`` file to
run the style checks on the appropriate files within the project and
report any errors.

In PyAnsys libraries, flake8 is run as part of the CI/CD for code style.
This action is run as a required check on pull requests, preventing
code in violation of these style rules from being merged into the code
base.

Utilizing Black
~~~~~~~~~~~~~~~
Manually checking for code styling can be a tedious task. Luckily,
there are several python tools for autoformatting code to meet PEP8
standards to help with this. The PyAnsys project suggests the use of the
the formatting tool `black`_.


Upon completing a code change, and before committing, `black`_ can be
run to reformat the code, following the PEP8 guidelines enforced through
flake8. This will limit any manual code changes needed to address style
rules.

.. _black: https://black.readthedocs.io/en/stable/

Optionally, it is possible to automate the use of ``black`` as well.
This can be done with the tool `pre-commit`_. Setting up a `pre-commit hook
to run black <https://black.readthedocs.io/en/stable/integrations/source_version_control.html>`_
will automatically format the code before committing. This is the
simplest way to incorporate code style checks into the development
workflow with the least amount of manual effort to maintain PEP8 guidelines.

.. _pre-commit: https://pre-commit.com/

Minimum Standards
~~~~~~~~~~~~~~~~~
The following section describes the minimum set of code style standards
expected in an PyAnsys library.

* All extra whitespace should be trimmed.
    There should be no trailing whitespace on code lines and no
    whitespace at all on blank lines.
* Code blocks should be correctly indented.
    Indentations should be four spaces. Review
    `PEP8 Indentation <https://www.python.org/dev/peps/pep-0008/#indentation>`_
    guidelines for more infromation on proper indentation.
* There should be one blank line at the end of every file.
* All methods should have a single line between them.
* Double quotes should be used instead of single quotes.
* Operators should be surrounded by one space on other side.
* One space should follow a ``,``, ``;``, or ``:``.
* All code lines should not exceed 100 characters.
    The `PEP8 line length <https://www.python.org/dev/peps/pep-0008/#maximum-line-length>`_
    guidelines suggest a maximum line length of 79. Following this limit
    is not as necessary due to modern screen sizes. The suggested maximum
    length of 100 can be easier to accomodate and can still support
    viewing files side-by-side in code editors.
* Only import modules that are actually used.
* ``import *`` should never be used.
    Importing modules this way leads to uncertainty and pollutes the
    code. You cannot know exactly what is being imported and it can
    often lead to name clashes. It is best to import the exact modules
    to be used.
* Limit complexity of code.
    Complexity is a software metric used to determine stability and
    confidence in a piece of code. By limiting complexity, code is
    easier to understand and less risky to modify. Writing low complexity
    code when possible is preferred.
