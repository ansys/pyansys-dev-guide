Required Sphinx configuration
=============================
The following page explains the minimum required `Sphinx`_ configuration for
building the documentation of a PyAnsys project.

When installing `Sphinx`_, a program named ``sphinx-build`` gets installed too.
This program is in charge of collecting, parsing and rendering all the
ReStructured Text files in :ref:`The \`\`doc/\`\` directory`.

The behavior of ``sphinx-build`` is controlled through a ``Makefile`` (to be
used in POSIX systems) or a ``make.bat`` file (used in Windows systems). Once
the ``sphinx-build`` command is triggered, the configuration declared in the
``conf.py`` is applied when rendering the documentation pages. 


The ``conf.py`` file
--------------------
The following code snippet collects the minimum required configuration for a
``conf.py`` file. Custom additions should be done on top of this configuration
to guarantee that a minimum consistency applies across different PyAnsys
projects.

.. literalinclude:: code/required_conf.py

Automation files
----------------
As introduced at the beginning of this section, the ``sphinx-build`` program and
all its options and arguments can be automated through the usage of a
``Makefile`` file or a `make.bat`` file. These files should be placed at the
first level of :ref:`The \`\`doc/\`\` directory`, next to the ``source/``
directory.

Notice that both files contain a ``SPHINXOPTS`` variable containing the ``-j auto -W --keep-going``:

- The ``-j`` flag indicates the number of "jobs" (i.e. the number of cores to be
  used). Default value is ``auto``, so it automatically detects the amount of
  cores of a CPU.

- The ``-W`` flag turns warnings into errors. This guarantees that documentation
  health is maximum.

- The ``--keep-going`` flag is used to render the whole documentation even if a
  warning was found, so developers are aware about the full set of warnings.

A special rule named ``pdf`` is also included. This rule is in charge of
generating the ``PDF`` documentation of the project.


Example ``Makefile``
^^^^^^^^^^^^^^^^^^^^
The following code collects the required options and automation rules to be used
in a ``Makefile`` for building the documentation of a PyAnsys project:

.. literalinclude:: code/required_makefile

Example ``make.bat``
^^^^^^^^^^^^^^^^^^^^
The following code collects the required options and automation rules to be used
in a ``make.bat`` for building the documentation of a PyAnsys project:

.. literalinclude:: code/required_make.bat


.. LINKS & REFERENCES:

.. _Sphinx: https://www.sphinx-doc.org/en/master/
