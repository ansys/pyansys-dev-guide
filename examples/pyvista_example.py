"""
.. _adding_a_new_gallery_example:

Adding a new gallery example
============================

This example demonstrates how to add a new PyAnsys `Sphinx Gallery
<https://sphinx-gallery.github.io/>`_ example as well as being a template that
can be used in their creation.
Each example should have a reference tag/key in the form:
``.. _<example-name>_example:``.

The ``.. _`` is necessary. Everything that follows is your reference tag, which
can potentially be used within a docstring. As convention, we keep all
references in ``snake_case``.
This section should give a brief overview of what the example is about and/or
demonstrates. The title should be changed to reflect the topic your example
covers.
New examples should be added as python scripts to:
``examples/<index>-<directory-name>/<some-example>.py``

.. note::

   Avoid creating new directories unless absolutely necessary. If you *must*
   create a new folder, make sure to add a ``README.txt`` containing a
   reference, a title and a single sentence description of the folder.
   Otherwise the new folder will be ignored by Sphinx.

Example file names should be hyphen separated snake case:
``some-example.py``
After this preamble is complete, the first code block begins. This is where you
typically set up your imports.
"""
import pyvista as pv

###############################################################################
# Section title
# ~~~~~~~~~~~~~
#
# Code blocks can be broken up with text "sections" which are interpreted as
# restructured text.
#
# This will also be translated into a markdown cell in the generated Jupyter
# notebook or the HTML page.
#
# Sections can contain any information you may have regarding the example
# such as step-by-step comments or notes regarding motivations etc.
#
# As in Jupyter notebooks, if a statement is unassigned at the end of a code
# block, output will be generated and printed to the screen according to its
# ``__repr__`` method. Otherwise, you can use ``print()`` to output text.

# Create a dataset and exercise its repr method

dataset = pv.Sphere()
dataset

###############################################################################
# Plots and images
# ~~~~~~~~~~~~~~~~
# If you use anything that outputs an image (for example,
# :func:`pyvista.Plotter.show`) the resulting image is rendered within the
# output HTML.
#
# .. note::
#
#    Unless ``sphinx_gallery_thumbnail_number = <int>`` is included at the top
#    of the example script, first figure (this one) is used for the
#    gallery thumbnail image.
#
#    Also note that this image number uses one based indexing.

dataset.plot(text="Example Figure")

###############################################################################
# Caveat - plotter must be within one cell
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# It's not possible for a single :class:`pyvista.Plotter` object across
# multiple cells because these are closed out automatically at the end of a
# cell.
#
# Here we just exercise the :class:`pyvista.Actor` ``repr`` for demonstrating
# why you might want to instantiate a plotter without showing it in the same
# cell.

pl = pv.Plotter()
actor = pl.add_mesh(dataset)
actor

###############################################################################
# This cell cannot run the plotter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The plotter is already closed by ``sphinx_gallery``.

# This cannot be run here because the plotter is already closed and would raise
# an error:
# >>> pl.show()

# You can, however, close out the plotter or access other attributes.

pl.close()

###############################################################################
# Making a pull request
# ~~~~~~~~~~~~~~~~~~~~~
# Once your example is complete and you've verified it builds locally, you can
# make a pull request (PR).
#
# Branches containing examples should be prefixed with `docs/` as per the branch
# naming conventions found in out `Contributing Guidelines
# <https://dev.docs.pyansys.com/how-to/contributing.html#branch-naming-conventions>`_.
#
# .. note::
#
#    You only need to create the Python source example (``*.py``).  The Jupyter
#    notebook and the example HTML are auto-generated via `sphinx-gallery
#    <https://sphinx-gallery.github.io/>`_.
