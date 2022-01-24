.. _api_documentation:

API Documentation Style
#######################
Good API documentation drives library adoption and usage and is the
foundation for a good developer experience.  Even with the best
interfaces and the most functional product, no one will adopt the API
if they don't know how to use it or if they aren't satisfied with the
documentation or examples they are presented with.

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

* Module, class, method, and function documentation strings. See
  :ref:`docstrings`.
* Full gallery of examples. See `PyMAPDL Examples
  <https://mapdldocs.pyansys.com/examples/index.html>`_
* User guide for the library.
* Link to this developer's guide.

.. toctree::
   :hidden:
   :maxdepth: 3

   docstrings
   class_documentation
   coding_style
