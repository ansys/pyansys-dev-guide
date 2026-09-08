.. _images:

Images
======

You use the ``image`` or ``figure`` directive to add an image to
a RST file.

Both directives support these types of image files: PNG, JPG, and GIF.

While these two directives are similar, the ``figure`` directive supports adding
a label and a caption for the image, where the label can be used for cross-referencing
in your documentation.

For either directive, the setup is the same:

#. Place the image file in your library's ``doc/source/_static`` directory.
#. Place the directive in your RST file where you want the image to appear,
   using the relative path to this image file in the ``image`` or ``figure``
   directive.

Add an image using the ``image`` directive
-----------------------------------------------

When you use the ``image`` directive to add an image, you only need to specify the path
to the image file. However, specifying the optional ``alt`` attribute, which provides text for
the image, is strongly recommended::

  .. image:: ..//_static/image1.png
     :alt: Example first image

This next ``image`` directive provides all optional attributes::

  .. image:: ..//_static/image2.png
     :width: 300
     :height: 200
     :alt: Example second image
     :align: center

Here are descriptions of all optional attributes for the ``image`` directive:

- ``width`` and ``height``: Control the width and height of the image in pixels.
  You can specify one of these attributes to maintain the aspect ratio, or specify
  both attributes to set specific dimensions.
- ``alt``: Provides text for the image. This attribute is used for accessibility
  and should provide a concise description of the image content. It is also displays
  if the image fails to load.
- ``align``: Controls the horizontal alignment of the image. Options are  ``left``,
  ``right``, and ``center``. If omitted, the image is left-aligned.

Add an image using the ``figure`` directive
------------------------------------------------

When you use the ``figure`` directive to add an image, you can specify the  ``name``
attribute and a caption. The ``name`` attribute is a custom label that can
be used to cross-reference the image in your documentation. The caption provides
context or explanations.

Here is an example of a ``figure`` directive::

  .. figure:: ..//_static/image3.png
     :figwidth: 300
     :alt: Example figure
     :name: custom-label

     You add the caption here.

To reference this image elsewhere in your documentation, use the custom label defined
for the ``name`` attribute::

  For the plot of the temperatures, see :ref:`custom-label`.

This creates a reference to the image where the ``name`` attribute is defined as ``custom-label``.
Sphinx displays this image with its caption and specified label in the rendered documentation.
