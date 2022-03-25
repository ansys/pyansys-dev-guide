Project, Repository, and Library Names
######################################
Large organizations providing Python packages 
follow a consistent naming pattern. Ansys follows 
these naming conventions: 

- The project name is to be ``Py<project>``. For example, 
  ``PyMAPDL`` is the project name for MAPDL and ``PyAEDT`` 
  is the project name for AEDT.
- The repository name as hosted on GitHub should be all 
  lowercase to follow GitHub community standards. For 
  example, `pymapdl`_ and `pyaedt`_.
- The Python library name is to be in the format 
  ``ansys-<product/service>-<feature>``. For example, 
  `ansys-mapdl-core <https://pypi.org/project/ansys-mapdl-core/>`_ 
  is the name for the core MAPDL library. 

Using long Python library names provides two primary advantages:

- `Namespace Packages`_ can be used to designate official 
  Ansys packages
- Consistent branding and style can be applied to PyAnsys libraries


gRPC Interface Package
----------------------
Lower level gRPC interface packages like `ansys-api-mapdl`_ should always be
named ``ansys-api-<product/service>`` or may contain an additional level with
``ansys-api-<product/service>-<secondlevel>``.

This is to standarize the API packages:

.. code::

   ─ansys
   │   ├───api
   │   │   ├───<product/service>
   │   │   │   ├───VERSION
   │   │   │   ├───v1
   │   │   │   │   ├───sample.proto


Where the package name within ``sample.proto`` would be:

.. code::

   package ansys.api.<product/service>.v1;


.. _PyMAPDL: https://github.com/pyansys/pymapdl
.. _PyAEDT: https://github.com/pyansys/PyAEDT
.. _Namespace Packages: https://packaging.python.org/guides/packaging-namespace-packages/
.. _ansys-api-mapdl: https://pypi.org/project/ansys-api-mapdl/
