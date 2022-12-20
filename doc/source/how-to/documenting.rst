Documenting
===========
PyAnsys documentation must not only be written but also maintained. If you are
new to writing developer documentation, see the `Google Developer Documentation
Style Guide <https://developers.google.com/style>`_. It provides
editorial guidelines for writing clear and consistent developer documentation,
allowing this guide to supply guidance only specific to PyAnsys library
documentation.

When writing developer documentation, the relationship between code and
documentation is key. To keep documentation up to date with evolving
code:

- Minimize the content footprint.
- Write `timeless documentation <https://developers.google.com/style/timeless-documentation>`_.
- Support contributions from both inside and outside of the development team.
- Perform periodic reviews.

Documentation sources
---------------------
.. raw:: html

    <div align="center">
      <img src="https://www.sphinx-doc.org/en/master/_static/sphinxheader.png">
    </div>
    <br>

The generation of PyAnsys documentation uses `Sphinx
<https://www.sphinx-doc.org/en/master/>`__ and an Ansys-branded theme
(`ansys-sphinx-theme <https://github.com/ansys/Sansys-sphinx-theme>`_) to
assemble content in:

- Docstrings
- reStructuredText (RST) files
- Python (PY) example files

Docstrings
~~~~~~~~~~
Docstrings must be formatted so that Sphinx can parse them. Sphinx provides
these extensions for docstring formatting:

- `numpydoc <https://pypi.org/project/numpydoc/>`_
- `napoleon <https://pypi.org/project/sphinxcontrib-napoleon/>`_

Using the ``numpydoc`` extension is preferred because it supports an API
documentation structure with one page per method, providing Python community
members with documentation like that generated for the `pandas <https://pandas.pydata.org/>`_
and `numpy <https://numpy.org/>`_ packages. If your API is very linear, you
can use the ``napoleon`` extension because it supports a documentation
structure where everything needed to solve a certain problem can be shown on one page.

The ``numpydoc`` extension provides its own `style guide
<https://numpydoc.readthedocs.io/en/latest/format.html>`_ and a `user guide
<https://numpydoc.readthedocs.io/en/latest/>`_ that explains how to use the
extension with Sphinx. The ``napoleon`` extension, which parses both numpydoc and
Google style docstrings, refers you to the `Google Python Style Guide
<https://google.github.io/styleguide/pyguide.html>`_.

Regardless of the extension that you choose for generating documentation, using
numpy-style docstrings ensures that there is consistency within PyAnsys libraries.
For more information, see :ref:`Documentation style`.

RST files
~~~~~~~~~
To provide general usage information in your documentation, use your favorite
editor to create RST (ReStructured Text) files that you then place in :ref:`The \`\`doc/\`\`
directory` directory. The ``index.rst`` file in the ``doc/source`` directory
defines the first level of your documentation hierarchy. The ``toctree``
directive (which stands for "table of contents tree") indicates the maximum
number of heading levels that the documentation is to display. Following this
directive are the directory names for your documentation sections.

.. include:: diag/doc_layout.rst

Each documentation section has its own ``index.rst`` file, as shown by the preceding
figure. The documentation layout can be modeled using the following code in
each one of the ``index.rst`` files.

.. tab-set::

    .. tab-item:: index.rst

        .. code-block:: rst

            Welcome to the Library Documentation
            ####################################

            This is the content of the root `index.rst` file.

            .. toctree::

                section_A/index
                section_B/index

    .. tab-item:: section_A/index.rst

        .. code-block:: rst

            Section A
            #########

            This is the content of the `section_A/index.rst` file.

            .. toctree::

                section_1
                section_2
                ...

    .. tab-item:: section_B/index.rst

        .. code-block:: rst

            Section B
            #########

            This is the content of the `section_B/index.rst` file.

            .. toctree::

                another_section
                ...

While you do not include the ``.rst`` extension when defining the section
structure, the index file referenced for each section must be named
``index.rst``.

After you build documentation locally as described in :ref:`Build
documentation`, the first-level heading in the ``index.rst`` file for each
section is shown as a clickable link in the header of the
documentation's generated HTML output. For more information on defining a
documentation structure, see the `Sphinx Getting Started
<https://www.sphinx-doc.org/en/master/usage/quickstart.html>`_ guide.

