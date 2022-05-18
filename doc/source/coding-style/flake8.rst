.. _style-guide-enforcement:

Style Guide Enforcement
=======================
This topic describes the use of `Flake8`_ for `PEP8`_ style
enforcement and the minimum standards expected. PyAnsys libraries
are expected to be consistent with these guidelines.

.. _PEP8: https://www.python.org/dev/peps/pep-0008/

Flake8
~~~~~~
`Flake8`_ is a Python tool for enforcing code styling. It is a wrapper
around the following three tools: `PyFlakes`_, `pycodestyle`_, and
`Ned Batchelder's McCabe script for complexity`_. Flake8 runs all three tools at once,
checking the code against a variety of style rules, such as line length,
code complexity, and whitespace.

.. _Flake8: https://flake8.pycqa.org/en/latest/index.html
.. _PyFlakes: https://pypi.org/project/pyflakes/
.. _pycodestyle: https://pypi.org/project/pycodestyle/
.. _`Ned Batchelder's McCabe script for complexity`: https://github.com/PyCQA/mccabe
.. _configuring-flake8:

Configuring Flake8
------------------
Flake8 supports configuring a specific set of style rules to
enforce. This configuration can be stored in your library in a
``setup.cfg``, ``tox.ini``, or ``.flake8`` file. PyAnsys libraries
store the Flake8 configuration in a ``.flake8`` file at the root of the
repository.

Here is an example of a ``.flake8`` configuration file from a PyAnsys
library:

.. code::

    [flake8]
    exclude = venv, __init__.py, doc/_build
    select = W191, W291, W293, W391, E115, E117, E122, E124, E125, E225, E231, E301, E303, E501, F401, F403
    count = True
    max-complexity = 10
    max-line-length = 100
    statistics = True

Flake8 has many options that can be set within the configuration file.
For a list and descriptions, see this `Flake8 documentation topic
<https://flake8.pycqa.org/en/latest/user/options.html>`__.

The example configuration defines the following options:

- ``exclude``
    Denotes subdirectories and ``doc/_build``, along with all
    ``__init__.py`` files to be excluded from the check.

- ``select``
    Sequence of error codes that Flake8 will report errors
    for. The set in the above configuration is a basic set of errors to
    check for and is not an exhaustive list.

    For a full list of error codes and their descriptions, see this `Flake8
    documentation topic <https://flake8.pycqa.org/en/3.9.2/user/error-codes.html>`__.

- ``count``
    Total number of errors to print at the end of the check.

- ``max-complexity``
    Sets the maximum allowed McCabe complexity value for a block of code.
    The value of 10 was chosen because it is a common default.

- ``max-line-length``
    Denotes the maximum line length for any one line of code.
    The `PEP8`_ standard advises a maximum line length of 79. Because
    this is a bit limiting in some cases, the maximum line length
    recommended for a PyAnsys library is 100.

- ``statistics``
    Number of occurrences of each error or warning code
    to be printed as a report at the end of the check.


Running Flake8
--------------
First, to install Flake8, run:

.. code::

    python -m pip install flake8

Then, you can run Flake8 from inside your project directory by executing:

.. code::

    flake8 .

This uses the configuration defined in the ``.flake8`` file to
run the style checks on the appropriate files within the project and
report any errors.

In PyAnsys libraries, Flake8 is run as part of the CI/CD for code style.
This action is run as a required check on pull requests, preventing
code in violation of style rules from being merged into the code
base.


Utilizing Black
~~~~~~~~~~~~~~~
Manually checking for code styling can be a tedious task. Luckily,
several Python tools for auto-formatting code to meet PEP8 standards
are available to help with this. The PyAnsys project suggests the use of the
the formatting tool `black`_.

On completing a code change, and before committing, `black`_ can be
run to reformat the code, following the PEP8 guidelines enforced through
Flake8. This will limit any manual code changes needed to address style
rules.

.. _black: https://black.readthedocs.io/en/stable/

Optionally, it is possible to automate the use of `black`_. This can be
done with the tool `pre-commit`_. Setting up a `pre-commit hook
to run black <https://black.readthedocs.io/en/stable/integrations/source_version_control.html>`_
will automatically format the code before committing. This simple way of
incorporating code style checks into the development workflow to maintain
PEP8 guidelines requires minimal manual effort.

