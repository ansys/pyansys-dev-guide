###################################################
The PyAnsys Project - Overview and Developers Guide
###################################################

The PyAnsys project is an effort by Ansys to provide Python libraries
that expose Ansys technologies into the Python ecosystem through APIs
and interfaces that are clear, concise and maintainable.

PyAnsys libraries are more than just reusable "scripts"; they are a set
of useful functions, classes, and plugins that eliminate the need to
write scripts and code from scratch.  These libraries are intended to
play a vital role in:

- Application automation
- Machine learning
- Post processing
- Data visualization
- Orchestrating workflows
- Data manipulation and export


Purpose of this Documentation and Intended Audience
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This documentation is to be a central document for:

- Ansys developers who wish to create Python libraries and "own" the
  project.
- Contributors (anyone) who wish to contribute to an existing pyansys
  project.
- Those interested in learning more regarding the PyAnsys Project.


PyAnsys Project Structure
=========================
The PyAnsys project hosted on GitHub at `PyAnsys
<https://github.com/pyansys>`_ contains several repositories that
provide interfaces to Ansys's products or services.  If you are a new
user wishing to try out one of PyAnsys's libraries, visit one of the
following links:

* `PyAnsys Library Overview <https://docs.pyansys.com/>`_
* `PyMAPDL`_
* `PyAEDT`_
* `DPF-Core <https://github.com/pyansys/DPF-Core>`_
* `DPF-Post <https://github.com/pyansys/DPF-Post>`_
* `Legacy PyMAPDL Reader <https://github.com/pyansys/pymapdl-reader>`_

If you are a new developer wishing to create, develop, or contribute
to a PyAnsys project, reference one of the following links.

* `Project Overview and Development <https://github.com/pyansys/about>`_
* `PyAnsys Documentation Theme <https://github.com/pyansys/pyansys-sphinx-theme>`_
* `gRPC Hello-world Example <https://github.com/pyansys/pyansys-helloworld>`_
* `Material Example <https://github.com/pyansys/example-data>`_

These tools are intended to be used by developers to generate packages
from proto files, create coverage reports, or provide users with tools
to report system coverage.

* `pyansys-protos-generator <https://github.com/pyansys/pyansys-protos-generator>`_
* `example-coverage <https://github.com/pyansys/example-coverage>`_
* `system-reporting-tool <https://github.com/pyansys/system-reporting-tool>`_


Project Licensing and Approval
==============================
The PyAnsys project is designed to allow users to create their own
workflows and interfaces to our products using our APIs.  This approach is designed to require anyone using PyAnsys library to use our licensed products either directly or indirectly, while allowing for users to distribute their custom made applications/workflows internally or externally.

To accomplish this, PyAnsys projects use the MIT license.  MIT
licenses allow commercial use. As the MIT license falls in the
BSD-style class of licenses, users do not have to provide any other
source code when releasing new software.  The user only needs to
include the original MIT license in the reused code to make the
PyAnsys project suitable for commercial use.

See `LICENSE` in this repository for the standard PyAnsys license.
This should be included in the root directory of any PyAnsys projects.

Exposing new Ansys technologies to PyAnsys and subject to internal
review and decision process. Reach out to Stephane Marguerin and
Alexander Kaszynski  for any requests.


PyAnsys Library Overview
========================
A PyAnsys library eliminates the need to share snippets of code that
perform actions, but rather allows the user to create workflows
consisting of their own Python modules and third-party libraries.
This is done to extend Ansys's products in a way that matches how
libraries are created in the Python community while still maintaining
the separation between Products, APIs, and PyAnsys client libraries.

The general pattern for a PyAnsys project avoids the anti-pattern of
providing single-use scripts by ensuring:

* Clear, open-source APIs consistent with community standards hosted
  on GitHub.
* Reusable packages that can be updated and patched outside of the
  Ansys release schedule, while still being directly dependent on
  Ansys's products.
* Unit testing, release packaging, and documentation.

To do this, each PyAnsys library that extends a product follows the
general pattern in the following figure:

