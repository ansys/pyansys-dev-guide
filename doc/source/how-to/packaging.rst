Packaging
=========

Packaging is the process for distributing software to guarantee that final users
can use it. By packaging Python libraries, it is possible to declare which
source code or binary files must be distributed, project metadata, and
third-party dependencies.

:ref:`Packaging style` collects the fundamentals of Python packaging and packaging style
guidelines that apply to PyAnsys projects.

Dependencies
------------

It is common to take advantage of third-party libraries to simplify
source code. The formal way of doing so is by specifying these third-party
libraries as dependencies. There are two types of dependencies: :ref:`Required
dependencies` and :ref:`Optional dependencies`.

Required dependencies
~~~~~~~~~~~~~~~~~~~~~

Required dependencies are third-party libraries that a software requires to
properly function. If these dependencies are not installed or present, the
software does not work as expected.

Required dependencies must be declared in :ref:`The \`\`setup.py\`\` file` or
in :ref:`The \`\`pyproject.toml\`\` file`, according to the 
selected :ref:`Build system`:

.. tab-set::

    .. tab-item:: flit

        .. code-block:: toml

            [project]
            dependencies = [
                "ansys-api-service==X.Y.Z",
                "matplotlib>=3.5.2",
                "numpy",
            ]

    .. tab-item:: poetry

        .. code-block:: toml

            [tool.poetry.dependencies]
            ansys-api-service = "^X.Y.Z"
            matplotlib = "^3.5.2"
            numpy = "*"

    .. tab-item:: setuptools

        .. code-block:: python

            from setuptools import setup

            setup(
                ...,
                install_requires=[
                    "ansys-api-service==X.Y.Z",
                    "matplotlib >= 3.5.2",
                    "numpy",
                    ...,
                ],
            )

Optional dependencies
~~~~~~~~~~~~~~~~~~~~~

Optional dependencies are third-party libraries without which a software is not
able to execute particular features. This makes it convenient to declare
dependencies for ancillary functions such as plotting, tests, or documentation. You
can programmatically integrate dependencies that are to be installed as optional
requirements rather than individual packages.

You may want to have optional packages for your PyAnsys library for a variety of
reasons, including:

- **Not all users want to use the feature.** For example, you might want
  to make using `Matplotlib <https://matplotlib.org/>`_ or `PyVista
  <https://docs.pyvista.org/>`_ optional if you expect your PyAnsys library is
  to be used primarily for headless scripting rather than visualization.

- **Not all users can install the optional package.** For certain less popular
  or obscure environments, some binary wheels might not be available or compatible
  with the user's environment. For example, if a user of CentOS 6.9 needs to
  have the ``manylinux1`` package but CentOS 6.9 only supports ``manylinux2014`` (CentOS
  7+ and later), the user's environment wouldn't be able to run the PyAnsys
  library.

- **Reduce dependency bloat.** Removing the package as a "required"
  dependency reduces the number of packages to install at installation time,
  speeding up the installation and reducing the possibility of dependency
  conflicts. The trade-off here is that any user who wants to access features that
  require the optional package must install it separately.

If you choose to implement optional packages for your PyAnsys library, some helpful
best practices follow.

Implement optional packages in the build system
+++++++++++++++++++++++++++++++++++++++++++++++

The following code snippets show how to implement and use optional requirements for
the three most popular build systems:

.. tab-set::

   .. tab-item:: flit

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

      Install ``package-name`` with the optional ``qt`` packages with this command

      .. code-block:: text

          pip install package-name --extras=all

   .. tab-item:: poetry

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

      Install ``package-name`` with the optional ``qt`` packages with this command:

      .. code-block:: text

          poetry install --extras "plotting qt"


   .. tab-item:: setuptools

      .. code-block:: python

         from setuptools import setup

         setup(
             ...,
             extras_require={
                 "all": ["matplotlib", "pyvista", "pyside"],
                 "plotting": ["matplotlib", "pyvista"],
                 "qt": ["pyside"],
             },
             ...,
         )

      Install ``package-name`` with the optional ``qt`` packages with this command:

      .. code-block:: text

          pip install package-name[qt]

Implement optional libraries in features
++++++++++++++++++++++++++++++++++++++++

One of the best ways to implement an optional dependency is to execute a *lazy
import* at runtime for the feature in question. For example, if your library
has an optional dependency on Matplotlib, you can implement it like this:

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
easier to add these lazy imports and helpful error messages. Here is an example:

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

You use the decorator with a method like this:

.. code:: python

    class MyClass:
        def __init__(self, sz):
            self._a = np.arange(sz)
            self._b = np.arange(sz)

        @requires_package("emoo")
        def plot(self):
            """Plot the internal arrays ``_a`` and ``_b``.

            Notes
            -----
            This method requires ``matplotlib``.

            """
            import matplotlib.pyplot as plt

            plt.plot(self._a, self._b)


In practice, if the user does not have Matplotlib installed, this is the
behavior that the user would expect:

.. code-block:: pycon

   >>> my_inst = MyClass(10)
   >>> my_inst.plot()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>

   ModuleNotFoundError: To use the method 'plot', the package 'matplotlib' is required.

   Install 'matplotlib' with:
   pip install matplotlib

Dependabot
----------

Dependabot is a built-in tool for keeping project dependencies updated. It informs
you of the latest releases of the packages being used.

The ``dependabot.yml`` file
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dependabot version updates are performed by checking a ``dependabot.yml``
configuration file into your repository. In this file, one should specify the
location of the project's requirement files, so that Dependabot knows where to
look. On top of that, Dependabot is also capable of updating GitHub actions
versions.

The following code snippets show the required configuration for Dependabot
according to the type of file in which the dependencies are specified:

.. tab-set::

    .. tab-item:: With requirements/\*.txt

        .. code:: yaml
    
            version: 2
            updates:
            - package-ecosystem: "pip" # See documentation for possible values
                directory: "/requirements" # Location of package manifests
                schedule:
                    interval: "daily"
            - package-ecosystem: "github-actions"
              directory: "/"
              schedule:
                interval: "daily"

    .. tab-item:: With pyproject.toml

        .. code:: yaml

            version: 2
            updates:
            - package-ecosystem: "pip" # See documentation for possible values
                directory: "pyproject.toml" # Location of package manifests
                schedule:
                    interval: "daily"
            - package-ecosystem: "github-actions"
              directory: "/"
              schedule:
                interval: "daily"

    .. tab-item:: With setup.py

        .. code:: yaml

            version: 2
            updates:
            - package-ecosystem: "pip" # See documentation for possible values
                directory: "setup.py" # Location of package manifests
                schedule:
                    interval: "daily"
            - package-ecosystem: "github-actions"
              directory: "/"
              schedule:
                interval: "daily"

        
This file should be located in the ``.github`` folder of your repository for
GitHub to detect it automatically. There are several main options:

* **package-ecosystem**: Lets Dependabot know what your package manager is.
  PyAnsys projects typically use ``pip``. However, ``conda`` could also be used.
* **directory**: Lets Dependabot know where your requirement files are located.
  PyAnsys projects typically contain all their requirements inside a ``requirements``
  directory. Other directories could be used.
* **schedule**: Lets Dependabot know the frequency to perform subroutines
  for checking for updates.

Dependabot updates
~~~~~~~~~~~~~~~~~~

Dependabot determines (using semantic versioning) whether a requirement should
be updated due to the existence of a newer version. When Dependabot identifies
an outdated dependency, it raises a pull request to update these requirement
files.

Dependabot allows for two different types of updates:

* **Dependabot security updates**: Automated pull requests that help update
  dependencies with known vulnerabilities.
* **Dependabot version updates**: Automated pull requests that keep dependencies updated,
  even when they don’t have any vulnerabilities. To check the status of version updates,
  navigate to the **Insights** tab of your repository and then select **Dependency Graph**
  and **Dependabot**.


.. caution::

    Dependabot only works for *pinned-down* versions of requirements (or, at most, versions
    with an *upper-limits* requirement such as ``pyvista <= 0.34.0``). However, this is not
    a best practice for *run-time* dependencies (that is, the usage of a package should support
    the oldest available version if possible). Thus, it is only recommended to fully pin
    **documentation** and **testing** requirements (that is, using ``==``). Having the latest
    dependencies available in your requirements testing files lets you test the
    *latest* packages against your library.

Dependabot version updates
~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable version updates for your repository, see
`Enabling Dependabot version updates
<https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#enabling-dependabot-version-updates>`_
in the GitHub documentation.

Dependabot security updates
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dependabot security updates make it easier for you to fix vulnerable dependencies in your
repository. If you enable this feature, when a Dependabot alert is raised for a vulnerable
dependency in the dependency graph of your repository, Dependabot automatically tries to fix it.

For information on enabling security updates and notifications for your repository, see
`Enabling or disabling Dependabot security updates for an individual repository
<https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#enabling-or-disabling-dependabot-security-updates-for-an-individual-repository>`_
in the GitHub documentation.
