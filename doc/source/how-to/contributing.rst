Contributing
============
This page explains how PyAnsys development is conducted. When contributing to a
PyAnsys repository, use these general coding paradigms:

#. Follow the `Zen of Python <https://www.python.org/dev/peps/pep-0020/>`__.
   As silly as core Python developers are sometimes, there's much to be
   gained by following the basic guidelines listed in PEP 20. As suggested
   in these guidelines, focus on making your additions intuitive, novel,
   and helpful for PyAnsys users. When in doubt, use ``import this``.
   For Ansys code quality standards, see :ref:`Coding Style`.

#. Document your contributions. Include a docstring for any added function,
   method, or class, following :ref:`Numpydoc Docstrings`, as specified by
   PyAnsys :ref:`Documentation Style`. Always provide at least one simple use
   case for a new feature.

#. Test your contribution. Because Python is an interpreted language, if
   it's not tested, it's probably broken. At the minimum, include a unit
   test for each new feature within the ``tests`` directory. Ensure that
   each new method, class, or function has a reasonable (>80%) coverage.
   See :ref:`Testing` for automating testing.

#. Do not include any datasets for which a license is not available
   or commercial use is prohibited.

#. Review our `Code of Conduct
   <https://github.com/pyansys/.github/blob/main/CODE_OF_CONDUCT.md>`_.


All ``PyAnsys`` projects are hosted in `GitHub <https://www.github.com/>`_ in
the form of :ref:`Git` repositories. GitHub is a platform not only provides
storage for projects but also additional features like code reviews or issue
boards.

.. raw:: html

     <br>
     <div align="center">
       <img width="50%;" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Logo.png">
     </div>


Creating a GitHub account
-------------------------
To use GitHub, start by creating a new account in the platform. Follow the
`GitHub Join Process <https://github.com/join>`_. If you require access to the
`PyAnsys Organization <https://github.com/pyansys>`_, refer to `Alexander
Kaszinsky <mailto:alexander.kaszinsky@ansys.com>`_.

GitHub Repository Sections
--------------------------

Once you have a GitHub account and access granted to the `PyAnsys` organization,
you will be able to interact with the different repositories. All the
repositories contain the following sections:

.. figure:: images/github_sections.png
   :alt: GitHub repository sections
   :align: center

* ``Code``: a tree view of the project's structure.
* ``Issues``: the issue and feature request board.
* ``Pull requests``: a board collecting new changes to be merged.
* ``Discussions``: dialogs about development practices to be used by project maintainers.
* ``Actions``: the CI/CD panel showing the different available workflows.
* ``Projects``: a panel for organizing and planning development in the repository.
* ``Wiki``: devoted to show quick information of the project.
* ``Security``: configurations related to security issues, vulneravilities and alerts.
* ``Insights``: generic information about the repository and its contributors.
* ``Settings``: allows to configure access and integration with third party tools.

.. note:: 

   Depending on your access level, you may not be able to see some of the
   previous sections.

Creating an Issue
-----------------
Issues are the way of requesting for help, a new feature or reporting a bug.
They act like small posts including a comments section. This last section allows
you to interact with other users, developers and project maintainers.

To open an issue, check the ``Issues`` section in the :ref:`GitHub Repository
Sections` and click ``New Issue``. GitHub issues require the usage of Markdown
instead of RST. You can check `Basic Writing and Formatting Syntax
<https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax>`_
for this language.

Requesting New Features
~~~~~~~~~~~~~~~~~~~~~~~
If you would like a new feature to be included in the software, you can create a
new issue. When requesting a new feature, it is interesting that you include the
following sections:

- Describe the main goal of the feature to be included and why it is bennefitial
  to the project.

- If possible, describe how it could get implemented and which steps should be
  followed.

- Add any references which could help during the development process.


Reporting Bugs
~~~~~~~~~~~~~~
If you encounter some bug in your code, you can create a new issue to request a
fix. When reporting a bug try to include the following data:

- Indicate your operating system, Python version and the version of the library
  you are using.

- Include a small piece of code to allow others to reproduce the bug you found.

- Any additional data you consider useful for fixing the bug.