.. image:: https://github.com/pyansys/about/raw/main/doc/source/images/diagram.png
  :width: 400
  :alt: Overview Diagram

In this overview, the product or service exposes an interface that is
either locally accessible (in the case of .NET using `pythoncom`_,
`SWIG`_, or `C extensions`_) or a service that is locally and
remotely accessible (`REST`_ or `gRPC`_).  This will be refereed to as
the program API.  While this API can be directly accessed, this often
results in unreadable and unmaintainable code that forces users to
rewrite setup boilerplate and other methods from scratch.


PyAnsys Library Basic Structure
===============================
All PyAnsys libraries are expected to follow a consistent pattern for:

  - Project and library name
  - Repository directory structure
  - Licensing
  - Package configuration in ``setup.py``
  - Unit testing
  - CI/CD using Azure Devops and GitHub Actions
  - Documentation


Project, Repository and Library Name
------------------------------------
Project name is expected to be ``py<project>``.  For example,
``PyMAPDL`` for MAPDL, `PyAEDT`` for AEDT.  The repository name as
hosted on GitHub should be all lowercase to follow GitHub community
standards as in the case of `pymapdl`_.  Finally, the Python library
name is expected to be in the format
``ansys-<product/service>-<feature>``.  For example, the core MAPDL
library is `ansys-mapdl-core <https://pypi.org/project/ansys-mapdl-core/>`_.

The reasoning behind long python library names is to allow for the
usage of `Namespace Packages`_ in order to designate which are
official Ansys packages and to provide a consistent branding and style
to PyAnsys libraries.  This is a consistent pattern among large
organizations who wish to provide many individual Python packages
while following a consistent package name pattern.


Repository Directory Structure
------------------------------
The source of a PyAnsys project is expected to be hosted on an
individual repository under the `PyAnsys Organization Account
<https://github.com/pyansys>`__.  This repository is expected to
contain the source, documentation, and unit testing of the project in
the following directory structure.

::

   .ci/azure-pipelines.yml
   .github/workflows/ci.yml
   ansys/
       <product/service>/
           <feature>/
               __init__.py
               my_module.py
               my_other_module.py
   doc/
       conf.py
       index.rst
       requirements.txt
   LICENSE
   README.rst
   requirements.txt
   setup.py
   tests/
       requirements.txt
       test_basic.py
       test_advanced.py


CI/CD with ``.github/workflows/`` and ``.ci/azure...``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CI/CD should use either public `Azure Devops
<https://azure.microsoft.com/en-us/services/devops/>`_ or public
`GitHub Actions <https://github.com/features/actions>`_ for unit
testing, release builds, and documentation builds.  This should also
be used for branch protection (see repository administration).

A good example for a documentation build action can be found at
`PyAnsys Sphinx Theme Documentation Action <https://github.com/pyansys/pyansys-sphinx-theme/blob/main/.github/workflows/ci-build.yml>`_.
This is used to generate the `PyAnsys Sphinx Theme Documentation
<https://sphinxdocs.pyansys.com/>`__.  Also, see `MAPDL Documentation Action https://github.com/pyansys/pymapdl/blob/main/.github/workflows/ci-build.yml`__ for how to generate documentation using product containers.

The `PyAEDT Unit Testing Action <https://github.com/pyansys/PyAEDT/blob/main/.github/workflows/unit_tests.yml>`_ shows how to run unit testing using an application pre-installed on a self-hosted agent.

See `MAPDL Azure Devops <https://github.com/pyansys/pymapdl/blob/main/.ci/azure-pipelines.yml>`_ for an azure pipeline that uses a containerized application to run unit testing.  See `DPF-Core Azure Devops <https://github.com/pyansys/DPF-Core/blob/master/.ci/azure-pipelines.yml>`_ for an example that uses a universal package to run unit testing.


Source Organization ``ansys/<product/service>/<feature>/``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PyAnsys projects follow the `Namespace Packages`_ convention to allow
for multiple libraries to use the same shared ``ansys`` namespace.  For
example, the `PyMAPDL`_ library with the ``ansys-mapdl-core`` package
name has the following directory structure:

