.. _resolve_failing_checks:

Resolve issues causing check failures
=====================================

All checks in the CI/CD process must pass before a PR can be approved and
merged. Even if you remember to run ``pre-commit`` and Vale locally and resolve
all issues, when you push your changes to the PR, checks in the CI/CD process
can still fail.

For information on continuous integration and the required workflows that run
checks on a PR for a PyAnsys library, see :ref:`continuous_integration`.

When a check in the CI/CD process fails, you can click **Details** to the right
of the check to view its log. You are taken to the bottom of the log, where you can see
the total number of warnings and errors.

While you can scroll the log to find these warnings and errors, the log can be quite
long. Use the **Search logs** option in the upper right of the window to search
first for ``warning`` and then for ``error``. (This sequence is recommended because
warnings and errors are often related.)

The first occurrence of ``warning`` in the log is a hint about how to suppress a
warning about the name of the initial branch of the repository. This is not
a warning included in the count to resolve and can be safely ignored. Subsequent
occurrences of ``warning``, and then ``error``, reveal the issues, with the filenames
and lines where you must resolve them.

Your objective should always be to eliminate or mitigate issues before creating
or pushing changes to a PR. For example, running ``pre-commit`` and Vale locally
lets you proactively resolve typos and trailing whitespaces. However,
oftentimes, you must resolve issues that cause the checks run by the CI/CD
process to fail.

Resolve typos
-------------

In PyAnsys projects, two tools in the CI/CD process check for typos,
`codespell <codespell_>`_ and `Vale <Vale_>`_. ``codespell`` is one
of the code style tools that ``pre-commit`` is configured to run. If
you always run ``pre-commit`` and ``Vale`` before creating or
pushing changes to a PR, these two checks in the CI/CD process
should not fail.

- For more information, see :ref:`run_precommit`.
- For more information, see :ref:`run_Vale_locally`.

.. note::
    If the **Vale** check on a PR fails, the **Documentation style** check also
    fails. Resolving the Vale issues might be all you need to do to get
    the **Documentation style** check to pass successfully.

Resolve trailing whitespaces
----------------------------

If you forget to run ``pre-commit`` locally, when you create or push
changes to a PR, the CI/CD process is likely to raise errors about
trailing whitespaces. Rather than locating and resolving these errors manually,
run ``pre-commit`` locally to have it find and automatically trim these trailing
whitespaces for you. Then, commit and push the files that ``pre-commit`` has modified
to the PR.

Resolve formatting issues
-------------------------

When you push changes to a PR, you might see one of the documentation checks fail,
even if you ran ``pre-commit`` locally and all configured tools ran successfully.
Documentation check failures are usually the result of formatting issues and
incorrect links, resulting in warnings and errors like these:

.. code::

    WARNING: Inline emphasis start-string without end-string.
    WARNING: Inline literal start-string without end-string.
    WARNING: document isn't included in any toctree
    WARNING: Literal block ends without a blank line; unexpected unindent.
    WARNING: Enumerated list ends without a blank line, unexpected unindent.
    WARNING: undefined label: 'py_file_formatting'
    WARNING: Duplicate explicit target name: "py_code_comments".
    ERROR: Unexpected indentation.
    ERROR: Unknown interpreted text role "files".
    ERROR: Indirect hyperlink target "numpydoc docstrings" refers to target "dev_guide_numpy_docstrings", which does not exist.
    ERROR: Unknown target name: "dev_guide_numpy_docstrings".


For each warning and error, a filename and line is indicated. You must go to these
locations and make the changes necessary to resolve the warnings and errors.
Actions that you might take include these:

- Add missing start or end strings to various types of format tags.
- Add a new RST file to the appropriate :file:`index.rst` file.
- Indent all lines in a literal block correctly.
- Add blank lines both before and after a list or literal block.
- Correct links to internal labels and external targets.


.. _resolve_too_long_lines_broken_links:

Resolve too long line lengths and broken links
----------------------------------------------

In PyAnsys projects, `Flake8 <Flake8_>`_ is a code style tool in the CI/CD process
that checks the quality of the Python code. When you run ``pre-commit`` locally,
Flake8 is one of the tools that it is configured to run. If Flake8 finds a line in a
Python file that is too long, it raises an error. Providing that this line is a
docstring or message string, you can manually change it in the PY file.

