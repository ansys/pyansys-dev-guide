.. _doc_links:

Links
=====

A link consists of some explicit markup with a *named target* that is either
internal or external to your project. You can also create a link for downloading
a file or for going to the description of a Python object in your API reference
documentation.

.. _doc_links_internal:

Internal links
--------------

You use the ``ref`` role to link to a target that you place before a heading.
This allows Sphinx to use the heading as the display text for the link, thereby
reducing maintenance if the heading later changes.

You first insert the target in the RST file before the heading that you want
to link to. The target consists of these parts:

- An explicit markup start (``..``) followed by a space
- An underscore followed by the target name and a colon

Always insert blanks lines both before and after the target.

Here is the target for :ref:`Ansys_Python_Manager` in this guide::

  .. _Ansys_Python_Manager:

To link to this target from any RST or PY file in this guide, use the
``ref`` role and the target name within a sentence, surrounding the target name
in single backticks::

  For more information, see :ref:`Ansys_Python_Manager`.

In the documentation, the display text for the link is the heading that follows this target.

If the target is not placed before a heading, or if you want to customize the display text,
you must provide the display text::

  This :ref:`open source Python QT app <Ansys_Python_Manager>` streamlines the setup of
  development environments for people new to the Python ecosystem.

.. _doc_links_external:

External links
--------------

There are several methods that you can use to link to external targets. The
simplest way is to specify the display text for the link and a URL directly in
a sentence::

    For more information on creating NumPy arrays, see
    `Array creation <https://numpy.org/doc/stable/user/basics.creation.html>`_
    in the NumPy documentation.

The display text for a link should either exactly match the title or heading
that you are referencing or provide a description of the destination page, as
specified in `Link text <Google_dev_doc_link_text_>`_ in the
*Google developer documentation style guide*. As shown in the example sentence,
you should follow a link with a descriptor that indicates where the
linked content resides, such as in a product's documentation or on an
organization's website.

The problem with specifying a URL as a target is that if the URL changes or the
page is later removed, you must update the URL in every place where it is used. This can
become quite burdensome if you have many links to the same URL.

To reduce maintenance of external links, you can use one of these methods to link to
named targets:

- Insert named targets at the bottom of individual RST files. For more information,
  see :ref:`named_targets_bottom_rst_files`.
- Insert named targets in a central list file, which is usually the :file:`list.rst`
  file, in the project's ``doc/source`` directory. For more information, see
  :ref:`named_targets_link_rst_file`.

.. note::
   You should choose only one of these methods. If you mix them, you might use
   the same target name in both an individual RST file and the :file:`list.rst` file,
   which causes Sphinx to raises errors about duplicated targets when building the
   documentation.

Guidelines for target names
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When naming targets, you must adhere to these guidelines to avoid errors
that Sphinx might otherwise raise when building the documentation:

- Do not use spaces in target names. Instead, use underscores to separate words.
  For example, ``_numpy`` is the name of the target that links
  to the `NumPy website <numpy_>`_.
- Abbreviate target names however you want. Keep in mind that longer, more
  descriptive names are easier to find if you ever need to replace them.
  For example, ``_python_main`` is a better target name for the Python organization
  than ``_python``.
- Do not use the same names for both internal and external targets. Varying how the
  names are capitalized does not cause Sphinx to see them as unique. For example, having an
  internal target named ``_RST_files`` and an external target named ``_rst_files`` causes
  Sphinx to raise errors when building the documentation because it sees them as
  duplicate targets.

.. _named_targets_bottom_rst_files:

Named targets at the bottom of RST files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assume that you want to add links in a RST file to the websites for `NumPy <numpy_>`_, `SciPy <scipy_>`_,
and `pandas <pandas_>`_, the  "big three" data science packages. At the bottom of
the RST file, you insert named targets to these websites like this:

.. code:: rst

  .. LINKS AND REFERENCES

  .. _NumPy_link: https://numpy.org/
  .. _SciPy_link: https://www.scipy.org/
  .. _pandas_link: https://pandas.pydata.org/

To insert links to these targets in a sentence in the RST file, you surround
each target name in single backticks and follow it with an underscore:

.. code:: rst

    All PyAnsys libraries are expected be consistent in style and formatting with the
    libraries for the "big three" data science packages: `NumPy_link`_, `SciPy_link`_, and `pandas_link`_.

When using this named target method, you must add targets to the bottom of every RST file
where you want to insert links to these targets, which requires much more effort and
maintenance than if you insert all targets in a central :file:`list.rst` file.

.. _named_targets_link_rst_file:

Named targets in a :file:`list.rst` file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add a central RST file in your project's ``doc/source`` directory and have the
Sphinx configuration file read this file to load all named targets, allowing you to insert
links to any of these targets in any RST file. Consolidating all targets in one file,
which is usually the :file:`list.rst` file, can significantly reduce maintenance over
time.

Set up the Sphinx configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To use a :file:`list.rst` file, you must set it up in the Sphinx configuration file
(``doc/source/conf.py``):

#. Open the :file:`conf.py` file.
#. Search to see if the ``exclude_patterns`` variable is defined.
#. If this variable is defined, add this line to the list of files and
   directories that Sphinx is to ignore  when looking for source files::

        ``links.rst,``

#. If this variable is not defined, after the lines configuring
   ``numpydoc`` and enabling ``numpydoc`` validation, define this variable and add the
   :file:`links.rst` file::

        exclude_patterns = [
            "links.rst",
        ]

   If you do not add the :file:`links.rst` file to the ``exclude_patterns`` variable,
   Sphinx raises this warning during documentation generation: ``document isn't included in any toctree``.

