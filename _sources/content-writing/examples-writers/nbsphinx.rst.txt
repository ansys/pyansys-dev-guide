.. _nbsphinx:

Use ``nbsphinx``
================

``nbsphinx`` uses a source parser for Jupyter notebooks (IPYNB files) to generate
interactive examples. This extension uses custom Sphinx directives to show notebook
code cells (and their results) in both HTML and LaTeX output. If a notebook is unevaluated
(has no stored output cells), it is automatically executed during the Sphinx documentation
build process. Notebooks with stored output cells are not executed by default.

Install Jupyter kernel
----------------------

To execute and convert Jupyter notebooks, you must have the appropriate Jupyter kernel
installed in your development environment. For example, you can install the IPython kernel
from the `ipykernel <Sphinx_nbsphinx_ipykernal_pkg_>`_ package.

Create and document notebooks
-----------------------------

When using ``nbsphinx``, you place the IPYNB files for the "Examples" section in the
``examples`` directory. To add documentation to your notebooks, use Markdown cells.


Configure the use of ``nbsphinx``  in the Sphinx configuration file
-------------------------------------------------------------------

To build the "Examples" section, developers configure the use of the ``nbsphinx``
extension in the project's :file:`conf.py` file. After installing and adding this
extension to the ``extensions`` variable as described in :ref:`add_sphinx_extensions`,
developers configure the ``nbsphinx_execute`` and ``nbsphinx_thumbnails`` variables.

Here is what these variables look like in the :file:`conf.py` file for PyAnsys Geometry:

.. code-block:: rst

   # Examples gallery customization
   nbsphinx_execute = "always"
   nbsphinx_custom_formats = {
       ".mystnb": ["jupytext.reads", {"fmt": "mystnb"}],
   }
   nbsphinx_thumbnails = {
       "examples/01_getting_started/01_math": "_static/thumbnails/101_getting_started.png",
       "examples/01_getting_started/02_units": "_static/thumbnails/101_getting_started.png",
       "examples/01_getting_started/03_sketching": "_static/thumbnails/101_getting_started.png",
       "examples/01_getting_started/04_modeling": "_static/thumbnails/101_getting_started.png",
        "examples/01_getting_started/05_plotter_picker": "_static/thumbnails/101_getting_started.png",  # noqa: E501
        "examples/02_sketching/basic_usage": "_static/thumbnails/basic_usage.png",
        "examples/02_sketching/dynamic_sketch_plane": "_static/thumbnails/dynamic_sketch_plane.png",
        "examples/02_sketching/advanced_sketching_gears": "_static/thumbnails/advanced_sketching_gears.png",  # noqa: E501
        "examples/03_modeling/add_design_material": "_static/thumbnails/add_design_material.png",
        "examples/03_modeling/plate_with_hole": "_static/thumbnails/plate_with_hole.png",
        "examples/03_modeling/tessellation_usage": "_static/thumbnails/tessellation_usage.png",
        "examples/03_modeling/design_organization": "_static/thumbnails/design_organization.png",
        "examples/03_modeling/boolean_operations": "_static/thumbnails/boolean_operations.png",
   }
   nbsphinx_epilog = """

Add ``nbsphinx`` to the documentation requirements
--------------------------------------------------

To include ``nbsphinx`` in your project's documentation requirements, you must
add it as a dependency. Depending on the project's configuration, you add the required ``pip``
packages in either the :file:`pyproject.toml` file or the :file:`requirements_doc_txt` file.
For more information, see :ref:`doc_ext_requirements`.
