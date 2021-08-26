Data Transfer and Representation
================================
When transferring data from a local application or remote service, you 
do not want to return raw JSON, gRPC classes, Python lists, or, even worse, 
strings. A best practice is to represent arrays as ``numpy.ndarray`` or
``pandas.DataFrame`` objects.

This example generates a simple mesh in MAPDL:

.. code:: python

   >>> mapdl.prep7()
   >>> mapdl.block(0, 1, 0, 1, 0, 1)
   >>> mapdl.et(1, 186)
   >>> mapdl.vmesh('ALL')

At this point, the only two ways within MAPDL to access the nodes and
connectivity of the mesh are either to print it using the ``NLIST``
command or to write it to disk using the ``CDWRITE`` command. Both 
methods are remarkably inefficient, requiring:

- Serializing the data to ASCII on the server
- Transfering the data
- Deserializing the data within Python
- Converting the data to an array
  
This example prints node coordinates using the ``NLIST`` command:

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
``pandas.DataFrame`` or ``numpy.ndarray``).  Here, within `PyMAPDL`_,
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
