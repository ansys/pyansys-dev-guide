.. _documenting_developers:

Documenting
===========

PyAnsys documentation must not only be written but also maintained. If you are
new to writing PyAnsys documentation, see the `Google developer documentation
style guide <https://developers.google.com/style>`_, which provides the
general guidelines that you are to follow. This page supplies guidance specific
to PyAnsys documentation.

.. note::
    For comprehensive information on contributing new content or revising existing
    content in PyAnsys documentation, see :ref:`content_writing`.

When writing developer documentation, the relationship between code and
documentation is key. To keep documentation up to date with evolving
code, always perform these tasks:

- Minimize the content footprint.
- Write `timeless documentation <https://developers.google.com/style/timeless-documentation>`_.
- Support contributions from both inside and outside of the development team.
- Perform periodic reviews.

Documentation sources
---------------------

.. raw:: html

    <div align="center">
      <img width="30%" src="https://www.sphinx-doc.org/en/master/_static/sphinx-logo.svg">
    </div>

The generation of PyAnsys documentation uses `Sphinx`_ and an Ansys-branded theme
(`Ansys_Sphinx_theme_repo`_) to assemble content in:

- Docstrings
- reStructuredText (RST) files
- Python (PY) example files

Docstrings
~~~~~~~~~~

You must format docstrings  so that Sphinx can parse them. Sphinx provides
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

Regardless of the extension that you choose for generating documentation from docstrings,
using numpy-style docstrings ensures that there is consistency within PyAnsys libraries.
For more information, see :ref:`Documentation style`.

.. _rst_files_developers:

RST files
~~~~~~~~~

To provide general usage information in your documentation, use your favorite
editor to create RST (ReStructuredText) files that you then place in :ref:`The \`\`doc/\`\`
directory`. The ``index.rst`` file in the ``doc/source`` directory
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

            Welcome to the library documentation
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
documentation's generated HTML output. For more information on defining the
documentation structure, see `Getting Started
<https://www.sphinx-doc.org/en/master/usage/quickstart.html>`_ in the Sphinx
documentation.

Indicating RST titles
+++++++++++++++++++++

Within RST files, heading titles are to use sentence case per the
`capitalization guidelines <https://developers.google.com/style/capitalization>`_
in the *Google developer documentation style guide*. The line that follows
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

Because you must be familiar with the content in this guide, explore its HTML pages
and then the RST files in its `repository <https://github.com/ansys/dev-guide>`_. This 
should help you to understand the syntax and see how RST files are nested to create the guide.

Recommended sections
++++++++++++++++++++

Although each PyAnsys library is different, its documentation has the same goal:
provide instructions and guidelines for users. Thus, you can find some common sections
across the documentation for many PyAnsys libraries. Try to include these top-level
sections in your library's documentation:

- ``Getting started``: Explains how to install and set up the library.
- ``User guide``: Describes how to use basic features of the library.
- ``API reference`` Documents API resources provided by the library.
- ``Examples``: Provides fully fledged examples for using the library.
- ``Contributing``: Refers to the *PyAnsys developer's guide*
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


In the Sphinx configuration file (``doc/conf.py``), enable the ``sphinx-gallery`` exentenion:

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
     'gallery_dirs': 'examples',  # path where the gallery generated outputs are to be saved
    }

Because these examples are
built using the `sphinx-gallery
<https://sphinx-gallery.github.io/stable/index.html>`_ extension, you must
follow its `coding guidelines
<https://sphinx-gallery.github.io/stable/index.html>`_.

:ref:`General example` uses Python and the ``sphinx gallery``
extension.

Document Python code
--------------------

You can use the `sphinx.ext.autodoc` extension to generate documentation from your Python
code. When using this extension, you can include these directives in your :ref:`RST files`:

* ``automodule``: For documenting modules.
* ``autoclass``: For documenting classes.
* ``autofunction``: For documenting methods and functions.

