Setting up your development environment
=======================================
Before you can contribute to any PyAnsys project, you must set up
your developer environment.

Python
------
.. raw:: html
    
    <div align="center">
      <img src="https://github.com/python/pythondotorg/raw/main/static/community_logos/python-logo-inkscape.svg">
    </div>

All PyAnsys projects require a Python interpreter for interacting
with PyAnsys libraries. Therefore, you must ensure that at least one Python
interpreter is installed on your local machine.

Installation
~~~~~~~~~~~~
There are several ways to install a Python package on your local machine:

- Use an official installer from the `official Python download section <https://www.python.org/downloads/>`_.
- Install via a package manager or "store" on your machine.

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

        To install Python on a machine running the macOS:
        
        1. Download the `latest stable Python version for macOS <https://www.python.org/downloads/macos/>`_.
        2. Execute the installer, referring to `Using Python on
           a Mac <https://docs.python.org/3/using/mac.html>`_ for
           detailed installation instructions.

        .. note::

            It is likely that your macOS distribution already comes with some
            version of Python installed. For more information, see :ref:`Verification`.

    .. tab-item:: Linux/UNIX

        To install Python on a machine running Linux/UNIX:
        
        1. Download the `latest stable Python version for Linux/UNIX <https://www.python.org/downloads/source/>`_.
        2. Decompress the source code and follow the installation instructions in the
           ``README.rst`` file. For more information, see `Using Python on Unix Platforms
           <https://docs.python.org/3/using/unix.html>`_.

        .. note::

            It is likely that your Linux/UNIX distribution already comes with some
            version of Python installed. For more information, see :ref:`Verification`.


Verification
~~~~~~~~~~~~
Once your Python installation is complete, verify it with:

.. tab-set::

    .. tab-item:: Windows

        .. tab-set::

            .. tab-item:: CMD

                .. code-block:: bash

                    py --version

            .. tab-item:: PowerShell

                .. code-block:: bash

                    py --version

    .. tab-item:: macOS

        .. code-block:: bash

            python --version

    .. tab-item:: Linux/UNIX

        .. code-block:: bash

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
Before creating a new virtual environment, you must run this code to see if you are already
working with one:

.. tab-set::

    .. tab-item:: Windows

        .. tab-set::

            .. tab-item:: CMD

                .. code-block:: text

                    where.exe python

            .. tab-item:: PowerShell

                .. code-block:: text

                    where.exe python

    .. tab-item:: macOS

        .. code-block:: text

            which python

    .. tab-item:: Linux/UNIX

        .. code-block:: text

            which python

This command returns the path to the Python virtual environment that your system is currently using. 

Ensure that it points to your default installation and not to a virtual
environment. If it points to a virtual environment, see :ref:`Deactivate` for
information on deactivating your virtual environment.

Create
~~~~~~
Usually, virtual environments are named ``venv`` or ``.venv``.
You can create a virtual environment named `<venv>` with:

.. tab-set::

    .. tab-item:: Windows

        .. tab-set::

            .. tab-item:: CMD

                .. code-block:: text

                    py -m venv <venv>

            .. tab-item:: PowerShell

                .. code-block:: text

                    py -m venv <venv>

    .. tab-item:: macOS

        .. code-block:: text

            python -m venv <venv>

    .. tab-item:: Linux/UNIX

        .. code-block:: text
            
            python -m venv <venv>

Activate
~~~~~~~~
You would activate the preceding virtual environment with:

.. tab-set::

    .. tab-item:: Windows

        .. tab-set::

            .. tab-item:: CMD

                .. code-block:: text

                    <venv>\Scripts\activate.bat

            .. tab-item:: PowerShell

                .. code-block:: text

                    <venv>\Scripts\Activate.ps1

    .. tab-item:: macOS

        .. code-block:: text

            source <venv>/bin/activate

    .. tab-item:: Linux/UNIX

        .. code-block:: text

            source <venv>/bin/activate

Deactivate
~~~~~~~~~~
You would deactivate a virtual environment with:

.. tab-set:: 

    .. tab-item:: Windows

        .. tab-set::

            .. tab-item:: CMD

                .. code-block:: text

                    deactivate

            .. tab-item:: PowerShell

                .. code-block:: text

                    deactivate

    .. tab-item:: macOS

        .. code-block:: text

            deactivate

    .. tab-item:: Linux/UNIX

        .. code-block:: text

            deactivate