::

   setup.py
   ansys/
       mapdl/
           core/
               __init__.py
               launcher.py
               mapdl_grpc.py
               ...

This allows for us to import the `PyMAPDL`_ library with:

.. code:: python

   >>> from ansys.mapdl import core as pymapdl

With this approach, other namespace packages can use the
``ansys-mapdl`` namespace, for example:

.. code:: python

   >>> from ansys.mapdl import reader as pymapdl_reader

.. note::

   Both the first and second level directories must not include
   ``__init__.py``.  If this is included, namespace packages will
   conflict and only one will be able to be imported.

While verbose, it is important for PyAnsys libraries to use the
``ansys-<product/service>`` namespace for consistency and to allow for
multiple products and services to share the same namespace.  This
makes it easy when searching for "ansys" packages within the `Python
Package Index PyPi <https://pypi.org/>`_.


README File (Either ``README.rst`` or ``README.md``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Each PyAnsys project should contain a README file at the root directory.  This README file should use follow either `reStructuredText Markup Syntax`_ or `Markdown Syntax`_ .  While Markdown has better GitHub support, rst text can be reused within Sphinx documentation to avoid duplicating any auto-generated Sphinx pages.  For example, see `pyansys-sphinx-theme index.rst`_.

.. _pyansys-sphinx-theme index.rst: https://github.com/pyansys/pyansys-sphinx-theme/blob/main/doc/source/index.rst
.. _reStructuredText Markup Syntax: https://docutils.sourceforge.io/rst.html
.. _Markdown Syntax: https://www.markdownguide.org/basic-syntax/


This README should at the minimum contain:

- PyAnsys library title
- General Description
- Installation directions (via ``pip install`` and ``git clone ...``)
- Basic usage
- Links to the full documentation

This README will also be reused within the ``long_description`` within
the package ``setup.py``.


Setup File ``setup.py``
~~~~~~~~~~~~~~~~~~~~~~~
The PyAnsys library package setup file is expected to contain the following elements:

- Name (e.g. ``ansys-mapdl-core``)
- Packages (e.g. ``ansys.mapdl.core``)
- Short description
- Long description using ``README.md`` or ``README.rst``
- `Single sourced package version <https://packaging.python.org/guides/single-sourcing-package-version/>`_
- Author of ``'ANSYS, Inc.'``
- Maintainer and maintainer email.
- Dependency requirements
- Applicable classifiers

The ``ansys-<product/service>-<feature>`` would have at the minimum
the following within its ``setup.py``.

.. code:: python

   """Setup file for ansys-<product/service>-<feature>"""
   import codecs
   import os
   from io import open as io_open
   from setuptools import setup

   THIS_PATH = os.path.abspath(os.path.dirname(__file__))
   __version__ = None
   version_file = os.path.join(THIS_PATH, 'ansys', '<product/service>',
                               '<feature>', '_version.py')
   with io_open(version_file, mode='r') as fd:
       exec(fd.read())

   setup(
       name='ansys-<product/service>-<feature>',
       packages=['ansys.<product/service>.<feature>'],
       version=__version__,
       description='Short description',
       long_description=open('README.rst').read(),
       long_description_content_type='text/x-rst',
       url='https://github.com/pyansys/pyansys-package-example/',
       license='MIT',
       author='ANSYS, Inc.',
       maintainer='First Last',
       maintainer_email='first.last@ansys.com',
       install_requires=['grpcio>=1.30.0'],
       python_requires='>=3.5',
       classifiers=[
           'Development Status :: 4 - Beta',
           'Programming Language :: Python :: 3',
           'License :: OSI Approved :: MIT License',
           'Operating System :: OS Independent',
       ],
   )


Documentation Directory ``doc``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The documentation directory ``doc`` contains the full PyAnsys library
documentation including:

- The same information as the README on the main page.  Reuse the ``README.rst`` if possible to avoid duplication.
- In-depth getting started including installation details.
- API Reference containing `Sphinx autosummary API documentation <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`_.
- User guide containing basic examples, thorough description of the library, use case scenarios, descriptive examples explaining methodology.
- Examples gallery containing jupyter notebook examples.
- Contributing section (can be linked to the about page general contributing section).

For further details regarding the the structure of the documentation directory, see `pyansys-sphinx-theme <https://sphinxdocs.pyansys.com/>`_.


Abstraction and Encapsulation
=============================
Abstraction in Python is the process of hiding the real implementation
of an application from the user and emphasizing only on usage of it.

One of the main aims of PyAnsys libraries is to wrap data and methods
within units of execution while hiding data or parameters in protected
variables.  The following sections demonstrate how applications or 
complex services expose functionalities that matter to the user and
hide all else. For example, background details, implementation
and hidden states do not need to be exposed.

Application Interface Abstraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Many Ansys applications are designed around user interaction within a
desktop GUI-based environment.  As such, scripts are often recorded
directly from user sessions and are in the context manipulating a
desktop application. Instead, scripts should be written for an API structured
around data represented as classes and modules.

PyAnsys seeks to make the API a "first class citizen" in regards to
interacting with Ansys's products by presenting the product as a
stateful data model.  Consider the following comparison between the
recorded script from AEDT and the PyAEDT example where we create an
open region in the active editor:

+------------------------------------------------------+----------------------------------------------+
| Using AEDT with MS COM Methods                       | Using AEDT with the `PyAEDT`_ Library        |
+------------------------------------------------------+----------------------------------------------+
| .. code:: python                                     | .. code:: python                             |
|                                                      |                                              |
|    import sys                                        |    from pyaedt import Hfss                   |
|    import pythoncom                                  |                                              |
|    import win32com.client                            |    hfss = Hfss()                             |
|                                                      |    hfss.create_open_region(frequency="1GHz") |
|    # initialize the desktop using pythoncom          |                                              |
|    Module = sys.modules['__main__']                  |                                              |
|    oDesktop = Module.oDesktop                        |                                              |
|    oProject = oDesktop.SetActiveProject("Project1")  |                                              |
|    oDesign = oProject.SetActiveDesign("HFSSDesign1") |                                              |
|    oEditor = oDesign.SetActiveEditor("3D Modeler")   |                                              |
|    oModule = oDesign.GetModule("BoundarySetup")      |                                              |
|                                                      |                                              |
|    # create an open region                           |                                              |
|    parm = [                                          |                                              |
|        "NAME:Settings",                              |                                              |
|        "OpFreq:=", "1GHz",                           |                                              |
|        "Boundary:=", "Radition",                     |                                              |
|        "ApplyInfiniteGP:=", False                    |                                              |
|    ]                                                 |                                              |
|    oModule.CreateOpenRegion(parm)                    |                                              |
+------------------------------------------------------+----------------------------------------------+

Besides length and readability, the biggest difference between the two
approaches is how the methods and attributes from the `Hfss` class
are encapsulated.  For example, desktop no longer needs to be
explicitly instantiated and is hidden as a protected attribute
``_desktop``.  The connection to the application takes place
automatically when `Hfss` is instantiated, and the active project,
editor, and module are automatically used when creating the open
region.

Furthermore, the `create_open_region` method within `Hfss`
contains a full Python documentation string with keyword arguments,
clear `numpydoc`_ parameters and returns, and a basic example.
These are unavailable when directly using COM methods and precludes
the usage of contextual help within a Python IDE.

What follows is the source of the method in ``hfss.py`` within
`PyAEDT`_.  Note how calls to the COM object are encapsulated all
within this method.

.. code:: python

    def create_open_region(self, frequency="1GHz", boundary="Radiation",
                           apply_infinite_gp=False, gp_axis="-z"):
       """Create an open region on the active editor.

       Parameters
       ----------
       frequency : str, optional
           Frequency with units. The  default is ``"1GHz"``.
       boundary : str, optional
           Type of the boundary. The default is ``"Radiation"``.
       apply_infinite_gp : bool, optional
           Whether to apply an infinite ground plane. The default is ``False``.
       gp_axis : str, optional
           The default is ``"-z"``.

       Returns
       -------
       bool
           ``True`` when successful, ``False`` when failed.

       Examples
       --------
       Create an open region in the active editor at 1GHz

       >>> hfss.create_open_region(frequency="1GHz")
        
       """
       vars = [
           "NAME:Settings",
           "OpFreq:=", frequency,
           "Boundary:=", boundary,
           "ApplyInfiniteGP:=", apply_infinite_gp
       ]
       if apply_infinite_gp:
           vars.append("Direction:=")
           vars.append(gp_axis)

       self._omodelsetup.CreateOpenRegion(vars)
       return True

Here, we abstract the COM `CreateOpenRegion` method and encapsulate
model setup object.  There's no reason why the user needs direct
access to `_omodelsetup`, and hence why it's protected in the
`Hfss` class.  Additionally, we simplify calling the method by
providing (and documenting) the defaults using keyword arguments and
placing them into the ``vars`` list, all while following the `Style
Guide for Python Code (PEP8)`_


Service Abstraction
~~~~~~~~~~~~~~~~~~~
Some Ansys products are exposed as services that permit remote
execution using technologies like `REST`_ or `gRPC`_.  These services
are typically exposed in a manner where the API has already been
abstracted as not all methods can be exposed through a remote API.
Here, the abstraction of the service is as crucial as in the case of
the "desktop API".  In this case, remote API calls should be identical
if the service is local or remote, with the only difference being that local
calls are faster to execute.

Consider the following code examples.  The left-hand example shows the
amount of work to start, establish a connection to, and submit an
input file to MAPDL using auto-generated gRPC interface files. For
further details, see `pyansys-protos-generator
<https://github.com/pyansys/pyansys-protos-generator>`_.)  On the
right-hand side is the same workflow, but using the `PyMAPDL`_ library.