.. _pre-commit: https://pre-commit.com/


Minimum Standards
~~~~~~~~~~~~~~~~~
The following section describes the minimum set of code style standards
expected in a PyAnsys library.

* `W191`_ - **Indentation contains tabs.**

    Indentations should be composed of four spaces, not tabs.

* `W291`_ - **Trailing whitespace.**

    There should be no trailing whitespace after the final character
    on a line.

* `W293`_ - **Blank line contains whitespace.**

    Blank lines should not have any tabs or spaces.

* `W391`_ - **Blank line at the end of every file.**

    There should be only one blank line at the end of each file. This
    warning will occur when there are zero, two, or more than two blank
    lines.

* `E115`_ - **Comment block expected an indent.**

    An indented block comment was expected but a non-indented block
    comment was found instead.

* `E117`_ - **Line over-indented.**

    Lines should be consistently indented in increments of two or four.

* `E122`_ - **Continuation line missing indentation or outdented.**

    Continuation line is not indented as far as it should be or is
    indented too far.

* `E124`_ - **Closing bracket does not match indentation.**

    Closing bracket does not match the indentation of the opening bracket.

* `E125`_ - **Continuation line with same indent as next logical line.**

    Continuation line is indented at the same level as the next logical
    line. It should be indented to one more level to distinguish it from
    the next line.

* `E225`_ - **Missing whitespace around operator.**

    There should be one space before and after all operators.

* `E231`_ - **Missing whitespace after certain special characters.**

    There should be one space after the characters ``,``, ``;``, and ``:``.

* `E301`_ - **Expected a blank line, found none.**

    All methods of a class should have a single line between them.

* `E303`_ - **Too many blank lines.**

    There should be one line between methods and two lines between
    methods and classes.

* `E501`_ - **Line too long.**

    All code lines should not exceed 100 characters. The
    `PEP8 line length guideline <https://www.python.org/dev/peps/pep-0008/#maximum-line-length>`_
    suggests a maximum line length of 79. Following this limit
    is not as necessary today due to modern screen sizes. The suggested maximum
    length of 100 can be easier to accommodate and can still support
    viewing files side by side in code editors.

* `F401`_ - **Module imported but unused.**

    Modules should only be imported if they are actually used.

* `F403`_ - **'from module import *' used.**

    Importing using wildcards (``*``) should never be done. Importing
    modules this way leads to uncertainty and pollutes the code. You
    cannot know exactly what is being imported and name clashes are common.
    Import only the modules to be used.

* **Limit complexity of code to 10.**

  This is enforced by the ``max-complexity`` option described in
  :ref:`configuring-flake8`. Limiting code complexity leads to code that
  is easier to understand and less risky to modify. Write low-
  complexity code when possible.


Your ``.flake8`` file should be:

.. code::

    [flake8]
    exclude = venv, __init__.py, doc/_build
    select = W191, W291, W293, W391, E115, E117, E122, E124, E125, E225, E231, E301, E303, E501, F401, F403
    count = True
    max-complexity = 10
    max-line-length = 100
    statistics = True


.. _W191: https://www.flake8rules.com/rules/W191.html
.. _W291: https://www.flake8rules.com/rules/W291.html
.. _W293: https://www.flake8rules.com/rules/W293.html
.. _W391: https://www.flake8rules.com/rules/W391.html
.. _E115: https://www.flake8rules.com/rules/E115.html
.. _E117: https://www.flake8rules.com/rules/E117.html
.. _E122: https://www.flake8rules.com/rules/E122.html
.. _E124: https://www.flake8rules.com/rules/E124.html
.. _E125: https://www.flake8rules.com/rules/E125.html
.. _E225: https://www.flake8rules.com/rules/E225.html
.. _E231: https://www.flake8rules.com/rules/E231.html
.. _E301: https://www.flake8rules.com/rules/E301.html
.. _E303: https://www.flake8rules.com/rules/E303.html
.. _E501: https://www.flake8rules.com/rules/E501.html
.. _F401: https://www.flake8rules.com/rules/F401.html
.. _F403: https://www.flake8rules.com/rules/F403.html

