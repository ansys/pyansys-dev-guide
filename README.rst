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

  * `PyMAPDL`_
  * `PyAEDT`_
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
either locally accessible (in the case of .NET using `pythoncom`_,
`SWIG`_, or `C extensions`_) or a service that is locally and
remotely accessible (`REST`_ or `gRPC`_).  This will be refereed to as
the program API.  While this API can be directly accessed, this often
results in unreadable and unmaintainable code that forces users to
rewrite setup boilerplate and other methods from scratch.


Abstraction and Encapsulation
-----------------------------
Abstraction in Python is the process of hiding the real implementation
of an application from the user and emphasizing only on usage of it.

One of the main aims of PyAnsys libraries is to wrap data and methods
within units of execution while hiding data or parameters in protected
variables.  The following sections demonstrate how desktop
applications or complex services in order to expose functionalities
that matter to the user and hiding all else.  Background details,
implementation, hidden states, all of these do not need to be exposed
to the user.

Application Interface Abstraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Many Ansys applications are designed around user interaction within a
desktop GUI based environment.  As such, scripts are often recorded
directly from user sessions and are in the context manipulating a
desktop application rather than manipulating an API centered around
data structures represented as classes and modules.

PyAnsys seeks to make the API a "first class citizen" in regards to
interacting with Ansys's products by presenting the product as a
stateful data model.  Consider the following comparison between the
recorded script from AEDT and the PyAEDT example where we create an
open region in the active editor:

+------------------------------------------------------+----------------------------------------------+
| Using AEDT using MS COM Methods                      | Using AEDT Using the `PyAEDT`_ Library       |
+------------------------------------------------------+----------------------------------------------+
| .. code:: python                                     | .. code:: python                             |
|                                                      |                                              |
|    import sys                                        |    from pyaedt import Hfss                   |
|    import pythoncom                                  |                                              |
|    import win32com.client                            |    hfss = Hfss()                             |
|                                                      |    hfss.create_open_region(frequency="1GHz") |
|    # initialze the desktop using pythoncom           |                                              |
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
approaches is how the methods and attributes from the ``Hfss`` class
are encapsulated.  For example, desktop no longer needs to be
explicitly instantiated and is hidden as a protected attribute
``_desktop``.  The connection to the application takes place
automatically when ``Hfss`` is instantiated, and the active project,
editor, and module are automatically used when creating the open
region.

Furthermore, the ``create_open_region`` method within ``Hfss``
contains a full Python documentation string with keyword arguments,
clear `numpydoc`_ parameters and returns, as well as a basic example.
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
           Type of the boundary. The default is ``"Radition"``.
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

Here, we abstract the COM ``CreateOpenRegion`` method and encapsulate
model setup object.  There's no reason why the user needs direct
access to ``_omodelsetup``, and hence why it's protected in the
``Hfss`` class.  Additionally, we simplify calling the method by
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
if the service is local or remote, with the only difference that local
calls are faster to execute.

Consider the following code examples.  The left-hand example shows the
amount of work to start, establish a connection to, and submit an
input file to MAPDL using auto-generated gRPC interface files (for
further details, see `pyansys-protos-generator
<https://github.com/pyansys/pyansys-protos-generator>`_.  On the
right-hand side is the same workflow, but using the `PyMAPDL`_ library.

+----------------------------------------------------------+--------------------------------------------+
| Using gRPC Autogenerated Interface                       | Using the `PyMAPDL`_ Library               |
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
provide a simplified interface to start-up mapdl, and the classes,
methods, and functions all have full documentation strings.

To properly abstract a service, the user needs to have the option to
launch the service and connect to it locally if the software exists on
their machine, or connect to a remote instance of the service.  Once
way to do this is to include a function to launch the service (as done
here in ``launch_mapdl``), which brokers a connection via a ``Mapdl``
class.  For example:

.. code:: python

   >>> from ansys.mapdl.core import Mapdl
   >>> mapdl = Mapdl(ip=<IP Address>, port=<Port>)
   >>> print(mapdl)
   Product:             Ansys Mechanical Enterprise
   MAPDL Version:       21.2
   ansys.mapdl Version: 0.59.dev0

With this approach, we've provided a straightforward approach to
connect to a local or remote instance of MAPDL via gRPC by
instantiating an instance of ``Mapdl``.  At this point, because the
assumption is MAPDL is always remote, it's possible to issue commands
to MAPDL, including those requiring file transfer like
``Mapdl.input``.


Data Transfer and Representation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Regarding data transfer from a local application or remote service,
one best practice is to represent arrays as ``numpy.ndarray`` or
``pandas.DataFrame`` objects, rather than returning raw JSON, gRPC
classes, Python lists, or at worst, a string.  In the following
example we generate a simple mesh in MAPDL.

.. code::

   >>> mapdl.prep7()
   >>> mapdl.block(0, 1, 0, 1, 0, 1)
   >>> mapdl.et(1, 186)
   >>> mapdl.vmesh('ALL')

At this point, the only two ways within MAPDL to access the nodes and
connectivity of the mesh are to either print it using the ``NLIST``
command or by writing to disk via CDWRITE.  Both methods are remakably
inefficient and they would require serializing the data to ASCII on
the server, transfering it, and then deserialzing it within Python and
converting it to an array.  For example:

.. code:: python

   >>> print(mapdl.nlist())
       NODE        X             Y             Z
        1   0.0000        1.0000        0.0000
        2   0.0000        0.0000        0.0000
        3   0.0000       0.75000        0.0000

Instead, it's more efficient to transfer the node array as either a
series of repeated ``Node`` messages, or better yet, serialize the
entire array into a bytes and deserialze it on the client side.  For a
concrete and standalone example of this in C++ and Python, see
`grpc_chunk_stream_demo`_.  While raw byte streams are vasty more
efficient, one major disavantage of this approach is the structure of
the data is lost when serializing the array; this should be considered
when deciding how to write your API.

Regardless of the serialization or message format, the user will
expect Python native types (or a common type for a common libary like
``pandas.DataFrame`` or ``numpy.ndarray``.  Here, within `PyMAPDL`_,
the nodes of the mesh are acessible as the ``nodes`` attribute within
the ``mesh`` attribute, which provides an encapsulation of the mesh
within the MAPDL database.

.. code::

   >>> mapdl.mesh.nodes
   array([[0.  , 1.  , 0.  ],
          [0.  , 0.  , 0.  ],
          [0.  , 0.75, 0.  ],
          ...
          [0.5 , 0.5 , 0.75],
          [0.5 , 0.75, 0.5 ],
          [0.75, 0.5 , 0.5 ]])


PyAnsys Package Basic Structure
===============================


.. code:: 
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
.. _PyAEDT: https://github.com/pyansys/PyAEDT
.. _Style Guide for Python Code (PEP8): https://www.python.org/dev/peps/pep-0008
.. _PyMAPDL: https://github.com/pyansys/pymapdl
.. _grpc_chunk_stream_demo: https://github.com/pyansys/grpc_chunk_stream_demo
.. _numpydoc: https://numpydoc.readthedocs.io/en/latest/format.html
