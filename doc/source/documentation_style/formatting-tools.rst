Formatting Tools
================

There are plenty of tools for documentation style and coverage. This section
presents some of the most popular ones in the Python ecosystem. A minimum
configuration is provided for each one so you can easily include them in your
PyAnsys project.

Most of the tools presented can be configured using :ref:`the
\`\`pyproject.toml\`\` file`, avoiding dotfiles and thus leading to a much
cleaner root project directory.


Codespell
---------

`Codespell`_ checks for common misspellings in text files. This implies that it
is not limited to Python files but can check any human-readable file.

It is possible to ignore words that are flagged as misspelled. You can specify these words in a
file that can hen be passed to `codespell` by running:

.. code:: bash

   codespell --write-changes --ignore-words=<FILE>


Docformatter
------------

`Docformatter`_ allows you to automatically format Python docstrings according
to `PEP 257`_. To make sure `docformatter`_ wraps your docstrings at a given
number of characters, the following configuration should be used:


.. code:: bash

   docformatter -r -i --wrap-summaries <length> --wrap-descriptions <length> src


Doctest
-------

`Doctest`_ is a module from the Python standard library, which means it is
included by default with your Python installation. It is used for checking the
examples provided inside docstrings to make sure that they reflect the current usage
of the source code. `Doctest`_ can be integrated with ``pytest`` in :ref:`The
\`\`pyproject.toml\`\` File`:

.. code:: toml

   [tool.pytest.ini_options]
   addopts = "--doctest-modules"


Interrogate
-----------

`Interrogate`_ is a tool for checking docstring coverage. Similar to source code
coverage tools, this tool tests how many functions, classes, and modules in a Python
library hold a docstring.

.. code:: toml

    [tool.interrogate]
    exclude = ["setup.py", "doc", "tests"]
    color = true
    verbose = 2

Alternate tools to `interrogate`_ are `docstr-coverage`_ and
`docstring-coverage`_. However, `interrogate`_ is modern and maintained, with
output resembling that of `pytest-cov`_, which is the the equivalent tool
for source code coverage.


Pydocstyle
----------

`Pydocstyle`_ is a tool for checking the compliance of Python docstrings with `PEP
257`_.  Its configuration can be defined in the :ref:`The \`\`pyproject.toml\`\`
File`.  By default, it will match all ``*.py`` files except those starting with
``test_*.py``. Default `pydocstyle`_ configuration should be enough for a
PyAnsys project. If additional configuration is needed, it must be included
under the ``[tool.pydocstyle]`` entry:

.. code:: toml

   [tool.pydocstyle]
   # Additional configuration

.. include:: ../links.rst
