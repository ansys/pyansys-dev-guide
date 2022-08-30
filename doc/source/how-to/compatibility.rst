Ansys product compatibility
============================
As the different PyAnsys libraries evolve, backward and forward compatibility
issues can occur. Some of the most common cases are:

* An Ansys product has implemented certain features in its new server version
  that are not available in previous server versions. This causes backward
  incompatibility issues.
* New server versions have suppressed support for certain operations after a
  a given version. This causes forward incompatibility issues.

Though there are different ways to handle these issues, some of the PyAnsys libraries,
such as `PyMAPDL <https://github.com/pyansys/pymapdl>`_ and
`PyDPF-Core <https://github.com/pyansys/pydpf-core>`_, handle them in
the same way. To homogenize implementations in PyAnsys libraries,
following their approach is recommended.

``check_version.py`` module approach
------------------------------------
A *version checking* module determines whether the Ansys product server you are connecting
to provides support for certain operations. For implementation examples, see the
``check_version.py`` files for the following PyAnsys libraries:

* `ansys/mapdl/core/check_version.py <https://github.com/pyansys/pymapdl/blob/main/src/ansys/mapdl/core/check_version.py>`_
* `ansys/dpf/core/check_version.py <https://github.com/pyansys/pydpf-core/blob/master/ansys/dpf/core/check_version.py>`_

One of the easiest ways to keep track of the versions supported is setting up a
**minimum version** data structure, in which forward compatibility is ensured.
Server versions earlier than the minimum version do not have access to this
functionality. In the case of `ansys/mapdl/core/check_version.py`_, this is the
``VERSIONS_MAP`` structure.

Most Ansys products provide forward compatibility, meaning that features
introduced in an earlier version are also supported in later versions. Suppressing
a feature would lead to a backward compatibility issue.

Because the same type of issues can happen with the PyAnsys servers wrapping
Ansys products, creating a similar data structure for a  maximum version is
is necessary. While there are no implementations yet of this feature, it should work
in the same way as the minimum version mechanism works.

``version_requires`` decorator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The ``@version_requires`` decorator applies version logic to the different
functionalities and methods available in the client. You can see how this
decorator is used in `ansys/mapdl/core/check_version.py`_ and
`ansys/dpf/core/check_version.py`_. Here is a generalized example:


.. code:: python

    class Client():
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
above the threshold.

You can create a ``@max_version_supported`` decorator to implement this same
kind of logic for forward incompatibility. Changing the ``@version_requires``
decorator to ``@min_version_required`` is recommended.