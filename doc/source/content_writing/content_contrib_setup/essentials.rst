.. _essentials:

Essentials for new PyAnsys writers
==================================

This page provides essential information for writers who are new
to contributing to PyAnsys documentation. While earlier sections of
this guide provide tremendous resources for all PyAnsys contributors,
they are written by developers for developers. While it is important
that content writers become familiar with these earlier sections, the
objective of this content writing sectio is to present documentation
writers with only what information they need to know in the
order in which they need to know it.

These earlier topics are related to documentation and contributions:

- The `Documenting <Documenting_>`_ page provides an overview of key documentation concepts
  along with some how-to information.

- The `Documentation style <Doc_style_>`_ section provides valuable information
  about API documentation, Sphinx configuration, NumPy-style docstrings, documentation
  generation, and tools for documentation style and coverage.

- The `Contributing <Contributing_>`_ page provides the general coding paradigms used for
  PyAnsys development.

Google developer documentation style guide
------------------------------------------

All writers contributing to PyAnsys documentation must follow the guidelines in the
`Google developer documentation style guide <Google_dev_doc_style_guide_>`_.
While you should become familiar with this entire style guide, periodically revisit the
`Highlights <Google_dev_doc_highlights_>`_ page to ensure that you are adhering to its most important points.

When the `Ansys templates <Ansys_templates_>`_ tool is used to create a PyAnsys project from the
``pyansys`` or ``pyansys-advanced`` template, `Vale <Vale_>`_, a rule-based tool for maintaining
a consistent style and voice in your documentation, is implemented. This tool, which is one of
many run by the CI/CD process, is configured to check content in RST and Markdown (MD) files
based on the *Google developer documentation style guide*.

To eliminate or mitigate the number of warnings and errors that Vale raises in a PR, you can install
Vale locally and then run it before you create or submit changes to a PR. For more information,
see :ref:`install_Vale_locally` and :ref:`run_Vale_locally`.

PyAnsys documentation
---------------------

On the right of the home page for a GitHub repository is an **About** area. Each PyAnsys project
has a link in this area to the library's documentation. For example, here is the **About** area
for this guide:

.. image:: ..//_static/GitHub_about_area.png
   :alt: **About** area with link to the *PyAnsys developer's guide*

You can also view the documentation for public PyAnsys libraries from the
`PyAnsys <PyAnsys_landing_page_>`_ landing page or from the Ansys Python Manager by
selecting **Help > PyAnsys Documentation**. For more information about this Python QA
app, see :ref:`Ansys_Python_Manager`.

All links to PyAnsys documentation take you to documentation for the latest (stable)
release because this is what users of the library generally want to see. In some cases,
users might want to see documentation for a legacy version of the library. Project contributors,
on the other hand, likely want to see the documentation for the development (main) branch of the
library.

Rather than hosting many separate documentation sites, the PyAnsys team provides support
for *multi-versions*, making it possible for you to select the documentation for different versions
from a dropdown on the right side of the documentation title bar.

.. image:: ..//_static/multi_version_doc_selector.png
   :alt: Version selector

This dropdown provides for selecting the documentation for the stable version, development (dev)
version, and three previous legacy versions by default. However, the selections it displays
can be customized. For information on how this dropdown is enabled and customized, see
`Enabling multi-version documentation <multiversion_doc_>`_.

Because writers want to edit and contribute to the documentation for the development branch,
whenever you view documentation, you should select **dev** from this dropdown.

.. tip::
    When you are viewing PyAnsys documentation, the right navigation pane typically
    displays **Show Source** and **Edit on GitHub** links. For information on using
    the **Show Source** link to see how a page's source file is formatted and how
    you can reuse this content, see :ref:`rst_file_formatting`. For information on
    using the **Edit on GitHub** link to use the GitHub web editor to submit
    suggested changes to a page in a PR, see :ref:`edit_on_GitHub`.
