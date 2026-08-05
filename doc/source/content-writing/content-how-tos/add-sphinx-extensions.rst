.. _add_sphinx_extensions:

Add Sphinx extensions
=====================

The Sphinx configuration (``doc/source/conf.py``) file contains an ``extensions``
variable that specifies the list of extensions that are configured for use by
Sphinx when generating documentation. When the `Ansys templates <Ansys_templates_>`_
tool is used to create a PyAnsys project from the ``pyansys`` or ``pyansys-advanced``
template, the ``extensions`` variable lists these extensions by default:

.. code::

    # Sphinx extensions
    extensions = [
        "sphinx.ext.autodoc",
        "sphinx.ext.autosummary",
        "numpydoc",
        "sphinx.ext.intersphinx",
        "sphinx_copybutton",
    ]

Extensions with names beginning with ``sphinx_ext`` are native (built-in) and are
available for Sphinx's use without any additional installation. Extensions with names
that do not begin with ``sphinx_ext`` are external extensions and require installation.
If a non-native extension is not installed but added to the :file:`conf.py` file in the
``doc/source`` directory, attempts to build the documentation fail because Sphinx cannot
find the needed extension.

.. _links_to_objects_in_other_doc:

Link to Python objects in other Sphinx documentation
----------------------------------------------------

The ``sphinx.ext.intersphinx`` extension is configured by default in your project's
:file:`conf.py` file so that you can link to Python objects in other Sphinx documentation.
The ``intersphinx_mapping`` variable specifies the URIs for the Sphinx documentation with
the objects that you want to link to.

For example, this ``intersphinx_mapping`` variable provides mappings to the Sphinx documentation
for several other projects:

.. code::

   # Intersphinx mapping
   intersphinx_mapping = {
       "python": ("https://docs.python.org/3/", None),
        "scipy": ("https://docs.scipy.org/doc/scipy/", None),
        "numpy": ("https://numpy.org/doc/stable/", None),
        "matplotlib": ("https://matplotlib.org/stable/", None),
        "pandas": ("https://pandas.pydata.org/docs/", None),
        "pyvista": ("https://docs.pyvista.org/version/stable/", None),
        "grpc": ("https://grpc.github.io/grpc/python/", None),
        "pypim": ("https://pypim.docs.pyansys.com/version/dev/", None),
        "ansys-dpf-core": ("https://dpf.docs.pyansys.com/version/stable/", None),
        "ansys-math-core": ("https://math.docs.pyansys.com/version/stable/", None),
   }

To be able to link to a Python object in other Sphinx documentation, the object must be part
of that documentation's inventory (:file:`object.inv`) file. You map the target (base URI of
the external documentation or the local path) to the documentation's :file:`object.inv`
file. The keyword ``None`` indicates that this file is found at the same location. If it is not,
you must supply the appropriate URI.

Given that a target for a Python object exists in the Sphinx documentation that you want to
link to, you can link to it using the same roles that you use to link to a Python object in
your documentation. Here are some examples:

- SciPy ``odeint()`` function:

  - ``:func:`odeint() <scipy.integrate.odeint>` odeint()``
  - ``:func:`scipy.integrate.odeint` scipy.integrate.odeint()``

- SciPy ``quad()`` function:

  - ``:func:`quad() <scipy.integrate.quad>` quad()``
  - ``:func:`scipy.integrate.quad` scipy.integrate.quad()``

- Matplotlib ``hist()`` method:

  - ``:meth:`hist() <matplotlib.axes.Axes.hist>` hist()``
  - ``:meth:`matplotlib.axes.Axes.hist` matplotlib.axes.Axes.hist()``

- NumPy module:

  - ``:mod:`numpy <numpy>` numpy``
  -  ``:mod:`numpy` numpy``

- NumPy ``matrix`` class:

  - ``:class:`matrix <numpy.matrix>` matrix``
  - ``:class:`numpy.matrix.` numpy.matrix``

- NumPy matrix attribute shape:

  - ``:attr:`shape() <numpy.ndarray.shape>` shape()``
  - ``:attr:`numpy.ndarray.shape` numpy.ndarray.shape``

For more information, see :ref:`API_object_links`.

.. _add_native_sphinx_ext:

Add a native extension
----------------------

To use the special features provided by a native Sphinx extension, you only need to add
the extension to the ``extensions`` variable in the project's :file:`conf.py`
file.

