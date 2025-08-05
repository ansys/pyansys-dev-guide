.. _setting_up_dev_environment:

Environment setup
=================

Before you can contribute to any PyAnsys project, you must set up
your developer environment.

Python
------
.. raw:: html
    
    <div align="center">
        <img 
            src="https://github.com/python/pythondotorg/raw/main/static/community_logos/python-logo-inkscape.svg" 
            width="40%"
        >
    </div>

All PyAnsys projects require a Python interpreter for interacting
with PyAnsys libraries. Therefore, you must ensure that at least one Python
interpreter is installed on your local machine.

Install Python
~~~~~~~~~~~~~~

There are several ways to install a Python package on your local machine:

- Use an installer from the `official Python download page <https://www.python.org/downloads/>`_.
- Use a package manager or "store" on your machine.

.. warning:: 

    Ensure that you install Python from an official channel. Do not trust
    third-party websites or download executable content from them.

.. tab-set::

    .. tab-item:: Windows

        To install Python on a machine running Windows:
        
        1. Download the `latest stable Python version for Windows <https://www.python.org/downloads/windows/>`_.
        2. Execute the installer, referring to  `Using Python on
           Windows <https://docs.python.org/3/using/windows.html>`_ for
           detailed installation instructions.

    .. tab-item:: macOS

        To install Python on a machine running macOS:
        
        1. Download the `latest stable Python version for macOS <https://www.python.org/downloads/macos/>`_.
        2. Execute the installer, referring to `Using Python on
           a Mac <https://docs.python.org/3/using/mac.html>`_ for
           detailed installation instructions.

        .. note::

            It is likely that your macOS distribution already comes with some
            version of Python installed. For more information, see :ref:`Verify Python version`.

    .. tab-item:: Linux/UNIX

        To install Python on a machine running Linux/UNIX:
        
        1. Download the `latest stable Python version for Linux/UNIX <https://www.python.org/downloads/source/>`_.
        2. Decompress the source code and follow the installation instructions in the
           ``README.rst`` file. For more information, see `Using Python on Unix Platforms
           <https://docs.python.org/3/using/unix.html>`_.

        .. note::

            It is likely that your Linux/UNIX distribution already comes with some
            version of Python installed. For more information, see :ref:`Verify Python version`.


Verify Python version
~~~~~~~~~~~~~~~~~~~~~

Once your Python installation is complete, verify it with this command:

.. code-block:: text

    python --version

Virtual environments
--------------------

When working in multiple Python projects, it is likely each of these projects has its
own requirements. Sometimes, requirements across projects can be incompatible.
Virtual environments were devised to isolate Python environments, which guarantees
that you do not face dependency problems when working in multiple projects.

For information on the most fundamental commands for manipulating and
interacting with a Python virtual environment, see the `official Python documentation on
the venv module <https://docs.python.org/3/library/venv.html>`_.

Check
~~~~~

Before creating a virtual environment, you must run the command for your OS to see if you are already
using one:

.. tab-set::

    .. tab-item:: Windows

        .. tab-set::

            .. tab-item:: CMD

                .. code-block:: text

                    where python

            .. tab-item:: PowerShell

                .. code-block:: text

                    where.exe python

    .. tab-item:: macOS/Linux/UNIX

        .. code-block:: text

            which python

The command returns the path to the Python virtual environment that your system is currently using. 

Ensure that it points to your default installation and not to a virtual
environment. If it points to a virtual environment, see :ref:`Deactivate` for
information on deactivating the virtual environment.

Create
~~~~~~

Usually, virtual environments are named ``venv`` or ``.venv``.
You can create a virtual environment named ``<venv>`` with this command:

.. code-block:: text

    python -m venv <venv>

Activate
~~~~~~~~

You would activate the preceding virtual environment with the command for your OS:

.. tab-set::

    .. tab-item:: Windows

        .. tab-set::

            .. tab-item:: CMD

                .. code-block:: text

                    <venv>\Scripts\activate.bat

            .. tab-item:: PowerShell

                .. code-block:: text

                    <venv>\Scripts\Activate.ps1

    .. tab-item:: macOS/Linux/UNIX

        .. code-block:: text

            source <venv>/bin/activate


Deactivate
~~~~~~~~~~

You can deactivate a virtual environment with the command for your OS:

.. code-block:: text

    deactivate

Git
---

.. raw:: html
    
    <div align="center">
        <img 
            src="https://github.com/git/git-scm.com/raw/main/public/images/logo%402x.png"
            width="20%"
        >
    </div>