Sometimes, however, the line that is too long is for a URL added to the ``linkcheck_ignore``
variable in the Sphinx configuration (``doc/source/conf.py``) file. Here is an example of how
this can happen. The central links (``doc/source/links.rst``) file for this guide contains
explicit target names for joining the two Ansys GitHub accounts:

.. code::

    .. _join_ansys_organization: https://myapps.microsoft.com/signin/8f67c59b-83ac-4318-ae96-f0588382ddc0?tenantId=34c6ce67-15b8-4eff-80e9-52da8be89706
    .. _join_ansys_internal_organization: https://myapps.microsoft.com/signin/42c0fa04-03f2-4407-865e-103af6973dae?tenantId=34c6ce67-15b8-4eff-80e9-52da8be89706

When building documentation, Sphinx checks all links to ensure that they are valid. In most cases,
broken links are the result of formatting errors that you must fix manually. However, the
URLs for the preceding targets are behind firewall rules. Because Sphinx is unable to validate these links,
it indicates that they are broken. 

Because Sphinx is also unable to validate the ``38-comments-and-docstrings``
anchor in the following named target to a section in the *Google Python Style Guide*, it identifies it as broken:

.. code::

    .. _Google_docstrings: https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings

To resolve links that are identified as broken because they are behind firewall rules, you must add the
URLs (and any comments about these URLs) to the ``linkcheck_ignore`` variable in the Sphinx
:file:`config.py` file. To resolve links with anchors that are identified as broken, you must
add the anchor to the ``linkcheck_anchors_ignore`` variable in the Sphinx :file:`config.py` file.

Here is what adding these lines looks like:

.. code::

    # Linkcheck ignore too long lines

    linkcheck_ignore = [
        "https://myapps.microsoft.com/signin/8f67c59b-83ac-4318-ae96-f0588382ddc0?tenantId=34c6ce67-15b8-4eff-80e9-52da8be89706", # Join Ansys GitHub account
        "https://myapps.microsoft.com/signin/42c0fa04-03f2-4407-865e-103af6973dae?tenantId=34c6ce67-15b8-4eff-80e9-52da8be89706", # Join Ansys internal GitHub account
    ]

    # Linkcheck ignore broken anchors:

    linkcheck_anchors_ignore = [
        # these anchors are picked by linkcheck as broken but they are not.
        "38-comments-and-docstrings",
    ]

If you committed the preceding changes, Sphinx would no longer find any broken links. However, Flake8
would throw line length errors for the two lines that define the items for the ``linkcheck_ignore`` variable
in the Sphinx :file:`config.py` file. Because you cannot modify the length of these lines, you must follow
each of these URLs (and any comment about it) with a space and then ``# noqa: 501``.

You can scroll to the end of these lines to see how they now conclude with ``# noqa: 501``:

.. code::

    # Linkcheck ignore too long lines

    linkcheck_ignore = [
        "https://myapps.microsoft.com/signin/8f67c59b-83ac-4318-ae96-f0588382ddc0?tenantId=34c6ce67-15b8-4eff-80e9-52da8be89706", # Join Ansys GitHub account # noqa: 501
        "https://myapps.microsoft.com/signin/42c0fa04-03f2-4407-865e-103af6973dae?tenantId=34c6ce67-15b8-4eff-80e9-52da8be89706", # Join Ansys internal GitHub account # noqa: 501
    ]

When you commit these changes, Flake sees the ``# noqa: 501`` comments at the end of these lines
and knows to ignore their long line lengths.

.. _resolve_mismatched_message_strings:

Resolve mismatched message strings
----------------------------------

As indicated in :ref:`py_message_strings`, you want to ensure that the message
strings in PY files provide clear and understandable information or instructions
to users. Sometimes, editing a message string can cause a test on the PR to fail.
This occurs when a test checks for the occurrence of a particular message string,
but this message string is no longer found in the PY file.

When a test on a PR fails, you can click ``Details`` to the right of this test to
see the log. An error indicates that the message string in the test does not match
a message string in the PY file.

.. tip::
    To quickly find the error, you can use the **Search logs** option in the
    upper right of the window to search for ``match=``.

To resolve the error, you must open the indicated test file and edit the message
string in it to match the message string in the PY file.

.. todo::
  Find a test failure due to a message string mismatch to possible include an
  example and ensure the the information provided in this topic is correct.
