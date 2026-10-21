Deprecation best practices
==========================

Deprecating an API gives users time to migrate before a feature is removed or
its behavior changes. `PEP 702 <https://peps.python.org/pep-0702/>`_ introduces
a standard decorator for marking deprecated APIs so that type checkers and
editors can report their use, in addition to runtime warnings. This topic
provides deprecation best practices for PyAnsys libraries.

.. note::
    This page covers API-level deprecation of methods, classes, and functions.
    For retiring an entire repository or package lifecycle, see
    :ref:`deprecating`.

Choose the mechanism that matches the scope of the deprecation:

- Use the PEP 702 ``@deprecated`` decorator when an entire method, class,
  property or function is deprecated.
- Use ``warnings.warn(..., DeprecationWarning)`` when only a parameter,
  parameter value, or behavior within a function is deprecated.

Keep the deprecated API working during the migration period. When possible,
have the old implementation call its replacement and preserve its return value.
When possible, document the version in which the API was deprecated, the
replacement, and the planned removal version in the docstring and release notes.
Follow your library's compatibility policy when deciding how long to retain it.

Deprecate an entire API with PEP 702
------------------------------------

The `warnings.deprecated
<https://docs.python.org/3.13/library/warnings.html#warnings.deprecated>`_
decorator is available in Python 3.13 and later. For earlier Python versions,
use `typing_extensions.deprecated
<https://typing-extensions.readthedocs.io/en/latest/#typing_extensions.deprecated>`_,
which is available in ``typing-extensions`` 4.5.0 and later.

Use a version-dependent import to support both:

.. code:: python

    import sys

    if sys.version_info >= (3, 13):
        from warnings import deprecated
    else:
        from typing_extensions import deprecated

Declare ``typing-extensions`` as a runtime dependency for Python versions below
3.13, not just a development dependency. For example, add the following entry
to your project's existing ``[project].dependencies`` list:

.. code:: toml

    [project]
    dependencies = [
        "typing-extensions>=4.5; python_version < '3.13'",
    ]

By default, ``@deprecated`` emits a ``DeprecationWarning`` when a decorated
function or method is called, or when a decorated class is instantiated or
inherited from. Supporting type checkers and editors can also flag deprecated API
usage without executing the code, depending on their configuration. The
decorator does not remove the API or prevent its execution.

Document deprecation and removal versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``@deprecated`` does not update the docstring or generate Sphinx directives.
It accepts a message, not structured metadata such as ``deprecated_in`` or
``removed_in``. Versions mentioned in that message are informational: the
decorator does not compare versions, schedule removal, or start raising an
error when a removal version is reached.

In the docstring of the old method, use a Sphinx `deprecated directive
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-deprecated>`_
to record the deprecation version, link to the replacement, and describe the
planned removal version in the directive body. Keep these details consistent
with the decorator's message and release notes. The directive affects the
rendered documentation, whereas ``@deprecated`` provides static diagnostics
and, by default, a runtime warning. Neither replaces the other.

The following example uses the ``deprecated`` import shown earlier:

.. code:: python

    class FieldAnalysis2D:
        """Manage a two-dimensional field analysis."""

        @deprecated(
            "`assignmaterial` is deprecated since 0.4.0. "
            "Use `assign_material` instead. It will be removed in 0.6.0."
        )
        def assignmaterial(self, obj, mat):
            """Assign a material to one or more objects.

            .. deprecated:: 0.4.0
               Use :meth:`FieldAnalysis2D.assign_material` instead.
               This method will be removed in 0.6.0.

            """
            return self.assign_material(obj, mat)

        def assign_material(self, obj, mat):
            """Assign a material to one or more objects."""
            ...

Do not add a manual warning for the same deprecation inside a decorated
function, the decorator already emits one. If an existing implementation must
retain its own warning logic, ``@deprecated("...", category=None)`` adds the
static deprecation marker without emitting an additional runtime warning.

Combine documentation and PEP 702 decorators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of writing the directive manually for every API, a project can use
an additional decorator to store version metadata and update the docstring.
For example, the following documentation-only decorator adds a Sphinx
directive without wrapping the function or changing its runtime behavior:

.. code:: python

    import inspect
    import re


    def deprecation_doc(*, deprecated_in, removed_in):
        """Add deprecation details to a function's documentation."""

        def decorator(func):
            message = getattr(func, "__deprecated__", None)
            if not isinstance(message, str):
                raise ValueError(
                    "Apply deprecated_doc above the standard @deprecated decorator."
                )
            docstring = func.__doc__ or ""
            if ".. deprecated::" not in docstring:
                docstring = inspect.cleandoc(docstring)
                directive = f".. deprecated:: {deprecated_in}\n   Scheduled for removal in {removed_in}."
                paragraphs = re.split(r"\n[ \t]*\n", docstring, maxsplit=1)
                summary = paragraphs[0]
                remainder = paragraphs[1] if len(paragraphs) > 1 else ""
                func.__doc__ = "\n\n".join(
                    part for part in (summary, directive, remainder) if part
                )
            return func

        return decorator


    @deprecation_doc(deprecated_in="0.4.0", removed_in="0.6.0")
    @deprecated("`old_function` is deprecated, use `new_function` instead.")
    def old_function():
        """Perform the original operation."""
        ...

Verify both the rendered documentation and static diagnostics when composing
decorators, and check that warnings still point to the user's call site.

If a third-party decorator also emits runtime deprecation warnings, configure
one of the decorators not to emit them. For example, use
``@deprecated("...", category=None)`` for the static marker and let the other
decorator own the runtime warning.

Deprecate part of a function
----------------------------

Using ``warnings.warn`` with ``DeprecationWarning`` remains valid and is
recommended for conditional deprecations. For example, a function might still
be supported while one of its parameter values or execution paths is not.
Decorating the entire function would incorrectly mark all calls as deprecated.

.. code:: python

    def output_restult(output_format):
        """Output results.

        The ``"legacy"`` output format is deprecated. Use ``"json"`` instead.

        """
        if output_format == "legacy":
            warnings.warn(
                'The "legacy" output format is deprecated since 0.4.0. '
                'Use "json" instead.',
                DeprecationWarning,
                stacklevel=2,
            )
        elif output_format == "json":
            ...

Here, only calls that request ``output_format="legacy"`` emit a warning.
The default JSON format remains supported without a deprecation warning.
Set ``stacklevel=2`` so that the warning points to the caller rather than to
the ``warnings.warn`` call. Adjust it if additional wrapper functions are used.
