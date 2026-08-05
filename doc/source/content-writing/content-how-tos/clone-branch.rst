.. _clone_branch:

Clone and branch a repository
=============================

This page describes how to clone (download) a GitHub repository and then provides
conceptual information on how you use your Git tool to create a local branch where
you modify or add to the codebase, eventually submitting your suggested changes in
a PR to the GitHub repository. For Git-related procedural information, see the
documentation for your preferred Git tool.

.. _clone_repo:

Clone a repository
------------------

Before you can contribute to a PyAnsys project, you must clone the GitHub
repository.

#. Copy the URL for the repository.
#. If the Ansys Python Manager and the **Administrator** window are not
   open, open them. For more information, see :ref:`Ansys_Python_Manager`.
#. In the **Administrator** window, use the ``cd`` command to go to the
   directory where you want to clone the repository.

   For example, run a command like this one::

      cd C:\AnsysDev\GitRepos\PyAnsys

#. Run this ``git`` command, where ``<url>`` is the URL for the repository::

      git clone <url>

   For example, run a command like this one::

      git clone https://github.com/ansys/pymechanical

.. _pull_from_repo:

Pull changes from the main branch on GitHub
-------------------------------------------

Once you have a clone of the repository, before creating a local branch to work
in, ensure that you have the latest codebase. Using your Git tool, pull changes
from the remote main branch on GitHub into the main branch of your locally cloned
repository.

.. _create_local_branch:

Create a local branch
---------------------

Once your clone of the repository is up to date, use your Git tool to create a local
branch to make changes in. For changes related to documentation, your branch name
should begin with ``doc/`` followed by a descriptive name. For example, you might
name your branch ``doc/overall_review`` if that describes your suggested changes.
You might name your branch ``doc/hfss_py_edits`` if your are suggesting changes
to that particular PY file. For more information on naming branches, see
:ref:`branch_naming`.

.. _commits_pulls:

Commit local changes and pull remote changes
--------------------------------------------

As you work in your local branch, periodically commit your changes and
pull changes from the remote main branch to ensure that no changes
there conflict with changes that you have made in your local branch. If conflicts do exist,
resolve them in your local branch before pushing your changes to a PR.

.. _push_changes:

Push changes to a PR
--------------------

When you are ready to push your changes to a PR, first pull changes again
from the remote main branch to your local branch. Providing that there are no
conflicts to resolve, push your changes to create a PR or add to an existing
PR. For more information, see :ref:`create_pr`. Ensure that all checks run by
the CI/CD process are successful. If any checks fail, see :ref:`resolve_failing_checks`.
