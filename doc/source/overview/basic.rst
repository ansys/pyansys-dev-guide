############################
PyAnsys Project Organization
############################

The PyAnsys project is hosted on GitHub at `PyAnsys`_. It contains several
repositories with Python libraries that interface with Ansys products or
services.  To try out a library, visit one of these links:

* `PyAnsys`_ Project
* `PyMAPDL`_
* `PyAEDT`_
* `DPF-Core`_
* `DPF-Post`_
* `Legacy PyMAPDL Reader`_

If you want to create, develop, or contribute to a PyAnsys library, 
visit these links:

* `PyAnsys Project Developer's Guide`_
* `PyAnsys Sphinx Theme Documentation`_
* `gRPC Hello-world Example`_
* `Material Example Data`_

Using the following tools, developers generate library packages from 
PROTO files, create coverage reports, and report on system coverage:

* `pyansys-protos-generator`_
* `example-coverage`_
* `system-reporting-tool`_

#################
Quick Start Guide
#################

This is a brief overview on how to get started right away with your own PyAnsys
repository on the `PyAnsys GitHub Organization`_. A repository is generally a
project for a particular PyAnsys library.

#. **Create a new project:** take advantage of the `ansys-templates`_ tool for
   this task.

#. **Create the repository:** push previously generated project. Be sure that
   the `repository visibility`_ is initially private.
   
#. **Rename the package:** Rename ``ansys/product/library`` to match your
   product or library.  For example, the package name for PyMAPDL is
   ``ansys/mapdl/core``. Do the same renaming in ``setup.py``. Do this as a pull
   request.  In fact, only add code as pull requests. Do not push to ``main``.)

#. **Add source:** Add your source files to
   ``ansys/<product>/<library>`` or create them.  Also add unit tests to 
   ``tests/`` following the `pytest`_ convention. Be sure to maintain
   sufficient coverage when adding your library. See `pytest-cov`_.

   .. note::
      If your tests require an active service, application, or product,
      be sure to set up this application to run in an automated manner.

#. **Update documentation:** The documentation source and content will
   vary from repository to _repository. In ``doc/``, there are folders for
   different types of documentation, which can include guides, examples,
   and API. Ensure that all documentation is updated. See :ref:`API Documentation Style`.

#. **Prepare the package for release:** When you are ready to release
   your package publicly, email `pyansys.support@ansys.com`_
   to obtain the release checklist for obtaining official Ansys approval.
   Once you have completed this checklist, change the `repository visibility`_
   to public and create a release branch.


.. todo::

   gRPC - Starting Guide

.. todo::

   C Extension - Starting Guide

.. todo::

   Others like requests, RPC, COM, etc.


.. Links and References
.. include:: ../links.rst
