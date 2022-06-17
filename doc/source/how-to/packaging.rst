Packaging
=========
Packaging is the process for distributing software to guarantee that final users
can use it. By packaging Python libraries, it is possible to declare which
source code or binary files need to be distributed, project metadata and third
party dependencies.


The fundamentals of Python packaging together with the packaging style
guidelines that apply to PyAnsys projects are collected in :ref:`Packaging
Style` chapter.


Specifying Dependencies
-----------------------
It is common to take advantage of third party libraries in order to simplify
source code. The formal way of doing so is by specifying these third party
libraries as dependencies. There are two types of dependencies: :ref:`Required
Dependencies` and :ref:`Optional Dependencies`.

Required Dependencies
~~~~~~~~~~~~~~~~~~~~~
Required dependencies are third party libraries that a software requires to
properly function. If these dependencies are not installed or present, the
software will not work as expected.

Required dependencies need to be declared in :ref:`The \`\`setup.py\`\` File` or
in :ref:`The \`\`pyproject.toml\`\` File`, according to the selected :ref:`Build
System`:


.. tabs::

    .. group-tab:: flit

        .. code-block:: toml

            [project]
            dependencies = [
                "matplotlib >= 3.5.2",
                "numpy",
                ...
            ]

    .. group-tab:: poetry

        .. code-block:: toml

            [tool.poetry.dependencies]
            matplotlib = "^3.5.2"
            numpy = "*"
            ...

    .. group-tab:: setuptools

        .. code-block:: python

            from setuptools import setup

            setup(
                ...
                install_requires=[
                    "matplotlib >= 3.5.2",
                    "numpy",
                    ...
                ]
            )


Optional Dependencies
~~~~~~~~~~~~~~~~~~~~~
Optional dependencies are third party libraries without which a software is not
able to execute particular features. This makes it convenient to declare
dependencies for ancillary functions such as "plotting", "tests", or "docs". You
can programmatically integrate dependencies that can be installed as optional
requirements rather than individual packages.

You may want to have optional packages for your PyAnsys library for a variety of
reasons, including:

- **Not all users will want to use the feature.** - For example, you might want
  to make using `matplotlib <https://matplotlib.org/>`_ or `pyvista
  <https://docs.pyvista.org/>`_ optional if you expect your PyAnsys library is
  to be used primarily for headless scripting rather than visualization.

- **Not all users can install the optional package.** - For certain less popular
  or obscure environments, some binary wheels may not be available or compatible
  with the user's environment. For example, if a user of CentOS 6.9 needs to
  have ``manylinux1`` but the package only supports ``manylinux2014`` (CentOS
  7+) or newer, the user's environment wouldn't be able to run the PyAnsys
  library.

- **Reducing dependency bloat** - Removing the package as a "required"
  dependency reduces the number of packages to install at installation -time,
  speeding up the installation and reducing the possibility of dependency
  conflicts. The trade-off here is any user who wants to access features that
  require the optional package will have to install it piecemeal.

If you choose to implement optional packages for your PyAnsys library, here are
some helpful best practices to follow.


Implementing Optional Packages in the Build System
++++++++++++++++++++++++++++++++++++++++++++++++++
Here's how to implement and use optional requirements for the three most
popular build systems:

.. tabs::

   .. group-tab:: flit

      .. code-block:: toml

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

      .. code-block:: text

          pip install package-name --extras=all

   .. group-tab:: poetry

      .. code-block:: toml

         ...
         [tool.poetry.dependencies]
         matplotlib = {version = "^3.5", optional = true}
         pyvista = {version = "^0.32", optional = true}
         pyside = {version = "^1.2", optional = true}
         ...

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

      .. code-block:: text

          poetry install --extras "plotting qt"


   .. group-tab:: setuptools

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

      .. code-block:: text

          pip install package-name[qt]


Implementing Optional Libraries in Features
+++++++++++++++++++++++++++++++++++++++++++
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
               "To use this feature, install 'matplotlib' with:\n\n"
               "pip install matplotlib"
           )
       plt.plot(x, y)

Note that the ``import`` statement is within the method and not at the module
level. Normally this is a bad practice because it can cause runtime errors. However,
for optional features where the user isn't expected to have the library
installed, this is one of the best ways of handling it. Otherwise, the PyAnsys
library might fail to import because the optional package might not be installed.

Also note how this code snippet adds a helpful `ModuleNotFoundError
<https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError>`_ rather
than simply allowing the error to be raised. This lets the user know that this
error is expected because the feature relies on an optional dependency.

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
           Raise ``ModuleNotFoundError`` if the package is not installed. The default
           is ``False``.

       Raises
       ------
       ModuleNotFoundError
           Raise when a package is not installed and ``raise_error=True``.

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
                       f"Install '{package_name}' with:\n"
                       f"pip install {package_name.replace('.','-') if 'ansys' in package_name else package_name}"
                   )

                   if raise_error:
                       raise ModuleNotFoundError(msg)
                   else:
                       warnings.warn(msg)
                       return

           return wrapper

       return decorator

You use the decorator with a method with:

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
behavior that the user would expect:

.. code-block:: pycon

   >>> my_inst = MyClass(10)
   >>> my_inst.plot()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>

   ModuleNotFoundError: To use the method 'plot', the package 'matplotlib' is required.

   Install 'matplotlib' with:
   pip install matplotlib