`Git <https://git-scm.com/>`_ is an open source VCS (version control system). It
is used to track changes and register new content in software-related projects. Git
registers the author and date of the changes so that accurate tracking of the
software's evolution is available.

Install Git
~~~~~~~~~~~

.. tab-set::

    .. tab-item:: Windows

        To install Git on a machine running Windows:
        
        1. Download the `latest stable standalone Git version for Windows <https://git-scm.com/download/win>`_.
        2. Execute the installer and follow the installation instructions.

    .. tab-item:: macOS

        To install Git on a machine running macOS:
        
        1. Check the `latest stable Git version for macOS <https://git-scm.com/download/mac>`_.
        2. Run the installation command for your package manager.

    .. tab-item:: Linux/UNIX

        To install Git on a machine running Linux/UNIX:
        
        1. Check the `latest stable Git version for Linux/UNIX <https://git-scm.com/download/linux>`_.
        2. Run the installation command for your package manager.

Verify Git version
~~~~~~~~~~~~~~~~~~

Once your Git installation finishes, verify it with this command:

.. code-block:: text

    git --version

Use Git
~~~~~~~

If you're new to Git, see the `Git documentation <https://git-scm.com/doc>`_
for comprehensive usage information.

For an understanding of Git workflows and branching strategies, 
see the `Learn Git Branching <https://learngitbranching.js.org/>`_ tutorial.

If you're unfamiliar with GitHub, see 
`The Official GitHub Training Manual <https://githubtraining.github.io/training-manual/>`_
for guidance.

Configure Git
~~~~~~~~~~~~~

It is very important to properly configure Git so that every modification that you make
to the code points to you. There are two types of Git configuration:
:ref:`Global` and :ref:`Local`. It is also possible to combine both to have
a :ref:`Dynamic` configuration. 

Global
++++++
A global configuration is automatically included in every Git repository on
your machine unless overridden by a :ref:`Local` configuration, which
is located in ``C:\Users\<username>\.gitconfig`` for Windows users or in
``/home/<username>/.gitconfig`` for macOS, Linux, or UNIX users.

You can set the value for any variable in a field with this command:

.. code-block:: bash

   git config --global <field>.<varname> <value>

Some examples of setting values follow.

**Set your name** 

.. code-block:: bash

    git config --global user.name <Your Name>

**Set your email** 

.. code-block:: bash

    git config --global user.email <Ansys Email>

**Set the default branch name** 

.. code-block:: bash

    git config --global init.defaultBranch main

Local
+++++

There might be a time when you want to declare a specific configuration to use only
in a given project. To override the global configuration, you can declare a local
configuration.

In a local configuration, the commands are the same as in the global configuration. The
one exception is that instead of using the ``--global`` flag, you use the ``--local`` flag.
Ensure that you run the commands in the root directory of your project and that a ``.git``
directory exists.

If you would like to manually modify your local configuration, it is saved in
the ``.git/config`` file.

Dynamic
+++++++

It is possible to configure Git such that it selects between multiple
configuration profiles according to whether your project is located on your system.
This lets you define common configurations for working under
``Ansys`` or other open source projects from which Ansys benefits.

As an example, consider the following scenario for setting up two Git
configuration profiles for working with Ansys projects and personal projects.

Create the two files, naming them so that they are easily distinguishable. For
example, name them ``.gitconfig-ansys`` and ``.gitconfig-personal``. Then, use Git
`Conditional includes <https://git-scm.com/docs/git-config#_conditional_includes>`_
to control which Git configuration is applied based on whether the project is located
on your system.

Here are examples of what these files might look like:

.. tab-set::

    .. tab-item:: .gitconfig

        .. code-block:: text

            [includeIf "gitdir:path/to/your/ansys/folder/of/projects"]
              path = path/to/.gitconfig-ansys

            [includeIf "gitdir:path/to/your/personal/folder/of/projects"]
              path = path/to/.gitconfig-personal

    .. tab-item:: .gitconfig-ansys

        .. code-block:: text

            [user]

              name = <Ansys Name>
              email = <Ansys Email>
              signingkey = <Ansys GPG Key>

    .. tab-item:: .gitconfig-personal

        .. code-block:: text

            [user]

              name = <Name or Nickname>
              email = <Personal Email>
              signingkey = <Personal GPG Key>


Sign commits
~~~~~~~~~~~~

To verify which code changes were made by you, signing the commit
is required. To sign a commit, you must generate a ``GPG`` key, associate it with
GitHub, and specify it in your Git configuration.

