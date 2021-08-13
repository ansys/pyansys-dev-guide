********************************
Coding Style and Best Practices
********************************
.. note::
   Until we have a site up for our best practices and coding style,
   the sphinx documentation site will host the coding style as well.

This page describes coding best practices applicable to the `pyansys
<https://pypi.org/project/pyansys/>`_ project.  The purpose of this
page is not to repeat coding style documentation, but rathers to state
the approach used by the pyansys project when there are any
delineations, clarifications, or additional procedures above and 
beyond `PEP8 <https://www.python.org/dev/peps/pep-0008/>`__.

For example, deprecation best practices are outlined in a `Stack
Overflow Answer <https://stackoverflow.com/questions/2536307>`_ and
there's even a `Deprecation library
<https://deprecation.readthedocs.io/>`_ but there is no official
guidance regarding deprecating features in an API within Python.  This
document seeks to clarify this issue and others.

Aside from pyansys specific directives, the best coding practice is to simply
follow established guidelines from `PEP8 <https://www.python.org/dev/peps/pep-0008/>`__.


Deprecation Best-Practice
-------------------------
Whenever a method, class, or function is deprecated, we must provide
an old method that calls the new method and raises a warning, or raise
an ``AttributeError`` if the method has been removed
altogether. Provide a `Sphinx Deprecated Directive
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-deprecated>`_
in the docstring of the older method and link to the newer method.

This way, when API changes are made we give the user a chance to
change theirs too or at least be notified when it changes. Otherwise,
they'll simply stop upgrading, or worse, using our API due to
stability concerns. For this reason, it's best to use a warning first
and then using an error after a minor release or two.


.. code:: python

    class FieldAnalysis2D():
        """Class docstring"""

        def assignmaterial(self, obj, mat):
            """Assign a material to one or more objects.

            .. deprecated:: 0.4.0
               Use :func:`FieldAnalysis2D.assign_material` instead.

            """
            # one of the following:

            # raise a DeprecationWarning.  User won't have to change anything
            warnings.warn('assignmaterial is deprecated.  Please use assign_material instead',
                          DeprecationWarning)
            self.assign_material(obj, mat)

            # or raise an AttributeError (could also make a custom DeprecationError)
            raise AttributeError('assignmaterial is deprecated.  Please use assign_material instead')

        def assign_material(self, obj, mat):
            """Assign a material to one or more objects.
            ...


If a method is outright removed, there's no reason to provide a link
to the old method, and we should simply raise an ``AttributeError``
should this be part of a class, or simply an ``Exception``.  For
example:

.. code:: python

    def hello_world():
        """Print ``"hello_world"``

        .. deprecated:: 0.4.0
            This function has been deprecated.

        """
        raise Exception('`my_function` has been deprecated')

Alternatively, you can create a custom ``DepricationError`` since
there is no built-in depreciation error within Python.

.. code:: python

    class DeprecationError(RuntimeError):
        """Used for depreciated methods and functions."""

        def __init__(self, message='This feature has been depreciated'):
            """Empty init."""
            RuntimeError.__init__(self, message)

Then simply use that inplace of ``Exception``

.. code:: python

    def hello_world():
        """Print ``"hello_world"``

        .. deprecated:: 0.4.0
            This function has been deprecated.

        """
        raise DeprecationError('`my_function` has been deprecated')


Notes Regarding Semantic Versioning and API Changes
---------------------------------------------------
According to `Semantic Versioning <https://semver.org/>`_, you should
increment the MAJOR version when you make incompatible changes.
However, adding or eliminating methods should not be considered
incompatible changes to a code base, but rather incremental changes
what are backwards compatible (to a degree).  Therefore, whenever a
method or feature is added, changed, or removed, the minor version
should be bumped.

To avoid constantly bumping the minor version, one approach to for
source-control branching is to create release branches where only
patch fixes are pushed to, and API changes occur between minor
releases.  See `Trunk Based Development
<https://trunkbaseddevelopment.com/>`_.  In summary, the mainline
branch (commonly named ``main`` or ``master`` must be already read to
release, and developers should create release branches to maintain at
least of one prior minor version.

The reason behind this is if a user wants to use API 0.4.0 instead of
0.5.0 due to some pressing deadline where they want to avoid a code
refactor, the maintainers of the API can back-port a bug-fix via ``git
cherry-pick <COMMIT-HASH>``.  This way users are given some time to
update any projects dependent on the API while still being treated as
"first-class" users.  Note that due to the complexity of maintaining
multiple "release branches" in a repository, the number of active
release branches should be between one and three.
