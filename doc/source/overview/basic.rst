Quick Start Guide
=================

This is a brief overview on how to get started right away with your own PyAnsys library on the `PyAnsys GitHub Organization`_

#. **Create the Repository:** Create a new repository from the
   `pyansys/template`_.  See
   `Creating a repository from a template`_.  Be sure to start as a
   private repository.

#. **Rename the Package:** Rename ``ansys/product/library`` to match
   your product or library.  For example ``ansys/mapdl/core``.  Do the
   same in ``setup.py``.  Do this as a pull request.  In fact, only add
   code as pull requests (don't push to main).

#. **Add Source:** Add your source files to
   ``ansys/<product>/<library>``, or create them.  At the same time,
   add unit tests to ``tests/`` following the `pytest`_ convention.
   Be sure to maintain sufficient coverage when adding your library.
   See `pytest-cov`_.

   .. note::
      If your tests require an active service,
      application, or product, be sure to setup this application to run
      in an automated manner.

#. **Documentation:** Update documentation at ``doc/``.  There are two
   types of docs, User-Guide and API.  Be sure that both are updated.
   See :ref:`api_documentation`.

#. **Package Release:** When ready to release your package publicly,
   contact alexander.kaszynski@ansys.com to obtain the release
   checklist in regards to official Ansys approval.  Once the
   checklist is complete, change the `repository visibility`_,
   create a release branch.

The manner of the source and content of the documentation will vary
from project to project.

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