Indicating RST titles
+++++++++++++++++++++
Within RST files, heading titles are to use sentence case per
`capitalization guidelines <https://developers.google.com/style/capitalization>`_
in the *Google Developer Documentation Style Guide*. The line that follows
the heading title must have a string of characters that is the same length
as the heading title. If the length of the characters under the heading title
do not match the length of the heading title, Sphinx generates a warning.

For consistency within PyAnsys libraries, the use of these special characters
is recommended for headings but is not enforced:

- For section-level headings, use ``###``.
- For subsection-level headings, use ``===``.
- For subsubsection-level headings, use ``---``.
- For subsubsubsection-level headings, use ``~~~``.
- For paragraph-level headings, use ``+++``.

For comprehensive syntax information, see the `reStrucutredText Markup Specification
<https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`_.

Because you need to be familiar with the content in the `PyAnsys Developer's
Guide <dev.docs.pyansys.com/>`_, explore its HTML pages and then the RST files
in its `repository <https://github.com/pyansys/dev-guide>`_. This should help
you to understand the syntax and see how RST files are nested to create this guide.

Recommended sections
++++++++++++++++++++
Although each project is different, documentation has the same goal: providing
instructions and guidelines for users. Thus, you can find some common sections
across the documentation for PyAnsys libraries. Try to include these top-level
sections in your library documentation:

- ``Getting started`` explains how to install and set up the library.
- ``User guide`` describes how to use basic features of the library.
- ``API reference`` documents API resources provided by the library.
- ``Examples`` provides fully fledged examples for using the library.
- ``Contributing`` refers to the `PyAnsys Developer's Guide <dev.docs.pyansys.com/>`_
  for overall guidance and provides library-specific contribution information.


Examples
~~~~~~~~
Examples come in two formats:

- Basic code snippets demonstrating the feature
- Full-fledged standalone examples that are meant to be run as downloadable scripts

Place basic code snippets in the ``doc/source/`` directory.
Place full-fledged standalone examples in the ``examples/`` directory
at the root of the repository. All of these examples must be compliant
with :ref:`PEP 8`. They are compiled dynamically during the build process.
Always ensure that your examples run properly locally because they are
verified through the CI performed via GitHub Actions.

Adding a new standalone example consists of placing it in an applicable
subdirectory in the ``examples/`` directory. If none of the existing directories
match the category of your example, create a new subdirectory with a
``README.txt`` file describing the new category which implies 
the Python project has the following structure:

.. code-block:: text

    .
    ├── doc
    │   ├── conf.py
    │   ├── index.rst
    |   ├── make.bat
    │   └── Makefile
    ├── my_python_module
    │   ├── __init__.py
    │   └── mod.py
    └── examples
        ├── plot_example.py
        ├── example.py
        └── README.txt (or .rst)


Enable the Sphinx-Gallery in the Sphinx doc/conf.py file with:

.. code:: Python

    extensions = [
        ...
        'sphinx_gallery.gen_gallery',
        ]

The following configuration declares the location of the `examples` directory 
to be ``../examples`` and the `output` directory to be ``examples``:

.. code:: Python

    sphinx_gallery_conf = {
     'examples_dirs': '../examples',   # path to your example scripts
     'gallery_dirs': 'examples',  # path where the gallery generated output will be saved
    }

Because these examples are
built using the `Sphinx-Gallery
<https://sphinx-gallery.github.io/stable/index.html>`_ extension, you must
follow its `coding guidelines
<https://sphinx-gallery.github.io/stable/index.html>`_.

Using python, here is a :ref:`General example` using sphinx gallery.

Document Python code
--------------------
You can use `sphinx.ext.autodoc` to generate documentation from your Python
code. When using this extension, you can include these directives in your :ref:`RST files`:

* ``automodule`` for documenting modules
* ``autoclass`` for documenting classes
* ``autofunction`` for documenting methods and functions

