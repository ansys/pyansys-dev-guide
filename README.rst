####################################################
The PyAnsys Project - Overview and Developer's Guide
####################################################

The PyAnsys project is an effort by Ansys to provide Python libraries
that expose Ansys technologies in the Python ecosystem through APIs
and interfaces that are clear, concise, and maintainable.

PyAnsys libraries are more than just reusable scripts. They are a set
of useful functions, classes, and plugins that eliminate the need to
write scripts and code from scratch. These libraries are intended to
play a vital role in:

- Application automation
- Machine learning
- Postprocessing
- Data visualization
- Workflow orchestrations
- Data manipulation and export


Purpose of this Documentation and Intended Audience
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This documentation is to be a central document for:

- Ansys developers who want to create Python libraries and "own" the
  project
- Contributors (anyone) who want to contribute to an existing PyAnsys
  project
- Those interested in learning more about the PyAnsys project.


PyAnsys Project Structure
=========================
The PyAnsys project is hosted on GitHub at `PyAnsys
<https://github.com/pyansys>`_. It contains several repositories that
provide interfaces to Ansys products or services.  If you want to try 
out a PyAnsys library, visit one of these links:

* `PyAnsys Library Overview <https://docs.pyansys.com/>`_
* `PyMAPDL`_
* `PyAEDT`_
* `DPF-Core <https://github.com/pyansys/DPF-Core>`_
* `DPF-Post <https://github.com/pyansys/DPF-Post>`_
* `Legacy PyMAPDL Reader <https://github.com/pyansys/pymapdl-reader>`_

If you want to create, develop, or contribute to a PyAnsys project, 
visit these links:

* `Project Overview and Development <https://github.com/pyansys/about>`_
* `PyAnsys Documentation Theme <https://github.com/pyansys/pyansys-sphinx-theme>`_
* `gRPC Hello-world Example <https://github.com/pyansys/pyansys-helloworld>`_
* `Material Example <https://github.com/pyansys/example-data>`_

These tools are intended to be used by developers to generate packages
from PROTO files, create coverage reports, and report on system coverage:

* `pyansys-protos-generator <https://github.com/pyansys/pyansys-protos-generator>`_
* `example-coverage <https://github.com/pyansys/example-coverage>`_
* `system-reporting-tool <https://github.com/pyansys/system-reporting-tool>`_


Project Licensing and Approval
==============================
The PyAnsys project allows users to create their own workflows and 
interfaces to Ansys products using Ansys APIs. While using a PyAnsys 
library requires relevant Ansys products to be licensed either directly 
or indirectly, users can distribute their custom-made applications 
and workflows internally or externally.

To accomplish this, PyAnsys projects use the MIT license, which 
allows commercial use. Because the MIT license falls in the
BSD-style class of licenses, users do not have to provide any other
source code when releasing new software. Users only need to
include the original MIT license in the reused code to make the
PyAnsys project suitable for commercial use.

See `LICENSE` in this repository for the standard PyAnsys license.
This file should be included in the root directory of any PyAnsys 
project.

Exposing new Ansys technologies to PyAnsys is subject to an internal
review and decision process. Reach out to Stephane Marguerin and
Alexander Kaszynski for any requests.


PyAnsys Library Overview
========================
A PyAnsys library eliminates the need to share snippets of code that
perform actions. Users can instead create workflows consisting of 
their own Python modules and third-party libraries. This extends 
Ansys's products in a way that matches how libraries are created 
in the Python community while still maintaining the separation 
between products, APIs, and PyAnsys client libraries.

The general pattern for a PyAnsys project avoids the anti-pattern of
providing single-use scripts by ensuring:

* Clear, open-source APIs consistent with community standards hosted
  on GitHub
* Reusable packages that can be updated and patched outside of the
  Ansys release schedule, while still being directly dependent on
  Ansys's products
* Unit testing, release packaging, and documentation

Each PyAnsys library that extends a product should follow the
general pattern in this figure:

.. image:: https://github.com/pyansys/about/raw/main/doc/source/images/diagram.png
  :width: 400
  :alt: Overview Diagram

The product or service exposes an interface that is either locally accessible 
(in the case of .NET using `pythoncom`_, `SWIG`_, or `C extensions`_) or a 
service that is locally and remotely accessible (`REST`_ or `gRPC`_). This 
is referred to as the program API. While this API can be directly accessed, 
this often results in unreadable and unmaintainable code that forces users to
rewrite setup boilerplate and other methods from scratch.

PyAnsys Library Basic Structure
===============================
All PyAnsys libraries are expected to follow a consistent pattern for:

  - Project, repository, and library names
  - Repository directory structure
  - Licensing
  - Package configuration in ``setup.py``
  - Unit testing
  - CI/CD using Azure Devops and GitHub Actions
  - Documentation


Project, Repository, and Library Names
--------------------------------------
The project name is expected to be ``py<project>``. For example,
``PyMAPDL`` for MAPDL or `PyAEDT`` for AEDT. The repository name as
hosted on GitHub should be all lowercase to follow GitHub community
standards. For exmaple, `pymapdl`_.  Finally, the Python library
name is expected to be in the format
``ansys-<product/service>-<feature>``. For example, the core MAPDL
library is `ansys-mapdl-core <https://pypi.org/project/ansys-mapdl-core/>`_.

