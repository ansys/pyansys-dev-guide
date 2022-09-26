.. _ref_example_gallery:

============
Add Examples
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

The following configuration declares the location of the ‘examples’ directory 
('example_dirs') to be ../examples and the ‘output’ directory ('gallery_dirs') to
be auto_examples:

.. code:: Python
    
    sphinx_gallery_conf = {
         'examples_dirs': '../examples',   # path to your example scripts
         'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
    }

Here are the contents of an example Python file using the ‘code block’ functionality:  

.. code:: rst

    ""
    This is my example script
    =========================

    This example doesn't do much, it just makes a simple plot
    """

    # %%
    # This is a section header
    # ------------------------
    # This is the first section!
    # The `#%%` signifies to Sphinx-Gallery that this text should be rendered as
    # rST and if using one of the above IDE/plugin's, also signifies the start of a
    # 'code block'.

    # This line won't be rendered as rST because there's a space after the last block.
    myvariable = 2
    print("my variable is {}".format(myvariable))
    # This is the end of the 'code block' (if using an above IDE). All code within
    # this block can be easily executed all at once.

    # %%
    # This is another section header
    # ------------------------------
    #
    # In the built documentation, it will be rendered as rST after the code above!
    # This is also another code block.

    print('my variable plus 2 is {}'.format(myvariable + 2))

General example
###############

This gallery consists of introductory example.

.. toctree::
   :hidden:
   :maxdepth: 2