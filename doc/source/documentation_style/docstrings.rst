Docstring Standards
###################

When writing docstrings for PyAnsys libraries, use the `numpydoc`_ style,
regardless as to whether you are using this Sphinx extension or the `napoleon`_
Sphinx extension to generate your library documentation.

You add the extension to use for documentation generation in your ``conf.py`` file.
For example, to use `numpydoc`_, you would add:

.. code:: python

  extensions = [
      'numpydoc',
      ...
  ]

For consistency within PyAnsys libraries, always use ``"""`` to introduce and conclude a
docstring, keeping the line length shorter than 70 characters. Ensure that there are
no blank spaces at the end of a line because they will cause errors in build checks that you
will have to resolve.

A blank line signifies the start of a new paragraph. To create a bulleted or numbered list,
ensure that there is a blank line before the first item and after the last item. Because you
use the same markup in docstrings as you do in RST files, see this `quick reference`_.


Surround any text that you want to set apart as literal text in double back ticks to render
it in a monospace gold font. Use double back ticks to surround the names of files, folders,
classes, methods, and variables. For example::

  """Initialize the ``Desktop`` class with the version of AEDT to use."""


.. note::
   The PyAnsys style uses two back ticks to surround the names of classes, methods, and
   variables, not the single back tick that is recommended by `numpydoc`_ 
   style. 

 
Minimum Section Requirements
----------------------------
PyAnsys library docstrings contain these `numpydoc`_ sections as a minimum:

* `Short description <https://numpydoc.readthedocs.io/en/latest/format.html#short-summary>`_
* `Extended Summary <https://numpydoc.readthedocs.io/en/latest/format.html#extended-summary>`_ if applicable
* `Parameters <https://numpydoc.readthedocs.io/en/latest/format.html#parameters>`_ if applicable
* `Returns <https://numpydoc.readthedocs.io/en/latest/format.html#returns>`_ if applicable
* `Examples <https://numpydoc.readthedocs.io/en/latest/format.html#examples>`_

These sections should follow numpydoc style. To avoid inconsistencies between
PyAnsys libraries, adhere to the additional style guidelines that follow.

Classes
~~~~~~~
A class is a 'noun' representing a collection of methods. For consistency within PyAnsys libraries,
always start the brief description for a class with a verb ending in 's', followed by an extended
summary if applicable::

  class FieldAnalysis3D(Analysis):
    """Manages 3D field analysis setup in HFSS, Maxwell 3D, and Q3D.

    This class is automatically initialized by an application call from one of
    the 3D tools. For parameter definitions, see the application function.

    ...
    """


Ensure that there is a line break between the end of a class docstring and the subsequent methods.

Methods
~~~~~~~
A method is a 'verb' representing an action that can be performed. For consistency within PyAnsys
libraries, always start the brief description for a method with a verb not ending in 's', followed
by an extended summary if applicable::

  def export_mesh_stats(self, setup_name, variation_string="", mesh_path=None):
    """Export mesh statistics to a file."""
      

Methods with a leading underscore (_) are 'protected' methods, meaning that they are not rendered in the
documentation unless an explicit request is made to add them using Sphinx directives. However, clearly
written descriptions for private methods are still important.

If a method has the decorator ``@property``, it is turned into a property, which is described as a
'noun' rather than a 'verb'. Because the resulting property cannot have parameters, you remove
the 'Parameters' section for this method. If a setter follows the decorator ``@property``, do not
add a docstring for the setter. A setter simply exposes both the GET and SET methods rather
just the GET method. Examples should be included to demonstrate usage.

Parameters
~~~~~~~~~~
Both classes and methods have parameters in their function signatures. All parameters in a function
signature should appear in the 'Parameters' section for the class or method. 

Here is an example of a 'Parameters' section for a class in PyAEDT::

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
        Whether to release  AEDT on exit. The default is ``False``.
    student_version : bool, optional
        Whether to enable the student version of AEDT. The default
        is ``False``.
    
The name of each parameter is followed by a space, a colon, a space, and then
the data type. A parameter is optional if its keyword argument has a default shown
in the function signature. For an optional parameter, the data type is followed by a
comma and ``optional``.

The brief description for a parameter is generally a sentence fragment. However, 
additional information is provided in clear, complete sentences. For an optional
parameter, the description specifies the default along with any information that might
be needed about the behavior that occurs when the default is used.
  
Returns
~~~~~~~
The 'Returns' section contains only the return data type and a brief description
that concludes with a period::

  Returns
  -------
    dict
      Dictionary of components with their absolute paths.
 

A class does not have a 'Returns' section. If a Boolean is returned, format the
'Returns` section like this::

  Returns
  --------
    bool
      ``True`` when successful, ``False`` when failed.


It is possible for more than one item to be returned::

  Returns
  --------
    type
      Ground object.
    str
      Ground name.


If a method does not have a decorator, the basic implementation of Python
methods is used. In this case, while ``None`` is returned, you do not document it.
Consequently, such a method does not have a 'Returns' section.

Example Docstrings
------------------
Methods and functions should generally be documented within the
'Examples' section to make the usage of the method or function clear.
Here is a sample function:

.. literalinclude:: sample_func.py

To include the docstring of a function within Sphinx, you use the
``autofunction::`` directive:

.. code::

   .. autofunction:: pyansys_sphinx_theme.sample_func.func

This directive renders the sample function as:

.. autofunction:: pyansys_sphinx_theme.sample_func.func


Validation
----------
Enable validation of docstrings during the Sphinx build by adding the
following line to the ``conf.py`` file::

  numpydoc_validation_checks = {"GL08"}

This will issue the following warning for any object without a docstring::

  "The object does not have a docstring"

The ``"GL08"`` code is required at minimum for PyAnsys libraries.
Other codes may be enforced at a later date. For a full listing,
see `Docstring Validation`_
in the `numpydoc`_.


Additional Information
----------------------
You can find additional information and examples at `numpydoc`_. Reference
this documentation as the primary source regarding docstring styles for directives
that are not covered here. For example, you use the ``note::`` directive to highlight
important information and the ``warning::`` directive to point out an action that
might result in data loss.

.. LINKS AND REFERENCES
.. include::  ../links.rst

.. _quick reference: https://docutils.sourceforge.io/docs/user/rst/quickref.html
.. _Docstring Validation: https://numpydoc.readthedocs.io/en/latest/validation.html#validation