Forking a Repository
--------------------
Forking a repository is like copy-pasting a project into your own GitHub
profile. Notice that only ``public`` labeled repositories can be forked. Those
labeled as ``internal`` or ``private`` cannot be forked.

To fork a repository click in the ``Fork`` button at the top of the project's
page you wish to fork.


Cloning a Repository
--------------------
Cloning a repo means downloading it to your local machine. There two ways of
doing this: using ``HTTPS`` or ``SSH``. To force the usage of ``SSH``, only this
method is exaplined in here.

Cloning using SSH
~~~~~~~~~~~~~~~~~
Cloning using ``SSH`` requires you :ref:`Enabling SSH`. After that, you can
clone a repository by running:

.. code-block:: bash

    git clone git@github.com:<user>/<repository-name>.git

For example, to clone the `PyMAPDL <https://github.com/pyansys/pymapdl/>`_
project, you just need to run:

.. code-block:: bash

    git clone git@github.com:pyansys/pymapdl.git


Installing in Editable Mode 
---------------------------
It is possible to install a Python library in so-called "editable mode". This
allows you to modify the source code and reflect these new changes in your
Python environment.

To install a Python library in editable mode follow these steps:

1. Make sure you :ref:`Create` and :ref:`Activate` a Python virtual environment,
   as explained in the :ref:`Virtual Environments` section.

2. Update `pip` by running:

   .. code-block:: bash

       python -m pip install --upgrade pip

3. Install the library using:

   .. code-block:: bash

       python -m pip install --editable .


Creating a New Branch
---------------------
It is likely that the default branch name is ``main`` or ``master``. This is the
development branch, considering the :ref:`Branching Model` followed in PyAnsys
projects. 

New contributions need to be implemented in a different branch. Then, these
changes are merged into ``main`` by :ref:`Creating a Pull Request`. To create a
new branch run:

.. code-block:: bash

    git checkout -b <new branch name>

Branch Naming Conventions
~~~~~~~~~~~~~~~~~~~~~~~~~
To streamline development, we have the following requirements for naming
branches. These requirements help core developers know what kind of
changes any given branch is introducing before looking at the code.

-  ``fix/``: any bug fixes, patches, or experimental changes that are
   minor
-  ``feat/``: any changes that introduce a new feature or significant
   addition
-  ``junk/``: for any experimental changes that can be deleted if gone
   stale
-  ``maint/``: for general maintenance of the repository or CI routines
-  ``doc/``: for any changes only pertaining to documentation
-  ``no-ci/``: for low-impact activity that should not trigger the CI
   routines
-  ``testing/``: Improvements or changes to testing
-  ``release/``: Releases (see below)


Pushing a New Branch
--------------------
Once you have implemented new changes and committed those, you need to push your
branch. Pushing a branch means uploading your changes to the repository. These
changes will only be seen by the branch you just created.

.. code-block:: bash

   git push -u origin <new branch name>

Creating a Pull Request
-----------------------
Once you have tested your branch locally, create a PR and target your merge to
``main``. This will automatically run CI testing and verify that your changes
will work across all supported platforms. A detailed guideline of the process is
collected under the `Creating a pull request
<https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`_
section in the GitHub documentation.

For code verification, someone from the PyAnsys development team will review
your code to verify that it meets the :ref:`Packaging Style`, :ref:`Coding
Style`, :ref:`Documentation Style`.

Once your code is approved, if you have write permission, you may merge the PR
branch. If you don't have write permission, the reviewer or someone else with
write permission will merge your PR and then delete your PR branch.

.. admonition:: Always delete your PR branch after merging it into main branch

   Deleting merged branches is a good practice which ensures that origin
   branches do not get cluttered. Automatic deletion of branches can be setup in
   ``Settings -> General -> Pull Requests`` section.


Using GitHub CLI
----------------
Developers may find useful not leaving the terminal when working in a project.
For this reason, `GitHub CLI <https://cli.github.com/>`_ was devised.

This program allows you to interact with most of the features available in the
web version of Github. A full list of the available commands is provided in the
`official GitHub CLI manual <https://cli.github.com/manual/gh>`_.
