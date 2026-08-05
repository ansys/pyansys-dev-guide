Service
=======

Some Ansys products are exposed as services that permit remote
execution using technologies like `REST`_ or `gRPC`_.  These services
are typically exposed in a manner where the API has already been
abstracted because not all methods can be exposed through a remote API.
Here, the abstraction of the service is as crucial as in the case of
the *desktop API*. In this case, remote API calls should be identical
if the service is local or remote, with the only difference being that local
calls are faster to execute.

Consider the following code examples. The left-hand side shows the
amount of work to start, establish a connection to, and submit an
input file to MAPDL using auto-generated gRPC interface files. For
more information, see `pyansys-protos-generator
<https://github.com/ansys/pyansys-protos-generator>`_.  The 
right-hand side shows the same workflow but uses `PyMAPDL`_.

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

The approach on the right has a number of advantages, including:

- Readability due to the abstraction of the service startup
- Short package names 
- Simplified interface for starting MAPDL
- Full documentation strings for all classes, methods, and functions

To properly abstract a service, you must have the option to
either launch the service and connect to it locally if the software exists on
your machines or connect to a remote instance of the service. One
way to do this is to include a function to launch the service.

This example includes the ``launch_mapdl`` function, which brokers a connection with
the ``Mapdl`` class:

.. code:: pycon

   >>> from ansys.mapdl.core import Mapdl
   >>> mapdl = Mapdl(ip=whatever_ip, port=whatever_port)
   >>> print(mapdl)

   Product:             Ansys Mechanical Enterprise
   MAPDL Version:       21.2
   ansys.mapdl Version: 0.59.dev0

This straightforward approach connects to a local or remote instance 
of MAPDL using gRPC by instantiating an instance of the ``Mapdl`` class. 
At this point, because the assumption is that MAPDL is always remote, it's 
possible to issue commands to MAPDL, including those requiring 
file transfer like ``Mapdl.input``.