Git
---
.. raw:: html
    
    <div align="center">
      <img src="https://github.com/git/git-scm.com/raw/main/public/images/logo%402x.png">
      <br><br>
    </div>

`Git <https://git-scm.com/>`_ is an open source version control system (VCS). It
is used to track changes and register new content in software-related projects. Git
registers the author and date of the changes so that accurate tracking of the
software's evolution is available.

Installation
~~~~~~~~~~~~

.. tab-set::

    .. tab-item:: Windows

        To install Git on a machine running Windows:
        
        1. Download the `latest stable standalone Git version for Windows <https://git-scm.com/download/win>`_.
        2. Execute the installer and follow the installation instructions.

    .. tab-item:: macOS

        To install Git on a machine running the macOS:
        
        1. Check the `latest stable Git version for macOS <https://git-scm.com/download/mac>`_.
        2. Run the installation command for your package manager.

    .. tab-item:: Linux/UNIX

        To install Git on a machine running Linux/UNIX:
        
        1. Check the `latest stable Git version for Linux/UNIX <https://git-scm.com/download/linux>`_.
        2. Run the installation command for your package manager.


Verification
~~~~~~~~~~~~
Once your installation process is complete, verify your Git installation with:

.. tab-set:: 

    .. tab-item:: Windows

        .. tab-set::

            .. tab-item:: CMD

                .. code-block:: text

                    git --version

            .. tab-item:: PowerShell

                .. code-block:: text

                    git --version

    .. tab-item:: macOS

        .. code-block:: text

            git --version

    .. tab-item:: Linux/UNIX

        .. code-block:: text

            git --version

Usage
~~~~~
If you are not familiar with Git, see the `Git Reference Manual <https://git-scm.com/doc>`_.
for comprehensive information on how to use it.

If you are not familiar with Git and the Git workflows in terms of development, it is
recommended that you follow this tutorial on `Learning Git branching <https://learngitbranching.js.org/>`_.

Also, if you are not that familiar with GitHub, feel free to go through the
`GitHub Training Manual <https://githubtraining.github.io/training-manual/>`_.

Configuration
~~~~~~~~~~~~~
It is very important to properly configure Git so that every modification that you make
to the code points to you. There are two types of configuration:
:ref:`Global` and :ref:`Local`. It is also possible to combine both to have
a :ref:`Dynamic` configuration. 

Global
++++++
Global configuration are automatically included in every Git repository on
your machine unless overridden by a :ref:`Local` configuration, which
is located in ``C:\Users\<username>\.gitconfig`` for Windows users or in
``/home/<username>/.gitconfig`` for macOS, Linux, or UNIX users.

You can set the value for any variable in a field with:

.. code-block:: bash

   git config --global <field>.<varname> <value>

Some examples follow.

**Set up your name** 

.. code-block:: bash

    git config --global user.name <Your Name>

**Set up your email** 

.. code-block:: bash

    git config --global user.email <Ansys Email>

**Set up the default branch name** 

.. code-block:: bash

    git config --global init.defaultBranch main

Local
+++++
There might be a time when you want to declare a specific configuration to use only
in a given project. To override the :ref:`Global` configuration, you can declare a local
configuration.

In a local configuration, the commands are the same as in the :ref:`Global` configuration. The
one exception is that instead of using the ``--global`` flag, you use the ``--local`` flag.
Ensure that you run the commands in the root directory of your project and that a ``.git/``
folder exists.

If you would like to manually modify your local configuration, it is saved in
the ``.git/config`` file.

Dynamic
+++++++
It is possible to configure :ref:`Git` such that it selects between multiple
configuration profiles according to whether your project is located in your system.
This allows you to define common configurations for working under ``PyAnsys``,
``Ansys``, or open source projects from which the company benefits.

As an example, consider the following scenario for setting up two :ref:`Git`
configuration profiles for working with ``Ansys`` and personal projects.

Create the two files, naming them so that they are easily distinguishable. For
example, ``.gitconfig-ansys`` and ``.gitconfig-personal``. Then, use `Git
Conditional Includes
<https://git-scm.com/docs/git-config#_conditional_includes>`_ to control which
:ref:`Git` configuration is applied based on whether the project is located in
your system.

