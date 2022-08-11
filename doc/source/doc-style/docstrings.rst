Numpydoc docstrings
###################

When writing docstrings for PyAnsys libraries, use the `numpydoc`_
style.

For consistency within PyAnsys libraries, always use ``"""`` to introduce and conclude a
docstring, keeping the line length shorter than 70 characters. Ensure that there are
no blank spaces at the end of a line because they cause errors in build checks that you
must then resolve.

A blank line signifies the start of a new paragraph. To create a bulleted or numbered list,
ensure that there is a blank line before the first item and after the last item. Because you
use the same markup in docstrings as you do in RST files, see this `quick reference
<https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_.

Surround any text that you want to set apart as literal text in double back ticks to render
it in a gold monospaced font. Use double back ticks to surround the names of files, folders,
classes, methods, and variables. For example::

  """Initialize the ``Desktop`` class with the version of AEDT to use."""


.. note::
   The PyAnsys style uses two back ticks to surround the names of classes, methods, and
   variables, not the single back tick that is recommended by `numpydoc`_
   style.


Required docstring sections
===========================

PyAnsys library docstrings contain these `numpydoc`_ sections as a minimum:

* `Short Summary <https://numpydoc.readthedocs.io/en/latest/format.html#short-summary>`_
* `Extended Summary <https://numpydoc.readthedocs.io/en/latest/format.html#extended-summary>`_ if applicable
* `Parameters <https://numpydoc.readthedocs.io/en/latest/format.html#parameters>`_ if applicable
* `Returns <https://numpydoc.readthedocs.io/en/latest/format.html#returns>`_ if applicable
* `Examples <https://numpydoc.readthedocs.io/en/latest/format.html#examples>`_

These sections should follow numpydoc style. To avoid inconsistencies between
PyAnsys libraries, adhere to the additional style guidelines that follow.


Short summary
-------------
This is a single line that goes immediately after the declaration of the class
or function to briefly describe what the class or function does. The
`short summary` is mandatory. If it is not present, :ref:`Documentation style tools`
raises an error.

The short summary can be declared on the same line as the opening quotes or on
the next line. While `PEP 257
<https://peps.python.org/pep-0257>`_ accepts both ways, you must be consistent across your
project. If you decide to declare the short summary on the same line,
refer to :ref:`Numpydoc validation` because ``"GL01"`` checking must be
turned off.

The guidelines for documenting short summaries differ for classes versus
functions.

Short summaries for classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~
A class is a *noun* representing a collection of methods. For consistency within PyAnsys libraries,
always start the brief description for a class with a verb ending in 's', followed by an extended
summary in a new line if additional information is needed::

  class FieldAnalysis3D(Analysis):
    """Manages 3D field analysis setup in HFSS, Maxwell 3D, and Q3D.

    This class is automatically initialized by an application call from one of
    the 3D tools. For parameter definitions, see the application function.

    ...
    """

Ensure that there is a line break between the end of a class docstring and the subsequent methods.

Short summaries for methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~
A method is a *verb* representing an action that can be performed. For consistency within PyAnsys
libraries, always start the brief description for a method with a verb not ending in 's', followed
by an extended summary in a new line if additional information is needed::

  def export_mesh_stats(self, setup_name, variation_string="", mesh_path=None):
    """Export mesh statistics to a file.

    ...
    """

Methods with a leading underscore (_) are *protected* methods, meaning that they are not rendered in the
documentation unless an explicit request is made to add them using Sphinx directives. However, clearly
written descriptions for private methods are still important.

If a method has the decorator ``@property``, it is turned into a property, which is described as a
noun rather than a verb. Because the resulting property cannot have parameters, you remove
the ``Parameters`` section for this method. If a setter follows the decorator ``@property``, do not
add a docstring for the setter. A setter simply exposes both the GET and SET methods rather
just the GET method. You should include examples to demonstrate usage.

Parameters
----------
Functions may have parameters in their signatures. All these parameters should be documented in
the ``Parameters`` section.

Here is an example of a ``Parameters`` section for a class in PyAEDT:

.. code-block:: rst

  Parameters
  ----------
    application : str
        3D application that is to initialize the call.
    projectname : str, optional
        Name of the project to select or the full path to the project
        or AEDTZ archive to open. The default is ``None``, in which
        case an attempt is made to get an active project. If no
        projects are present, an empty project is created.
    designname : str, optional
        Name of the design to select. The default is ``None``, in
        which case an attempt is made to get an active design. If no
        designs are present, an empty design is created.
    solution_type : str, optional
        Solution type to apply to the design. The default is
        ``None``, in which case the default type is applied.
    setup_name : str, optional
        Name of the setup to use as the nominal. The default is
        ``None``, in which case the active setup is used or
        nothing is used.
    specified_version : str, optional
        Version of AEDT  to use. The default is ``None``, in which case
        the active version or latest installed version is used.
    non_graphical : bool, optional
        Whether to run AEDT in the non-graphical mode. The default
        is ``False``, in which case AEDT is launched in the graphical mode.
    new_desktop_session : bool, optional
        Whether to launch an instance of AEDT in a new thread, even if
        another instance of the ``specified_version`` is active on the
        machine. The default is ``True``.
    close_on_exit : bool, optional
        Whether to release AEDT on exit. The default is ``False``.
    student_version : bool, optional
        Whether to enable the student version of AEDT. The default
        is ``False``.

The name of each parameter is followed by a space, a colon, a space, and then
the data type. A parameter is optional if its keyword argument displays a default
in the function signature. For an optional parameter, the data type is followed by a
comma and ``optional``.

The brief description for a parameter is generally a sentence fragment. However,
additional information is provided in clear, complete sentences. For an optional
parameter, the description specifies the default along with any information that might
be needed about the behavior that occurs when the default is used.

Returns
-------
The ``Returns`` section contains only the return data type and a brief description
that concludes with a period:

.. code-block:: rst

  Returns
  -------
  dict
      Dictionary of components with their absolute paths.


A class does not have a ``Returns`` section. If a ``Boolean`` is returned, format the
``Returns`` section like this:

.. code-block:: rst

  Returns
  -------
  bool
      ``True`` when successful, ``False`` when failed.

It is possible for the ``Returns`` section to look like the ``Parameters`` section
if variable names are provided:

.. code-block:: rst

  Returns
  -------
  has_succeeded : bool
      ``True`` when successful, ``False`` when failed.

It is possible for more than one item to be returned:

.. code-block:: rst

  Returns
  -------
  type
      Ground object.
  str
      Ground name.

If a method does not have a decorator, the basic implementation of Python
methods is used. In this case, while ``None`` is returned, you do not document it.
Consequently, such a method does not have a ``Returns`` section.

Examples
--------

The ``Examples`` section provides one or more small code samples that make usage
of a method or function clear. They provide an easy place to start when
trying out the API.

Here is a sample ``Examples`` section from a Python file for PyAEDT.

.. code-block:: rst

   Examples
   --------
   Create an instance of HFSS and connect to an existing HFSS
   design or create a new HFSS design if one does not exist.

   >>> from pyaedt import Hfss
   >>> hfss = Hfss()
   pyaedt info: No project is defined...
   pyaedt info: Active design is set to...


Code supplied in an ``Examples`` section must be compliant with the
`doctest <https://docs.python.org/3/library/doctest.html>`_ format. This allows
the code to be used through `pytest <https://docs.pytest.org/en/latest/>`_ to
perform regression testing to verify that the code is executing as expected. 

If the definition of a method or function is updated, the code in the ``Examples`` section
must be updated. Any change within the API without a corresponding change
in the example code triggers a ``doctest`` failure.

Examples are not meant to replace a test suite but rather complement it. Because
examples must always match the API that they are documenting, they are an important
feature of maintainable documentation.

Type hints
==========

By default, Sphinx renders `type hints <https://peps.python.org/pep-0484/>`_ as part
of the function signature. This can become difficult to read because the signature
becomes very long.

Instead, you should render type hints as part of each parameter's description. To
accomplish this, you must combine the ``sphinx.ext.autodoc.typehints``, ``sphinx.ext.napoleon``,
and ``numpydoc`` extensions in the ``conf.py`` file:

.. code:: python

   extensions = [
       ...
       "sphinx.ext.autodoc.typehints",
       "sphinx.ext.napoleon",
       "numpydoc",
       ...
   ]
   autodoc_typehints = "description"

.. note::

   The order in which you include these extensions matters.

When using type hints in this way, the type information in the ``Parameters``
and ``Returns`` sections can be omitted.

Additional directives
=====================
Because Python docstrings are written using RST syntax, it is possible to take
advantage of some directives available in this Markup language. Commonly used
directives include:

- ``.. note::`` highlights important information in the rendered documentation.

- ``.. warning::`` typically points out an action that might result in data loss.

- ``.. deprecated:: X.Y.Z`` informs the user about the deprecated status of
  the object or feature.

You can find additional information and examples at `numpydoc`_. Reference
this documentation as the primary source regarding docstring styles for directives
that are not covered here.


Example
=======

Here is a generic docstring example compliant with PyAnsys guidelines:

.. literalinclude:: code/sample_func.py

To include the docstring of a function within Sphinx, you use the
``autofunction::`` directive:

.. code::

   .. autofunction:: ansys_sphinx_theme.sample_func.func

This directive renders the sample function as:

.. autofunction:: ansys_sphinx_theme.sample_func.func

.. _numpydoc: https://numpydoc.readthedocs.io/en/latest/format.html
.. _googledoc: https://google.github.io/styleguide/
