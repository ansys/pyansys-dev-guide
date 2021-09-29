Quick Start Guide
=================

General
-------

1. **Create the Repository:** Create a new repository from the `pyansys/template <https://github.com/pyansys/template>`_.  See `Creating a repository from a template <https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template>`_.  Be sure to start as a private repository.
2. **Rename the Package:** Rename `ansys/product/library` to match your product or library.  For example `ansys/mapdl/core`.  Do the same in `setup.py`.  Do this as a pull request.  In fact, only add code as pull requests (don't push to main).
3. **Add Source:** Add your source files to `ansys/<product>/<library>`, or create them.  At the same time, add to `tests/`.  Be sure to maintain full (or near full (+90%)) coverage.  See `pytest-cov <https://pytest-cov.readthedocs.io/en/latest/reporting.html>`_.  If your tests require an active service, application, or product, be sure to setup this application to run in an automated manner.
4. **Documentation:** Update documentation at `doc/`.  There are two types of docs, User-Guide and API.  Be sure that both are updated.  See :ref:`_reference-docs`.
5. **Package Release:** When ready to release your package publically, contact alexander.kaszynski@ansys.com to obtain the release checklist in regards to official Ansys approval.  Once the checklist is complete, change the `repository visibility <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility>`_, create a release branch.


.. todo::
   gRPC
   ----

.. todo::
   C Extension
   -----------

