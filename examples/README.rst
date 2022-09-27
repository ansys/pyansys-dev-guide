============
Add examples
============
Here are an example using sphinx gallery.

Consider the Python project has the following structure:

.. code:: rst

    ├── doc
    │   ├── conf.py
    │   ├── index.rst
    |   ├── make.bat
    │   └── Makefile
    ├── my_python_module
    │   ├── __init__.py
    │   └── mod.py
    └── examples
        ├── plot_example.py
        ├── example.py
        └── README.txt (or .rst)


Enable the Sphinx-Gallery in the Sphinx doc/conf.py file with:

.. code:: Python

    extensions = [
        ...
        'sphinx_gallery.gen_gallery',
        ]

The following configuration declares the location of the `examples` directory 
to be ``../examples`` and the `output` directory to be ``examples``:

.. code:: Python

    sphinx_gallery_conf = {
     'examples_dirs': '../examples',   # path to your example scripts
     'gallery_dirs': 'examples',  # path to where to save gallery generated output
    }

General example
###############

This gallery consists of introductory example using pyvista.