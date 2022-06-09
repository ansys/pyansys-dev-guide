Contributing
============
Before contributing to a PyAnsys repository, you must understand the general
coding paradigms being used for PyAnsys development.

#. Follow the `Zen of Python <https://www.python.org/dev/peps/pep-0020/>`__.
   As silly as core Python developers are sometimes, there's much to be
   gained by following the basic guidelines listed in PEP 20. As suggested
   in these guidelines, focus on making your additions intuitive, novel,
   and helpful for PyAnsys users. When in doubt, use ``import this``.
   For Ansys code quality standards, see :ref:`Coding Style`.

#. Document your contributions. Include a docstring for any added function,
   method, or class, following :ref:`Numpydoc Docstrings` as specified by
   PyAnsys :ref:`Documentation Style`. Always provide at least one simple use
   case for a new feature.

#. Test your contribution. Because Python is an interpreted language, if
   it's not tested, it's probably broken. At the minimum, include a unit
   test for each new feature within the ``tests`` directory. Ensure that
   each new method, class, or function has a reasonable (>80%) coverage.
   For information about automated testing, see :ref:`Testing`.

#. Do not include any datasets for which a license is not available
   or commercial use is prohibited.

#. Review our `Code of Conduct
   <https://github.com/pyansys/.github/blob/main/CODE_OF_CONDUCT.md>`_.


All ``PyAnsys`` projects are hosted in `GitHub <https://www.github.com/>`_ in
the form of :ref:`Git` repositories. GitHub is a platform that not only provides
storage for projects but also additional features like code reviews or issue
boards.

.. raw:: html

     <br>
     <div align="center">
       <img width="50%;" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Logo.png">
     </div>


Creating a GitHub account
-------------------------
To use GitHub, start by creating an account for the platform. Follow the
`GitHub Join Process <https://github.com/join>`_. If you require access to the
`PyAnsys Organization <https://github.com/pyansys>`_, email your request to `Alexander
Kaszinsky <mailto:alexander.kaszinsky@ansys.com>`_.

GitHub Repository Sections
--------------------------

Once you have a GitHub account and access to the `PyAnsys` organization,
you will be able to interact with the different repositories. While each
repository contains all tabbed sections that are shown and described below,
your access level determines tabbed sections you can see.

.. figure:: images/github_sections.png
   :alt: GitHub repository sections
   :align: center

* ``Code``: Tree view of the project's structure
* ``Issues``: Posts noting issues or requesting new features
* ``Pull requests``: Code changes either awaiting review or merging or already closed
* ``Discussions``: Exchanges about development practices with project maintainers
* ``Actions``: Available CI/CD workflows
* ``Projects``: Plans for organizing and developing the repository
* ``Wiki``: Basic project information
* ``Security``: Configurations related to security issues, vulnerabilities, and alerts
* ``Insights``: General information about the repository and its contributors
* ``Settings``: Configurations for access and integration with third-party tools

Creating an Issue
-----------------
You create an issue to either report a bug or request help or a new feature. Commenting
allows you to interact with other users, developers, and project maintainers.

To open an issue, select the ``Issues`` tab in the :ref:`GitHub Repository
Sections` and click ``New Issue``. Then, select a template for the type of issue
to open.

GitHub issues require the usage of Markdown files instead of ReStructured Text
files. For more information, see `Basic Writing and Formatting Syntax
<https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax>`_.

Requesting New Features
~~~~~~~~~~~~~~~~~~~~~~~
If you would like a new feature to be added to a PyAnsys library, you open a
new issue and select either the template for code enhancements or a
feature idea. In the issue, you then do the following:

- Describe the main goal of the feature that you'd like to have added and why it is beneficial
  to the project.

- Describe how this feature might possibly be implemented and the steps that should be
  followed.

- Add any references that could help during the development process.


Reporting Bugs
~~~~~~~~~~~~~~
If you encounter a bug in the code, you open a new issue and select the template
for creating a bug report. In the bug report, try to:

- Indicate the operating system, Python version, and library version that you are using.

