Data transfer
=============

Abstracted APIs should attempt to hide the implementation details of
the remote or local API in a well organized data model. This data
model should avoid returning raw JSON files, gRPC messages, SWIG objects,
or .NET objects. It should preferably return standard Python objects
like lists, strings, dictionaries when useful, and `numpy`_
arrays or `pandas`_ dataframes for more complex data.

For example, consider a simple mesh in MAPDL:

.. code:: python

   mapdl.prep7()
   mapdl.block(0, 1, 0, 1, 0, 1)
   mapdl.et(1, 186)
   mapdl.vmesh("ALL")

At this point, there are only two ways within MAPDL to access the nodes and
connectivity of the mesh, You can either print it using the ``NLIST``
command or write it to disk using the ``CDWRITE`` command. Both of these
methods are remarkably inefficient, requiring:

- Serializing the data to ASCII on the server
- Transferring the data
- Deserializing the data within Python
- Converting the data to an array
  
This example prints node coordinates using the ``NLIST`` command:

.. code:: pycon

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

Regardless of the serialization or message format, users
expect Python native types (or a common type for a common library like
``pandas.DataFrame`` or ``numpy.ndarray``).  Here, within `PyMAPDL`_,
the nodes of the mesh are accessible as the ``nodes`` attribute within
the ``mesh`` attribute, which provides an encapsulation of the mesh
within the MAPDL database.

.. code:: pycon

   >>> mapdl.mesh.nodes
   array([[0.  , 1.  , 0.  ],
          [0.  , 0.  , 0.  ],
          [0.  , 0.75, 0.  ],
          ...
          [0.5 , 0.5 , 0.75],
          [0.5 , 0.75, 0.5 ],
          [0.75, 0.5 , 0.5 ]])


REST versus RPC data and model abstraction
------------------------------------------

Because of the nature of most Ansys products, apps and
services can either fit into the Remote Procedure Call (RPC) interface,
where the API is centered around operations and commands, or the
REST model, where the API is centered around resources. Regardless of
the interface style, there are several items to consider.

API chattiness
~~~~~~~~~~~~~~

APIs must be efficient to avoid creating chatty input and output.
Because many Ansys products fit well with the RPC API implementation,
there is a temptation to design APIs that require constant communication
with the remote or local service. However, just because RPC interfaces
can do this, it does not mean that they should. The assumption should be
that each RPC call takes significant time to execute.

One way to avoid constant communication with the service is to serialize
several "commands" for services that employ an internal "command pattern"
for data exchange. Another approach is to encapsulate the data model
entirely on the server to avoid data transfer whenever possible and
expose only a limited number of RPC methods in the front-facing API.

Compatibility and efficiency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

APIs should be designed to be compatible with as many languages and
platforms as possible.  `gRPC`_ for RPC-like interfaces should be one
of the first choices due to its compatibility with nearly all popular
languages and its efficiency over REST in terms of speed, memory, and
payload size.

Typically, REST data exchanges should be limited to short messages
that are transferred using JSON files, and gRPC should be used for large data
transfers and bidirectional streaming.

Choosing gRPC over REST is generally preferable due to the performance
benefits of a binary compatible protocol. While REST provides a variety of
benefits, for complex client/server interactions, it is best to have an
interface that can efficiently exchange a wide variety of data formats and
messages.
