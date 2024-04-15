.. _sphinx-gallery:

Use sphinx-gallery
==================

The `sphinx_gallery <Sphinx_ext_sphinx_gallery_>`_ extension (Sphinx-Gallery) is
used to generate a gallery of examples from RST (or TXT) files, Python scripts
(PY files), and even Jupyter notebooks (IPYNB files). The RST (or TXT) files
introduce the one or more sections of examples. The PY and IPYNB files provide
the corresponding standalone, downloadable code. Sphinx-Gallery generates an HTML
page for each example, as well as both Python and Jupyter notebook files, which
users can download and execute.

Set up examples
---------------

When using Sphinx-Gallery, you place the files for the ``Examples`` section in the
``examples`` directory. An RST (or TXT) file in this directory provides the
introductory content for the section. In most libraries, a :file:`Readme.txt` file
is used.

In a larger library, you typically organize examples in subdirectories by categories.
An RST or TXT file in each subdirectory then provides the introductory content for the
examples in this category.

You also place the PY and IPYNB files in the ``examples`` directory or subdirectories.
These files contain the code and documentation explaining this code.

- For Python files, you must use a specific structure and reStructuredText syntax. For more
  information, see `Structuring Python scripts for Sphinx-Gallery <Sphinx_ext_sphinx_gallery_structure_>`_
  in the Sphinx-Gallery documentation. For information on adding a new example in a PY
  file, see :ref:`adding_a_new_gallery_example`. You can use this example as a template
  for creating Python files for Sphinx-Gallery.

- For IPYNB files, you use Markdown cells to provide section headings and to provide
  context and explanations for the code in the code cells.

Configure the use of Sphinx-Gallery in the Sphinx configuration file
--------------------------------------------------------------------

To build the "Examples" section, developers configure the use of Sphinx-Gallery in
the project's Sphinx configuration (``doc/source/conf.py``) file. After installing
and adding this extension to the ``extensions`` variable as described in
:ref:`add_sphinx_extensions`, developers configure the ``sphinx_gallery_conf`` variable.
This variable declares many values, including ``examples_dirs`` for the relative path to the
``examples`` directory and ``gallery_dirs`` for the relative path where the gallery-generated
outputs are saved.

While the values declared by the ``sphinx_gallery_conf`` variable vary from project to
project, here is what this variable looks like in the :file:`conf.py` file for PyAEDT:

.. code-block:: python

   sphinx_gallery_conf = {
       # convert rst to md for IPYNBb
       "pypandoc": True,
       # path to your examples scripts
       "examples_dirs": ["../../examples/"],
       # path where to save gallery generated examples
       "gallery_dirs": ["examples"],
       # Pattern to search for examples files
       "filename_pattern": r"\.py",
       # Remove the "Download all examples" button from the top level gallery
       "download_all_examples": False,
       # Sort gallery examples by file name instead of number of lines (default)
       "within_subsection_order": FileNameSortKey,
       # directory where function granular galleries are stored
       "backreferences_dir": None,
       # Modules for which function level galleries are created.  In
       "doc_module": "ansys-pyaedt",
       "image_scrapers": ("pyvista", "matplotlib"),
       "ignore_pattern": "flycheck*",
       "thumbnail_size": (350, 350),
       # 'first_notebook_cell': ("%matplotlib inline\n"
       #                         "from pyvista import set_plot_theme\n"
       #                         "set_plot_theme('document')"),
   }


Add Sphinx-Gallery to the documentation requirements
----------------------------------------------------

To include Sphinx-Gallery in your project's documentation requirements, you must
add it as a dependency. Depending on the project's configuration, you add the required ``pip``
packages in either the :file:`pyproject.toml` file or the :file:`requirements_doc_txt` file.
For more information, see :ref:`doc_ext_requirements`.