- Include a small piece of code to allow others to reproduce the bug you found.

- Add any additional information that you consider useful for fixing the bug.


Forking a Repository
--------------------
Forking a repository is like copying and pasting a project into your own GitHub
profile. Notice that only ``public`` labeled repositories can be forked. You
cannot fork a repository labeled as ``internal`` or ``private``.

To fork a repository, click the ``Fork`` button at the top of the project's
``Code`` tabbed section.


Cloning a Repository
--------------------
Cloning a repository means downloading it to your local machine. While there are two ways of
doing this (``HTTPS`` or ``SSH``), to force the usage of ``SSH``, only this method is explained.

Cloning Using SSH
~~~~~~~~~~~~~~~~~
Cloning using ``SSH`` requires :ref:`Enabling SSH`. After that, you can
clone a repository by running:

.. code-block:: bash

    git clone git@github.com:<user>/<repository-name>.git

For example, to clone the `PyMAPDL <https://github.com/pyansys/pymapdl/>`_
project, run:

.. code-block:: bash

    git clone git@github.com:pyansys/pymapdl.git


Installing in Editable Mode 
---------------------------
You can install a Python library in "editable mode", which
allows you to modify the source code and have these new changes
reflected in your Python environment.

To install a Python library in editable mode:

1. Ensure that you :ref:`Create` and :ref:`Activate` a Python virtual environment,
   as explained in the :ref:`Virtual Environments` section.

2. Update `pip` with:

   .. code-block:: bash

       python -m pip install --upgrade pip

3. Install the library with:

   .. code-block:: bash

       python -m pip install --editable .


Creating a Branch
-----------------
It is likely that the default branch name is ``main`` or ``master``. This is the
development branch for PyAnsys projects. For more information, see :ref:`Branching Model`. 

You must implement new contributions in a different branch and then merge
these changes into the ``main`` branch by :ref:`Creating a Pull Request`.

You create a branch with:

.. code-block:: bash

    git checkout -b <new branch name>

Branch Naming Conventions
~~~~~~~~~~~~~~~~~~~~~~~~~
The following requirements for naming branches helps to streamline
development. They help core developers know what kind of
changes any given branch is introducing before looking at the code.

-  ``fix/``: Bug fixes, patches, or experimental changes that are
   minor
-  ``feat/``: Changes that introduce a new feature or significant
   addition
-  ``junk/``: Experimental changes that can be deleted if they go
   stale
-  ``maint/``: General maintenance of the repository or CI routines
-  ``doc/``: Changes pertaining only to documentation
-  ``no-ci/``: Low-impact activity that should not trigger CI
   routines
-  ``testing/``: Improvements or changes to testing
-  ``release/``: Releases (see below)


Pushing a New Branch
--------------------
Once you have implemented new changes and committed them, you push your
branch, which uploads your changes to the repository. These changes are only
visible in the branch that you just pushed.

.. code-block:: bash

   git push -u origin <new branch name>

Creating a Pull Request
-----------------------
Once you have tested your branch locally, create a pull-request (PR) and target your merge to
``main``. This will automatically run CI testing and verify that your changes
will work across all supported platforms. For detailed procedural information, see `Creating a pull request
<https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`_
in the GitHub documentation.

After you submit your pull request, someone from the PyAnsys development team will review
your code to verify that it meets the :ref:`Packaging Style`, :ref:`Coding
Style`, and :ref:`Documentation Style`.

Once your code is approved, if you have write permission, you may merge the PR
and then delete the PR branch. If you don't have write permission, the reviewer or someone else with
write permission will merge your PR and then delete your PR branch.

.. admonition:: Always delete your PR branch after merging it into the main branch.

   You can set up automatic deletion
   of branches in ``Settings -> General -> Pull Requests``.

Using GitHub CLI
----------------
Because developers find not leaving their terminals useful when working in projects,
`GitHub CLI <https://cli.github.com/>`_ was devised.

This program allows you to interact with most of the features available in the
web version of Github. For a full list of available commands, see the
`official GitHub CLI manual <https://cli.github.com/manual/gh>`_.