For a full list of 'auto' directives, see `Include documentation from docstrings
<https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_ in the Sphinx
documentation.

Document classes
~~~~~~~~~~~~~~~~

There are two main ways of using Sphinx to document a class:

* Manually describe 'how' and 'why' you use a class in :ref:`RST files`.

* Automatically generate documentation for classes using the ``autoclass`` or
  ``autosummary`` directive in RST files.

Manually generate documentation
+++++++++++++++++++++++++++++++

To describe 'why' and 'how' you use a class within RST files, use the
``code-block`` directive:

.. tab-set::

    .. tab-item:: Doc surce code

        .. code-block:: rst

            Initialize ``my_module.MyClass`` with initial parameters. These
            parameters are automatically assigned to the class.

            .. code-block:: pycon

               >>> from my_module import MyClass
               >>> my_obj = MyClass(parm1="apple", parm2="orange")
               >>> my_obj.parm1
               'apple'

    .. tab-item:: Rendered doc

        Initialize ``my_module.MyClass`` with initial parameters. These
        parameters are automatically assigned to the class.

        .. code-block:: pycon

           >>> from my_module import MyClass
           >>> my_obj = MyClass(parm1="apple", parm2="orange")
           >>> my_obj.parm1
           'apple'

Automatically generate documentation
++++++++++++++++++++++++++++++++++++

To automatically generate class descriptions from the numpydoc strings in
your Python files, use either the ``autoclass`` or ``autosummary`` directive
in your RST files. For information on docstrings and required docstring
sections, see :ref:`Numpydoc docstrings`.  

For simple classes, use the ``autoclass`` directive:

.. tab-set::

    .. tab-item:: Doc Source Code

        .. code-block:: rst

            .. autoclass:: ansys_sphinx_theme.examples.samples.ExampleClass
               :members:

    .. tab-item:: Rendered Doc

        .. autoclass:: ansys_sphinx_theme.examples.samples.ExampleClass
            :members:


For complex classes with many methods, use the ``autosummary`` directive:

.. tab-set::

    .. tab-item:: Doc source code

        .. code-block:: rst

            .. autoclass:: ansys_sphinx_theme.examples.samples.Complex

            .. autosummary::
               :toctree: api/

               ansys_sphinx_theme.examples.samples.Complex.real
               ansys_sphinx_theme.examples.samples.Complex.imag
               ansys_sphinx_theme.examples.samples.Complex.abs

    .. tab-item:: Rendered doc

        .. autoclass:: ansys_sphinx_theme.examples.samples.Complex

        .. autosummary::

           ansys_sphinx_theme.examples.samples.Complex.real
           ansys_sphinx_theme.examples.samples.Complex.imag
           ansys_sphinx_theme.examples.samples.Complex.abs

When you use the ``autosummary`` directive, each class has its own dedicated page.
Each method and attribute in that class also has its own page.

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

`Sphinx`_ is used to build the documentation. You configure the entire build process in the
``conf.py`` file, located in the ``source/`` directory in :ref:`The \`\`doc/\`\` directory`.

This directory also contains a ``Makefile`` file and a ``make.bat`` file for
automating the building process. Different builders render different
documentation output, such as ``HTML``, ``LaTeX`` or ``PDF``.

Build HTML documentation
~~~~~~~~~~~~~~~~~~~~~~~~

You build HTML documentation with:

.. tab-set::

    .. tab-item:: Makefile

        .. code-block:: bash

            make html

    .. tab-item:: make.bat

        .. code-block:: bash

            make.bat html

The resulting HTML files are created in the ``_build/html`` directory,
located in :ref:`The \`\`doc/\`\` directory`.

You can display the HTML documentation with:

.. code-block:: text

    <browser> doc/_build/html/index.html

Build PDF documentation
~~~~~~~~~~~~~~~~~~~~~~~

To  build PDF documentation, the following rules must be added to
the ``Makefile`` and ``make.bat`` files:

.. tab-set::

    .. tab-item:: Makefile

        .. code-block:: text

            .PHONY: pdf

            pdf:
	            @$(SPHINXBUILD) -M latex "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	            cd $(BUILDDIR)/latex && latexmk -r latexmkrc -pdf *.tex -interaction=nonstopmode || true
	            (test -f $(BUILDDIR)/latex/*.pdf && echo pdf exists) || exit 1

    .. tab-item:: make.bat

        .. code-block:: text

            :PHONY pdf

            :pdf
                    %SPHINXBUILD% -M latex %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
	            cd "%BUILDDIR%\latex"
	            pdflatex \*.tex --interaction=nonstopmode

You can call the previous rules by running:

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

.. _multi_version_enabling:

Enabling multi-version documentation
------------------------------------

With the release of `ansys/actions@v4
<https://actions.docs.ansys.com/version/stable/index.html>`_ , projects can
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
              "json_url": f"https://{cname}/versions.json",
              "version_match": get_version_match(__version__),
          },
          ...
      }

  .. admonition:: About the ``DCOUMENTATION_CNAME`` environment variable
  
      The ``DOCUMENTATION_CNAME`` environment variable is expected to be
      declared in the YML file controlling the deployment of the documentation.
      The idea is that the canonical name (CNAME) is only defined in a single
      place, so it can be easily changed if required.

- Enable documentation deployment for development and stable versions, see
  :ref:`Deploying documentation`.

With all the previous configuration, your project is ready to use multi-version
documentation in an automated way. This means that every time you release a
new version, it is added to the drop-down button in the upper right corner of
the documentation's title bar. You use this drop-down button to 
switch from viewing the documentation for the latest stable release
to viewing the documentation for the development version or previously
released versions.

.. admonition:: Controlling the desired amount of versions showing up in the drop-down

    Only the development branch and the last three stable versions are
    shown by default in the documentation drop-down button. To show more versions,
    use the ``render-last`` variable in the `ansys/actions/doc-deploy-stable
    action
    <https://actions.docs.ansys.com/version/stable/doc-actions/index.html#doc-deploy-stable-action>`_.

If you require support for migrating to the multi-version documentation, email
`pyansys.core@ansys.com <pyansys.core@ansys.com>`_.

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
          # Deploy development only when merging or pushing to the 'main' branch
          if: github.event_name == 'push' && !contains(github.ref, 'refs/tags')
          runs-on: ubuntu-latest
          needs: build-library
          steps:
            - uses: ansys/actions/doc-deploy-dev@v4
              with:
                doc-artifact-name: '<html-artifact-name>'
                cname: ${{ env.DOCUMENTATION_CNAME }}
                token: ${{ secrets.GITHUB_TOKEN }}
        
        doc-deploy-stable:
          name: "Deploy stable documentation"
          # Deploy release documentation when creating a new tag
          if: github.event_name == 'push' && contains(github.ref, 'refs/tags')
          runs-on: ubuntu-latest
          needs: release
          steps:
            - uses: ansys/actions/doc-deploy-stable@v4
              with:
                doc-artifact-name: '<html-artifact-name>'
                cname: ${{ env.DOCUMENTATION_CNAME }}
                token: ${{ secrets.GITHUB_TOKEN }}

Deploying to another repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are planning to deploy documentation to a repository other than the one
for your project, make sure you create this new repository before deploying your
documentation for the first time.

Using the ``{{ secrets.GITHUB_TOKEN }}`` when deploying to another repository is
not possible due to the level of credentials of this token. Instead, use the
secrets generated by the ``PyAnsy Bot Application``.

For deploying the documentation to another repository, use the following
workflow:

.. code-block:: yaml

    env:
      DOCUMENTATION_CNAME: '<library>.docs.pyansys.com'
      DOCUMENTATION_REPOSITORY: '<organization-name>/<repository-name>'

    jobs:

        # Artifacts for HTML documentation need to be generated before 
        # executing the deployment jobs

        generate-token:
          name: "Generate deployment token"
          id: get_workflow_token
          uses: peter-murray/workflow-application-token-action@v1
          with:
            application_id: ${{ secrets.BOT_APPLICATION_ID }}
            application_private_key: ${{ secrets.BOT_APPLICATION_PRIVATE_KEY }}
    
        doc-deploy-dev:
          name: "Deploy development documentation"
          # Deploy development only when merging or pushing to the 'main' branch
          if: github.event_name == 'push' && !contains(github.ref, 'refs/tags')
          runs-on: ubuntu-latest
          needs: build-library
          steps:
            - uses: ansys/actions/doc-deploy-dev@v4
              with:
                doc-artifact-name: '<html-artifact-name>'
                cname: ${{ env.DOCUMENTATION_CNAME }}
                token: ${{ steps.get_workflow_token.outputs.token }}
                external-repository: ${{ env.DOCUMENTATION_REPOSITORY }}
        
        doc-deploy-stable:
          name: "Deploy stable documentation"
          # Deploy release documentation when creating a new tag
          if: github.event_name == 'push' && contains(github.ref, 'refs/tags')
          runs-on: ubuntu-latest
          needs: release
          steps:
            - uses: ansys/actions/doc-deploy-stable@v4
              with:
                doc-artifact-name: '<html-artifact-name>'
                cname: ${{ env.DOCUMENTATION_CNAME }}
                token: ${{ steps.get_workflow_token.outputs.token }}
                external-repository: ${{ env.DOCUMENTATION_REPOSITORY }}


Multi-version migration from ``ansys/actions@v3``  to ``ansys/actions@v4``
--------------------------------------------------------------------------

Projects using the multi-version feature should upgrade to `ansys/actions@v4
<https://actions.docs.ansys.com/version/stable/index.html>`_ or higher to
benefit from stable links. This is achieved by introducing a new layout that is
not compatible with older `ansys/actions` versions.

To perform the migration, follow these steps:

* Update all the continuous integration ``YML`` files to use
  ``ansys/actions@v4`` or higher.

* Make sure that the ``"json_url"`` key points to
  ``f"https://{cname}/versions.json"``. Note that the ``release/`` substring is
  dropped.

* Apply previous steps as fix patches in all the desired versions to be included
  in the multi-version documentation.

Access online documentation
---------------------------

Documentation for the latest stable release of a PyAnsys library is accessible
from its repository. The canonical name for the documentation of the project is
constructed using the following structure:

``https://<product>.docs.pyansys.com``

You can generally access the latest development version of the documentation by
adding the ``dev`` path to the URL as follows:

``https://<product>.docs.pyansys.com/dev``

.. warning::

    PyAnsys projects support now multi-version documentation, meaning that
    stable and development versions are collected under the same website. A
    drop-down button for selecting the desired version should be available in the
    top right corner of the documentation's navigation bar.

For example, consider the PyAEDT documentation:

- The URL for documentation of the latest stable release is `<https://aedt.docs.pyansys.com/>`_.
- The URL for documentation of the latest development version is `<https://aedt.docs.pyansys.com/version/dev/>`_.

The latest development versions of both the library and its documentation are
automatically kept up to date via GitHub actions.

To make documentation changes, you create a branch with a name that begins with
a prefix of ``doc/`` that is then followed by a short description of what you
are changing. For more information, see :ref:`Branch model`.

As you are making changes in this branch, you want to periodically generate the
documentation locally so that you can test your changes before you create a
GitHub pull request. For more information, see :ref:`Build documentation`.

Using PyMeilisearch as search engine
------------------------------------

PyMeilisearch is a Python client library that enables you to utilize MeiliSearch, an open-source search engine, 
to provide fast and relevant search capabilities for your application's data.

To enable multi-version documentation in your project, follow these steps:

- Use ``ansys-sphinx-theme>=0.9`` for building the documentation in your project.

- Include the following lines in the conf.py file:

  .. code-block:: python
  
      import os
  
      from ansys_sphinx_theme import convert_version_to_pymeilisearch
  
  
      cname = os.getenv("DOCUMENTATION_CNAME", "<DEFAULT_CNAME>")
      """The canonical name of the webpage hosting the documentation."""
  
      html_theme_options = {
          "use_meilisearch": {
            "api_key": os.getenv("MEILISEARCH_API_KEY", ""),
            "index_uids": {
              f"<your-index-name>{convert_version_to_pymeilisearch(__version__)}": "index name to be displayed",  # noqa: E501
            },
          },
          ...
      }
  
  In this code, replace <your-index-name> with the desired name for your MeiliSearch index.
  The ``convert_version_to_pymeilisearch`` function is to convert your package's version into a format suitable for MeiliSearch indexing.

  - Enable documentation index deployment for development and stable versions using GitHub Actions:
  
  .. code-block:: yaml

    jobs:
      doc-deploy-index:
        name: "Index the documentation and scrap using PyMeilisearch"
        runs-on: ubuntu-latest
        needs: doc-deploy
        if: github.event_name == 'push'
        steps:
          - name: Scrape the stable documentation to PyMeilisearch
            run: |
              VERSION=$(python -c "from <your-package> import __version__; print('.'.join(__version__.split('.')[:2]))")
              VERSION_MEILI=$(python -c "from <your-package> import __version__; print('-'.join(__version__.split('.')[:2]))")
              echo "Calculated VERSION: $VERSION"
              echo "Calculated VERSION_MEILI: $VERSION_MEILI"

          - name: "Deploy the latest documentation index"
            uses: ansys/actions/doc-deploy-index@v4.1
            with:
              cname: "<library>.docs.pyansys.com/version/$VERSION"
              index-name: "<index-name>v$VERSION_MEILI"
              host-url: "<meilisearch-host-url>"
              api-key: ${{ secrets.MEILISEARCH_API_KEY }}

Replace <your-package>, <your-index-name>, and <library> with appropriate values for your project. 
The version of your package is automatically calculated and used for indexing, ensuring that your documentation remains up-to-date.
For more information, see the `PyMeilisearch`_ and `ansys-sphinx-theme-doc`_ documentation.
By following these steps, you can effectively use PyMeilisearch as a search engine for multi-version documentation in your project.
