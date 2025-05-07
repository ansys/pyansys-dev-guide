# Copyright (C) 2021 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
.. _adding_a_new_gallery_example:

Adding a new gallery example
============================

This example shows how to add a new example to the PyAnsys `Sphinx-Gallery
<https://sphinx-gallery.github.io/>`_. You can use this example as a template
for adding your examples.

Each example should have a reference tag/key in the form:

``.. _<example-name>_example:``.

The ``.. _`` is necessary. Everything that follows is your reference tag, which
can potentially be used within a docstring. All references should be in snake case.

The first section, which is text, provides a brief overview of what the example is.
When using this example as a template, you would change the title to an appropriate
one for your example.

Add new examples as Python scripts like this:

``examples/<index>-<directory-name>/<some-example>.py``

.. note::

   Avoid creating directories unless absolutely necessary. If you *must*
   create a directory, make sure to add a ``README.txt`` file containing a
   reference, a title, and a one-sentence description of the directory.
   Otherwise, Sphinx ignores the new directory.

Example file names should use snake case and be hyphen-separated:

``some-example.py``

After this text section is the first code block. This is where you
typically set up your imports.
"""

import pyvista as pv

###############################################################################
# Section title
# ~~~~~~~~~~~~~
#
# Code blocks can be broken up with text sections, which are interpreted as
# ReStructuredText.
#
# The text sections are also translated into a markdown cell in the generated Jupyter
# notebook or in the HTML documentation.
#
# Text sections can contain any information that you may have regarding the example,
# such as step-by-step comments and notes regarding motivations.
#
# As in Jupyter notebooks, if a statement is unassigned at the end of a code
# block, output is generated and printed to the screen according to its
# ``__repr__`` method. Otherwise, you can use the ``print()`` function to output text.

# Create a dataset and exercise its ``__repr__`` method

dataset = pv.Sphere()
dataset

###############################################################################
# Plots and images
# ~~~~~~~~~~~~~~~~
# If you use anything that outputs an image (for example, the
# :func:`pyvista.Plotter.show` function), the resulting image is rendered in the
# HTML documentation.
#
# .. note::
#
#    Unless ``sphinx_gallery_thumbnail_number = <int>`` is included at the top
#    of the example script, the first figure (this one) is used for the
#    gallery thumbnail image.
#
#    Also note that this image number uses one-based indexing.

dataset.plot(text="Example Figure")

###############################################################################
# Caveat - plotter must be within one cell
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# It's not possible to have a single :class:`pyvista.Plotter` object across
# multiple cells because these are closed out automatically at the end of a
# cell.
#
# This code exercise the :class:`pyvista.Actor` ``repr`` to demonstrate
# why you might want to instantiate a plotter without showing it in the same
# cell:

pl = pv.Plotter()
actor = pl.add_mesh(dataset)
actor

###############################################################################
# This cell cannot run the plotter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Because the plotter is already closed by Sphinx-Gallery, the following code
# would raise an error:
#
# >>> pl.show()

# You can, however, close out the plotter or access other attributes.

pl.close()

###############################################################################
# Create a pull request
# ~~~~~~~~~~~~~~~~~~~~~
# Once your example is complete and you've verified that it builds locally, you can
# create a pull request.
#
# Branches containing examples should be prefixed with ``docs/`` as per `Branch-naming conventions
# <https://dev.docs.pyansys.com/how-to/contributing.html#branch-naming-conventions>`_.
#
# .. note::
#
#    You only need to create the Python source example (PY file). Sphinx-Gallery
#    automatically generates the Jupyter notebook and the RST file for generating
#    the HTML documentation page.
