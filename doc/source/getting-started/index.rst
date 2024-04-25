
Getting started
===============

The `PyAnsys project <https://docs.pyansys.com/>`_ exposes Ansys technologies
in client libraries within the Python ecosystem. Each library provides clear,
concise, and maintainable APIs. Useful Pythonic functions, classes, and plugins 
provide for interacting with targeted products and services in a high-level,
object-orientated approach.

The PyAnsys ecosystem refines the component-level interaction 
with Ansys solvers and tools. It also eliminates the inconsistent and
restrictive scripting environments found within product 
installations. For more information, see :ref:`componentizing`.

Additionally, libraries play vital roles in key simulation tasks,
including these:

- Application automation
- Machine learning
- Postprocessing
- Data visualization
- Workflow orchestration
- Data manipulation and export

Libraries also include plugins and interfaces to packages in the vast Python
ecosystem. Here are some examples:

- Arrays using `NumPy <https://numpy.org/>`_
- Data structures and tables using `pandas <https://pandas.pydata.org/>`_
- 2D visualization using `Matplotlib <https://matplotlib.org/>`_
- 3D visualization using `PyVista <https://docs.pyvista.org/>`_
- Advanced scientific computing using `SciPy`_
- Machine learning using `TensorFlow <https://www.tensorflow.org/>`_

.. note::
   If you are new to GitHub and open source projects, see `The ReadMe Project
   <https://github.com/readme>`_. This monthly newsletter highlights
   the best from the open source software community, providing links
   to feature articles, developer stories, guides, and podcasts.

.. toctree::
   :hidden:
   :maxdepth: 3

   basic
   administration
   componentization

Contributing to this guide
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you would like to contribute to this guide, maintainers gladly 
review all pull requests. For more information, see :ref:`Documentation style`.

This repository uses `pre-commit <https://pre-commit.com/>`_ to
automate style checking. To use it, enter your Python environment and install
``pre-commit`` with this command::

   pip install pre-commit

You can then run ``pre-commit`` manually with this command::

   pre-commit run --all-files

This performs various style and spelling checks to ensure your contributions
meet minimum coding style and documentation standards.

You can make sure that these checks are always run prior to ``git commit``
running them by installing ``pre-commit`` as a Git hook with this command::

  pre-commit install

Now, each time you run ``git commit``, your commit is only created if it
passes the minimum style checks that also run on the GitHub CI/CD.
