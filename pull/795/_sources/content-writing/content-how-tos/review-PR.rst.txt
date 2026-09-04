.. _review_pr:

Review a PR
===========

This page describes how to review a PR created by someone else. The
next page describes how to create your own PR.

When someone wants you to review a PR, this person generally tags you as a
reviewer on the PR. In the GitHub notification you receive, you can click the
link to go to the PR.

The simplest way to learn how to contribute to a project is to begin reviewing
PRs that other contributors have created. You can add suggestions in their PRs
for improving content, thereby build the confidence that you need to create your
own PRs.

Being an effective reviewer assumes that you are familiar with all the
resources listed in :ref:`resources_writers`.

.. _add_comments:

Add a comment
-------------

On the **Conversation** page of the PR, you can add a general comment on the
overall PR by scrolling to the bottom of the page, entering your comment in
the **Write** tab, and clicking **Comment**.

On the **Files changed** page of the PR, you can add a general comment on
a single changed line or multiple consecutive changed lines in a file. You can
also add a comment that suggests specific changes to a single line or multiple
consecutive lines.

If the PR includes changes to multiple files, the **Files changed** page has
two panes. The left pane displays a list of all changed files, and the right pane
displays the files themselves, with changes highlighted in green. To quickly
see the changes made to a particular file, click its entry in the left pane.

.. _add_comment_on_line:

Add a general comment on a line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add a general comment on a line:

#. Click the plus sign to the right of the line number.

   .. image:: ..//_static/GitHub-line-selector-suggestions.png
      :alt: Line selector

#. In the window that opens, type your comment.
#. Click **Add single comment** to add your comment and close the window.

Add a comment suggesting a change to a single line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add a comment suggesting a change to a single line:

#. Click the plus sign to the right of the line number.
#. In the window that opens, click the **Add a suggestion** icon:

   .. image:: ..//_static/icon-add-suggestion.png
      :alt: Add a suggestion icon

   GitHub copies the content of line, placing it in a ``suggestion`` tag in the
   window's **Write** tab. The suggestion tag begins and ends with triple
   backticks (:code:`\`\`\``) like this::

      ```suggestion
          This test shows how composite data can be stored.
      ```


#. Within the ``suggestion`` tag, edit the content to reflect your suggested
   changes.
#. If you want to provide any information about your suggested change, type it
   directly under the three backticks that close the ``suggestion`` tag::

      ```suggestion
          This test shows how composite data can be stored.
      ```
      Here is were you type information about your suggested change.

#. Click **Add single comment** to add your comment and close the window.

Add a comment suggesting changes to multiple lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add a comment suggesting changes to multiple consecutive lines:

#. Click the plus sign to the right of the first line number that you want to comment on
   and then drag the mouse to the last line number you want to comment on before
   releasing the mouse button.

   The selected lines are highlighted in yellow.

#. In the window that opens, click the **Add a suggestion** icon.

   GitHub places the content of the selected lines within a ``suggestion`` tag in
   the window's **Write** tab.

#. Within the ``suggestion`` tag, edit the content to reflect your suggested
   changes.
#. If you want to provide a comment about your suggested changes, type it
   directly under the three backticks that close the ``suggestion`` tag.
#. Click **Add single comment** to add your comment and close the window.

Submit your review
------------------

When you finish reviewing the PR, submit your review:

#. In the upper right corner of the GitHub window, click **Review changes** .

   The **Finish your review** window opens.

#. Leave a comment about your review.
#. Choose the **Comment**, **Approve**, or **Request changes** option.
#. Click **Submit review**.
