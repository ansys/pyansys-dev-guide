.. _docstrings:

Docstring Standards
###################
When writing docstrings for PyAnsys libraries, use the `numpydoc`_
documentation style. To use `numpydoc`_ add the following to your
``conf.py``:

.. code:: python

  extensions = ['numpydoc',
                # other extensions
  ]


Minimum Requirements
--------------------
PyAnsys libary docstrings contain at a minimum the following
`numpydoc`_ sections:

* `Short description <https://numpydoc.readthedocs.io/en/latest/format.html#short-summary>`_.
* `Extended Summary <https://numpydoc.readthedocs.io/en/latest/format.html#extended-summary>`_ (if applicable)
* `Parameters <https://numpydoc.readthedocs.io/en/latest/format.html#parameters>`_ if applicable
* `Returns <https://numpydoc.readthedocs.io/en/latest/format.html#returns>`_ if applicable
* `Examples <https://numpydoc.readthedocs.io/en/latest/format.html#examples>`_

These sections should follow the numpydoc standards.  To avoid
inconsistencies between PyAnsys libaries, adhere to the following
additional standards:


Parameters
~~~~~~~~~~
Always specify the type, and whenever necessary, provide the full class name::

  Parameters
  ----------
  my_obj : :class:`ansys.<product>.<library>.FooClass`
      Description of FooClass.
  some_int : int
      Some interger value.

.. note::
   These parameter descriptions have punctuation. 


Returns
~~~~~~~
Returns section contains only the return type and no the name and type::

  Returns
  -------
  int
      Description of some return value.

Example Docstrings
------------------
Methods and functions should generally be documented with the
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
Enable validation of docstrings during the sphinx build by adding the
following line to ``conf.py``::

  numpydoc_validation_checks = {"GL08"}

This will issue the following warning for any objects without a docstring::

  "The object does not have a docstring"

The ``"GL08"`` code is required at minimum for PyAnsys projects.
Other codes may be enforced at a later date; for a full listing see
`numpydoc Validation Check
<https://numpydoc.readthedocs.io/en/latest/validation.html#validation>`_.


Additional Information
----------------------
Additional examples and notes can be found at `numpydoc`_.  Reference
their documentation as the primary source of information regarding
docstring styles aside from the directives noted here.

.. _numpydoc: https://numpydoc.readthedocs.io/en/latest/format.html
.. _googledoc: https://google.github.io/styleguide/
