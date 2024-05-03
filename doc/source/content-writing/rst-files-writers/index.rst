.. _rst_files_writers:

Content in RST files
####################

reStructuredText, a plaintext markup language, uses simple and intuitive
constructs to indicate the structure of a document. You use reStructuredText (RST)
files to define the hierarchy of your documentation and provide manually authored
content.

This page describes the setup of RST files for PyAnsys documentation. It also
describes the option for using either a RST or Markdown (MD) file as the README
file for the GitHub repository of a PyAnsys project.

For resources related to RST and MD files, see :ref:`style_format_resources`.
To learn how RST files for PyAnsys libraries are formatted, see :ref:`rst_file_formatting`.

RST file setup
--------------

In a repository, the ``doc/source`` directory contains an ``index.rst`` file that defines
the overall hierarchy (major sections) of the documentation. The child directory for each
section has its own index file.

.. note::
   While most PyAnsys libraries use ``index.rst`` as the name for a section's index
   file, to optimize web searches of the generated HTML documentation, this file
   should have a short and descriptive name that contains keywords and uses hyphens
   (``-``) to separate words. All directory names should also use hyphens to separate
   words. For more information, see :ref:`SEO`.  

In the index file for a documentation section, the first-level heading is the name
of the section. Documentation for a PyAnsys client library generally has
five sections with these headings:

- Getting started
- User guide
- API reference
- Examples
- Contribute

After the section heading and any additional content, the index file includes the
``toctree`` directive to specify the pages that this section is to display.

The ``toctree`` directive for this **Content in RST files** page
(``doc/_build/html/content-writing/rst-files-writers/index.html``), looks like this::

   .. toctree::
      :maxdepth: 3
      :hidden:

      rst-file-formatting
      rst-format-rules
      notices
      doc-links
      code-blocks
      images
      tables
      cards
      tab-sets
      collapsible-sections

The ``maxdepth`` attribute of the ``toctree`` directive specifies the maximum number of
heading levels to show in the documentation's right pane, labeled **On this page**. The
``maxdepth`` attribute is set to ``3`` for all sections in this guide.

The ``toctree`` directive also includes an ordered list of the RST files to show in the
documentation's left pane, labeled **Section Navigation**. You omit the RST extensions
from this list of files.

To see the ``toctree`` directives for the other sections in this guide,
in the project's `repository <dev_guide_repo_>`_, go to the ``doc/source``
directory and look at the ``index.rst`` files in the child directories.

For more information on RST file setup, see :ref:`rst_files_developers` and 
`Getting Started <Sphinx_GS_doc_>`_ in the Sphinx documentation.

.. _readme_files:

``README.rst`` files
--------------------

Each PyAnsys repository has a README file in its root directory that explains the
project and points readers to the documentation. The README file can be an RST file
or a GitHub Flavored Markdown (MD) file. While RST and MD files are similar, the syntax
differs.

If your README file is an RST file, see :ref:`rst_file_formatting` for syntax information.
If your README file is an MD file, see `GitHub Flavored Markdown Spec <Markdown_GitHub_flavored_spec_>`_
and `Using Markdown and Liquid in GitHub Docs <GitHub_doc_flavored_markdown_>`_ for
syntax information.

You can reuse content in a ``README.rst`` file in the main ``index.rst``
file for your documentation or in the index file for its "Getting started"
section. However, you cannot reuse content in a ``README.md`` file. Thus, the
disadvantages of having to use a different syntax in the MD file and the
inability to reuse content in it in your documentation might influence you to use a
``README.rst`` file.

To reuse all content in a ``README.rst`` file in the main ``index.rst`` file for your
documentation, use the ``include`` directive::

   .. include:: ../../README.rst

To reuse only a portion of the content in a ``README.rst`` file, use this directive's ``start-line``
and ``end-line`` attributes::

   .. include:: ../../README.rst
      :start-line: 4
      :end-line: 72

Because using the preceding attributes necessitates having to change the line numbers
if content is later added to or removed from the ``README.rst`` file, you
might want to use this directive's ``start-after`` attribute instead. It allows
you to reuse content from a given point to the end of the file.

You first insert a target in the ``README.rst`` file where you want to start the reuse.
For example, assume that the ``README.rst`` file has an "Overview" section where you want the reuse
to begin. Before this section, insert an explicit target name like this, followed by a blank line::

   .. reuse_start

In the main ``index.rst`` file for your documentation, now insert an ``include``
directive with a ``start-after`` attribute that specifies this explicit target name::

   .. include:: ../../README.rst
      :start-after: .. reuse_start

If your ``README.rst`` file has links to sections or pages in the documentation, you must
use either URLs or insert explicit targets at the bottom of the ``README.rst`` file that you can then
use in this file. If your project has a central ``links.rst`` file in the ``doc/source`` directory,
you might be tempted to simply use the explicit target names named defined in it in the ``README.rst``
file. However, the GitHub renderer is unaware of the ``links.rst`` file. For more information, see
:ref:`doc_links_external`.


.. toctree::
   :maxdepth: 3
   :hidden:

   rst-file-formatting
   rst-format-rules
   notices
   doc-links
   code-blocks
   images
   tables
   cards
   tab-sets
   collapsible-sections
