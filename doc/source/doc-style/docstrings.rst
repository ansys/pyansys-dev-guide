.. _numpy_docstrings:

Numpydoc docstrings
===================

When writing docstrings for PyAnsys libraries, follow the syntax and best practices
described in `Style guide <numpydoc_style_guide_>`_ in the *numpydoc Manual*.

For consistency within PyAnsys libraries, always use ``"""`` to introduce and conclude a
docstring, keeping the line length shorter than 70 characters. Ensure that there are
no blank spaces at the end of a line because they cause errors in build checks that you
must then resolve.

A blank line signifies the start of a new paragraph. To create a bulleted or numbered list,
ensure that there is a blank line before the first item and after the last item. Because you
use the same markup in docstrings as you do in RST files, see `Quick reStructuredText
<https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_ for a markup summary.

Surround any text that you want to set apart as literal text (code entities) in double backticks
to render it in a monospaced font within a gray box. Use double backticks to surround the names
of files, folders, classes, methods, and variables.

For example::

  """Initialize the ``Desktop`` class with the version of AEDT to use."""

.. note::

   While the numpydoc style guide says to surround the names of classes, methods, and
   variables in a single backtick, you must use double backticks. Surrounding text in
   a single backtick in a PyAnsys library formats it in italic type rather than as a
   code entity.

Required docstring sections
---------------------------

PyAnsys library docstrings contain these numpydoc sections as a minimum:

* `Short Summary <https://numpydoc.readthedocs.io/en/latest/format.html#short-summary>`_
* `Extended Summary <https://numpydoc.readthedocs.io/en/latest/format.html#extended-summary>`_ if applicable
* `Parameters <https://numpydoc.readthedocs.io/en/latest/format.html#parameters>`_ if applicable
* `Returns <https://numpydoc.readthedocs.io/en/latest/format.html#returns>`_ if applicable
* `Examples <https://numpydoc.readthedocs.io/en/latest/format.html#examples>`_

These sections should follow numpydoc style. To avoid inconsistencies between
PyAnsys libraries, refer :ref:`docstring_formatting_rules`. 


Examples
--------

The "Examples" section provides one or more small code samples that make usage
of a method or function clear. They provide an easy place to start when
trying out the API.

Here is a sample "Examples" section from a Python file for PyAEDT.

.. code-block:: rst

   Examples
   --------
   Create an instance of HFSS and connect to an existing HFSS
   design or create a new HFSS design if one does not exist.

   >>> from pyaedt import Hfss
   >>> hfss = Hfss()
   pyaedt info: No project is defined...
   pyaedt info: Active design is set to...


Code supplied in an "Examples" section must be compliant with the
`doctest <https://docs.python.org/3/library/doctest.html>`_ format. This allows
the code to be used through `pytest`_ to perform regression testing to verify
that the code is executing as expected. 

If the definition of a method or function is updated, the code in the "Examples" section
must be updated. Any change within the API without a corresponding change
in the example code triggers a ``doctest`` failure.

Examples are not meant to replace a test suite but rather complement it. Because
examples must always match the API that they are documenting, they are an important
feature of maintainable documentation.

Type hints
----------

.. vale off

By default, Sphinx renders type hints as part of the function signature per
`PEP 484 – Type Hints <https://peps.python.org/pep-0484/>`_. This can become difficult
to read because the signature becomes very long.

.. vale off

Instead, you should render type hints as part of each parameter's description. To
accomplish this, you must combine the ``sphinx.ext.autodoc.typehints``, ``sphinx.ext.napoleon``,
and ``numpydoc`` extensions in the ``conf.py`` file in this order:

.. code:: python

   extensions = [
       ...,
       "sphinx.ext.autodoc.typehints",
       "sphinx.ext.napoleon",
       "numpydoc",
       ...,
   ]
   autodoc_typehints = "description"

When using type hints in this way, you can omit the type information in the "Parameters"
and "Returns" sections.

Additional directives
---------------------

Because Python docstrings are written using reStructuredText syntax, you can take
advantage of some of the directives available in this plaintext markup language.
Here are some Sphinx directives that can be used in docstrings, although they
should be used sparingly as they do not look very good in text terminals.

- ``note``: Highlights important information to be aware of.
- ``warning``: Points out an action that might result in data loss or cause
  some other issue, such as performance degradation.
- ``deprecated``: ``X.Y.Z`` Indicates the deprecation status of an object or
  feature.

Example
-------

Here is a generic docstring example compliant with PyAnsys guidelines:

.. literalinclude:: code/sample_func.py

To include the docstring of a function within Sphinx, you use the
``autofunction`` directive:

.. code::

   .. autofunction:: ansys_sphinx_theme.examples.sample_func.func

This directive renders the sample function as:

.. autofunction:: ansys_sphinx_theme.examples.sample_func.func

.. _googledoc: https://google.github.io/styleguide/