+----------------------------------------------------------+--------------------------------------------+
| Using the gRPC Auto-generated Interface                  | Using the `PyMAPDL`_ Library               |
+==========================================================+============================================+
| .. code:: python                                         | .. code:: python                           |
|                                                          |                                            |
|    import grpc                                           |    from ansys.mapdl import core as pymapdl |
|                                                          |                                            |
|    from ansys.mapdl import mapdl_pb2 as pb_types         |    # start mapdl and read the input file   |
|    from ansys.mapdl import mapdl_pb2_grpc as mapdl_grpc  |    mapdl = pymapdl.launch_mapdl()          |
|    from ansys.mapdl import kernel_pb2 as anskernel       |    output = mapdl.input('ds.dat')          |
|    from ansys.client.launcher.client import Launcher     |                                            |
|                                                          |                                            |
|    # start MAPDL                                         |                                            |
|    sm = Launcher()                                       |                                            |
|    job = sm.create_job_by_name("mapdl-212")              |                                            |
|    service_name = f"grpc-{job.name}"                     |                                            |
|    mapdl_service = sm.get_service(name=service_name)     |                                            |
|                                                          |                                            |
|    # create a gRPC channel                               |                                            |
|    channel_str = '%s:%d' % (mapdl_service.host,          |                                            |
|                             mapdl_service.port)          |                                            |
|    channel = grpc.insecure_channel(channel_str)          |                                            |
|    stub = mapdl_grpc.MapdlServiceStub(channel)           |                                            |
|                                                          |                                            |
|    # send an input file request                          |                                            |
|    request = pb_types.InputRequest(filename='ds.dat')    |                                            |
|    response = stub.InputFileS(request)                   |                                            |
|    # additional postprocessing to parse response         |                                            |
|                                                          |                                            |
+----------------------------------------------------------+--------------------------------------------+

