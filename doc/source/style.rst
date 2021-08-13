*******************
Documentation Style
*******************

PyAnsys packages should pick either the Google or Numpy documentation
style when writing their docstrings.  Adhering to this style permits
the usage of the `sphinx.ext.napoleon
<https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_
extension, which is included in ``sphinx`` in version 1.3 and later.

Methods and functions should generally be documented with the
``Examples`` docstring section to make the usage of the method or
function clear.  Here is a sample function:

.. literalinclude:: ../../pyansys_sphinx_theme/sample_func.py

To include the docstring of function within sphinx, use the
``autofunction::`` directive:

.. code::

   .. autofunction:: pyansys_sphinx_theme.sample_func.func

Which causes the function to be rendered as:

.. autofunction:: pyansys_sphinx_theme.sample_func.func


More Details
~~~~~~~~~~~~
Additional examples and notes regarding Numpy or Google docstrings can
be found at `sphinx.ext.napoleon
<https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_.
Attempt to follow a consistent documentation style whenever possible.
