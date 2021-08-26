Docstrings
##########

When writing docstrings for PyAnsys libraries, you should pick either 
the `numpydoc`_ or `googledoc`_ documentation style. Adhering to the 
selected style permits usage of the `sphinx.ext.napoleon
<https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_
extension, which is included in Sphinx version 1.3 and later.

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


Additional Information
----------------------
Additional examples and notes regarding Numpy or Google docstrings can
be found at `sphinx.ext.napoleon
<https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_. 
A consistent documentation style should be followed whenever possible.

.. _numpydoc: https://numpydoc.readthedocs.io/en/latest/format.html
.. _googledoc: https://google.github.io/styleguide/