For example, the native ``sphinx.ext.todo`` extension was added to the ``extensions``
variable in the :file:`conf.py` file for this guide. This extension supports
use of the ``todo`` directive to create a specially formatted block of text for
a task that must still be done. The blocks for ``todo`` directives do not render
in the documentation by default. However, to render them in the documentation, you
can add a ``todo_include_todos`` variable to the :file:`conf.py` file and then set
this variable to ``True``.

Add an external extension
-------------------------

To use the special features provided by an external Sphinx extension is a bit
more complicated. You must install the extension in your development environment and then
add it to both the project's :file:`conf.py` and its list of documentation requirements.

For example, to use cards and tab sets in your documentation, you must install and configure
the external `sphinx-design <Sphinx_ext_sphinx_design_>`_ extension for use:

#. If the Ansys Python Manager and **Administrator** window are not still
   open, open them.
#. From the **Administrator** window's command prompt, run the command
   for installing the external extension in your development environment::

     python -m pip install <external-extension-name>

   Examples follow for some of the external extensions mentioned in this
   documentation.
   
   - To install the external ``sphinx-design`` extension, run this command::
    
        python -m pip install sphinx-design

   - To install the external ``sphinx_toolbox.collapse`` extension, run this command::

        python -m pip install sphinx_toolbox.collapse

#. Add the external extension to the ``extensions`` variable in your project's
   :file:`conf.py` file.

#. Add the external extension to your project's documentation requirements as indicated
   in the next topic.

.. _doc_ext_requirements:

Add the extension to the documentation requirements
---------------------------------------------------

Documentation requirements list the ``pip`` packages that Sphinx requires for
building the documentation. Depending on the project's configuration, you list these
packages in either the :file:`pyproject.toml` file or the :file:`requirements_doc_txt`
file.

The ``pyproject.toml`` file
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most projects specify documentation requirements in a :file:`pyproject.toml` file, which
resides in the root folder. In this file, the ``doc`` variable defines the required ``pip``
packages and their versions like this.

.. code::

   doc = [
       "ansys-sphinx-theme==0.12.3",
       "docker==6.1.3",
       "ipyvtklink==0.2.3",
       "jupyter_sphinx==0.4.0",
       "jupytext==1.15.2",
       "myst-parser==2.0.0",
       "nbconvert==7.9.2",
       "nbsphinx==0.9.3",
       "notebook==7.0.5",
       "numpydoc==1.6.0",
       "panel==1.2.3",
       "pyvista[trame]==0.41.1",
       "requests==2.31.0",
       "sphinx==7.2.5",
       "sphinx-autoapi==3.0.0",
       "sphinx-autodoc-typehints==1.24.0",
       "sphinx-copybutton==0.5.2",
       "sphinx_design==0.5.0",
       "sphinx-jinja==2.0.2",
       "vtk==9.2.6",
   ]

The ``requirements_doc_txt`` file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some projects specify documentation requirements in a :file:`requirements_doc_txt`
file. The root folder of such a project typically has a ``requirements`` directory
that contains this TXT file, which defines the required ``pip`` packages and their
versions like this:

.. code::

   Sphinx==7.1.2
   jupyter_sphinx==0.4.0
   numpydoc==1.5.0
   matplotlib==3.7.2
   ansys-sphinx-theme==0.10.2
   pypandoc==1.11
   pytest-sphinx==0.5.0
   sphinx-autobuild==2021.3.14
   sphinx-autodoc-typehints==1.24.0
   sphinx-copybutton==0.5.2
   sphinx-gallery==0.13.0
   sphinx-notfound-page==0.8.3
   sphinxcontrib-websupport==1.2.5
   sphinxemoji==0.2.0
   autodocsumm==0.2.11

Learn more about extensions
---------------------------

As you can see, PyAnsys projects add many extensions to their :file:`conf.py` files
and documentation requirements. Here are some other native and non-native extensions
that you might see:

- ``sphinx.ext.coverage``
- ``sphinx.ext.doctest``
- ``sphinx.ext.extlinks``
- ``sphinx.ext.graphviz``
- ``sphinx.ext.napoleon``
- ``sphinx.ext.viewcode``
- ``sphinx_toolbox.collapse``

For more information on extensions, see `Extensions <Sphinx_extensions_>`_ in the
Sphinx documentation. In addition to the external (third-party) extensions collected
in the `sphinx-contrib <Sphinx_contrib_org_>`_ organization, you can search the internet
to find other Sphinx extensions or learn more about the ones in the preceding list.
