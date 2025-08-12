.. _code_blocks:

Code blocks
===========

You can introduce a short standalone code block in an RST file by ending a sentence with two
colons (``::``).

This example shows how to use this method to create a standalone code block.

.. tab-set::

    .. tab-item:: Doc surce code

        .. code-block:: rst

            This is a normal text paragraph in your RST file. The next paragraph is a code sample::
                
                A code sample is not processed in any way. In the documentation, it is rendered in
                a monsopaced font in a gray block.

                A code sample can span multiple lines.
 
            This is a normal text paragraph again.

    .. tab-item:: Rendered doc

        This is a normal text paragraph in your RST file. The next paragraph is a code sample:

        .. code-block:: rst

            A code sample is not processed in any way. In the documentation, it is rendered in
            a monsopaced font in a gray block.

            A code sample can span multiple lines.

        This is a normal text paragraph again.


In most cases, to create standalone code blocks that contain multiple lines of code,
you should use either the ``code`` or ``code-block`` directive. While you can use
these two directives interchangeably, the ``code-block`` directive offers more flexibility
and control over code block formatting.

Both the ``code`` and ``code-block`` directives support a ``language`` option
for specifying the programming language that the code is written in. When you specify
the language, the code block uses the syntax highlighting for this language.

This example shows a ``code-block`` directive for importing and using a Python function.

.. tab-set::

    .. tab-item:: Doc surce code

        .. code-block:: rst

            This ``code`` directive shows how to import a function (``my_function``)
            from a Python module (``mylibrary``) and then uses it.

            .. code-block:: pycon

               from mylibrary import my_function

               # Usage example
               result = my_function(42)
               print(result)

    .. tab-item:: Rendered doc

        This ``code`` directive shows how to import a function (``my_function``)
        from a Python module (``mylibrary``) and then uses it.

        .. code-block:: pycon

           from mylibrary import my_function

            # Usage example
            result = my_function(42)
            print(result)


This example shows a ``code-block`` directive for turning off a log handler.

.. tab-set::

    .. tab-item:: Doc surce code

        .. code-block:: rst

           This ``code-block`` directive shows how to turn off a log handler.

           .. code-block:: pycon

              for handler in design_logger.handlers:
                  if isinstance(handler, logging.FileHandler):
                      handler.close()
                      design_logger.removeHandler(handler)

    .. tab-item:: Rendered doc

        This ``code-block`` directive shows how to turn off a log handler.

        .. code-block:: pycon

           for handler in design_logger.handlers:
               if isinstance(handler, logging.FileHandler):
                   handler.close()
                   design_logger.removeHandler(handler)


Code blocks can include comments and message strings that you might need to edit.
Because comments and message strings are more often seen in PY files than in RST
files, see :ref:`py_code_comments_message_strings` in the section on PY files.

Number lines in a code block
----------------------------

You can use the optional ``linenos`` attribute to generate line numbers for a code block.

This example shows a ``code-block`` directive that uses the ``linenos`` attribute without
any value to generate line numbers for all lines.

.. tab-set::

    .. tab-item:: Doc surce code

        .. code-block:: rst

           This ``code-block`` directive shows to generate line numbers for all lines.

           .. code-block:: pycon
              :linenos:

              from __future__ import division
              import numpy

              def volume(height, radius):
                  pi = 3.14
                  vol = (1.0/3.0) * height * pi * pow(radius,2)
                  return vol

              vol = volume(2.0, 10)
              print vol, "(m^3)"

    .. tab-item:: Rendered doc

        This ``code-block`` directive shows to generate line numbers for all lines.

        .. code-block:: pycon
              :linenos:

              from __future__ import division
              import numpy

              def volume(height, radius):
                  pi = 3.14
                  vol = (1.0/3.0) * height * pi * pow(radius,2)
                  return vol

              vol = volume(2.0, 10)
              print vol, "(m^3)"


To set the line where numbering is to start, you use the optional ``lineno-start``
attribute, which automatically activates the ``linenos`` attribute.

This example shows a ``code-block`` directive that uses the ``lineno-start`` attribute to
start numbering at line 12.

.. tab-set::

    .. tab-item:: Doc surce code

        .. code-block:: rst

            This ``code`` directive numbers starts numbering at line 12.

            .. code-block:: pycon
               :lineno-start: 12

               Some more Python code, with line numbering starting at line 12.

    .. tab-item:: Rendered doc

        This ``code`` directive numbers starts numbering at line 12.

        .. code-block:: pycon
           :lineno-start: 12

           Some more Python code, with line numbering starting at line 12.


Emphasize lines of code
-----------------------

With the ``code-block`` directive, you can use the optional ``emphasize-lines`` attribute
to emphasize particular lines of code by highlighting them.

This example shows a ``code-block`` directive that emphasizes lines 3 and 5.

.. tab-set::

    .. tab-item:: Doc surce code

        .. code-block:: rst

            This ``code`` directive emphasizes lines 3 and 4.

            .. code-block:: pycon
               :emphasize-lines: 3,5

               def some_function():
                   interesting = False
                   print("This line is highlighted.")
                   print("This line is no highlighted.")
                   print("This line is highlighted.")

    .. tab-item:: Rendered doc

        This ``code`` directive emphasizes lines 3 and 4.

        .. code-block:: pycon
           :emphasize-lines: 3,5

            def some_function():
                interesting = False
                print("This line is highlighted.")
                print("This line is no highlighted.")
                print("This line is highlighted.")


Define a caption and name for referencing a code block
------------------------------------------------------
With the ``code-block`` directive, you can use the optional ``caption`` and ``name``
attributes to use either the ``ref`` or ``numref`` role to reference this code block from
elsewhere in your documentation.

This example shows a ``code`` directive that uses the ``caption`` and ``name`` attributes.

.. tab-set::

    .. tab-item:: Doc surce code

        .. code-block:: rst

            This ``code`` directive use the optional ``caption`` and ``name`` attributes.

            .. code-block:: pycon
               :caption: this.py
               :name: this-py

                print("Explicit is better than implicit.")

    .. tab-item:: Rendered doc

        This ``code`` directive use the optional ``caption`` and ``name`` attributes.

        .. code-block:: pycon
           :caption: this.py
           :name: this-py

            print("Explicit is better than implicit.")


You then give the ``name`` attribute to the ``numref`` role to create the cross-reference::

    For an example, see :numref:`this-py`.

If you only define the ``name`` attribute, you can use the ``ref`` role to create the
cross-reference providing that you explicitly provide the display text for the link::

    For an example, see :ref:`this code snippet <this-py>`.

Include code files
------------------

You can use the ``literalinclude`` directive to include a file containing plain
text as a code block in your documentation. For example, this directive includes a Python
file named ``example_code.py`` in your documentation::

    .. literalinclude:: example_code.py

Like the ``code-block`` directive, the ``literalinclude`` directive supports the
``linenos`` attribute to switch on line numbers, the ``lineno-start`` attribute
to set the line to start the numbering at, the ``emphasize-lines`` attribute to emphasize
particular lines, and the ``name`` attribute to provide an implicit target name.

For more information, see `Showing code examples <Sphinx_doc_directives_code_examples_>`_ in the
Sphinx documentation on directives.
