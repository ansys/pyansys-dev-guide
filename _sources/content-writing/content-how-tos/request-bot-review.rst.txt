.. _bot_reviews:

Request a bot review
====================

You can have the `Ansys Review Bot <review_bot_>`_ perform a review of your changes.
If this bot is already turned on in your project, this comment from the bot
displays on the **Conversation** page of the PR::

    Thanks for opening a Pull Request. If you want to perform a review write a
    comment saying:

    @ansys-reviewer-bot review

.. note::
    If your project is in the Ansys internal account, the comment that you write
    is ``@ansys-internal-reviewer-bot review``. This topic assumes that you
    write ``@ansys-reviewer-bot review`` because your project is public.

If you do not see a comment from the bot but want to use it, email
`pyansys.core@ansys.com <pyansys_core_email_>`_ to request that they turn
the bot on in your project.

To use the bot:

#. Copy ``@ansys-reviewer-bot review`` from the bot's comment.
#. Scroll to the bottom of the page, paste this comment in the **Write** tab, and click **Comment**.

   The bot responds with this comment::

    Okay, I will trigger a review of your PR.

   Depending on how large your PR is, it may take a few minutes before comments
   from the bot begin to appear. If comments never appear, the bot service has
   likely stopped responding. You can email `pyansys.core@ansys.com <pyansys_core_email_>`_
   to request that they restart the service.

#. Resolve bot comments just like you resolve other reviewer comments. For more
   information, see :ref:`resolve_reviewer_comments`.

You can run the bot again when you next push changes to the PR.