The approach on the right has a variety of advantages, chief of those
is readability due to the abstraction of the start of the service.
Furthermore, package names are short, work is done for the user to
provide a simplified interface to start up MAPDL, and the classes,
methods, and functions all have full documentation strings.

To properly abstract a service, the user needs to have the option to
either launch the service and connect to it locally if the software exists on
their machine or connect to a remote instance of the service.  One
way to do this is to include a function to launch the service (as done
here in `launch_mapdl`), which brokers a connection via a `Mapdl`
class.  For example:

.. code:: python

   >>> from ansys.mapdl.core import Mapdl
   >>> mapdl = Mapdl(ip=<IP Address>, port=<Port>)
   >>> print(mapdl)
   Product:             Ansys Mechanical Enterprise
   MAPDL Version:       21.2
   ansys.mapdl Version: 0.59.dev0

This straightforward approach
connects to a local or remote instance of MAPDL via gRPC by
instantiating an instance of `Mapdl`.  At this point, because the
assumption is MAPDL is always remote, it's possible to issue commands
to MAPDL, including those requiring file transfer like
`Mapdl.input`.


Data Transfer and Representation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Regarding data transfer from a local application or remote service,
one best practice is to represent arrays as ``numpy.ndarray`` or
``pandas.DataFrame`` objects, rather than returning raw JSON, gRPC
classes, Python lists, or at worst, a string.  The following
example generates a simple mesh in MAPDL.

