.. _optional_packages:

Handling Optional Packages
==========================

The ``setuptools``, ``flit``, and ``poetry`` build systems all allow you to
declare dependencies that only get installed under specific circumstances. This
makes it convenient to declare dependencies for ancillary functions such as
"plotting", "tests", or "docs". This allows you to pragmatically integrate
optional dependencies which can be installed as optional requirements rather
than individual packages.

You may want to have optional packages for your pyansys library for a variety
of reasons, including:

- **Not all users will want to use the feature.** - For example, you might want
  to make the usage of `matplotlib <https://matplotlib.org/`_ or `pyvista
  <https://docs.pyvista.org/>`_ if you expect your pyansys library to be used
  primarily for headless scripting rather than visualization.
- **Not all users can install the optional package.** - For certain less popular
  or obscure environments, some binary wheels may not be available or
  compatible with the user's environment. For example, if they're using CentOS
  6.9 and need a ``manylinux1`` but the package only supports ``manylinux2014``
  (CentOS 7+) or newer, their environment wouldn't be able to run the pyansys
  library.
- **Reducing Dependency Bloat** - Removing the package as a "required"
  dependency reduces the number of packages installed at install-time, speeding
  up the install and reducing the possibility of dependency conflicts. The
  trade-off here is any user who wishes to access features which require the
  optional package will have to install it piecemeal.

If you choose to implement optional packages for your pyansys library, here are
some helpful best-practices to follow.


Implementing Optional Packages in the Build System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Here's how to implement and use optional requirements for the three most
popular build systems.

.. tabs::

   .. tab:: poetry

      .. code-block::

         [tool.poetry.extras]
         all = [
             "matplotlib",
             "pyvista",
             "pyside",
         ]
         plotting = [
             "matplotlib",
             "pyvista",
         ]
         qt = [
             "pyside",
         ]

         Install ``package-name`` with the optional ``qt`` packages with:

         .. code-block::

            poetry install --extras "plotting qt"

   .. tab:: flit

      .. code-block::

         [project.optional-dependencies]
         all = [
             "matplotlib",
             "pyvista",
             "pyside",
         ]
         plotting = [
             "matplotlib",
             "pyvista",
         ]
         qt = [
             "pyside",
         ]

         Install ``package-name`` with the optional ``qt`` packages with:

         .. code-block::

            pip install package-name --extras=all

   .. tab:: setuptools

      .. code-block:: python

         from setuptools import setup

         setup(
             ...
             extras_require={
                'all': ['matplotlib', 'pyvista', 'pyside'],
                'plotting': ['matplotlib', 'pyvista'],
                 'qt': ['pyside'],
             },
             ...
         )

         Install ``package-name`` with the optional ``qt`` packages with:

         .. code-block::

            pip install package-name[qt]


Implementing Optional Libraries in Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
One of the best ways to implement an optional dependency is to execute a "lazy
import" at runtime for the feature in question. For example, if your library
has an optional dependency on ``matplotlib``, you can implement it with:

.. code:: python

   def plot(x, y):
       """Plot two numpy arrays.

       Parameters
       ----------
       x : numpy.ndarray
           Numpy array sized (n, ).
       y : numpy.ndarray
           Numpy array sized (n, ).

       Notes
       -----
       This function requires ``matplotlib``.

       """
       try:
           import matplotlib.pyplot as plt
       except ModuleNotFoundError:  # pragma: no cover
           raise ModuleNotFoundError(
               "Please install matplotlib to use this feature with:\n\n"
               "pip install matplotlib"
           )
       plt.plot(x, y)

Note that the import statement is within the method and not at the module
level. Normally this is a bad practice as this can cause runtime errors, but
for optional features where the user isn't expected to have the library
installed, this is one of the best ways of handling it. Otherwise, the pyansys
library might fail to import as the optional package might not be installed.

Also note how this code snippet adds a helpful note `ModuleNotFoundError
<https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError`_ rather
than simply letting the error to be raised. This lets the user know that this
error is expected as the feature relies on an optional dependency.

If you have many methods that rely on an optional feature, you can implement a
`decorator <https://realpython.com/primer-on-python-decorators/>`_ to make it
easier to add these lazy imports and helpful error messages. For example:

.. code:: python

   from functools import wraps
   import importlib
   import warnings


   def requires_package(package_name, raise_error=False):
       """
       Check if a package is installed by importing it.

       Parameters
       ----------
       package_name : str
           Name of the package.
       raise_error : bool, optional
           Raise a ``ModuleNotFoundError`` is the package is not installed.

       Raises
       ------
       ModuleNotFoundError
           Raise when a package is not installed and ``raise_error`` is True.

       """

       def decorator(function):
           @wraps(function)
           def wrapper(self, *args, **kwargs):

               try:
                   importlib.import_module(package_name)
                   return function(self, *args, **kwargs)

               except ModuleNotFoundError:
                   msg = (
                       f"To use the method '{function.__name__}', "
                       f"the package '{package_name}' is required.\n"
                       f"Please try to install '{package_name}' with:\n"
                       f"pip install {package_name.replace('.','-') if 'ansys' in package_name else package_name}"
                   )

                   if raise_error:
                       raise ModuleNotFoundError(msg)
                   else:
                       warnings.warn(msg)
                       return

           return wrapper

       return decorator

Which is used within a class method with:

.. code:: python

    class MyClass:

        def __init__(self, sz):
            self._a = np.arange(sz)
            self._b = np.arange(sz)

        @requires_package('emoo')
        def plot(self):
            """Plot the internal arrays ``_a`` and ``_b``.

            Notes
            -----
            This method requires ``matplotlib``.

            """
            import matplotlib.pyplot as plt
            plt.plot(self._a, self._b)


In practice, if the user does not have ``matplotlib`` installed, this is the
behavior they would expect:

.. code:: python

   >>> my_inst = MyClass(10)
   >>> my_inst.plot()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>

   ModuleNotFoundError: To use the method 'plot', the package 'matplotlib' is required.

   Please try to install 'matplotlib' with:
   pip install matplotlib
