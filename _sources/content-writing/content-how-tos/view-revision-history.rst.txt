.. _View_revision_history:

View revision history on GitHub
===============================

GitHub *blame* is a feature that lets you view the revision history of a
file in a repository to see who made changes and when these changes were
made. You can use the GitHub blame feature for a variety of use cases, including
these:

- **Knowledge expansion**: When implementing something new or making changes in unfamiliar areas
  of the codebase, you can use GitHub blame to see how someone else implemented or changed
  something similar.
- **Code review**: When reviewing code changes, you can use GitHub blame to understand why
  specific lines were modified and by whom, making it easier to provide feedback or
  ask questions.
- **Debugging**: When you encounter a bug or an issue in the code, you can use GitHub blame
  to help identify when and where a particular piece of problematic code was introduced.
- **Accountability**: When you need to resolve disputes or track collaborations, you can use
  GitHub blame to see who made specific changes.

Here is how you use GitHub blame:

#. Navigate to a specific file in a GitHub repository.
#. To see the revision history for the entire file, click the **Blame** tab in the
   file header.
#. To go to the revision history for a particular line of code, on the **Code** tab,
   click this line number, and when the box with an ellipsis (``...``) appears, click
   this box and select **View git blame**.

   This takes you to the selected line on the **Blame** tab. However, you can always
   scroll to see the revision history for all lines in the file.

On the right side, you see how long ago a change was made to the file or a specific line,
who made the change, and the PR in which the change was made. Clicking the PR takes
you to it so that you can view all changes made to all files in the PR.
