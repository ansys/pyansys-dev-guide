Overview and Strategy
=====================

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
