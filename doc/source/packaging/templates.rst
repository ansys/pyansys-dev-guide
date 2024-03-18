.. _templates:

Templates
=========

Starting a new project from scratch is a tedious task. To simplify the starting process
and make project generation more dynamic, the `ansys-templates`_ tool was created. Using this
tool ensures that any project rendered is compliant with the latest PyAnsys
coding and API style guidelines.

The ``ansys-templates`` tool
============================

The ``ansys-templates`` tool is a command-ine interface that provides a
collection of templates. When you use this tool to create a PyAnsys project, your
responses to the several questions that are asked result in dynamic project generation.

To install the latest stable version of this tool, see `Getting started`_ in the
Ansys templates documentation. Here are important links for this tool:

- **Repository**: https://github.com/ansys/ansys-templates
- **Documentation**: https://templates.ansys.com
- **Issues board**: https://github.com/ansys/ansys-templates/issues

.. note::

   If you encounter any problem during the installation or usage of this tool,
   open a new issue on the `ansys-templates issues board`_.

PyAnsys available templates
===========================

There are two templates that you can use to create PyAnsys
projects: ``pyansys`` and ``pyansys-advanced``. 

.. important::

   To access these templates, you must install the ``ansys-templates`` package.
   For information on how to use this tool, see `User guide`_ in the
   Ansys templates documentation.

PyAnsys template 
----------------

The ``pyansys`` template ships only with the required directories and files to
quickly set up a PyAnsys-compliant project. This template provides the following:

- A ``src/ansys/product/library/`` directory
- A ``setup.py`` file
- Generation of ``doc/`` and ``tests/`` directories
- A generic ``.gitignore`` file for Python libraries
- Build, doc, and test requirements files
- Metadata files like ``README.rst`` and ``LICENSE``

To create a project based on the ``pyansys`` template, run
this code:

.. code:: bash

   ansys-templates new pyansys

PyAnsys advanced template
-------------------------

The ``pyansys-advanced`` template is an enhanced version of the ``pyansys`` template.
It ships with the same files as the preceding template but also includes additional
features:

- Allows you to select the project file (``setup.py`` or ``pyproject.toml``)
- Uses `Tox`_ for testing and task automation
- Includes GitHub Actions for CI purposes
- Uses `pre-commit`_ for checking coding style

To create a project based on the ``pyansys-advanced`` template, run this code:

.. code:: bash

   ansys-templates new pyansys-advanced

.. _Getting started: https://templates.ansys.com/version/stable/getting_started/index.html
.. _User guide: https://templates.ansys.com/version/stable/user_guide/index.html
.. _ansys-templates issues board: https://github.com/ansys/ansys-templates/issues
