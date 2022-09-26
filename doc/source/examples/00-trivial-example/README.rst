.. _ref_how_to_add_an_example_reference_key:

The ``examples`` contains the files used by Sphinx-Gallery to build the gallery.

.. code:: rst

    In the built documentation, it will be rendered as rST. All rST lines
    must begin with '# ' (note the space) including underlines below section
    headers.

    # %%
    # This is a section header
    # ------------------------
    # This is the first section!
    # The `#%%` signifies to Sphinx-Gallery that this text should be rendered as
    # rST and if using one of the above IDE/plugin's, also signifies the start of a
    # 'code block'

    These lines won't be rendered as rST because there is a gap after the last
    commented rST block. Instead, they'll resolve as regular Python comments.
        
    # This is commented python

General examples
################

This gallery consists of introductory example.