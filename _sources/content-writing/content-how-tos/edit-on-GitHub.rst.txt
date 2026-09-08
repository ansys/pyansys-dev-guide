.. _edit_on_GitHub:

Edit on GitHub
==============

The easiest way to contribute to a PyAnsys project is to make changes in GitHub,
letting the CI/CD process handle the build. When you are viewing PyAnsys
documentation, the right navigation pane might display an **Edit on GitHub** link.
You can use this feature to submit changes to this page by creating a PR on GitHub:

#. Click the **Edit on GitHub** link.

   The GitHub web editor opens with the **Edit** tab active by default.
   You can search within the file using **ctrl+F**.

#. Make suggested changes to the file.
#. When finished, in the top right corner of the window, click **Commit
   changes**.

   The **Propose changes** window opens.

#. Supply a commit message and an optional extended description.
#. Because you must create a new branch for committing this suggestion
   and creating the PR, supply a branch name.

   For PRs related to documentation, your branch name should begin with
   ``doc/`` followed by a descriptive name. For example, you might supply
   ``doc/fix_broken_link`` if that is what your suggested change does. For
   more information, see :ref:`branch_naming`.

#. Click **Propose changes**.

The PR is created, and the checks configured by the CI/CD process run. Your next
steps are basically the same as if you had created the PR from a cloned copy of
the repository:

#. Resolve failed checks.
#. Download and view documentation artifacts.
#. Tag reviewers.
#. Resolve reviewer comments.
#. Merge your PR.

For more information, see :ref:`create_pr`.

.. tip::
   If you need to make changes to other files as part of this PR, you can use
   your preferred GitHub tool to check out the branch and work in it.
