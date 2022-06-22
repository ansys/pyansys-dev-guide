############################
PyAnsys project organization
############################

The `PyAnsys Project <https://docs.pyansys.com/>`_ is hosted on GitHub at `PyAnsys
<https://github.com/pyansys>`_. It contains several repositories with 
Python libraries that interface with Ansys products or services. 
To try out a library, visit one of these links:

* `PyAEDT`_
* `PyDPF-Core <https://github.com/pyansys/DPF-Core>`_
* `PyDPF-Post <https://github.com/pyansys/DPF-Post>`_
* `PyMAPDL`_
* `PyMAPDL Legacy Reader <https://github.com/pyansys/pymapdl-reader>`_
* `PyPIM <https://github.com/pyansys/pypim>`_

If you want to create, develop, or contribute to a PyAnsys library, 
visit these links:

* `PyAnsys Project Developer's Guide <https://github.com/pyansys/about>`_
* `Ansys Sphinx Theme Documentation <https://github.com/ansys/ansys-sphinx-theme>`_
* `gRPC Hello-world Example <https://github.com/pyansys/pyansys-helloworld>`_
* `Material Example Data <https://github.com/pyansys/example-data>`_

Using the following tools, developers generate library packages from 
PROTO files, create coverage reports, and report on system coverage:

* `pyansys-protos-generator <https://github.com/pyansys/pyansys-protos-generator>`_
* `example-coverage <https://github.com/pyansys/example-coverage>`_
* `system-reporting-tool <https://github.com/pyansys/system-reporting-tool>`_

#################
Quick start guide
#################

This is a brief overview on how to get started right away with your own PyAnsys
repository on the `PyAnsys GitHub Organization`_. A repository is generally a
project for a particular PyAnsys library.

#. **Create the repository:** Create a repository from the
   `pyansys/template`_.  See `Creating a repository from a template`_.
   Be sure that the `repository visibility`_ is initially private.
   
#. **Rename the package:** Rename ``ansys/product/library`` to match
   your product or library. For example, the package name for
   PyMAPDL is ``ansys/mapdl/core``. Do the
   same renaming in ``setup.py``. Do this as a pull request. In fact, only add
   code as pull requests. Do not push to ``main``.)

#. **Add source:** Add your source files to
   ``ansys/<product>/<library>`` or create them.  Also add unit tests to 
   ``tests/`` following the `pytest`_ convention. Be sure to maintain
   sufficient coverage when adding your library. See `pytest-cov`_.

   .. note::
      If your tests require an active service, app, or product,
      be sure to set up this app to run in an automated manner.

#. **Update documentation:** The documentation source and content 
   vary from repository to repository. In ``doc/``, there are folders for
   different types of documentation, which can include guides, examples,
   and API. Ensure that all documentation is updated. See :ref:`Documentation
   Style`.

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

.. _PyAEDT: https://github.com/pyansys/PyAEDT
.. _PyMAPDL: https://github.com/pyansys/pymapdl
.. _pytest-cov: https://pytest-cov.readthedocs.io/en/latest/reporting.html
.. _pyansys/template: https://github.com/pyansys/template
.. _Creating a repository from a template: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template
.. _repository visibility: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility
.. _PyAnsys GitHub Organization: https://github.com/pyansys
.. _pytest: https://pytest.org/
