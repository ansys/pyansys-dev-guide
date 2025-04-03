Product compatibility
=====================

As PyAnsys libraries evolve, backward and forward compatibility issues can
occur. Here are examples of two common issues:

* An Ansys product has implemented certain features in its new server version
  that are not available in previous server versions. This causes backward
  incompatibility issues.
* New server versions have suppressed support for certain operations after a
  a given version. This causes forward incompatibility issues.

Although there are different ways to handle these issues, some PyAnsys libraries,
such as `PyMAPDL`_ and `PyDPF-Core <https://github.com/ansys/pydpf-core>`_, handle them in
the same way. To homogenize implementations in PyAnsys libraries, following their
approach is recommended.

``check_version.py`` module approach
------------------------------------

A *version checking* module determines whether the Ansys product server you are connecting
to provides support for certain operations. For an implementation example, see the
`check_version.py <https://github.com/ansys/pydpf-core/blob/master/src/ansys/dpf/core/check_version.py>`_
file for the DPF-Core library.

One of the easiest ways to keep track of the versions supported is to set up a
*minimum version* data structure in which forward compatibility is ensured.
Server versions earlier than the minimum version do not have access to this
functionality. The previously referenced ``check_version.py`` file uses the
``VERSIONS_MAP`` structure.

Most Ansys products provide forward compatibility, meaning that features
introduced in an earlier version are also supported in later versions. Suppressing
a feature would lead to a backward compatibility issue.

Because the same type of issues can happen with the PyAnsys servers wrapping
Ansys products, creating a similar *maximum version* data structure is
is necessary. While there are no such implementations yet, it should work
in the same way as the minimum version data structure.

``version_requires`` decorator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``@version_requires`` decorator applies version logic to
functionalities and methods available in the client. You can see how this
decorator is used in the `check_version.py <https://github.com/ansys/pydpf-core/blob/master/src/ansys/dpf/core/check_version.py>`_
file. Here is a generalized example:

.. code:: python

    class Client:
        def __init__(self):
            """Connect to a fake server."""
            self._server = FakeServer()

        @version_requires((0, 1, 3))  # require 0.1.3
        def meth_a(self):
            """Call method ``a`` on the server."""
            return self._server.meth_a()

        @version_requires((0, 2, 3))  # require 0.2.3
        def meth_b(self):
            """Call method ``b`` on the server."""
            return self._server.meth_b()

Whenever a ``client`` object is created and a call is made to any of its methods,
such as ``meth_a()``, the decorator checks that the version is later than the one
specified in the decorator's call. If it is not, a ``VersionError`` is raised.

The ``self._server`` member of the class is the server that the client is connected to. This
member is expected to have version information in its ``self._server._server_version``
attribute. The decorator uses this version information to determine if the version is
higher than the threshold.

You can create a ``@max_version_supported`` decorator to implement this same
kind of logic for forward incompatibility. Changing the ``@version_requires``
decorator to ``@min_version_required`` is recommended.
