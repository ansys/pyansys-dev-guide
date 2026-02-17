.. _docstring_formatting_rules:

Docstring formatting rules
==========================

In the PY files for PyAnsys libraries, docstrings always start and
end with triple quotation marks (``"""``). Within a docstring, content is
formatted similarly to RST files.

The first docstring in a PY file provides a short summary of the module
itself. For short summaries to fit on one line in the library's API reference
summary tables, you must keep the line lengths of your docstrings
to no more than 100 characters. This is different than the maximum line length
for source code, which might be set to as many as 120 characters.


Most of the time, a module contains only a single class. This page summarizes
PyAnsys-specific formatting rules for the sections more commonly found in a
docstring for a class or one of its methods:

- Short summary
- Deprecation warning
- Extended summary
- Parameters
- Returns
- Raises
- Examples

In most PyAnsys libraries, the docstrings in PY files do not contain these sections:

- Yields
- Receives
- Other Parameters
- Warns
- Warnings
- See Also
- Notes
- References

If a docstring in a PY file contains one of these sections,
see `Sections <numpydoc_style_guide_sections_>`_ in the *numpydoc Style guide*
for information on how to format its content. This page also indicates the order
of all sections possible in a docstring.

Docstring sections are always contained within the triple quotation marks that denote
a docstring. The sections more commonly found in PyAnsys docstrings must be in
the order indicated in this page's right pane.

Some of the docstrings shown on this page display ellipses to indicate
that they provide additional sections.


.. tip::
  You might want to open one of the larger PY files for your PyAnsys library
  and look at its docstrings while reading about how they are formatted. These
  PY files are typically in the ``src`` directory.


Short summary
-------------

This unnamed docstring section is a one-line summary written in plain English. This
single line immediately follows the declaration of a function, class, or method to
briefly describe what it does. A short summary for these Python objects is mandatory.
If it is not present, documentation style tools in the CI/CD process raise errors
when you push changes to a PR.

You can declare the short summary on the same line as the opening quotation marks
of the docstring or on the next line. While `PEP 257`_ accepts both ways,
docstrings must be consistent across your project. If the developers of a PyAnsys
library are declaring the short summary on the same line as the opening quotation marks,
they have turned off ``"GL01"`` checking in the ``numpydoc_validation_checks`` dictionary
of the ``numpydoc`` extension. For more information on documentation style tools and the
validation of NumPy-style docstrings, see `doc_style_tools_>`.

The short summary should not use code entities to refer to the names of Python
objects unless absolutely necessary. This is because the use of code entities
reduces readability of the short summary.

Because the short summary cannot exceed the maximum line length of 100 characters,
use a sentence fragment that starts with a verb and ends with a period. If additional
information is needed to clarify what the function, class, or method does, provide
this information in the :ref:`docstring_extended_summary`.

.. note::
   In Python, functions are not defined within a class but rather perform actions or
   operations on collections (lists, tuples, dictionaries, and sets). Methods, which
   are functions defined within a class, are associated with instances of that class.
   They perform actions or operations related to that class. While the subsequent content
   focuses on docstrings for classes and methods, docstrings for functions are
   basically formatted the same as those for methods.

Short summary for a class
~~~~~~~~~~~~~~~~~~~~~~~~~

A class is a *noun* representing a collection of methods. For consistency within PyAnsys libraries,
start the short summary for a class with a verb ending in "s" or "es" so that the summary table
of the classes in a module have consistently formatted descriptions::

    class Emit(Design, object):
        """Provides the EMIT application interface.

        ...

        """

Initializing an instance of a class often requires specifying parameters, which are indicated
in a ``def __init__`` definition. These parameters are described in the :ref:`docstring_parameters`
section of the docstring for the class.

Short summary for a method
~~~~~~~~~~~~~~~~~~~~~~~~~~

A method is a *verb* representing an action that can be performed. For consistency
within PyAnsys libraries, start the short summary for a method with a verb not ending
in "s" or "es" so that the summary table of the methods for a class have consistently
formatted descriptions::

  def export_mesh_stats(self, setup_name, variation_string="", mesh_path=None):
    """Export mesh statistics to a file.

    ...

    """

Using a method almost always requires specifying parameters, which are indicated in parentheses
in the method's definition. These parameters, except for the ``self`` parameter, are always described
in the :ref:`docstring_parameters` section for the method. The ``self`` parameter does not have to
be documented because it is a reference to the instance of the parent class (and its properties)
that the method is being called on.

Methods with a leading underscore (``_``) are *protected* methods, meaning that they are not
rendered in the documentation unless an explicit request is made to add them using Sphinx
directives. The plus side to this is that docstrings for protected methods can be more
developer-focused. However, writing clear docstrings for protected methods is still
important.

If a method has an ``@exceperty`` decorator, it means that it has no parameters. Thus,
you can remove the "Parameters" section from the docstring for this method.

If a method has an ``@property`` decorator, it is turned into a property, which must be described
as a noun rather than a verb. Because the resulting property cannot have parameters, it does
not have a "Parameters" section. If a ``setter`` follows the ``@property`` decorator, do not
add a docstring for the setter. A ``setter`` simply exposes both the GET and SET methods rather
than only the GET method. Developers should include examples to show how to use the GET and SET
methods if necessary. A "Returns" section is only included if the property calculates
and returns a result. Otherwise, the description should clearly explain the value that
is returned.

Deprecation warning
-------------------

This unnamed docstring section follows the short summary only if the Python object is being
deprecated or has been deprecated. It consists of a ``deprecated`` directive that warns
users about when this object is to be removed (or was removed) from the API. The
``deprecated`` directive gives a reason for the deprecation, such as the
object is superseded or duplicates functionality found elsewhere. Lastly, it recommends
how to obtain the same functionality.

Here is an example of a PyAEDT method with a ``deprecated`` directive. It indicates
the version for the deprecation and explains that this method is superseded by functionality
in another method. It uses the ``func`` role to link to the method that should be used::

  def create_polygon_from_points(self, point_list, layer_name, net_name=""):
        """Create a new polygon from a point list.

        .. deprecated:: 0.6.73
        Use the :func:`create_polygon` method instead. It now supports point lists as arguments.

.. _docstring_extended_summary:

Extended summary
----------------

If the short summary does not clearly and fully explain the functionality of the object,
this unnamed docstring section provides the additional information that is needed in
complete sentences. A blank line must always be inserted before and after the extended
summary.

While you can use inline code entities in the extended summary, you should not describe
any named objects that are parameters here in this section because they are described in
the subsequent "Parameters" section. You should place any needed implementation information
or background theory in a "Notes" section. For more information, see
`Sections <numpydoc_style_guide_sections_>`_ in the *numpydoc Style guide*.

.. _docstring_parameters:

Parameters
----------

This named docstring section describes the parameters listed in the definition
of an instance method. The first parameter in the definition is ``self`` by convention.
As explained earlier, it represents the instance of the class that a method is being
called on. The other parameters listed in the definition pass input data. In the "Parameters"
section, all parameters except for ``self`` must be documented in the order in which they appear
in the definition.

Parameters for initializing an instance of a class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can find the parameters for initializing a class in an ``__init__`` definition.

Here is the ``__init__`` definition for the PyAEDT ``Emit`` class::

  def __init__(
      self,
      projectname=None,
      designname=None,
      solution_type=None,
      setup_name=None,
      specified_version=None,
      non_graphical=False,
      new_desktop_session=True,
      close_on_exit=True,
      student_version=False,
      machine="",
      port=0,
      aedt_process_id=None,
  ):

.. _docstring_parameters_optional_usage:

The parameters for this class are defined in the "Parameters" section like this:

.. code-block:: rst

  Parameters
  ----------
  projectname : str, optional
      Name of the project to select or the full path to the project
      or AEDTZ archive to open.  The default is ``None``, in which case
      an attempt is made to get an active project. If no projects are
      present, an empty project is created.
  designname : str, optional
      Name of the design to select. The default is ``None``, in which case
      an attempt is made to get an active design. If no designs are
      present, an empty design is created.
  solution_type : str, optional
      Solution type to apply to the design. The default is ``None``, in which
      case the default type is applied.
  setup_name : str, optional
      Name of the setup to use as the nominal. The default is ``None``, in
      which case the active setup is used or nothing is used.
  specified_version : str, optional
      Version of AEDT to use. The default is ``None``, in which case
      the active setup is used or the latest installed version is
      used.
  non_graphical : bool, optional
      Whether to launch AEDT in non-graphical mode. The default
      is ``False``, in which case AEDT is launched in graphical mode.
      This parameter is ignored when a script is launched within AEDT.
  new_desktop_session : bool, optional
      Whether to launch an instance of AEDT in a new thread, even if
      another instance of the ``specified_version`` is active on the
      machine. The default is ``True``.
  close_on_exit : bool, optional
      Whether to release AEDT on exit. The default is ``False``.
  student_version : bool, optional
      Whether to start the AEDT student version. The default is ``False``.
  machine : str, optional
      Machine name to connect the desktop session to. The default is ``""``.
      This parameter works only in AEDT 2022 R2 or later. The remote server
      must be up and running with the ``ansysedt.exe -grpcsrv portnum``
      command. If the machine is ``"localhost"``, the server also starts
      if it is not present.
  port : int, optional
      Port number for starting the desktop communication on an already
      existing server. The default is ``0``. This parameter is ignored when
      creating a server and works only in AEDT 2022 R2 or later. The
      remote server must be up and running with the ``ansysedt.exe -grpcsrv portnum``
      command.
  aedt_process_id : int, optional
      Process ID for the instance of AEDT to point PyAEDT at. The default is
      ``None``. This parameter is only used when ``new_desktop_session = False``.

Parameters for a function or method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. vale off

You can find the parameters for a function or method in parentheses in its definition
(function signature). Here is the definition for the ``add_sweep`` method in the PyAEDT
:file:`SolveSetup.py` file::

  @pyaedt_function_handler()
  def add_sweep(self, sweepname=None, sweeptype="Interpolating"):

.. vale on

The parameters for this method are defined in the "Parameters" section like this:

.. code-block:: rst

  Parameters
  ----------
  sweepname : str, optional
      Name of the sweep. The default is ``None``.
  sweeptype : str, optional
      Type of the sweep. The default is ``"Interpolating"``.


For the first parameter, the behavior that occurs when the default of ``None`` is used
is unclear. For the second parameter, no options other than the default are given.
Because the goal is to have well written and consistently formatted docstrings, when
submitting suggested changes in a PR, you would want to add comments like these to the
parameter descriptions:

- For the ``sweepname`` parameter, what behavior occurs when the default of
  ``None`` is used?
- For the ``sweeptype`` parameter, what are all the options so that they
  can be listed in the description alphabetically in either a sentence or itemized list?

For information on making a comment when reviewing a PR, see :ref:`add_comment_on_line`.

Parameter formatting
~~~~~~~~~~~~~~~~~~~~

The first line for each parameter provides the name and data type and indicates
if specifying a value is optional. Always follow the parameter name with a space,
a colon, and a space. Next, specify the data type of the parameter, being as precise
as possible.

Parameter data types
^^^^^^^^^^^^^^^^^^^^

The preceding examples show the ``str``, ``bool``, ``int``, and ``list`` data types.
Additional common data types include ``float``, ``dict``, and ``tuple``. For more
information, see :ref:`py_file_primitive_data_types` and :ref:`py_file_collections`.
Because your PyAnsys project might support other data types, consult with your developers
before making any changes to them.

Here are some guidelines to follow when specifying the one or more data types that a parameter
supports as inputs:

- For a parameter with a numerical default, let the developer set the data type. While
  it seems intuitive that a numerical default with a decimal point is a float, a float value
  might accept an integer (and vice versa).

- When the code shows that a parameter is being converted to a string with ``str(rjc)``, the
  data type can be a string, float, or integer. You can format these multiple data types as
  indicated in the next bullet.

- When a parameter supports multiple data types, place the word "or" between each type::

    isconvergence : bool or str or list

Optional parameters
^^^^^^^^^^^^^^^^^^^

A parameter is optional if a default is shown in the definition. If no value is programmatically
specified for the parameter, the default is used. PyAnsys libraries use two different methods
for providing the default for an optional parameter.

In the PY files for most projects, the data type is followed by a comma and ``optional``, which is
the method used in the two "Parameters" sections shown earlier. Following the short summary of the
parameter, a complete sentence then provides the default.

However, recent extension enhancements support placing the default after the data type, which
eliminates the need for a sentence indicating what the default is (unless the behavior that occurs
when this default is used is unclear). Here is a "Parameters" section that uses this second method:

  .. code-block:: rst

    Parameters
    ----------
    port : int, default: -1
        Port to use for communication.
    open_new_instance : bool, default: True
        Whether to open a new instance. When ``False``, try to connect to an existing instance
        using the URL specified by the ``url`` parameter.
    enable_exceptions : bool, default: True
        Whether to show Motor-CAD communication errors as Python exceptions.
    enable_success_variable : bool, default: False
        Whether Motor-CAD methods return a success variable (first object in tuple).
    reuse_parallel_instances : bool, default: False
        Whether to reuse MotorCAD instances when running in parallel. When ``True``,
        you must free instances after use.
    url: str, default: ""
        Full URL for the Motor-CAD connection if connecting to an existing Motor-CAD
        instance.

Projects using the older ``optional`` method might eventually want to migrate to this newer
method to reduce the length of many of their parameter descriptions.

Parameter descriptions
^^^^^^^^^^^^^^^^^^^^^^

When writing the description for a parameter, always follow these rules, referring
back to them as needed:

- Indent the parameter's short summary and all subsequent sentences four spaces.

- For the short summary, use a sentence fragment that omits a leading article
  (such as "A," "An," or "The") and conclude this fragment with a period. Although omitting the
  article contradicts the `Articles <Google_dev_doc_articles_>`_ guideline in the Google style
  guide, removing them at the beginning of short summaries here and in other docstring sections
  ensures that the first word is an important descriptor.

- End the short summary (and complete sentences) with prepositions if it improves readability.
  For example, "Frequency to set the adaptive convergence at" is more readable than
  "Frequency at which to set the adaptive convergence."

- After the short summary, use complete sentences, including articles, to provide additional
  information.

- When a sentence is used to specify the default, this sentence should immediately follow the
  short summary. If other possible options are not evident, begin the next sentence with an
  "Options are" phrase and then specify all options, including the default, in alphabetical
  order. If there are many options, consider formatting the options in a bulleted list. Or,
  in situations where listing specific options is not practical or necessary, format the
  parameter description similarly to this one::

    unit : str, optional
        Unit of the frequency. For example, ``"GHz"`` or ``"MHz"``. The default is ``"GHz"``.

- When specifying the default for a string parameter, surround the default in both
  double backticks (:code:`\`\``) and double quotation marks (``"``)::

    The default is ``"0.5cm"``.

- When the default for a string parameter is ``None``, surround the default only in
  double backticks because ``None`` has programmatic meaning and is not a string value.
  ``None`` represents the absence of a value or a null value. Thus, the sentence
  indicating this default usually requires a non-restrictive "in which case" clause that
  explains the behavior that occurs when ``None`` is used. Many examples of using an
  "in which case`` clause appear in the "Parameters" section shown earlier for
  the PyAEDT ``Emit`` class.

- Start the description for a Boolean parameter with a "Whether to" phrase and surround
  the default in only double backticks because ``True`` and ``False`` have programmatic
  meaning and are not string values::

    include_signal : bool, optional
        Whether to generate extended signal nets. The default is ``True``.

  Do not include "or not" in the description because the true or false nature of a Boolean
  parameter makes this obvious. If the default for the Boolean parameter does not clearly
  describe the behavior that occurs, follow the default with a non-restrictive "in which case"
  clause that explains the behavior::

    non_graphical : bool, optional
      Whether to launch AEDT in non-graphical mode. The default is ``False``,
      in which case AEDT is launched in graphical mode. This parameter is
      ignored when a script is launched within AEDT.

- Enclose all code entities in double backticks. If you surround a code entity in only a single
  backtick (:code:`\``), it is incorrectly rendered in italics in the documentation.

- Use the present tense for verbs. Occurrences of ``will`` cause `Vale`_ to
  raise warnings about not using phrases expressing future actions.

- When documenting variable length positional or keyword arguments, leave the leading single
  asterisk (``*``) or double asterisks  (``**``) in front of their names::

    *args : tuple
        Additional arguments to pass as keyword arguments.
    **kwargs : dict, optional
        Extra arguments to the ``metric`` parameter. For a list of all possible arguments,
        see the ``metric`` documentation.

Returns
-------

The docstring for a class should not have a named "Returns" section because it is assumed that
a class always returns an instance of itself. If a class has a "Returns`` section, you can
remove it from the docstring.

In Python, a method decorator is a function that can be used to modify or extend the behavior of
a method in a class without changing the method's source code. Method decorators are typically
applied to methods using the ``@`` symbol followed by the decorator function's name. They are
usually defined separately from the class and are often used to wrap or modify the method that
they decorate.

When a function or method has no decorator, the vanilla implementation of a Python method is
being used, which means that the function or method has no return value. (While there is actually
a return value of ``None``, this is something that you do not document.) For such methods, you
can remove the "Returns" section from their docstrings.

When a function returns one or more values, the "Returns" section must provide the
data type and a description for each value returned.

When only a non-Boolean value is returned, format the "Returns" like this:

.. code-block:: rst

  Returns
  -------
  int
      Port being used for communication.


When only a Boolean value is returned, format the "Returns" section like this:

.. code-block:: rst

  Returns
  -------
  bool
      ``True`` when successful, ``False`` when failed.

When a method has an ``@exceperty`` decorator, it always returns a Boolean value. Thus,
format the ``Returns`` section for such a method as shown in the preceding example.

When multiple values are returned, format the "Returns" section like the "Parameters"
section:

.. code-block:: rst

  Returns
  -------
  err_code : int
      Non-zero value that indicates an error code or ``0`` on success.
  err_msg : str or None
      Human-readable error message, or ``None`` on success.

Raises
------

This named docstring section is optional. It lists the errors that can be raised and explains when
they are raised. While many PyAnsys libraries do not include a "Raises" section in their docstrings,
including this section can be valuable for users.

.. code-block:: rst

  Raises
  ------
  RuntimeError
      If the name given is not the name of an existing result set and a current result
      set already exists.

Examples
--------

This named section is optional but strongly recommended. The one or more interactive examples placed
in this section demonstrate usage. They do not provide a testing framework. Those types of tests
are typically placed in the ``tests`` directory. For more information, see :ref:`testing`.

According to documentation published by the Python organization, the `doctest <doctest_>`_ module executes
the examples in the "Examples" section of the docstring to verify that they work.

Place any description of what the example code demonstrates immediately after the ``Examples`` section
heading. Follow this description with a blank line. Then, precede each line of code with three right
carats (``>>>``) to render them in a code block.

Use blank lines to separate comments from lines of code. Also use blank lines
to separate multiple code examples.

Here is an "Examples" section for the ``element_dot`` method in PyDPF-Core:

.. code-block::

  Examples
  --------
  Compute the element-wise dot product.

  >>> from ansys.dpf import core as dpf
  >>> import numpy as np
  >>> data = np.random.random((10, 3))
  >>> field_a = dpf.field_from_array(data)
  >>> field_b = dpf.field_from_array(data)
  >>> fout = dpf.help.element_dot(field_a, field_b)
  >>> fout.shape
  10

  >>> # Numpy equivalent
  >>> arr_a = np.random.random((10, 3))
  >>> arr_b = np.random.random((10, 3))
  >>> edot = np.sum(arr_a*arr_b, 1)
  >>> edot.shape
  (10,)

The returned value for this example is ``10``. If you are writing an example and want to test
it locally, you can copy and paste the lines beginning with the three right carats into
JupyterLab and execute them. You can then paste the returned value into the example but
without the three right carats.
