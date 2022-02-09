Class Documentation
###################

There are two main ways of using Sphinx to document a class:

* Manually describe 'how' and 'why' to use a class in either 
  a "User Guide" or an example within the library's documentation
* Automatically generate documentation for classes using the 
  ``autoclass`` or ``autosummary`` directive

Manual Documentation
--------------------

To manually describe 'how' and 'why' to exercise a class, use the 
``.. code:: python`` directive::

   Initialize ``my_module.MyClass`` with initial parameters. These
   parameters are automatically assigned to the class.

    .. code:: python

       >>> from my_module import MyClass
       >>> my_obj = MyClass(parm1='apple', parm2='orange')
       >>> my_obj.parm1
       'apple'

In the documentation, this is rendered as:

Initialize ``my_module.MyClass`` with initial parameters.  These
parameters are automatically assigned to the class.

.. code:: python

   >>> from my_module import MyClass
   >>> my_obj = MyClass(parm1='apple', parm2='orange')
   >>> my_obj.parm1
   'apple'


Auto-generated Documentation
----------------------------

To automatically generate class descriptions, use either the ``autoclass``  
or ``autosummary`` directive.

For simple classes, use the ``autoclass`` directive::

   .. autoclass:: pyansys_sphinx_theme.samples.ExampleClass
       :members:

In the documentation, this is rendered as:

.. autoclass:: pyansys_sphinx_theme.samples.ExampleClass
    :members:

For complex classes with many methods, use the 
``autosummary`` directive::

   .. autoclass:: pyansys_sphinx_theme.samples.Complex

   .. autosummary::
      :toctree: api/

      pyansys_sphinx_theme.samples.Complex.real
      pyansys_sphinx_theme.samples.Complex.imag
      pyansys_sphinx_theme.samples.Complex.abs


The above code generates the following documentation, with each 
method or attribute on its own page.

.. autoclass:: pyansys_sphinx_theme.samples.Complex


.. autosummary::
   :toctree: api/

   pyansys_sphinx_theme.samples.Complex.real
   pyansys_sphinx_theme.samples.Complex.imag
   pyansys_sphinx_theme.samples.Complex.abs
