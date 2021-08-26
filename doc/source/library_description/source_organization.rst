Source Organization 
###################
PyAnsys libraries follow the `Namespace Packages`_ convention to allow
multiple libraries to use the same shared ``ansys`` namespace:

``ansys/<product/service>/<feature>/``

For example, the `PyMAPDL`_ library with the ``ansys-mapdl-core`` package
name has the following directory structure:

::

   setup.py
   ansys/
       mapdl/
           core/
               __init__.py
               launcher.py
               mapdl_grpc.py
               ...

This allows the `PyMAPDL`_ library to be imported with:

.. code:: python

   >>> from ansys.mapdl import core as pymapdl

When using this convention, other namespace packages can use the
``ansys-mapdl`` namespace. 

For example:

.. code:: python

   >>> from ansys.mapdl import reader as pymapdl_reader

.. note::

   Do not include ``__init__.py`` in first-level and second-level 
   directories. If ``__init__.py`` is included in these levels, 
   namespace packages will conflict, allowing only one to be imported.

While the ``ansys-<product/service>`` namespace is verbose, using it 
consistently is important because it allows multiple products and services 
to share the same namespace. This makes it easy when searching for "ansys" 
packages within the `Python Package Index PyPi <https://pypi.org/>`_.

.. _Namespace Packages: https://packaging.python.org/guides/packaging-namespace-packages/
.. _PyMAPDL: https://github.com/pyansys/pymapdl