The reasoning behind long Python library names is two-fold:

  - Allows using `Namespace Packages`_ to designate which are official 
  Ansys packages
  - Provides a consistent branding and style to PyAnsys libraries
  
This pattern for consistently naming packages is followed by 
large organizations who provide many individual Python packages.


Repository Directory Structure
------------------------------
The source of a PyAnsys project is expected to be hosted in an
individual repository under the `PyAnsys Organization Account
<https://github.com/pyansys>`__.  This repository should contain 
the source, documentation, and unit testing of the project in
the following directory structure:

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
testing, release builds, and documentation builds.  The selected 
method should also be used for branch protection. For more 
information, see Repository Administration.

Here are some good examples of using actions:
  - The `PyAnsys Sphinx documentation theme action <https://github.com/pyansys/pyansys-sphinx-theme/blob/main/.github/workflows/ci-build.yml>`_ 
  generates Ansys Python package documentation using the `PyAnsys Sphinx theme <https://sphinxdocs.pyansys.com/>`__.  
  - The `MAPD documentation action <https://github.com/pyansys/pymapdl/blob/main/.github/workflows/ci-build.yml>`_ 
  generates MAPDL documentation using product containers.
  - The `PyAEDT unit testing action <https://github.com/pyansys/PyAEDT/blob/main/.github/workflows/unit_tests.yml>`_ 
  runs unit testing using an application preinstalled on a self-hosted agent.
  - The `MAPDL Azure DevOps action <https://github.com/pyansys/pymapdl/blob/main/.ci/azure-pipelines.yml>`_ 
  uses a containerized application to run unit testing for an Azure pipeline.
  - The `DPF-Core Azure DevOps action <https://github.com/pyansys/DPF-Core/blob/master/.ci/azure-pipelines.yml>`_ 
  uses a universal package to run unit testing.

Source Organization ``ansys/<product/service>/<feature>/``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PyAnsys projects follow the `Namespace Packages`_ convention to allow
multiple libraries to use the same shared ``ansys`` namespace. For
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

This allows the `PyMAPDL`_ library to be imported with:

.. code:: python

   >>> from ansys.mapdl import core as pymapdl

With this approach, other namespace packages can use the
``ansys-mapdl`` namespace, for example:

.. code:: python

   >>> from ansys.mapdl import reader as pymapdl_reader

.. note::

   The directories at the first and second level must not include
   ``__init__.py``.  If this is included, namespace packages will
   conflict, allowing only one to be imported.

While the ``ansys-<product/service>`` namespace is verbose, using it 
consistently for PyAnsys libraries is important because it allows 
multiple products and services to share the same namespace. This
makes it easy when searching for "ansys" packages within the `Python
Package Index PyPi <https://pypi.org/>`_.


