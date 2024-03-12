.. _rst_files_writers:

Content in RST files
####################

reStructuredText, a plaintext markup language, uses simple and intuitive
constructs to indicate the structure of a document. You use reStructuredText (RST)
files to define the hierarchy of the documentation and provide manually authored
content.

This page describes the setup of RST files for PyAnsys documentation. It also
describes the option for using either a RST or Markdown (MD) file as the README
for a PyAnsys project.

For resources related to RST and MD files, see :ref:`style_format_resources`.
To learn how RST files for PyAnsys libraries are formatted, see :ref:`rst_file_formatting`.

RST file setup
--------------

In a repository, the ``doc`` directory contains an ``index.rst`` file that defines
the overall hierarchy (major sections) of the documentation. Each referenced child
directory has its own ``index.rst`` file. Its first-level heading is the name
of the documentation section. Documentation for a PyAnsys client library generally has
five sections:

- Getting started
- User guide
- API reference
- Examples
- Contribute

In addition to providing the section name, the ``index.rst`` file includes the
``.. toctree::`` directive to specify how to build and display the content
for this section.

.. note::
   A directive is a generic block of explicit markup that sets off a specific block
   of text. For more information, see `Directives <Sphinx_doc_directives_>`_ in the
   Sphinx documentation.

For example, here is the ``.. toctree::`` directive in the ``index.rst`` file for
this **RST files** section::

   .. toctree::
      :maxdepth: 3
      :hidden:

      rst_file_formatting
      rst_format_rules
      notices
      doc_links
      code_blocks
      images
      tables
      cards
      tab_sets

The ``maxdepth`` attribute of the ``.. toctree::`` directive specifies the maximum number of
heading levels to show in the documentation's right pane, labeled **On this page**. In this writer's
guide, the ``maxdepth`` attribute is set to ``3`` for all sections. The ``.. toctree::`` directive
then includes an ordered list of the RST files to show in the **Section Navigation** pane. The
RST extensions for the files in this list are omitted.

To see the ``.. toctree::`` directives for the other sections in this writer's guide,
in the project's `repository <PyAnsys_writers_guide_repo_>`_, go to the ``doc/source``
directory and look at the ``index.rst`` files in the child directories for the
documentation sections.

For more information on RST file setup, see these resources:

- `RST files <RST_files_url_>`_ in the *PyAnsys developer's guide*
- `Getting Started <Sphinx_GS_doc_>`_ in the Sphinx documentation

.. _readme_files:

README file
-----------

Each PyAnsys repository has a README file in its root directory. This file explains the
project and points readers to key documentation. The README file can be an RST file
or a GitHub Flavored Markdown (MD) file. While RST and MD files are similar, the syntax
differs. If the README file in your repository is an MD file, see
`GitHub Flavored Markdown Spec <Markdown_GitHub_flavored_spec_>`_
and `Using Markdown and Liquid in GitHub Docs <GitHub_doc_flavored_markdown_>`_.

If your README file is an RST file, you can reuse content in it in the overall ``index.rst``
file for a library's documentation. However, you cannot reuse content if your README file
is an MD file. Thus, the disadvantages of having to use a different syntax in the MD file and the
inability to reuse this MD file on the initial page of your documentation may influence you to
use an RST file for your README file.

To reuse all content from a ``README.rst`` file in the overall ``index.rst`` file for your
documentation, use the ``.. include::`` directive::

   .. include:: ../../README.rst

To reuse only a portion of the content in the ``README.rst`` file, use this directive's ``:start-line:``
and ``:end-line:`` attributes::

   .. include:: ../../README.rst
      :start-line: 4
      :end-line: 72

Using the preceding attributes necessitates having to change the line numbers
if content is later added to or removed from the ``README.rst`` file. Thus, you
might want to use this directive's ``:start-after:`` attribute instead. It allows
you to reuse content from a given point to the end of the file.

You first insert a target in the ``README.rst`` file where you want to start the reuse.
For example, assume that the ``README.rst`` file has an "Overview" section where you want the reuse
to begin. Before this section, insert a target like this, followed by a blank line::

   .. reuse_start

In the overall ``index.rst`` file for your library's documentation, now insert an ``.. include::``
directive with a ``:start-after:`` attribute that specifies this target::

   .. include:: ../../README.rst
      :start-after: .. reuse_start

If your ``README.rst`` file has links to sections or pages in the library's documentation, you must
use external links. You can use either URLs or named targets. However, named targets must be inserted
at the bottom of the ``README.rst`` file. If your project has a central ``links.rst``
file in the project's ``doc/source`` directory, inserting named targets for links in the
``README.rst`` file does not work because the GitHub renderer is unaware of this ``links.rst`` file.
For more information, see :ref:`doc_links_external`.

.. toctree::
   :maxdepth: 3
   :hidden:

   rst_file_formatting
   rst_format_rules
   notices
   doc_links
   code_blocks
   images
   tables
   cards
   tab_sets