#. Beneath the ``exclude_patterns`` variable, add these lines to enable the ``rst_epilog``
   reStructuredText string::

       # make rst_epilog a variable, so you can add other epilog parts to it
       rst_epilog = ""

       # Read link all targets from file
       with open("links.rst") as f:
           rst_epilog += f.read()

   You might want to look at the `config.py <PyMAPDL_config_>`_ file for PyMAPDL because
   the ``exclude_patterns`` variable for this project lists many files and directories for
   Sphinx to ignore when looking for source files. Additionally, the ``rst_epilog``
   string contains a ``replace`` step that look for a ``VERSION`` variable
   to easily update targets with the MAPDL version for the latest MAPDL release.

When building the documentation, Sphinx dynamically includes the content in the ``rst_epilog``
string at the bottom of every RST file. Because this string tells Sphinx to read all targets
in the :file:`list.rst` file, you are able to link to any of these targets from any RST or PY
file in the project.

You can use another name for the :file:`list.rst` file or use multiple RST files for organizing
external links as long as you make the appropriate changes to the lines enabling the
``rst_epilog`` string.

.. note::
  When documentation checks run on a PR, Sphinx might indicate some links or link anchors are broken,
  which results in errors. For more information on resolving these errors, see
  :ref:`resolve_too_long_lines_broken_links`.

Link to named targets in the :file:`list.rst` file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To link to a named target in the :file:`list.rst` file, you drop the leading underscore in the
target name and add a trailing underscore after the target name. For example, the :file:`list.rst`
file for this project includes a target named ``_Style_guide_Sphinx_doc``. To link to this target
from any RST or PY file in this guide, here is how you insert the link::

  The `Style guide for Sphinx-based documentation <Style_guide_Sphinx_doc_>`_
  indicates that lines should be limited to a maximum of 79 characters.

While the link still begins with a single backtick and the display text for the link,
carats surround the target name and an underscore. Following the closing carat, you must
have a closing single backtick and another underscore.

For examples of named targets and how to organize them by categories, see the
:file:`list.rst` file in the ``doc/source`` directory for this project or the
`PyMAPDL <Links_for_pymapdl_>`_ project.

Download links
--------------

To create a link that downloads a file, you can use either a ``download`` link that specifies
a URL for the file or the ``download`` role and a named target in the :file:`list.rst` file.

This sentence uses a ``download`` link that specifies the URL to download the PDF file for the
PyFluent cheat sheet::

  You can `download <https://cheatsheets.docs.pyansys.com/pyfluent_cheat_sheet.pdf>`_ the PyFluent
  cheat sheet, which is a one-page reference that provides syntax rules and commands for using PyFluent.

This next sentence uses the ``download`` role and a named target in the :file:`list.rst` file
for the PyMAPDL project to download the PDF file for the PyMAPDL cheat sheet::

  Download the :download:`PyMAPDL cheat sheet <Cheat_Sheet_PyMAPDL.pdf>` to help you to learn PyMAPDL.

.. _API_object_links:

Python object links
-------------------

To link to Python objects in your API reference documentation, you use Python-specific roles.
For a list of these roles, see `Cross-referencing Python objects <Sphinx_doc_ref_Python_objects_>`_ in
the Sphinx documentation. For descriptions of fundamental Python objects, see :ref:`py_file_format`.

If the role links to a Python object in the same module, you only need to use the object name
in the role (as shown in the first of the following three examples). If the role links to a
Python object in a different module, you must use the module name and object name in the role
(as shown in the second and third of the following three examples).

Python uses a period (``.``) to denote submodules. If you need to see where a Python object is
defined in your API, use the GitHub search function. For example, to see where the
``Primitives3DLayout`` class is defined in the PyAEDT API, search its repository for this string:

``class Primitives3DLayout``

Search results indicate that this class is defined here: ``pyaedt.modeler.Primitives3DLayout.Primitives3DLayout``.

.. tip::
  Because using the full module name and object name in the role always works, when you perform a
  search to see where a Python object is defined, consider collecting the result in a TXT file. When
  you next need to link to this object, you can easily search this text file for the object name
  and then copy its full module name and object name into your RST file.  

Examples of Python object links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here are some examples of using Python-specific roles to link to Python objects.

**Example 1**

Assuming that your project is PyAEDT, you can use the ``class`` role to link to the
``Desktop`` class in the PyAEDT API reference documentation::

  The :class:`pyaedt.Desktop` class initializes AEDT and starts the specified version in
  the specified mode.

**Example 2**

Assuming that your project is PyMAPDL, you can use the ``func`` role to link to the
``run_batch()`` function in the PyMAPDL API reference documentation::

  You can use the pool to run a set of pre-generated input files using the
  :func:`run_batch <ansys.mapdl.core.LocalMapdlPool.run_batch>` function.

**Example 3**

Also assuming that your project is PyMAPDL, you can use both the ``func`` and
``attr`` roles to link to the ``nodal_displacement()`` function and then the
``selected_nodes`` attribute in the PyMAPDL API reference documentation::

  If you have subselected a certain component and want to also limit the result of a certain output
  (:func:`nodal_displacement <ansys.mapdl.core.post.PostProcessing.nodal_displacement>`), use the
  :attr:`selected_nodes <ansys.mapdl.core.post.PostProcessing.selected_nodes>` attribute to get a
  mask of the currently selected nodes.

More examples of Python object links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To see more examples of how to use Python-specific roles to link to Python objects
in your API reference documentation, use the GitHub search feature to find the following
strings in the repositories for PyAnsys libraries, keeping in mind that only some subset
of these roles is likely used in any library:

- ``mod``
- ``func``
- ``data``
- ``const``
- ``class``
- ``meth``
- ``attr``
- ``exc``
- ``obj``

To learn how you can also use Python-specific roles to link to Python objects in the
Sphinx documentation for other projects, see :ref:`links_to_objects_in_other_doc`.
