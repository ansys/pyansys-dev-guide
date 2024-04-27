.. _rst_formatting_rules:

RST formatting rules
====================

This page provides a summary of RST formatting rules to help you ensure that your
PyAnsys documentation renders correctly. For a summary of the most important
writing guidelines, frequently review the `Highlights <Google_dev_doc_highlights_>`_
page in the *Goggle developer documentation style guide*.

- Use sentence case for headings and titles in PyAnsys documentation, as specified
  in `Headings and titles <Google_dev_doc_headings_>`_ in the *Google developer
  documentation style guide*.

- Underline (and optionally overline) titles to indicate the heading hierarchy.
  The string of characters indicating the title level should be the same length
  as the title and must be at least as long as the title. You should have only
  one top-level heading per RST file. For consistency within PyAnsys libraries,
  the use of these characters is recommended but not enforced:

  - For section-level headings, use ``###``.
  - For subsection-level headings, use ``===``.
  - For subsubsection-level headings, use ``---``.
  - For subsubsubsection-level headings, use ``~~~``.
  - For paragraph-level headings, use ``+++``.

- Use blank lines to separate text into paragraphs.

- Ensure that there are no blank spaces at the end of a line. (Running ``pre-commit``
  finds and removes any trailing white spaces, saving you from seeing errors
  when you create or push changes to a PR. For more information, see :ref:`run_precommit`.)

- As in Python, indentation is significant. All lines of the same paragraph must be left-aligned to the
  same level of indentation. Use spaces (and not tabs) for indentation.

- Do not exceed the maximum number of characters per line specified for your PyAnsys
  library. While the `Style guide for Sphinx-based documentation <Style_guide_Sphinx_doc_>`_
  indicates that lines should be limited to a maximum of 79 characters, many PyAnsys
  libraries extend this limit, sometimes to as many as 120 characters, because
  today's larger screens can support longer lines.

- Use standard American spelling and punctuation.

- Use ``you`` and ``your`` rather then ``we`` and ``our``.

- Omit the word "please" and replace the phrase "In order to" with "To."

- Italicize a word or phrase by surrounding it in a single asterisk (``*``) or a
  single backtick (:code:`\``). In PyAnsys documentation, the following are italicized: words
  or phrases to be emphasized, first occurrence of a new term, and a publication title
  that is not a link.

- Bold a word or phrase by surrounding it in double asterisks (``**``). In PyAnsys
  documentation, the following are in bold: words or phrases to be strongly
  emphasized and GUI (graphical user interface) components.

- Separate lists from paragraphs with blank links. Begin each item in a bulleted list
  with either a ``-`` or ``*`` followed by a space. Begin each item in a numbered
  list with ``#.`` followed by a space. While nested lists are supported, you must
  separate them from parent list items with blank lines and indent them appropriately.

- For a horizontal list, use the ``hlist`` directive. This directive
  specifies that list items are to display horizontally in three columns::

    .. hlist::
       :columns: 3

       * List item 1
       * List item 2
       * List item 3
       * List item 4
       * List item 5

  This is how the preceding list items, which are in a sublist, are rendered in the
  documentation:

  .. hlist::
     :columns: 3

     * List item 1
     * List item 2
     * List item 3
     * List item 4
     * List item 5

- Indicate a code entity within text by surrounding it in double backticks
  (:code:`\`\``). While the `numpydoc Style guide <numpydoc_style_guide_>`_
  says to surround a code entity in a single backtick, this renders it incorrectly
  as italics in PyAnsys documentation. Surrounding it in double backticks
  correctly renders it in a monospaced font within a gray block.

  Always follow a code entity with a noun that indicates the object type. For general
  guidelines, see `Code in text <Google_dev_doc_code_in_text_>`_ in the *Google developer
  documentation style guide*. 
  
  Code entities include the names of Python objects, such as packages, modules, functions,
  classes, methods, and attributes. Code entities also include the following objects:

  - File paths
  - Names of directories, files, and environment variables
  - Text to type in a command line or in a GUI component
   
  .. note::
    Some PyAnsys projects use the ``file`` and ``envvar`` interpretive text
    roles for names of files and environment variables:

    - :file:`myfile.txt`
    - :envvar:`MY_ENVAR`

    Roles insert semantic markup in your source files for cross-references to named
    targets of the type indicated by the role. Because the CSS for the
    `Ansys Sphinx Theme <Ansys_Sphinx_theme_repo_>`_ assigns the same semantic markup to
    the ``file`` role as it does to a filename surrounded in double backticks, it
    does not matter which markup you use.

- Use the ``code`` role to format text as a code entity if surrounding the text in double
  backticks is problematic because it contains characters that cause regular
  expression errors. For example, in this sentence describing the use of double backticks,
  the ``code`` role had to be used to format the double backticks as a code entity::

    Indicate a code entity within a paragraph by surrounding it in double backticks
    (:code:`\`\``).

  If you want, you can use the ``code`` role within any sentence to identify small
  pieces of inline code, individual identifiers (like function names or variable names),
  or inline code phrases. Most of the time though, using double backticks is easier.

- To create a standalone code block within your documentation, use either the
  ``code`` or ``code-block`` directive. For more information on code blocks,
  see :ref:`code_blocks`.

- To comment out lines in an RST file so that they do render in the documentation,
  place two periods (``..``) and a space before each line that you want to hide::

    .. When content is drafted on reusable RST files, add the topic here.
    .. Also add links to this new topic in the ``documenting.rst" file.

  While this approach is useful if the native ``sphinx.ext.todo`` extension has not been
  added to the ``extensions`` variable in your documentation's Sphinx configuration
  (``doc/source/conf.py``) file, adding this extension is recommended. The specially
  formatted block of text for the ``.. todo::`` directive does not render in the
  documentation by default. Plus, you can easily search for occurrences of this directive
  later. For more information, see :ref:`add_native_sphinx_ext`.

Subsequent pages describe how to use other common Sphinx roles and directives. For
comprehensive lists of roles and directives, see `Roles <Sphinx_doc_roles_>`_ and
`Directives <Sphinx_doc_directives_>`_ in the Sphinx documentation.
