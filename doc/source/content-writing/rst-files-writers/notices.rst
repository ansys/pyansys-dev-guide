.. _notices:

Notices
=======

In the *Google developer documentation style guide*, the
`Notes, cautions, warnings, and other notices <Google_dev_doc_notices_>`_
page explains how notices offset important information. In addition to defining
types, it explains when notices should be used. Avoid overuse because notices
lose their visual distinctiveness if a page has multiple notices or two (or more)
consecutive notices.

PyAnsys documentation uses these admonition directives for common notices:

- ``note``
- ``caution``
- ``warning``
- ``important``
- ``tip``

Note example
------------
Here is a formatting example for a ``note`` directive::

  .. note::
      Some examples require additional Python packages. Ensure
      that you have these packages installed.

Here is how this note is rendered in the documentation:

.. note::
    Some examples require additional Python packages. Ensure
    that you have these packages installed.

Caution example
---------------
Here is a formatting example for a ``caution`` directive::

  .. caution::
      To ensure proper operation, modify this XML file carefully.
      All paths specified in this file must adhere to the path
      conventions of the respective operating system.

Here is how this caution is rendered in the documentation:

.. caution::
    To ensure proper operation, modify this XML file carefully.
    All paths specified in this file must adhere to the path
    conventions of the respective operating system.

Warning example
---------------
Here is a formatting example for a ``warning`` directive::

  .. warning::
      This method requires `NumPy <numpy_>`_` to be installed on your machine.

Here is how this warning is rendered in the documentation:

.. warning::
    This method requires `NumPy <numpy_>`_` to be installed on your machine.

Important example
-----------------
Here is a formatting example for an ``important`` directive::

  .. important::
      Net tracing is a critical requirement for using the ``auto_compoments``
      definition type when defining components on the die.

Here is how this important notice is rendered in the documentation:

.. important::
    Net tracing is a critical requirement for using the ``auto_compoments``
    definition type when defining components on the die.

Tip example
-----------

Here is a formatting example for a ``tip`` directive::

  .. tip::
      When you are viewing PyAnsys documentation, the right navigation pane typically
      displays **Edit on GitHub** and **Show Source** links. For information on
      using the **Edit on GitHub** link to use the GitHub web editor to submit
      suggested changes to a page in a PR, see :ref:`edit_on_GitHub`. For information
      on using the **Show Source** link to see how a page's source file is formatted and
      how you can reuse this content, see :ref:`rst_file_examples`.

Here is how this tip is rendered in the documentation:

.. tip::
    When you are viewing PyAnsys documentation, the right navigation pane typically
    displays **Edit on GitHub** and **Show Source** links. For information on
    using the **Edit on GitHub** link to use the GitHub web editor to submit
    suggested changes to a page in a PR, see :ref:`edit_on_GitHub`. For information
    on using the **Show Source** link to see how a page's source file is formatted and
    how you can reuse this content, see :ref:`rst_file_formatting`.