README File (Either ``README.rst`` or ``README.md``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Each PyAnsys project should contain a README file at the root directory. 
This README file should use either `reStructuredText Markup Syntax`_ 
or `Markdown Syntax`_.  While Markdown syntax has better GitHub support, 
text in REST files can be reused within Sphinx documentation, which 
avoids duplicating any auto-generated Sphinx pages. For example, 
see `pyansys-sphinx-theme index.rst`_.

.. _pyansys-sphinx-theme index.rst: https://github.com/pyansys/pyansys-sphinx-theme/blob/main/doc/source/index.rst
.. _reStructuredText Markup Syntax: https://docutils.sourceforge.io/rst.html
.. _Markdown Syntax: https://www.markdownguide.org/basic-syntax/


The README should at the minimum contain:

- PyAnsys library title
- General description
- Installation directions (via ``pip install`` and ``git clone ...``)
- Basic usage
- Links to the full documentation

The README will also be reused within the ``long_description`` in
the package ``setup.py``.


Setup File ``setup.py``
~~~~~~~~~~~~~~~~~~~~~~~
The PyAnsys library package setup file is expected to contain these elements:

- Name (such as ``ansys-mapdl-core``)
- Packages (such as ``ansys.mapdl.core``)
- Short description
- Long description in a ``README.md`` or ``README.rst`` file
- `Single-sourced package version <https://packaging.python.org/guides/single-sourcing-package-version/>`_
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

- The same information as the README on the main page.  Reuse the ``README.rst`` file if possible to avoid duplication.
- In-depth getting started information, including installation details.
- API Reference containing `Sphinx autosummary API documentation <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`_.
- User guide containing basic examples, thorough description of the library, use case scenarios, descriptive examples explaining methodology.
- Examples consisting of Jupyter Notebooks.
- Contributing section, which can be linked to general "Contributing" section of the About page.

For more information about the structure of the documentation directory, see `pyansys-sphinx-theme <https://sphinxdocs.pyansys.com/>`_.


Abstraction and Encapsulation
=============================
Abstraction in Python is the process of hiding the real implementation
of an application from the user and emphasizing only usage.

One of the main objectives of PyAnsys libraries is to wrap data and methods
within units of execution while hiding data or parameters in protected
variables.  The following sections demonstrate how applications or 
complex services expose functionalities that matter to the user and
hide all else. For example, background details, implementation,
and hidden states do not need to be exposed.

Application Interface Abstraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Many Ansys applications are designed around user interaction within a
desktop GUI-based environment. Consequently, scripts recorded
directly from user sessions and in the context of manipulating the
desktop application. Instead, scripts should be written for an API 
that is structured around data represented as classes and modules.

PyAnsys seeks to make the API a "first class citizen" in regards to
interacting with an Ansys product by presenting the product as a
stateful data model. Consider the following comparison between using a
recorded script from AEDT versus the PyAEDT libary to create an
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
``_desktop``. The connection to the application takes place
automatically when `Hfss` is instantiated, and the active project,
editor, and module are automatically used to create the open
region.

Furthermore, the `create_open_region` method within `Hfss`
contains a full Python documentation string with keyword arguments,
clear `numpydoc`_ parameters and returns, and a basic example.
These are unavailable when directly using COM methods, preventing
the use of contextual help from within a Python IDE.

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
       Create an open region in the active editor at 1 GHz.

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

Here, the COM `CreateOpenRegion` method is abstracted, encapsulating
the model setup object.  There's no reason why a user needs direct
access to `_omodelsetup`, which is why it's protected in the
`Hfss` class.  Additionally, calling the method is simplified by
providing (and documenting) the defaults using keyword arguments and
placing them into the ``vars`` list, all while following the `Style
Guide for Python Code (PEP8)`_.


Service Abstraction
~~~~~~~~~~~~~~~~~~~
Some Ansys products are exposed as services that permit remote
execution using technologies like `REST`_ or `gRPC`_.  These services
are typically exposed in a manner where the API has already been
abstracted becuase not all methods can be exposed through a remote API.
Here, the abstraction of the service is as crucial as in the case of
the "desktop API".  In this case, remote API calls should be identical
if the service is local or remote, with the only difference being that local
calls are faster to execute.

Consider the following code examples. The left-hand example shows the
amount of work to start, establish a connection to, and submit an
input file to MAPDL using auto-generated gRPC interface files. For
more information, see `pyansys-protos-generator
<https://github.com/pyansys/pyansys-protos-generator>`_.)  The 
right-hand side shows the same workflow but uses the `PyMAPDL`_ library.

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

The approach on the right has a number of advantages:

  - Readability due to the abstraction of service startup
  - Short package names 
  - Simplified interface for starting MAPDL
  - Full documentation strings for all classes, methods, and functions

To properly abstract a service, users must have the option to
either launch the service and connect to it locally if the software exists on
their machines or connect to a remote instance of the service.  One
way to do this is to include a function to launch the service. This example 
includes `launch_mapdl`, which brokers a connection via a `Mapdl`
class:

.. code:: python

   >>> from ansys.mapdl.core import Mapdl
   >>> mapdl = Mapdl(ip=<IP Address>, port=<Port>)
   >>> print(mapdl)
   Product:             Ansys Mechanical Enterprise
   MAPDL Version:       21.2
   ansys.mapdl Version: 0.59.dev0

This straightforward approach connects to a local or remote instance 
of MAPDL via gRPC by instantiating an instance of `Mapdl`. At this 
point, because the assumption is MAPDL is always remote, it's 
possible to issue commands to MAPDL, including those requiring 
file transfer like `Mapdl.input`.


Data Transfer and Representation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
One best practice for transferring data from a local application or 
remote service is to represent arrays as ``numpy.ndarray`` or
``pandas.DataFrame`` objects, rather than returning raw JSON, gRPC
classes, Python lists, or, at worst, a string.

This example generates a simple mesh in MAPDL:

.. code:: python

   >>> mapdl.prep7()
   >>> mapdl.block(0, 1, 0, 1, 0, 1)
   >>> mapdl.et(1, 186)
   >>> mapdl.vmesh('ALL')

At this point, the only two ways within MAPDL to access the nodes and
connectivity of the mesh are either to print it using the ``NLIST``
command or to write it to disk using the ``CDWRITE`` command. Both 
methods are remarkably inefficient and require:

  - Serializing the data to ASCII on the server
  - Transfering the data
  - Deserializing the data within Python
  - Converting the data to an array
  
This example printss using the ``NLIST`` command:

.. code:: python

   >>> print(mapdl.nlist())
       NODE        X             Y             Z
        1   0.0000        1.0000        0.0000
        2   0.0000        0.0000        0.0000
        3   0.0000       0.75000        0.0000

It's more efficient to transfer the node array as either a
series of repeated ``Node`` messages or, better yet, to serialize 
the entire array into bytes and then deserialize it on the client 
side. For a concrete and standalone example of this in C++ and Python, 
see `grpc_chunk_stream_demo`_.

While raw byte streams are vastly more efficient, one major disadvantage 
is that the structure of the data is lost when serializing the array. 
This should be considered when deciding how to write your API.

Regardless of the serialization or message format, users will
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
