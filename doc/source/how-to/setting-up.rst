Setting Up Your Development Environment
=======================================
Before you can contribute to any ``PyAnsys`` project, you must set up
your developer environment.

Python
------
.. raw:: html
    
    <div align="center">
      <img src="https://github.com/python/pythondotorg/raw/main/static/community_logos/python-logo-inkscape.svg">
    </div>

All ``PyAnsys`` projects require a Python interpreter for interacting
with the software. Therefore, you must ensure that at least one Python
interpreter is installed on your local machine.

Installation
~~~~~~~~~~~~
There are multiple ways to install a Python package on your local machine:

- Use an official installer from the `official Python download section <https://www.python.org/downloads/>`_.
- Install via a package manager or "store" on your machine.

.. warning:: 

    Ensure that you install Python from an official channel. Do not trust
    third-party websites or download executable content from them.

.. tabs::

    .. group-tab:: Windows

        To install Python on a machine running Windows:
        
        1. Download the `latest stable Python version for Windows <https://www.python.org/downloads/windows/>`_.
        2. Execute the installer, referring to  `Using Python on
           Windows <https://docs.python.org/3/using/windows.html>`_ for
           detailed installation information.

    .. group-tab:: macOS

        To install Python on a machine running the macOS:
        
        1. Download the `latest stable Python version for macOS <https://www.python.org/downloads/macos/>`_.
        2. Execute the installer, referring to `Using Python on
           a Mac <https://docs.python.org/3/using/mac.html>`_ for
           detailed installation information.

        .. note::

            It is likely that your macOS distribution already comes with some
            version of Python installed. For more information, see :ref:`Verification`.

    .. group-tab:: Linux/UNIX

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

.. tabs::

    .. group-tab:: Windows

        .. tabs::

            .. group-tab:: CMD

                .. code-block:: text

                    py --version

            .. group-tab:: PowerShell

                .. code-block:: text

                    py --version

    .. group-tab:: macOS

        .. code-block:: text

            python --version

    .. group-tab:: Linux/UNIX

        .. code-block:: text

            python --version


Virtual Environments
--------------------
When working in multiple Python projects, it is likely each of these projects has its
own requirements. Sometimes, requirements across projects can be incompatible.
Virtual environments were devised to isolate Python environments, which guarantees
that you do not face dependency problems when working in multiple projects.

For information on the most fundamental commands for manipulating and
interacting with Python virtual environments, see the `official Python documentation on
the venv module <https://docs.python.org/3/library/venv.html>`_.

Check
~~~~~
Before creating a new virtual environment, you must run the following command
to check if you are already working with one:

.. tabs::

    .. group-tab:: Windows

        .. tabs::

            .. group-tab:: CMD

                .. code-block:: text

                    where.exe python

            .. group-tab:: PowerShell

                .. code-block:: text

                    where.exe python

    .. group-tab:: macOS

        .. code-block:: text

            which python

    .. group-tab:: Linux/UNIX

        .. code-block:: text

            which python

This command will return the path to your system's currently used Python environment. 

Ensure that it points to your default installation and not to a virtual
environment. If it points to a virtual environment, see :ref:`Deactivate` for
information on deactivating your virtual environment.

Create
~~~~~~
To create a virtual environment named `<venv>`, run this command:

.. tabs::

    .. group-tab:: Windows

        .. tabs::

            .. group-tab:: CMD

                .. code-block:: text

                    py -m venv <venv>

            .. group-tab:: PowerShell

                .. code-block:: text

                    py -m venv <venv>

    .. group-tab:: macOS

        .. code-block:: text

            python -m venv <venv>

    .. group-tab:: Linux/UNIX

        .. code-block:: text
            
            python -m venv <venv>

Usually, virtual environments are named ``venv`` or ``.venv``.

Activate
~~~~~~~~
To activate a virtual environment, run this command:

.. tabs::

    .. group-tab:: Windows

        .. tabs::

            .. group-tab:: CMD

                .. code-block:: text

                    <venv>\Scripts\activate.bat

            .. group-tab:: PowerShell

                .. code-block:: text

                    <venv>\Scripts\Activate.ps1

    .. group-tab:: macOS

        .. code-block:: text

            source <venv>/bin/activate

    .. group-tab:: Linux/UNIX

        .. code-block:: text

            source <venv>/bin/activate

Deactivate
~~~~~~~~~~
To deactivate a virtual environment, run this command:

.. tabs:: 

    .. group-tab:: Windows

        .. tabs::

            .. group-tab:: CMD

                .. code-block:: text

                    deactivate

            .. group-tab:: PowerShell

                .. code-block:: text

                    deactivate

    .. group-tab:: macOS

        .. code-block:: text

            deactivate

    .. group-tab:: Linux/UNIX

        .. code-block:: text

            deactivate


Git
---
.. raw:: html
    
    <div align="center">
      <img src="https://github.com/git/git-scm.com/raw/main/public/images/logo%402x.png">
      <br><br>
    </div>

`Git <https://git-scm.com/>`_ is an open-source version control system (VCS). It
is used to track changes and register new content in software-related projects. Git
will register the author and date of the changes so that accurate tracking of the
software's evolution is available.

Installation
~~~~~~~~~~~~

.. tabs::

    .. group-tab:: Windows

        To install Git on a machine running Windows:
        
        1. Download the `latest stable standalone Git version for Windows <https://www.python.org/downloads/win/>`_.
        2. Execute the installer and follow the installation steps.

    .. group-tab:: macOS

        To install Git on a machine running the macOS:
        
        1. Check the `latest stable Git version for macOS <https://git-scm.com/download/mac>`_.
        2. Run the installation command for your package manager.

    .. group-tab:: Linux/UNIX

        To install Git on a machine running Linux/UNIX:
        
        1. Check the `latest stable Git version for Linux/UNIX <https://git-scm.com/download/linux>`_.
        2. Run the installation command for your package manager.