For a full list of auto-directives, see `Include Documentation From Docstrings
<https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_.


Document classes
~~~~~~~~~~~~~~~~
There are two main ways of using Sphinx to document a class:

* Manually describe 'how' and 'why' you use a class in :ref:`RST files`.

* Automatically generate documentation for classes using the ``autoclass`` or
  ``autosummary`` directive in :ref:`RST files`.

Manually generate documentation
+++++++++++++++++++++++++++++++
To describe 'why' and 'how' you use a class within :ref:`RST files`, use the
``code-block`` directive:

.. tab-set::

    .. tab-item:: Doc Source Code

        .. code-block:: rst

            Initialize ``my_module.MyClass`` with initial parameters. These
            parameters are automatically assigned to the class.

            .. code-block:: pycon

               >>> from my_module import MyClass
               >>> my_obj = MyClass(parm1='apple', parm2='orange')
               >>> my_obj.parm1
               'apple'

    .. tab-item:: Rendered Doc

        Initialize ``my_module.MyClass`` with initial parameters. These
        parameters are automatically assigned to the class.

        .. code-block:: pycon

           >>> from my_module import MyClass
           >>> my_obj = MyClass(parm1='apple', parm2='orange')
           >>> my_obj.parm1
           'apple'

Automatically generate documentation
++++++++++++++++++++++++++++++++++++
To automatically generate class descriptions from the numpydoc strings in
your Python files, use either the ``autoclass`` or ``autosummary`` directive
in your :ref:`RST files`. For information on docstrings and required docstring
sections, see  :ref:`Numpydoc docstrings`.  

For simple classes, use the ``autoclass`` directive:


.. tab-set::

    .. tab-item:: Doc Source Code

        .. code-block:: rst

            .. autoclass:: ansys_sphinx_theme.samples.ExampleClass
               :members:

    .. tab-item:: Rendered Doc

        .. autoclass:: ansys_sphinx_theme.samples.ExampleClass
            :members:


For complex classes with many methods, use the
``autosummary`` directive:

.. tab-set::

    .. tab-item:: Doc Source Code

        .. code-block:: rst

            .. autoclass:: ansys_sphinx_theme.samples.Complex

            .. autosummary::
               :toctree: api/

               ansys_sphinx_theme.samples.Complex.real
               ansys_sphinx_theme.samples.Complex.imag
               ansys_sphinx_theme.samples.Complex.abs

    .. tab-item:: Rendered Doc

        .. autoclass:: ansys_sphinx_theme.samples.Complex

        .. autosummary::

           ansys_sphinx_theme.samples.Complex.real
           ansys_sphinx_theme.samples.Complex.imag
           ansys_sphinx_theme.samples.Complex.abs

When you use the ``autosummary`` directive, each class has its own dedicated page,
and each method and attribute in that class also has its own page.

Document multiple classes
+++++++++++++++++++++++++
To document a set of small but highly cohesive classes, you can combine
the two preceding approaches. To accomplish this, you include multiple
``autoclass`` directives in the same RST file with headings and text blocks as
necessary to describe the relationships between the classes.

For example, the Granta MI BoM Analytics library uses this combined approach:
:external+grantami-bomanalytics:doc:`Part Compliance page <api/compliance/parts>`
first describes the
:external+grantami-bomanalytics:class:`~ansys.grantami.bomanalytics.queries.PartComplianceQuery`
class. It then describes the
:external+grantami-bomanalytics:class:`~ansys.grantami.bomanalytics._query_results.PartComplianceQueryResult`,
and
:external+grantami-bomanalytics:class:`~ansys.grantami.bomanalytics._item_results.PartWithComplianceResult`
classes returned by the query. Because the classes are only ever
encountered together in this context, they are documented on a
single page.

In contrast, the
:external+grantami-bomanalytics:class:`~ansys.grantami.bomanalytics.indicators.RoHSIndicator`
and
:external+grantami-bomanalytics:class:`~ansys.grantami.bomanalytics.indicators.WatchListIndicator`
classes are shared across multiple queries. Consequently, these classes are
documented separately.


Build documentation
-------------------
`Sphinx <https://www.sphinx-doc.org/en/master/>`_ is used to build the documentation.
You configure the entire build process in the ``conf.py`` file, located in the
``source/`` directory in :ref:`The \`\`doc/\`\` directory`.

This directory also contains a ``Makefile`` file and a ``make.bat`` file for
automating the building process. Different builders render different
documentation output, such as ``HTML``, ``LaTeX`` or
``PDF``.

Build HTML documentation
~~~~~~~~~~~~~~~~~~~~~~~~
You build ``HTML`` documentation with:

.. tab-set::

    .. tab-item:: Makefile

        .. code-block:: bash

            make html

    .. tab-item:: make.bat

        .. code-block:: bash

            make.bat html

The resulting ``HTML`` files are created in the ``_build/html`` directory,
located in :ref:`The \`\`doc/\`\` directory`.

You can display the HTML documentation with:

.. code-block:: text

    <browser> doc/_build/html/index.html

Build PDF documentation
~~~~~~~~~~~~~~~~~~~~~~~
To  build ``PDF`` documentation, the following rules must be added to
``Makefile`` and ``make.bat`` files:

.. tab-set::

    .. tab-item:: Makefile

        .. code-block:: text

            pdf:
	            @$(SPHINXBUILD) -M latex "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	            cd build/latex && latexmk -r latexmkrc -pdf *.tex -interaction=nonstopmode || true
	            (test -f build/latex/*.pdf && echo pdf exists) || exit 1

    .. tab-item:: make.bat

        .. code-block:: text

           :pdf
                   %SPHINXBUILD% -M latex %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
	           cd "%BUILDDIR%\latex"
	           pdflatex \*.tex --interaction=nonstopmode

You can call previous rules by running:

.. tab-set::

    .. tab-item:: Makefile

        .. code-block:: bash

            make pdf

    .. tab-item:: make.bat

        .. code-block:: bash

            make.bat pdf

The resulting PDF and intermediate LaTeX files are created in the
``_build/latex`` folder, located in :ref:`The \`\`doc/\`\` directory`.

.. admonition:: Always verify the content of your PDF file.

   Because warnings and errors that occur during the LaTeX building and rendering
   processes are ignored, it is possible that the PDF file has text formatting errors.

Enabling multi-version documentation
------------------------------------
With the release of `pyansys/actions@v2
<https://actions.docs.pyansys.com/release/2.0/index.html>`_, projects can
benefit from multi-version documentation. Projects taking advantage of this
feature need to apply different configurations according to their level of
maturity.

Follow these steps to enable multi-version documentation in your project:

- Use ``ansys-sphinx-theme>=0.8`` for building the documentation in your project.
- Include the following lines in :ref:`The \`\`conf.py\`\` file`:


  .. code-block:: python
  
      import os
  
      from ansys_sphinx_theme import get_version_match
  
  
      cname = os.getenv("DOCUMENTATION_CNAME", "<DEFAULT_CNAME>")
      """The canonical name of the webpage hosting the documentation."""
  
      html_theme_options = {
          "switcher": {
              "json_url": f"https://{cname}/release/versions.json",
              "version_match": get_version_match(__version__),
          },
          "navbar_end": ["version-switcher", "theme-switcher", "navbar-icon-links"],
          ...
      }
  
  
  .. admonition:: About the ``DCOUMENTATION_CNAME`` environment variable
  
      The ``DOCUMENTATION_CNAME`` environment variable is expected to be
      declared in the YML file controlling the deployment of the documentation.
      The idea is that the canonical name (CNAME) is only defined in a single
      place, so it can be easily changed if required.


- Create a ``gh-pages`` branch in the repository of your project.

- Create a ``release/`` directory and a ``versions.json`` containing:

  .. code-block:: json
  
      [
        {
          "version": "dev",
          "url": "https://<cname>/dev"
        }
      ]

- Enable documentation deployment for development and stable versions, see
  :ref:`Deploying documentation`.



With all the previous configuration, your project is ready to use multi-version
documentation in an automated way. This means that every time you release a
new version is it added to the drop-down button in the documentation page
of the project.

.. admonition:: Controlling the desired amount of versions showing up in the drop-down

    Only the development branch and the latest three stable versions are
    shown by default in the documentation drop-down. For showing more versions,
    use the ``render-last`` variable in the `pyansys/actions/doc-deploy-stable
    action
    <https://actions.docs.pyansys.com/release/2.0/doc-actions/index.html#doc-deploy-stable-action>`_.

.. warning::

    After enabling multi-version documentation, only new releases are
    automatically added to the ``versions.json`` file. **To show old releases,
    multi-version documentation needs to be enabled in old release branches.**


If you require support for migrating to the multi-version documentation, please
contact ``support@pyansys.com``.


Deploying documentation
-----------------------
PyAnsys libraries deploy their documentation online via `GitHub Actions`_ to
`GitHub Pages`_. This documentation is hosted on the `gh-pages`_ branch of the
repository of the project. Documentation deployment is done by uploading the
HTML documentation artifact to the `gh-pages`_ branch of the repository, see
`enabling GitHub pages`_.

Add the following workflow job to deploy both development and stable documentation
in an automated way.

.. code-block:: yaml

    env:
      DOCUMENTATION_CNAME: '<library>.docs.pyansys.com'

    jobs:

        # Artifacts for HTML documentation need to be generated before 
        # executing the deployment jobs
    
        doc-deploy-dev:
          name: "Deploy development documentation"
          # Deploy development only when merging to main
          if: github.event_name == 'push'
          runs-on: ubuntu-latest
          needs: doc-build
          steps:
            - name: "Deploy the latest documentation"
              uses: pyansys/actions/doc-deploy-dev@v2
              with:
                  doc-artifact-name: '<html-artifact-name>'
                  cname: ${{ env.DOCUMENTATION_CNAME }}
                  token: ${{ secrets.GITHUB_TOKEN }}
        
        doc-deploy-stable:
          name: "Deploy stable documentation"
          # Deploy release documentation when creating a new tag
          if: github.event_name == 'push' && contains(github.ref, 'refs/tags')
          runs-on: ubuntu-latest
          needs: doc-deploy-dev
          steps:
            - name: "Deploy the stable documentation"
              uses: pyansys/actions/doc-deploy-stable@v2
              with:
                  doc-artifact-name: '<html-artifact-name>'
                  cname: ${{ env.DOCUMENTATION_CNAME }}
                  token: ${{ secrets.GITHUB_TOKEN }}


Deploying to another repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you are planning to deploy documentation to a repository other than
the one for your project, make sure you create this new repository before deploying
your documentation for the first time.

.. warning::

    Deploying your documentation to another repository is discouraged. It
    translates to more maintenance work and does not support the multi-version
    documentation.

For deploying the documentation to another repository, use the following workflow:

.. code-block:: yaml

    doc-deploy:
      name: "Deploy documentation to a different repo"
      runs-on: ubuntu-latest
      needs: doc-build
      steps:
        - name: "Deploy documentation"
          uses: pyansys/actions/doc-deploy-to-repo@v2
          with:
            cname: "<library>.docs.pyansys.com"
            repository: "<owner>/<repository-name>"
            bot-id: ${{ secrets.BOT_APPLICATION_ID }}
            bot-token: ${{ secrets.BOT_APPLICATION_PRIVATE_KEY }}


Access online documentation
---------------------------
Documentation for the latest stable release of a PyAnsys library is accessible
from its repository. The canonical name for the documentation of the project is
constructed using the following structure:

``https://<product>.docs.pyansys.com``

You can generally access the latest development version of the documentation by
adding the prefix ``dev.`` to the URL for the latest stable release.

.. warning::

    PyAnsys projects support now multi-version documentation, meaning that
    stable and development versions are collected under the same website. A
    drop-down button for selecting desired version should be available in the
    top right corner of the navigation bar in the documentation page.

For example, consider PyAEDT documentation:

- The URL for documentation of the latest stable release is `<https://aedt.docs.pyansys.com/>`_.
- The URL for documentation of the latest development version is `<https://dev.aedt.docs.pyansys.com/>`_.

The latest development versions of both the library and its documentation are
automatically kept up-to-date via GitHub actions.

To make documentation changes, you create a branch with a name that begins with
a prefix of ``doc/`` that is then followed by a short description of what you
are changing. For more information, see :ref:`Branch model`.

As you are making changes in this branch, you want to periodically generate the
documentation locally so that you can test your changes before you create a
GitHub pull request. For more information, see :ref:`Build documentation`.


..
   Links

.. _GitHub Pages: https://pages.github.com/
.. _GitHub Actions: https://github.com/features/actions
.. _PyMAPDL Documentation: https://mapdldocs.pyansys.com/
.. _pyansys/pymapdl-docs: https://github.com/pyansys/pymapdl-docs
.. _gh-pages: https://github.com/pyansys/dev-guide/tree/gh-pages
.. _enabling GitHub pages: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site#creating-your-site
.. _tox: https://github.com/tox-dev/tox
.. _PyAnsys DNS Zones: https://portal.azure.com/#@ansys.com/resource/subscriptions/2870ae10-53f8-46b1-8971-93761377c38b/resourceGroups/pyansys/providers/Microsoft.Network/dnszones/pyansys.com/overview
.. _Maxime Rey: https://teams.microsoft.com/l/chat/0/0?users=maxime.rey@ansys.com
.. _Roberto Pastor Muela: https://teams.microsoft.com/l/chat/0/0?users=roberto.pastormuela@ansys.com
.. _Alex Kaszynski: https://teams.microsoft.com/l/chat/0/0?users=alexander.kaszynski@ansys.com
.. _PyAnsys Bot: https://github.com/apps/pyansys-bot
.. _PyAnsys Organization: https://github.com/pyansys
.. _ansys-templates: https://github.com/ansys/ansys-templates
