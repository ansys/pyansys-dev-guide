Overview
########

Through the PyAnsys project, Ansys provides Python libraries that
expose Ansys technologies to the Python ecosystem. These libraries 
are more than reusable scripts. They are clear, concise, and 
maintainable APIs and interfaces. Their useful functions, classes, 
and plugins eliminate the need to write scripts interfacing with low
level APIs, but rather interact with the product or service at a high
level, object orientated manner.

These libraries play a vital role in:

- Application automation
- Machine learning
- Post-processing
- Data visualization
- Workflow orchestration
- Data manipulation and export

The libraries also include plugins and interfaces to the vast python
ecosystem.  For example:

- Arrays using `NumPy <https://numpy.org/>`_
- Data structures and tables with `pandas <https://pandas.pydata.org/>`_
- 2D visualization using `Matplotlib <https://matplotlib.org/>`_
- 3D visualization using `pyvista <https://docs.pyvista.org/>`_
- Advanced scientific computing using `scipy <https://www.scipy.org/>`_
- Machine learning using `TensorFlow <https://www.tensorflow.org/>`_


Project Organization
~~~~~~~~~~~~~~~~~~~~

The PyAnsys project is hosted on GitHub at `PyAnsys
<https://github.com/pyansys>`_. It contains several repositories with 
Python libraries that interface with Ansys products or services. 
To try out a library, visit one of these links:

* `PyAnsys Packages Overview <https://docs.pyansys.com/>`_
* `PyMAPDL`_
* `PyAEDT`_
* `DPF-Core <https://github.com/pyansys/DPF-Core>`_
* `DPF-Post <https://github.com/pyansys/DPF-Post>`_
* `Legacy PyMAPDL Reader <https://github.com/pyansys/pymapdl-reader>`_

If you want to create, develop, or contribute to a PyAnsys library, 
visit these links:

* `About the PyAnsys Project <https://github.com/pyansys/about>`_
* `PyAnsys Documentation Theme <https://github.com/pyansys/pyansys-sphinx-theme>`_
* `gRPC Hello-world Example <https://github.com/pyansys/pyansys-helloworld>`_
* `Material Example Data <https://github.com/pyansys/example-data>`_

Using the following tools, developers can generate library packages from 
PROTO files, create coverage reports, and report on system coverage:

* `pyansys-protos-generator <https://github.com/pyansys/pyansys-protos-generator>`_
* `example-coverage <https://github.com/pyansys/example-coverage>`_
* `system-reporting-tool <https://github.com/pyansys/system-reporting-tool>`_

.. toctree::
   :hidden:
   :maxdepth: 3

   administration
   contributing

.. _PyAEDT: https://github.com/pyansys/PyAEDT
.. _PyMAPDL: https://github.com/pyansys/pymapdl
