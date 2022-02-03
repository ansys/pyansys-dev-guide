.. _docstrings:

Docstring Standards
###################
When writing docstrings for PyAnsys libraries, use the `numpydoc`_
documentation style. To use `numpydoc`_, add the following to your
``conf.py``:

.. code:: python

  extensions = ['numpydoc',
                # other extensions
  ]

For consistency within PyAnsys libraries, alwyas use ``"""`` to introduce and conclude a
docstring. Additonally, use double back ticks to surround words that are to be formatted
as literal strings, including the names of files, folders, classes, and methods. While the
`numpydoc`_ documentation style says to use one back tick to surround the names of classes
and methods, the PyAnsys style is to use two back ticks. 

Minimum Requirements
--------------------
PyAnsys library docstrings contain at a minimum the following
`numpydoc`_ sections:

* `Short description <https://numpydoc.readthedocs.io/en/latest/format.html#short-summary>`_.
* `Extended Summary <https://numpydoc.readthedocs.io/en/latest/format.html#extended-summary>`_ if applicable
* `Parameters <https://numpydoc.readthedocs.io/en/latest/format.html#parameters>`_ if applicable
* `Returns <https://numpydoc.readthedocs.io/en/latest/format.html#returns>`_ if applicable
* `Examples <https://numpydoc.readthedocs.io/en/latest/format.html#examples>`_

These sections should follow numpydoc standards. To avoid
inconsistencies between PyAnsys libraries, adhere to the additional 
standards that follow.

Classes
~~~~~~~
A class is a "noun" representing a collection of methods. For consistency within PyAnsys libraries,
always start the short description for a class with a verb ending in "s", followed by an extended
summary if applicable::

  class FieldAnalysis3D(Analysis, object):
    """Manages 3D field analysis setup in HFSS, Maxwell 3D, and Q3D.

    This class is automatically initialized by an application call from one of
    the 3D tools. See the application function for parameter definitions.


Always have a line break between the end of a class docstring and the subsequent methods.

Methods
~~~~~~~
A method is a "verb" representing an action that can be performed. For consistency within PyAnsys
libraries, always start the short description for a method with a verb not ending in "s", followed
by an extended summary if applicable::

  def export_mesh_stats(self, setup_name, variation_string="", mesh_path=None):
        """Export mesh statistics to a file.


If a method has the decorator ``@exceperty``, you can remove the Parameters section for this method.

Methods with a leading underscore are 'protected' methods, meaning that they aren't rendered in the
documentation unless an explicit require is made to add them using Sphinx directives. However, clear
documentation for these methods is still important.

Parameters
~~~~~~~~~~
Classes and functions both have parameters. After the name of a parameter, always specify the data type
and, whenever necessary, provide the full class name::

  Parameters
  ----------
  my_obj : :class:`ansys.<product>.<library>.FooClass`
      Description of FooClass.
  some_int : int
      Some integer value.

.. note::
   Parameter descriptions have punctuation. While the brief description itself
   is generally a sentence fragment, clear, complete sentences should be used to
   provide any additional information. 


Returns
~~~~~~~
The Returns section contains only the return type (not the name and type)
and a brief description::

  Returns
  -------
  int
      Description of some return value.

Classes do not have a Returns section.

Example Docstrings
------------------
Methods and functions should generally be documented within the
``Examples`` docstring section to make the usage of the method or
function clear.  Here is a sample function:

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
Other codes may be enforced at a later date. For a full listing, see
`numpydoc Validation Check
<https://numpydoc.readthedocs.io/en/latest/validation.html#validation>`_.


Additional Information
----------------------
Additional examples and notes can be found at `numpydoc`_. Reference
this documentation as the primary source of information regarding
docstring styles for directives not covered here.

.. _numpydoc: https://numpydoc.readthedocs.io/en/latest/format.html
.. _googledoc: https://google.github.io/styleguide/