Verification
~~~~~~~~~~~~
Once your installation process is complete, verify your Git installation by
running:

.. tabs:: 

    .. group-tab:: Windows

        .. tabs::

            .. group-tab:: CMD

                .. code-block:: text

                    git --version

            .. group-tab:: PowerShell

                .. code-block:: text

                    git --version

    .. group-tab:: macOS

        .. code-block:: text

            git --version

    .. group-tab:: Linux/UNIX

        .. code-block:: text

            git --version

Usage
~~~~~
If you are not familiar with Git, see the `Git Reference Manual <https://git-scm.com/doc>`_.
for comprehensive information on how to use it.

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
``/home/<username>/.gitconfig`` for macOS/Linux/UNIX users.

You can set the value for any variable in a field by running:

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
Sometimes, you may want to declare a specific configuration to be used only in a
project of your interest. To override the :ref:`Global` configuration, it is
possible to declare a local one.

Commands work the same as :ref:`Global` ones except that instead of the
``--global`` flag you need to use the ``--local`` flag. Make sure you run this
commands in the root directory of your project and that a ``.git/`` folder
exists.

If you would like to manually modify your local configuration, this is saved in
the ``.git/config`` file.

Dynamic
+++++++
It is possible to configure :ref:`Git` such that it selects between multiple
configuration profiles according to whether your project is located in your system.
This allows you to define common configurations for working under ``PyAnsys``,
``Ansys`` or open source projects from which the company benefits.

As an example, consider the following scenario for setting up two git
configuration profiles for working with ``Ansys`` and personal projects.

Create two files and name those such that you recognize which :ref:`Git`
configuration represent. For example, ``.gitconfig-ansys`` and
``.gitconfig-personal``. Finally, taking advantage of `Git Conditional Includes
<https://git-scm.com/docs/git-config#_conditional_includes>`_, it is possible to
control which :ref:`Git` configuration will be applied depending on whether the
project is located in your system:

Each one of these files may look like this:

.. tabs::

    .. tab:: .gitconfig

        .. code-block:: text

            [includeIf "gitdir:path/to/your/ansys/folder/of/projects"]
              path = path/to/.gitconfig-ansys

            [includeIf "gitdir:path/to/your/personal/folder/of/projects"]
              path = path/to/.gitconfig-personal


    .. tab:: .gitconfig-ansys

        .. code-block:: text

            [user]

              name = <Ansys Name>
              email = <Ansys Email>
              signingkey = <Ansys GPG Key>


    .. tab:: .gitconfig-personal

        .. code-block:: text

            [user]

              name = <Name or Nickname>
              email = <Personal Email>
              signingkey = <Personal GPG Key>


Signing Commits
~~~~~~~~~~~~~~~
To verify that some code changes were actually made by you, signing the commit
is required. To do so, you will need to generate a ``GPG`` key, associate it with
``GitHub`` and specify it in your ``Git`` :ref:`Configuration`.

The whole process is explained in the ``GitHub`` documentation chapter `Verify
Commit Signatures
<https://docs.github.com/en/authentication/managing-commit-signature-verification>`_.


Enabling SSH
~~~~~~~~~~~~
Working with ``Secure Shell Protocol (SSH)`` is not only a good practice but
also required for contributing to ``PyAnsys`` projects. Without an ``SSH`` key,
you will not be able to clone ``internal`` or ``private`` repositories neither
to push new changes.

The whole process for setting up ``SSH`` with ``GitHub`` is explained in
`Connecting to GitHub with SSH
<https://docs.github.com/en/authentication/connecting-to-github-with-ssh>`_.


WSL2
----
Some developers prefer using Windows as the operating system for their machines.
However, they may like to take advantage of some features provided by a Linux
operating system. The `Windows Subsystem for Linux
<https://docs.microsoft.com/en-us/windows/wsl/install>`_ was devised to solve
this problem.

Installation
~~~~~~~~~~~~
Open a new PowerShell session and run the following command:

.. code-block:: powershell

   wsl --install

After installing ``WSL``, ensure that you are running the ``WSL2`` version with:

.. code-block:: powershell

   wsl --set-default-version 2

Verification
~~~~~~~~~~~~
To verify your ``WSL`` version, run:

.. code-block:: powershell

   wsl --list -v

Linux Distribution
~~~~~~~~~~~~~~~~~~
After ``WSL2`` is installed, install a Linux distribution.
To get a list of available distributions, run:

.. code-block:: powershell

   wsl --list --online

Most developers choose `Ubuntu <https://ubuntu.com/download>`_ because it is a
well maintained Linux distribution with a huge collection of packages.

To install the Linux distribution of your choice, run:

.. code-block:: powershell

   wsl --install -d <distribution name>

You can use this command to install multiple Linux distributions. To indicate
the distribution that you would like to use to ``WSL2``, run:

.. code-block:: powershell
   
   wsl -d <distribution name>


Windows Terminal
----------------
.. image:: images/windows_terminal.png
    :align: center
    :alt: The Windows Terminal with different active shell sessions

.. raw:: html
    
    <br>

The `Windows Terminal <https://docs.microsoft.com/en-us/windows/terminal/>`_ is
an application that integrates multiple shells into a single console.  Windows
ships by default with two shells (``CMD`` and ``PowerShell``). If :ref:`WSL2` is
installed, a Linux shell is added.  Hence, the goal of the ``Windows Terminal``
is to collect and manage all shell sessions in a single program. 

Installation
~~~~~~~~~~~~
You can install ``Windows Terminal`` from the `official Microsoft Store package
<https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-us&gl=US>`_
directly from the Windows Store.