Each one of these files can look like this:

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


Signing commits
~~~~~~~~~~~~~~~
To verify which code changes were made by you, signing the commit
is required. To sign a commit, you must generate a ``GPG`` key, associate it with
``GitHub``, and specify it in your ``Git`` :ref:`Configuration`.

For an explanation of the process, in the ``GitHub`` documentation, see `Verify
Commit Signatures <https://docs.github.com/en/authentication/managing-commit-signature-verification>`_.


Enabling SSH
~~~~~~~~~~~~
Working with ``Secure Shell Protocol (SSH)`` is not only a good practice but
also required for contributing to PyAnsys projects. Without an ``SSH`` key,
you are not able to clone *internal* or *private* repositories or
to push new changes.

For information on setting up ``SSH`` with ``GitHub``, in the ``GitHub`` documentation,
see `Connecting to GitHub with SSH
<https://docs.github.com/en/authentication/connecting-to-github-with-ssh>`_.

Handling line endings
~~~~~~~~~~~~~~~~~~~~~
Every time you introduce a new line by pressing the **Enter** key, an invisible
character is introduced to represent a line ending. Each operating system manages
these end-of-line (EOL) characters in its own way. For Windows, the EOL is
also known as a `CRLF`, while in Linux it is known as a `LF`.

To avoid problems between developers working in the same repository but using
different operating systems, you can specify an EOL policy in a ``.gitattributes`` file.

In a ``.gitattributes`` file that you have committed to your repository, you can
customize the type of EOL characters that you expect developers to use. Git
then automatically manages these EOL characters so that developers do not
need to worry about them. Consider this example presented in `Configuring Git to handle line endings <https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings#example>`_:

.. code:: text

   # Set the default behavior, in case people don't have core.autocrlf set.
   * text=auto

   # Explicitly declare text files you want to always be normalized and converted
   # to native line endings on checkout.
   *.c text
   *.h text

   # Declare files that will always have CRLF line endings on checkout.
   *.sln text eol=crlf

   # Denote all files that are truly binary and should not be modified.
   *.png binary
   *.jpg binary


WSL2
----
Some developers prefer using Windows as the operating system for their machines.
However, they might like to take advantage of some features provided by a Linux
operating system. The `Windows Subsystem for Linux
<https://docs.microsoft.com/en-us/windows/wsl/install>`_ was devised to solve
this problem.

Installation
~~~~~~~~~~~~
Open a new PowerShell session and install the Windows Subsystem for Linux
(WSL) with:

.. code-block:: powershell

   wsl --install

After installing WSL, ensure that you are running the WSL2 version with:

.. code-block:: powershell

   wsl --set-default-version 2

Verification
~~~~~~~~~~~~
Verify your WSL version with:

.. code-block:: powershell

   wsl --list -v

Linux distribution
~~~~~~~~~~~~~~~~~~
After WSL2 is installed, install a Linux distribution.
Get a list of available distributions with:

.. code-block:: powershell

   wsl --list --online

Most developers choose `Ubuntu <https://ubuntu.com/download>`_ because it is a
well maintained Linux distribution with a huge collection of packages.

Install the Linux distribution of your choice with:

.. code-block:: powershell

   wsl --install -d <distribution name>

You can use this command to install multiple Linux distributions. Indicate
the distributions that you would like to use with WSL2 with:

.. code-block:: powershell
   
   wsl -d <distribution name>


Windows terminal
----------------
.. image:: images/windows_terminal.png
    :align: center
    :alt: The Windows Terminal with different active shell sessions.

.. raw:: html
    
    <br>

The `Windows Terminal <https://docs.microsoft.com/en-us/windows/terminal/>`_ is
an app that integrates multiple shells into a single console. Windows
ships by default with two shells: ``CMD`` and ``PowerShell``. If :ref:`WSL2` is
installed, a Linux shell is added. Hence, the goal of the ``Windows Terminal``
is to collect and manage all shell sessions in a single program. 

Installation
~~~~~~~~~~~~
You can install ``Windows Terminal`` directly from the `official Microsoft Store package
<https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-us&gl=US>`_.
