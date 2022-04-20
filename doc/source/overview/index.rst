########
Overview
########

Through the PyAnsys project, Ansys provides Python libraries that
expose Ansys technologies to the Python ecosystem. These libraries
are more than reusable scripts. They are clear, concise, and
maintainable APIs and interfaces. Their useful functions, classes,
and plugins eliminate the need to write scripts interfacing with low
level APIs, allowing you to now interact with the product or service
at a high level in an object-orientated manner.

These libraries play a vital role in:

- Application automation
- Machine learning
- Postprocessing
- Data visualization
- Workflow orchestration
- Data manipulation and export

The libraries also include plugins and interfaces to the vast Python
ecosystem. Examples include:

- Arrays using `NumPy`_
- Data structures and tables with `pandas`_
- 2D visualization using `Matplotlib`_
- 3D visualization using `PyVista`_
- Advanced scientific computing using `SciPy`_
- Machine learning using `TensorFlow`_

.. note::
   If you are new to GitHub, we suggest that you visit `The ReadMe Project
   <https://github.com/readme>`_.  It is a dedicated platform for highlighting
   the best from the open source software community.  Each monthly newletter
   provides links to feature articles, developer stories, guides, and podcasts.

.. toctree::
   :hidden:
   :maxdepth: 3

   basic
   administration
   contributing


Contributing to this Guide
~~~~~~~~~~~~~~~~~~~~~~~~~~
If you would like to contribute to this development guide, we will gladly review
all pull requests. Please feel free to submit them and follow the
:ref:`API Documentation Style`.

This repository uses the `pre-commit`_ library to
automate style checking. To use it, enter your Python environment and install
it with::

   pip install pre-commit

You can then run it manually with::

   pre-commit run --all-files

This performs various style and spelling checks to ensure your contributions
meet minimum coding style and documentation standards.

You can make sure that these checks are always run prior to ``git commit`` by
installing a pre-commit as a git hook with::

  pre-commit install

Now, each time you run ``git commit``, your commit will only be created if it
passes the minimum style checks that will also be run on the GitHub CI/CD.

.. LINKS AND REFERENCES
.. include:: ../links.rst
