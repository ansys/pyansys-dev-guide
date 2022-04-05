.. _templates:

#########
Templates
#########

Starting a new project from scratch is a tedious task. To simplify the starting process
and make it more dynamic, the `ansys-templates`_ tool was created . Using this
template ensures that any project rendered will be compliant with the latest PyAnsys
coding and API style guidelines.

The ``ansys-templates`` tool
============================

The `ansys-templates`_ tool is a command line interface that provides a
collection of templates. When you use this tool to create a new PyAnsys project, your
responses to the several questions that are asked result in dynamic project generation.

Please, follow the `ansys-templates installation guide`_ to get the latest stable
version installed in your system.

- **Repository**: https://github.com/pyansys/ansys-templates
- **Documentation**: https://github.com/pyansys/ansys-templates
- **Issues board**: https://github.com/pyansys/ansys-templates/issues


.. note::

   Open a new issue in the `ansys-templates issues board`_ if you encounter any
   problem during the installation or usage of the tool.


PyAnsys Available Templates
===========================

There are two templates which can be used as basis for creating new PyAnsys
projects. These are the ``pyansys`` and the ``pyansys-advanced`` templates. 

.. important::

   Install `ansys-templates`_ to access these templates. Refer to the
   `ansys-templates user guide`_ for more information on how to use this tool.


PyAnsys Template 
----------------

The ``pyansys`` template ships only with the required directories and files to
quickly setup a PyAnsys compliant project:

- Provides a ``src/ansys/product/library/`` layout
- Includes a ``setup.py`` file
- Generates a ``doc/`` and a ``tests/`` directories
- Generic ``.gitignore`` for Python libraries
- Includes building, doc, and test requirements files
- Metadata files like ``README.rst`` and ``LICENSE``

Create a new project based on the ``pyansys`` template by running:

.. code:: bash

   ansys-templates new pyansys


PyAnsys Advanced Template
-------------------------

The ``pyansys-advanced`` is an enhanced version of the ``pyansys`` template. It
ships with the same files as this last template except:

- Allows you to select the project file (``setup.py`` or ``pyproject.toml``)
- Uses `Tox`_ for testing and tasks automation
- Includes GitHub actions for CI purposes
- Uses `pre-commit`_ for checking coding style

Create a new project based on the ``pyansys-advanced`` template by running:

.. code:: bash

   ansys-templates new pyansys-advanced

.. _ansys-templates: https://templates.pyansys.com/index.html
.. _ansys-templates installation guide: https://templates.pyansys.com/getting_started/index.html
.. _ansys-templates user guide: https://templates.pyansys.com/user_guide/index.html
.. _ansys-templates issues board:  https://github.com/pyansys/ansys-templates/issues
.. _flit: https://flit.readthedocs.io/en/latest/
.. _poetry: https://python-poetry.org/
.. _pre-commit: https://pre-commit.com/
.. _setuptools: https://pypi.org/project/setuptools/
.. _Tox: https://tox.wiki/en/latest/
