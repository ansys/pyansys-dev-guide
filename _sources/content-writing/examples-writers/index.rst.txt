.. _examples_writers:

Content in examples
===================

Many PyAnsys libraries have an "Example" section. The `Sphinx-Gallery <Sphinx_ext_sphinx_gallery_>`_
extension (``sphinx_gallery``) is typically used to generate standalone, downloadable Python scripts
(PY files) or Jupyter notebooks (IPYNB files) that you can run. However, some
PyAnsys libraries use the `nbsphinx <Sphinx_nbsphinx_extension_>`_ extension,
which is specifically designed for working with and integrating Jupyter notebooks
into your Sphinx documentation.

When setting up a PyAnsys library, developers choose between Sphinx-Gallery or ``nbsphinx``
based on their specific documentation needs and the format of their code examples.

- Sphinx-Gallery is chosen if a gallery of examples is to be created from Python scripts and Jupyter
  notebooks. This extension automatically generates thumbnail images and links to the source code
  for each example. It also provides a number of configuration options for customizing the
  appearance of the gallery, providing a great way to showcase how to use your library
  in a structured manner with embedded code examples, explanations, and narrative text.

- The ``nbsphinx`` extension is chosen if developers want to integrate Jupyter notebooks into their Sphinx documentation. This
  extension processes Jupyter notebooks as inputs and offers custom Sphinx directives for rendering
  these notebooks as interactive HTML pages or LaTeX output. Within these formats, you can execute
  and modify code cells. Furthermore, ``nbsphinx`` can execute unevaluated notebooks automatically
  during the Sphinx build process. While this extension allows for some customization on the
  appearance of Jupyter notebooks in your Sphinx documentation, its scope is narrower than that
  of Sphinx Gallery.

For implementation information, see :ref:`sphinx-gallery` and :ref:`nbsphinx`.

.. toctree::
   :maxdepth: 3
   :hidden:

   sphinx-gallery
   nbsphinx
