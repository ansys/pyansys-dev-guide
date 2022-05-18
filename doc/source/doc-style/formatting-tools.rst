Doc Style Tools
===============
There are plenty of tools for documentation style and coverage. This section
presents some of the most popular ones in the Python ecosystem. A minimum
configuration is provided for each one so you can easily include them in your
PyAnsys project.

Most of the tools presented can be configured using :ref:`the
\`\`pyproject.toml\`\` file`, avoiding dotfiles and thus leading to a much
cleaner root project directory.


Blacken-Docs
------------

When writing documentation, it is frequent to include code-blocks which are used
as examples. However, these code snippets style cannot be verified with the usual code
formatting tools. This is where `blacken-docs`_ comes into play. You can execute
this tool by running:

.. code:: bash

   blacken-docs -l <line-length> doc/**/*.rst


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

Numpydoc Validation
-------------------
To validate the style of :ref:`Numpydoc Docstrings`, it is possible to
take advantage of the `numpydoc`_ Sphinx extension. Note that this extension
checks only for those objects whose docstrings must be rendered. It is not a
command line tool that checks the style of all docstrings in your source code.

Because `numpydoc`_ is a Sphinx extension, it must be configured in the
``conf.py`` file.  See :ref:`The \`\`doc/\`\` directory`. Start by adding it to the
list of extensions:

.. code-block:: python

  extensions = [
      'numpydoc',
      ...
  ]

Once the `numpydoc`_ extension is added, you can select which `validation checks
<https://numpydoc.readthedocs.io/en/latest/validation.html#built-in-validation-checks>`_
must be addressed by using the ``numpydoc_validation_checks`` dictionary:

.. code-block:: python

   numpydoc_validation_checks = {"GL08"}

This will issue the following warning for any object without a docstring:

.. code-block:: python

   "The object does not have a docstring"

For a complete list of available checks, see the `full mapping of
validation checks
<https://numpydoc.readthedocs.io/en/latest/validation.html#built-in-validation-checks>`_.

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
   convention = "numpy"


.. _blacken-docs: https://github.com/asottile/blacken-docs
.. _interrogate: https://interrogate.readthedocs.io/en/latest/
.. _docstr-coverage: https://docstr-coverage.readthedocs.io/en/latest/index.html
.. _docstring-coverage: https://bitbucket.org/DataGreed/docstring-coverage/wiki/Home
.. _pytest-cov: https://pytest-cov.readthedocs.io/en/latest/
.. _doctest: https://docs.python.org/3/library/doctest.html
.. _PEP 257: http://www.python.org/dev/peps/pep-0257/
.. _docformatter: https://github.com/PyCQA/docformatter
.. _codespell: https://github.com/codespell-project/codespell
.. _pytest-cov: https://pytest-cov.readthedocs.io/en/latest/
.. _numpydoc: https://numpydoc.readthedocs.io/en/latest/format.html
