Quick Start Guide
=================

This is a brief overview on how to get started right away with your own PyAnsys
repository on the `PyAnsys GitHub Organization`_. A repository is generally a
project for a particular PyAnsys library or tool.

#. **Create the repository:** Create a repository from the
   `pyansys/template`_.  See `Creating a repository from a template`_.
   Be sure that the `repository visibility`_ is initially private.
   
#. **Rename the package:** Rename ``ansys/product/library`` to match
   your product or library.  For example, the package name for
   PyMAPDL is ``ansys/mapdl/core``. Do the
   same renaming in ``setup.py``. Do this as a pull request.  In fact, only add
   code as pull requests. Do not push to ``main``.)

#. **Add source:** Add your source files to
   ``ansys/<product>/<library>`` or create them.  At the same time,
   add unit tests to ``tests/`` following the `pytest`_ convention.
   Be sure to maintain sufficient coverage when adding your library.
   See `pytest-cov`_.

   .. note::
      If your tests require an active service, application, or product,
      be sure to set up this application to run in an automated manner.

#. **Update documentation:** The documentation source and content will
   vary from project to project. In ``doc/``, there are folders for
   different types of documentation, which can include guides, examples,
   and API. Ensure that all documentation is updated. See :ref:`api_documentation`.

#. **Prepare the package for release:** When you are ready to release
   your package publicly, email `pyansys.support@ansys.com <pyansys.support@ansys.com>`_
   to obtain the release checklist for obtaining official Ansys approval.
   Once you have completed this checklist, change the `repository visibility`_
   to public and create a release branch.


.. todo::

   gRPC - Starting Guide

.. todo::

   C Extension - Starting Guide

.. todo::

   Others like requests, RPC, COM, etc.


.. _pytest-cov: https://pytest-cov.readthedocs.io/en/latest/reporting.html
.. _pyansys/template: https://github.com/pyansys/template
.. _Creating a repository from a template: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template
.. _repository visibility: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility
.. _PyAnsys GitHub Organization: https://github.com/pyansys
.. _pytest: https://pytest.org/
