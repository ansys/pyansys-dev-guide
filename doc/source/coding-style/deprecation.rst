Deprecation best practices
==========================

While deprecation best practices are outlined in 
this `deprecation documentation <https://deprecation.readthedocs.io/>`_,
there is no official guidance on deprecating features within Python.
Thus, this topic provides deprecation best practices for PyAnsys
libraries. 

Whenever you deprecate a method, class, or function, you must take one of
these actions:

- Have the old method call the new method and raise a warning.
- Raise an ``AttributeError`` if you remove the method entirely.

In the docstring of the old method, use a Sphinx `deprecated directive
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-deprecated>`_
that links to the new method. This way, you notify your users when you make
an API change and give them a chance to change their code. Otherwise,
users stop upgrading, or worse, stop using your API, due to stability concerns.
For this reason, it is best to use a warning first and then use an error after
a minor release or two.

.. code:: python

    import warnings


    class FieldAnalysis2D:
        """Class docstring"""

        def assignmaterial(self, obj, mat):
            """Assign a material to one or more objects.

            .. deprecated:: 0.4.0
               Use :func:`FieldAnalysis2D.assign_material` instead.

            """
            # one of the following:

            # raise a DeprecationWarning. User won't have to change anything
            warnings.warn(
                "`assignmaterial` is deprecated. Use `assign_material` instead.",
                DeprecationWarning,
            )
            self.assign_material(obj, mat)

            # or raise an AttributeError (could also make a custom DeprecationError)
            raise AttributeError(
                "`assignmaterial` is deprecated. Use `assign_material` instead."
            )

        def assign_material(self, obj, mat):
            """Assign a material to one or more objects.
            ...
            """


If you remove a method entirely, there is no reason to provide a link to the old
method. Simply raise an ``AttributeError`` as part of the class or raise an ``Exception``.

.. code:: python

    def hello_world():
        """Print ``"hello_world"``

        .. deprecated:: 0.4.0
            This function has been deprecated.

        """
        raise Exception("`my_function` has been deprecated")

Because there is no built-in deprecation error within Python, an alternate
approach is to create a custom ``DeprecationError``.

.. code:: python

    class DeprecationError(RuntimeError):
        """Used for deprecated methods and functions."""

        def __init__(self, message="This feature has been deprecated."):
            """Empty init."""
            RuntimeError.__init__(self, message)

You then use this custom ``DeprecationError`` in place of an ``Exception``.

.. code:: python

    def hello_world():
        """Print ``"hello_world"``

        .. deprecated:: 0.4.0
            This function has been deprecated.

        """
        raise DeprecationError("`my_function` has been deprecated.")