For an explanation of the process, see `Manage commit signature verification
<https://docs.github.com/en/authentication/managing-commit-signature-verification>`_
in the GitHub documentation.


Enable SSH
~~~~~~~~~~

Working with Secure Shell Protocol (SSH) is not only a good practice but
also required for contributing to PyAnsys projects. Without an SSH key,
you are not able to clone **internal** or **private** repositories or
to push new changes.

For information on setting up SSH with GitHub, see `Connecting to GitHub with SSH
<https://docs.github.com/en/authentication/connecting-to-github-with-ssh>`_
in the GitHub documentation.

Handle line endings
~~~~~~~~~~~~~~~~~~~

Every time you introduce a new line by pressing the **enter** key, an invisible
character is introduced to represent a line ending. Each operating system manages
these end-of-line (EOL) characters in its own way. For Windows, the EOL is
also known as a `CRLF`, while in Linux it is known as a `LF`.

To avoid problems between developers working in the same repository but using
different operating systems, you can specify an EOL policy in a ``.gitattributes`` file.

In a ``.gitattributes`` file that you have committed to your repository, you can
customize the type of EOL characters that you expect developers to use. Git
then automatically manages these EOL characters so that developers do not
need to worry about them. Consider this example in `Configuring Git to handle line endings
<https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings#example>`_
in the GitHub documentations:

.. code:: text

   # Set the default behavior, in case people don't have ``core.autocrlf`` set.
   * text=auto

   # Explicitly declare text files that you want to always be normalized and converted
   # to native line endings on checkout.
   *.c text
   *.h text

   # Declare files that always have CRLF line endings on checkout.
   *.sln text eol=crlf

   # Denote all files that are truly binary and should not be modified.
   *.png binary
   *.jpg binary

.. _git_clean:

Remove files and directories untracked by Git
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To remove files and directories that are not tracked by Git from your working directory,
you want to periodically run this command:

``git clean -fdx .``

Descriptions follow for each command option:

- ``f`` forces deletion of untracked files (and directories if ``d`` is also specified)
  without requiring additional confirmation.

- ``d`` deletes untracked directories. By default, the ``git clean``
  command does not recurse into untracked directories to avoid deleting too much.

- ``x`` deletes ignored files, which are those specified in your ``.gitignore`` file.
  You use this option when you want to clean up all untracked files, including build
  products.

The trailing ``.`` specifies the current directory as the starting point for the
cleaning. For example, to clean all of the untracked files that are generated by
building documentation locally, you would run the ``git clean -fdx .`` command
from the ``doc`` directory.

WSL2
----

Some developers prefer using Windows as the operating system for their machines.
However, they might like to take advantage of some features provided by a Linux
operating system. The Windows Subsystem for Linux (WSL) was devised to solve
this problem. For installation information, see `How to install Linux on Windows with WSL
<https://docs.microsoft.com/en-us/windows/wsl/install>`_ in the Microsoft Windows
documentation.

Install WSL2
~~~~~~~~~~~~

Open a new PowerShell session and install WSL with this command:

.. code-block:: powershell

   wsl --install

After installing WSL, ensure that you are running the WSL2 version with this
command:

.. code-block:: powershell

   wsl --set-default-version 2

Verify WSL version
~~~~~~~~~~~~~~~~~~

Verify your WSL version with this command:

.. code-block:: powershell

   wsl --list -v

Install Linux distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~

After WSL2 is installed, install a Linux distribution.
To get a list of available distributions, run this command:

.. code-block:: powershell

   wsl --list --online

Most developers choose `Ubuntu <https://ubuntu.com/download>`_ because it is a
well maintained Linux distribution with a huge collection of packages.

To install the Linux distribution of your choice, run this command:

.. code-block:: powershell

   wsl --install -d <distribution name>

You can use the preceding command to install multiple Linux distributions. Indicate
the distributions that you would like to use with WSL2 with this command:

.. code-block:: powershell
   
   wsl -d <distribution name>

Windows terminal
----------------

`Windows Terminal <https://docs.microsoft.com/en-us/windows/terminal/>`_ is
an app that integrates multiple shells into a single console. Windows
ships by default with two shells: ``CMD`` and ``PowerShell``. If :ref:`WSL2` is
installed, a Linux shell is added. Hence, the goal of Windows Terminal
is to collect and manage all shell sessions in a single program. You can install
Windows Terminal from the `Windows Terminal page
<https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-us&gl=US>`_
on the Microsoft Store.

.. image:: images/windows_terminal.png
    :align: center
    :alt: Windows Terminal with different active shell sessions.
