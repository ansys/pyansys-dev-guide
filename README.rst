###################
The PyAnsys Project
###################

The PyAnsys project is an effort by Ansys to provide Python libraries
that exploit the features of the Python language to produce APIs
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


Python - Strategy
=================

PyAnsys libraries are intended to extend and interface with existing
products of Ansys services **outside** of the application itself, and
in some cases permitting remote execution.  As such, this requires
that you have a working installation of Python, and ideally a Python
distribution like the `Anaconda Distribution`_.  For existing users
of Ansys who are not used to working with Python outside of the
product, this may seem to be an unnecessary step, but what this
approach provides is:

* The ability to connect with the vast ecosystem of `CPython
  <http://www.python.org/>`_ Packages including:

  * `NumPy <https://numpy.org/>`_
  * `SciPy <https://www.scipy.org/>`_
  * `Matplotlib <https://matplotlib.org/>`_
  * `VTK <https://vtk.org/>`_
  * `PyTorch <https://pytorch.org/>`_
  * `Qt for Python <https://wiki.qt.io/Qt_for_Python>`_
  * `Flask <https://flask.palletsprojects.com/>`_
  * 10,000s of others

  Depending on your python environment, you can use a package manager
  like `pip <https://pip.pypa.io/en/stable/>`_ or `conda
  <https://conda.io/>`_ to easily install the most up-to-date version
  of the library you need.

* Customization of your entire Python environment on the OS of your
  choosing.  For the applications that support it, you can even
  remotely connect with and manage the application via `gRPC`_.  For
  those that don't, you can still customize the version of Python and
  its packages.

* Create applications or pipelines that utilize Ansys products and
  expose features as a web-page, standalone application, or script to
  allow anyone to instantly Ansys's products on the desktop or web
  using a customized workflow.


PyAnsys Project Structure
=========================
The PyAnsys project hosted on GitHub at `PyAnsys
<https://github.com/pyansys>`_ contains repositories that provide:

* Interfaces to Ansys products or services:

  * `PyMAPDL <https://github.com/pyansys/pymapdl>`_
  * `PyAEDT <https://github.com/pyansys/PyAEDT>`_
  * `DPF-Core <https://github.com/pyansys/DPF-Core>`_
  * `DPF-Post <https://github.com/pyansys/DPF-Post>`_
  * `Legacy PyMAPDL Reader <https://github.com/pyansys/pymapdl-reader>`_

* Documentation and Examples

  * `Project Overview <https://github.com/pyansys/about>`_
  * `pyansys-sphinx-theme <https://github.com/pyansys/pyansys-sphinx-theme>`_
  * `pyansys_landing <https://github.com/pyansys/pyansys_landing>`_
  * `pyansys-helloworld <https://github.com/pyansys/pyansys-helloworld>`_
  * `example-data <https://github.com/pyansys/example-data>`_

* Tools

  * `pyansys-protos-generator <https://github.com/pyansys/pyansys-protos-generator>`_
  * `example-coverage <https://github.com/pyansys/example-coverage>`_
  * `system-reporting-tool <https://github.com/pyansys/system-reporting-tool>`_

For details regarding each project, visit the repository and either
view the README or visit the documentation linked to the repository.


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
either locally acessible (in the case of .NET using `pythoncom`_,
`SWIG`_, or `C extensions`_) or a service that is locally and
remotably acessible (`REST`_ or `gRPC`_).  This will be reffered to as
the program API.  While this API can be directly accessed 


+-------------------------------------------------------------------------+---------------------------------------------+
| Using gRPC Autogenerated Interface                                      | Using PyMapdl Library                       |
+-------------------------------------------------------------------------+---------------------------------------------+
| .. code:: python                                                        | .. code:: python                            |
|                                                                         |                                             |
|     import grpc                                                         |     from ansys.mapdl import core as pymapdl |
|                                                                         |                                             |
|     from ansys.api.mapdl.v0 import mapdl_pb2 as pb_types                |     # start mapdl and read the input file   |
|     from ansys.api.mapdl.v0 import mapdl_pb2_grpc as mapdl_grpc         |     mapdl = pymapdl.launch_mapdl()          |
|     from ansys.api.mapdl.v0 import kernel_pb2 as anskernel              |     output = mapdl.input('ds.dat')          |
|     from ansys.client.servicemanager.client import ServiceManagerClient |                                             |
|     sm = ServiceManagerClient()                                         |                                             |
|                                                                         |                                             |
|     # start MAPDL                                                       |                                             |
|     job = sm.create_job_by_name("mapdl-212")                            |                                             |
|     service_name = f"grpc-{job.name}"                                   |                                             |
|     mapdl_service = sm.get_service(name=service_name)                   |                                             |
|                                                                         |                                             |
|     # create a gRPC channel                                             |                                             |
|     channel_str = '%s:%d' % (mapdl_service.host, mapdl_service.port)    |                                             |
|     channel = grpc.insecure_channel(channel_str)                        |                                             |
|     stub = mapdl_grpc.MapdlServiceStub(channel)                         |                                             |
|                                                                         |                                             |
|     request = pb_types.InputFileRequest(filename=filename)              |                                             |
|     metadata = (('time-step-stream', '200'), ('chunk-size', '512'),)    |                                             |
|                                                                         |                                             |
|     response = stub.InputFileS(request, metadata=metadata)              |                                             |
+-------------------------------------------------------------------------+---------------------------------------------+




PyAnsys Package Basic Structure
===============================

ansys/<product>/<service>/my_module.py
ansys/<product>/<service>/my_other_module.py
ansys/<product>/<service>/__init__.py
README.rst
LICENSE (use Ansys license file in this repo)
setup.py
requirements.txt
docs/conf.py
docs/index.rst
tests/test_basic.py
tests/test_advanced.py
.github/workflows/ci.yml

This contains a `README.rst` containing
 - How to install...


Unit Testing
 - <you know the drill>
 - Will probably require your application/server to be packaged in a
   way that lets you consume it from public infrastructure.

Workflows
 - Test CI online
 - Deploy package automagically

Setup File
 - Defines what the "package is"

 <Setup File>


Python Modules
 - Non-proprietary source.
 - Exposes server functionality pythonically.


Documentation Directory `doc`
 - Use `pyansys-sphinx-theme <https://sphinxdocs.pyansys.com/>`_


.. _gRPC: https://grpc.io/
.. _pythoncom: http://timgolden.me.uk/pywin32-docs/pythoncom.html
.. _SWIG: http://www.swig.org/
.. _C extensions: https://docs.python.org/3/extending/extending.html
.. _Anaconda Distribution: https://www.anaconda.com/products/individual
.. _REST: https://en.wikipedia.org/wiki/Representational_state_transfer