.. code:: python

   >>> mapdl.prep7()
   >>> mapdl.block(0, 1, 0, 1, 0, 1)
   >>> mapdl.et(1, 186)
   >>> mapdl.vmesh('ALL')

At this point, the only two ways within MAPDL to access the nodes and
connectivity of the mesh are to either print it using the ``NLIST``
command or by writing to disk via CDWRITE.  Both methods are remarkably
inefficient and they would require serializing the data to ASCII on
the server, transferring it, and then deserializing it within Python and
converting it to an array.  For example:

.. code:: python

   >>> print(mapdl.nlist())
       NODE        X             Y             Z
        1   0.0000        1.0000        0.0000
        2   0.0000        0.0000        0.0000
        3   0.0000       0.75000        0.0000

Instead, it's more efficient to transfer the node array as either a
series of repeated ``Node`` messages, or better yet, serialize the
entire array into a bytes and deserialize it on the client side.  For a
concrete and standalone example of this in C++ and Python, see
`grpc_chunk_stream_demo`_.  While raw byte streams are vastly more
efficient, one major disadvantage is that the structure of
the data is lost when serializing the array. This should be considered
when deciding how to write your API.

Regardless of the serialization or message format, the user will
expect Python native types (or a common type for a common library like
``pandas.DataFrame`` or ``numpy.ndarray``.  Here, within `PyMAPDL`_,
the nodes of the mesh are accessible as the ``nodes`` attribute within
the ``mesh`` attribute, which provides an encapsulation of the mesh
within the MAPDL database.

.. code:: python

   >>> mapdl.mesh.nodes
   array([[0.  , 1.  , 0.  ],
          [0.  , 0.  , 0.  ],
          [0.  , 0.75, 0.  ],
          ...
          [0.5 , 0.5 , 0.75],
          [0.5 , 0.75, 0.5 ],
          [0.75, 0.5 , 0.5 ]])



.. _gRPC: https://grpc.io/
.. _pythoncom: http://timgolden.me.uk/pywin32-docs/pythoncom.html
.. _SWIG: http://www.swig.org/
.. _C extensions: https://docs.python.org/3/extending/extending.html
.. _Anaconda Distribution: https://www.anaconda.com/products/individual
.. _REST: https://en.wikipedia.org/wiki/Representational_state_transfer
.. _PyAEDT: https://github.com/pyansys/PyAEDT
.. _PyMAPDL: https://github.com/pyansys/pymapdl
.. _pymapdl: https://github.com/pyansys/pymapdl
.. _Style Guide for Python Code (PEP8): https://www.python.org/dev/peps/pep-0008
.. _grpc_chunk_stream_demo: https://github.com/pyansys/grpc_chunk_stream_demo
.. _numpydoc: https://numpydoc.readthedocs.io/en/latest/format.html
.. _Namespace Packages: https://packaging.python.org/guides/packaging-namespace-packages/
