###############
Getting started
###############

The PyAnsys project exposes Ansys technologies via libraries in the 
Python ecosystem. Each library provides clear, concise, and
maintainable APIs. Useful Pythonic functions, classes, and plugins 
allow users to interact with targeted products and services in a 
high-level, object-orientated approach.

The PyAnsys ecosystem refines the :doc:`component-level interaction 
with Ansys solvers and tools <componentization>`, and eliminates the 
inconsistent and restrictive scripting environments found within product 
installations.

These component libraries play a vital role in:

- Application automation
- Machine learning
- Postprocessing
- Data visualization
- Workflow orchestration
- Data manipulation and export

The libraries also include plugins and interfaces to packages in the vast Python
ecosystem. Examples include:

- Arrays using `numpy <https://numpy.org/>`_
- Data structures and tables with `pandas <https://pandas.pydata.org/>`_
- 2D visualization using `matplotlib <https://matplotlib.org/>`_
- 3D visualization using `pyvista <https://docs.pyvista.org/>`_
- Advanced scientific computing using `scipy <https://www.scipy.org/>`_
- Machine learning using `tensorflow <https://www.tensorflow.org/>`_

.. note::
   If you are new to GitHub, you should visit `The ReadMe Project
   <https://github.com/readme>`_.  It is a dedicated platform for highlighting
   the best from the open source software community. Each monthly newsletter
   provides links to feature articles, developer stories, guides, and podcasts.

.. toctree::
   :hidden:
   :maxdepth: 3

   basic
   administration
   componentization
   abbr

.. _PyAEDT: https://github.com/ansys/PyAEDT
.. _PyMAPDL: https://github.com/ansys/pymapdl


Contributing to this guide
~~~~~~~~~~~~~~~~~~~~~~~~~~
If you would like to contribute to this development guide, maintainers gladly 
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
running them by installing ``pre-commit`` as a git hook with this command::

  pre-commit install

Now, each time you run ``git commit``, your commit is only created if it
passes the minimum style checks that also run on the GitHub CI/CD.
