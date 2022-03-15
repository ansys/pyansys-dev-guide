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


Documenting Multiple Classes Together
-------------------------------------

To document a set of small but highly cohesive classes, an option
is to combine the two approaches described above. This is done by
including multiple ``autoclass`` directives on the same page with
headings and text blocks as necessary to describe the
relationships between the classes.

For example, the Granta MI BoM Analytics
:external+grantami-bomanalytics:doc:`Part Compliance page <api/compliance/parts>`
first describes the
:external+grantami-bomanalytics:class:`~ansys.grantami.bomanalytics.queries.PartComplianceQuery`
class, and then describes the
:external+grantami-bomanalytics:class:`~ansys.grantami.bomanalytics._query_results.PartComplianceQueryResult`,
and
:external+grantami-bomanalytics:class:`~ansys.grantami.bomanalytics._item_results.PartWithComplianceResult`
classes returned by the query. The classes are only ever
encountered together in this context, so they are documented on a
single page.

In contrast, the
:external+grantami-bomanalytics:class:`~ansys.grantami.bomanalytics.indicators.RoHSIndicator`
and
:external+grantami-bomanalytics:class:`~ansys.grantami.bomanalytics.indicators.WatchListIndicator`
classes are shared across multiple queries, and so they are
documented separately.
