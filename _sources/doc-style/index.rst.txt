.. _doc_style_developers:

Documentation style
===================

Good API documentation drives library adoption and usage and is the
foundation for a good developer experience. Even with the best
interfaces and the most functional product, an API is not adopted
if users aren't satisfied with a library's documentation or examples.

Good API documentation provides many benefits, including these:

* Increased adoption and improved experiences for developers using
  the API or library.
* Reduction in the time spent on-boarding new contributors and users
  of the library.
* Better maintenance of the code base. The time spent reading the
  source is often orders of magnitude greater than the time spent
  writing it. Well documented code (both in user-facing docstrings
  and developer comments) pays dividends in code maintenance.
* Reduction in the amount of time spent understanding the API features.

The documentation for a PyAnsys library should contain:

* Module, function, class, and method docstrings. See 
  :ref:`docstrings`.
* A full gallery of examples. See `PyMAPDL examples
  <https://examples.mapdl.docs.pyansys.com/>`_.
* General content on installing, using, and contributing.
* Link to the library's documentation from the repository's README file.

To ensure clear and consistent documentation, all PyAnsys libraries are to
follow the guidelines in the `Google developer documentation style guide
<Google_dev_doc_style_guide_>`_. Key guidelines include using:

- Sentence case for headings and titles
- Active voice
- Present tense
- Short, clear sentences

To help you follow the Google guidelines and any custom rules
developed by Ansys, you can implement `Vale <Vale_>`_.
This command-line tool brings code-like linting to prose.

Finally, the documentation should be public and hosted using GitHub pages, either as
a branch named ``gh-pages`` within the library repository or within a
``gh-pages`` branch within ``<library-repository>-docs``. 

For guidelines on how to acquire a specific DNS for hosting your documentation,
see :ref:`DNS configuration`. You should ensure that you are compliant with
the naming convention for your CNAME.

For procedural information related to crafting, building, and deploying
documentation, see :ref:`documenting_developers`. For comprehensive information
on writing content for PyAnsys developers, see :ref:`content_writing`.

.. toctree::
   :hidden:
   :maxdepth: 3

   doc-configuration  
   docstrings
   formatting-tools
