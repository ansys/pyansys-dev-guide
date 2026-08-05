.. _doc_style_tools:

Documentation style tools
=========================

There are plenty of tools for documentation style and coverage. This section
presents some of the most popular ones in the Python ecosystem. A minimum
configuration is provided for each one so you can easily include them in your
PyAnsys project.

Most of the tools presented can be configured using :ref:`The
\`\`pyproject.toml\`\` file`, avoiding dotfiles and thus leading to a much
cleaner root project directory.

The ``blacken-docs`` tool
-------------------------

When writing documentation, code blocks are frequently used to provide examples.
However, these code snippets cannot be verified with the usual code
formatting tools. This is where `blacken-docs`_ comes into play. You can execute
this tool by running this command:

.. code:: bash

   blacken-docs -l <line-length> doc/**/*.rst

The ``codespell`` tool
----------------------

The `codespell`_ tool checks for common misspellings in text files. This implies that it
is not limited to Python files but can run checks on any human-readable file.

It is possible to ignore words that are flagged as misspelled. You can specify these words in a
file that can then be passed to ``codespell`` by running this command:

.. code:: bash

   codespell --write-changes --ignore-words=<FILE>

The ``docformatter`` tool
-------------------------

The `docformatter`_ tool automatically formats Python docstrings according 
to `PEP 257`_. To make sure ``docformatter`` wraps your docstrings at a given
number of characters, use this configuration:

.. code:: bash

   docformatter -r -i --wrap-summaries <length> --wrap-descriptions <length> src

The ``doctest`` tool
--------------------

The `doctest`_ tool is a module from the Python standard library, which means it is
included by default with your Python installation. It is used for checking the
examples provided inside docstrings to make sure that they reflect the current usage
of the source code. You can integrate `doctest`_ with ``pytest`` in :ref:`The
\`\`pyproject.toml\`\` file`:

.. code:: toml

   [tool.pytest.ini_options]
   addopts = "--doctest-modules"

The ``interrogate`` tool
------------------------

The `interrogate`_ tool checks docstring coverage. Similar to source code
coverage tools, this tool tests how many modules, functions, classes, and
methods in a Python library hold a docstring.

.. code:: toml

    [tool.interrogate]
    exclude = ["setup.py", "doc", "tests"]
    color = true
    verbose = 2

Alternate tools to `interrogate`_ are `docstr-coverage`_ and
`docstring-coverage`_. However, `interrogate`_ is modern and maintained, with
output resembling that of `pytest-cov`_, which is the equivalent tool
for source code coverage.

Numpydoc validation
-------------------

To validate the style of :ref:`Numpydoc docstrings`, you can
take advantage of the Sphinx `numpydoc`_ extension. Note that this extension
checks only for those objects whose docstrings must be rendered. It is not a
command line tool that checks the style of all docstrings in your source code.

Because ``numpydoc`` is a Sphinx extension, it must be configured in the
``conf.py`` file. For more information, see :ref:`The \`\`doc\`\` directory`. Start by adding it to the
list of extensions:

.. code-block:: python

  extensions = ["numpydoc", ...]

Once the ``numpydoc`` extension is added, you can select which `built-in validation checks
<https://numpydoc.readthedocs.io/en/latest/validation.html#built-in-validation-checks>`_
must be addressed by using the ``numpydoc_validation_checks`` dictionary:

.. code-block:: python

   numpydoc_validation_checks = {"GL08"}

This issues the following warning for any object without a docstring:

.. code-block:: python

   "The object does not have a docstring"


The ``pydocstyle`` tool
-----------------------

The `pydocstyle`_ tool checks the compliance of Python docstrings with `PEP 257`_.
Its configuration can be defined in the :ref:`The \`\`pyproject.toml\`\` file`.
By default, `pydocstyle`_ matches all ``*.py`` files except those starting with
``test_*.py``. The default configuration should be enough for a PyAnsys project.
However, if additional configuration is needed, it must be included under the
``[tool.pydocstyle]`` entry:

.. code:: toml

   [tool.pydocstyle]
   convention = "numpy"

Vale
----

`Vale`_ is a tool for maintaining a consistent style and voice in your documentation.
Its configuration is defined in a ``.vale.ini`` file in the library's ``doc`` folder.
For PyAnsys libraries, ``Vale`` is configured to apply the guidelines in the
`Google developer documentation style guide <https://developers.google.com/style/>`_,
along with any custom Ansys rules and terminology lists, to reStructuredText (RST)
and Markdown (MD) files.

When ``Vale`` is implemented in your PyAnsys library, you can check
any content changes that you make in supported files locally.

In the library's ``doc`` folder, download the package with this command:

.. code-block:: bash

   vale sync

Check all files in the ``doc`` folder by running this command:

.. code-block:: bash

   vale .

To check all files in the repository, go to the ``root`` directory and run
this command:

.. code-block:: bash

   vale --config=doc/.vale.ini .

To check all files in only a particular folder, type ``vale`` followed by the
name of the folder.

Address any warnings and issues that display by either editing the
file to fix or adding a term to the ``accept.txt`` file in
``doc\styles\config\vocabularies\ANSYS``.
