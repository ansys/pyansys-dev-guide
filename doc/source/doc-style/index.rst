Documentation style
###################

Good API documentation drives library adoption and usage and is the
foundation for a good developer experience. Even with the best
interfaces and the most functional product, an API is not adopted
if users aren't satisfied with the documentation or the examples
that they are presented with.

Good API documentation provides:

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

* Module, class, method, and function docstrings. See 
  :ref:`docstrings`.
* Full gallery of examples. See `PyMAPDL Examples
  <https://mapdldocs.pyansys.com/examples/index.html>`_.
* General content on installing, using, and contributing.
* Link to the library's documentation from the repository's README file.

To ensure clear and consistent documentation, all PyAnsys libraries are to
follow the guidelines in the `Google developer documentation style guide
<https://developers.google.com/style/>`_. Key guidelines include using:

- Sentence case for headings and titles
- Active voice
- Present tense
- Short, clear sentences

To help you follow the Google guidelines and any custom rules
developed by Ansys, you can implement `Vale <https://vale.sh/>`_.
This command-line tool brings code-like linting to prose. For more
information, see :ref:`Vale`.

Finally, the documentation should be public and hosted via gh-pages, either as
a branch named ``gh-pages`` within the library repository or within a
``gh-pages`` branch within ``<library-repository>-docs``. 

For procedural information related to crafting, building, and deploying
documentation, see :ref:`Documenting` in the :ref`How-to` section.

.. toctree::
   :hidden:
   :maxdepth: 3

   doc-configuration  
   docstrings
   formatting-tools
