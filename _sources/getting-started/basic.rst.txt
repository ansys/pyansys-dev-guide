PyAnsys project organization
============================

The `PyAnsys project <PyAnsys_>`_ is a collection of many
Python packages for using Ansys products through Python. The
`Ansys organization <Ansys GitHub organization_>`_ on GitHub contains
several repositories with Python libraries for interfacing with Ansys
products or services. To go to the repository for a main PyAnsys library,
visit one of these links:

* `PyAEDT`_
* `PyAnsys Geometry`_
* `PyDPF-Core`_
* `PyDPF-Post`_
* `PyMAPDL`_
* `PyMAPDL Legacy Reader`_
* `PyMechanical`_
* `PyPIM`_

If you want to create, develop, or contribute to a PyAnsys library, 
visit these links:

* `PyAnsys developer's guide <dev_guide_repo_>`_
* `Ansys Sphinx Theme documentation <ansys-sphinx-theme-doc_>`_
* `gRPC Hello-world example <grpc_hello_world_>`_
* `Material example data <example_data_>`_

Developers use the following tools to generate library packages from 
PROTO files, create coverage reports, and report on system coverage:

* `pyansys-protos-generator <pyansys_proto_generator_>`_
* `example-coverage <example_coverage_>`_
* `pyansys-tools-report <pyansys_tools_report_>`_

PyAnsys repository creation
---------------------------

This is an overview on how to create your own PyAnsys repository in the
Ansys GitHub organization. A repository is generally a project for a
particular PyAnsys library.

#. **Create the repository:** Create a repository from the
   `ansys/template`_ repository. See `Creating a repository from a template`_
   in the GitHub documentation. Be sure that the `repository visibility`_ is initially private.
   
#. **Rename the package:** Rename ``ansys/product/library`` to match
   your product or library. For example, the package name for
   PyMAPDL is ``ansys/mapdl/core``. Do the
   same renaming in the ``setup.py`` file. Do this as a pull request. In fact, only add
   code as pull requests. Do not push to the ``main`` branch of the repository.

#. **Add source:** Add your source files to
   ``ansys/<product>/<library>`` or create them.  Also add unit tests to the
   ``tests`` directory, following the `pytest`_ convention. Be sure to maintain
   sufficient coverage when adding to your library. See the `pytest-cov`_ documentation.

   .. note::
      If your tests require an active service, app, or product,
      be sure to set it up to run in an automated manner.

#. **Update documentation:** The documentation source and content 
   vary from repository to repository. In the ``doc`` directory, there are child
   directories for different sections of the documentation, which can include getting
   started and user guides, examples, and an API reference. Ensure that all
   documentation is updated. See :ref:`Documentation
   style`.

#. **Prepare the package for release:** When you are ready to release
   your package publicly, email `pyansys.core@ansys.com <pyansys.core@ansys.com>`_
   to obtain the release checklist for obtaining official Ansys approval.
   Once you have completed this checklist, change the `repository visibility`_
   to public and create a release branch.

.. todo::

   gRPC - Starting Guide

.. todo::

   C Extension - Starting Guide

.. todo::

   Others like requests, RPC, COM, etc.
