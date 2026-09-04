.. _py_code_comments_message_strings:

Code comments and message strings
=================================

Python files often contain code comments and message strings.

- Code comments provide information to make the code more readable and maintainable.
- Message strings display information to users. Developers can also use message
  strings for debugging purposes to better understand the flow of the code.

.. _py_code_comments:

Code comments
-------------

Developers know that adding comments to code is a good practice when logic
might be hard to understand at first glance. They also know to avoid over-commenting
or writing comments that explain the obvious.

A code comment starts with the hash character (``#``) and a single space. It extends to
the end of the physical line. At least two spaces should separate the code from the comment.

While the code comments in PY files are not visible to users of the library. they are visible
to contributors of the library. Thus, when reviewing PY files, make suggestions for correcting
misspelled words and bad grammar.

You can also make suggestions for formatting code comments consistently. For example, you
might suggest starting all code comments in a PY file with a simple verb that always begins
with an uppercase letter. You might also suggest always concluding all code comments within
a code block with a period (``.``). Or, you might suggest that only code comments containing
multiple sentences should conclude with a period. Your objective is to ensure that code comments
within a code block are well written and consistently formatted.

.. _py_message_strings:

Message strings
---------------

Developers can create a simple message by assigning to a variable a text string that
is enclosed in either two single (``''``) or two double (``""``) quotation marks. They can
create a multi-line message using triple (``"""``) quotation marks like those used
for docstrings. Additionally, developers can perform other operations on strings,
such as concatenation, interpolation, slicing, and formatting.

Whenever possible, use double quotation marks to surround a message string.
If you need to use quotation marks inside the message string, then use single quotation marks.
The only exception is if you need to use double quotations inside the message string to
specify possible options that are string values. In this case, use single quotation
marks to surround this line and double quotation marks for other options::

  message=(
      "Conductor type is invalid. " \
      'Options are "SIGNAL", "POWER", and "SUBSTRATE".'
  )

When reviewing PY files, you want to ensure that message strings are clear
and concise so that users can easily understand the information or instructions
that they provide.

You should always ensure that a message string is a complete sentence
with a concluding period. Message strings should not conclude with an exclamation
point (``!``) or use the word *please*.

Because tests written for a PyAnsys project might check that a particular message
is shown, making changes to a message string could necessitate you having to also update
any test that checks for it. For more information, see :ref:`resolve_mismatched_message_strings`.
