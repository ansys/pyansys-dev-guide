Required Sphinx configuration
=============================

This page explains the minimum required `Sphinx`_ configuration for
building the documentation of a PyAnsys library.

When installing `Sphinx`_, a program named ``sphinx-build`` also gets installed.
This program is in charge of collecting, parsing, and rendering all
ReStructuredText (RST) files in :ref:`The \`\`doc\`\` directory`.

The behavior of the ``sphinx-build`` program is controlled through either
a ``Makefile`` (for POSIX systems) or a ``make.bat`` file (for Windows systems).
Once the ``sphinx-build`` command is triggered, the configuration declared in the
``conf.py`` file is applied when rendering the documentation pages. 

The ``conf.py`` file
--------------------

The following ``conf.py`` file provides the minimum required configuration for a
PyAnsys library. To guarantee consistency across PyAnsys libraries, you should
only make custom additions on top of this configuration.

.. literalinclude:: code/required_conf.py

Automation files
----------------

As indicated earlier on this page, the ``sphinx-build`` program and
all its options and arguments can be automated by using a
``Makefile`` file or a ``make.bat`` file. These files should be placed at the
first level of the ``doc`` directory, next to the ``source`` directory.

Notice that both files contain a ``SPHINXOPTS`` variable with these options: ``-j``,
``-W``, and ``--keep-going``.

- ``-j``: Indicates the number of jobs (number of cores) to use. 
  The default value is ``auto``, which means that the number of cores in
  the CPU is to be automatically detected.

- ``-W``: turns warnings into errors. This guarantees that documentation
  health is maximized.

- ``--keep-going``: Specifies whether to render the whole documentation,
  even if a warning is found. This option enables developers to be aware of the
  full set of warnings.

A special rule named ``pdf`` is also included. This rule is in charge of
generating a PDF file for the library's documentation.

Example for ``Makefile``
^^^^^^^^^^^^^^^^^^^^^^^^

The following code collects the required options and automation rules for the
``Makefile`` program to use when building documentation for a PyAnsys library:

.. literalinclude:: code/required_makefile

Example for ``make.bat``
^^^^^^^^^^^^^^^^^^^^^^^^

The following code collects the required options and automation rules for the
``make.bat`` program to use when building documentation for a PyAnsys project:

.. literalinclude:: code/required_make.bat
