Class Documentation
###################

There are two main ways of using Sphinx to document an API class:

* Manually describe "how" and "why" to use a class in either 
  a "User Guide" or an example within the library's documentation 
* Automatically generate API documentation for classes using the 
  ``autoclass`` or ``autosummary`` directive

Manual Documentation
--------------------

To manually describe the "how" and "why" usage of a class, use the 
``.. code:: python`` directive:

.. code::

   Initialize ``my_module.MyClass`` with initial parameters. These
   parameters are automatically assigned to the class.

    .. code:: python

       >>> from my_module import MyClass
       >>> my_obj = MyClass(parm1='apple', parm2='orange')
       >>> my_obj.parm1
       'apple'

Initialize ``my_module.MyClass`` with initial parameters.  These
parameters are automatically assigned to the class.

.. code:: python

   >>> from my_module import MyClass
   >>> my_obj = MyClass(parm1='apple', parm2='orange')
   >>> my_obj.parm1
   'apple'


Auto-Generated Documentation
----------------------------

To automatically genereate class descriptions, use either the ``autoclass``  
or ``autosummary`` directive.

For simple classes, you can use the ``autoclass`` directive:


.. code::

   .. autoclass:: pyansys_sphinx_theme.samples.ExampleClass
       :members:


.. autoclass:: pyansys_sphinx_theme.samples.ExampleClass
    :members:

For complex classes with many methods, you should use 
the ``autosummary`` directive:

.. code::

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
