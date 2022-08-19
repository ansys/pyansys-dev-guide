Ansys products compatibility
============================
As the different PyAnsys libraries evolve, backwards and forwards compatibility
issues may rise. Some of the most common cases are:

* An Ansys product has implemented certain features in its new server version
  which are not available in previous server versions. This causes backwards
  incompatibility issues.
* New server versions have suppressed support for certain operations after a
  a given version. This causes forwards incompatibility issues.

Though there are different ways to handle these issues, some of the PyAnsys libraries,
such as `PyMAPDL <https://github.com/pyansys/pymapdl>`_ and
`PyDPF-Core <https://github.com/pyansys/pydpf-core>`_, have started to handle them in
the same way. In order to homogenize implementations throughout the libraries,
it is recommended to follow their approach.

``check_version.py`` module approach
------------------------------------
As mentioned before, PyAnsys libraries have started to implement *version checking*
modules which allow to determine whether the Ansys product server you are connecting
to provides support for certain operations. Examples of this module may be found for
the following libraries:

* `PyMAPDL check_version.py module <https://github.com/pyansys/pymapdl/blob/main/src/ansys/mapdl/core/check_version.py>`_
* `PyDPF-Core check_version.py module <https://github.com/pyansys/pydpf-core/blob/master/ansys/dpf/core/check_version.py>`_

One of the easiest ways to keep track of the versions supported is setting up a
**minimum version** data structure, in which forwards compatibility is ensured.
Server versions prior to the minimum version do not have access to this
functionality. In the case of the `PyMAPDL check_version.py module`_, this is the
``VERSIONS_MAP`` structure.

Most Ansys products provide forwards compatibility, meaning that whatever feature
introduced in a previous version, is typically supported in upcoming versions
as well. In case that a feature was decided to be suppressed, this would lead to
backwards compatibility issues. The same would happen with the PyAnsys servers wrapping
the Ansys products. Thus, for this cases, it would also be necessary to create a
similar data structure, but in this case for a **maximum version**. Though there are
no implementations yet of this feature, the way it should work would be analogous to
the way the **minimum version** mechanism does.

``version_requires`` decorator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
How this logic is applied to the different functionalities and methods available in
the client is by using the ``@version_requires`` decorator. The PyAnsys libraries define
this decorator as seen in `PyMAPDL check_version.py module`_ or
`PyDPF-Core check_version.py module`_ and it is typically used as follows:

.. code:: python

    class Client():
        def __init__(self):
            '''Connects to a fake server'''
            self._server = FakeServer()

        @version_requires((0, 1, 3))  # require 0.1.3
        def meth_a(self):
            '''calls method a on the 'server''''
            return self._server.meth_a()

        @version_requires((0, 2, 3))  # require 0.2.3
        def meth_b(self):
            '''calls method b on the 'server''''
            return self._server.meth_b()

That way, whenever a ``Client`` object is created and a call to any of its methods is done,
such as ``meth_a()``, the decorator first checks that the version dealt with is above the one
specified in the decorator's call. Otherwise, a ``VersionError`` is raised.

The ``self._server`` member of the class (that is, the server the client is connected to) is
expected to have information on its version (that is, a ``self._server._server_version`` attribute),
which the decorator uses to determine if the version is above the threshold or not.

This same kind of logic could be implemented for forwards incompatibility, by creating a new
``@max_version_supported`` decorator. If this were to happen, it is suggested that the
``@version_requires`` decorator is changed to ``@min_version_required``.