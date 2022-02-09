Beyond PEP8
###########
This topic describes any delineations, clarifications, or additional procedures above and 
beyond `PEP8 <https://www.python.org/dev/peps/pep-0008/>`__.

For example, `Stack Overflow Answer <https://stackoverflow.com/questions/2536307>`_ 
outlines deprecation best practices and a `Deprecation library <https://deprecation.readthedocs.io/>`_ 
already exists. However, there is no official guidance regarding deprecating features 
in an API within Python. This page seeks to clarify this issue and others.

Aside from the following PyAnsys-specific directives, the best coding practice is to 
follow established guidelines from `PEP8 <https://www.python.org/dev/peps/pep-0008/>`__.


Deprecation Best Practice
-------------------------
Whenever a method, class, or function is deprecated, you must provide
an old method that both calls the new method and raises a warning. Or, 
if the method has been removed, you must raise an ``AttributeError``. 

In the docstring of the older method, provide a `Sphinx Deprecated Directive
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-deprecated>`_ 
and a link to the newer method. This way, users are notified that an API change 
has occurred and are given an opportunity to change their code. Otherwise, 
stability concerns can cause users to stop upgrading, or worse, stop using 
Ansys APIs. For this reason, it's best to use a warning first and then use 
an error after a minor release or two.


.. code:: python

    class FieldAnalysis2D():
        """Class docstring"""

        def assignmaterial(self, obj, mat):
            """Assign a material to one or more objects.

            .. deprecated:: 0.4.0
               Use :func:`FieldAnalysis2D.assign_material` instead.

            """
            # one of the following:

            # raise a DeprecationWarning. User won't have to change anything.
            warnings.warn('assignmaterial is deprecated. Use assign_material instead.',
                          DeprecationWarning)
            self.assign_material(obj, mat)

            # or raise an AttributeError (could also make a custom DeprecationError)
            raise AttributeError('assignmaterial is deprecated. Use assign_material instead.')

        def assign_material(self, obj, mat):
            """Assign a material to one or more objects.
            ...


If a method is removed entirely, there's no reason to provide a link
to the old method. If the method is part of a class, raise an 
``AttributeError``. Otherwise, raise an ``Exception``.

This example raises an ``Exception``:

.. code:: python

    def hello_world():
        """Print ``"hello_world"``

        .. deprecated:: 0.4.0
            This function has been deprecated.

        """
        raise Exception('`my_function` has been deprecated.')

Because there is no built-in deprecation error within 
Python, an alternative is to create a custom ``DeprecationError``.

.. code:: python

    class DeprecationError(RuntimeError):
        """Used for depreciated methods and functions."""

        def __init__(self, message='This feature has been depreciated.'):
            """Empty init."""
            RuntimeError.__init__(self, message)

You can then use this custom ``DeprecationError`` in place of an ``Exception``.

.. code:: python

    def hello_world():
        """Print ``"hello_world"``

        .. deprecated:: 0.4.0
            This function has been deprecated.

        """
        raise DeprecationError('`my_function` has been deprecated')


Semantic Versioning and API Changes
-----------------------------------
According to `Semantic Versioning <https://semver.org/>`_, you should
increment the MAJOR version when you make incompatible changes.
However, adding or eliminating methods should not be considered
incompatible changes to a code base but rather incremental changes
that are backwards-compatible (to a degree). Therefore, whenever a
method or feature is added, changed, or removed, the minor version
should be bumped.

To avoid constantly bumping the minor version, one approach to 
source-control branching is to create release branches where only
patch fixes are pushed and API changes occur between minor
releases. See `Trunk Based Development
<https://trunkbaseddevelopment.com/>`_.  

In summary, the mainline branch (commonly named ``main`` or ``master``) 
must always be ready to release, and developers should create 
release branches to maintain at least one prior minor version.

The reason behind this is if a user wants to use API 0.4.0 instead of
0.5.0 due to some pressing deadline where they want to avoid a code
refactor, the maintainers of the API can back-port a bug-fix via ``git
cherry-pick <COMMIT-HASH>``.  This gives users some time to update any 
projects dependent on the API while still treating them as
"first-class" users.  

Note that due to the complexity of maintaining multiple "release branches" 
in a repository, the number of active release branches should be between 
one and three.

Docstring Examples Best Practice
--------------------------------
Defining docstring examples for methods and classes is extremely 
useful. The examples give users an easy place to start when trying 
out the API, showing them exactly how to operate on a method or 
class. By using ``doctest`` through ``pytest``, docstring examples can 
also be used to perform regression testing to verify that the code is 
executing as expected.

This is an important feature of maintainable documentation as examples
must always match the API they are documenting. When using ``doctest`` 
through ``pytest``, any changes within the API without corresponding 
changes in the documentation will trigger doctest failures.

Setting Up ``doctest``
~~~~~~~~~~~~~~~~~~~~~~
First, install ``pytest``.

.. code::

    pip install pytest

Now, run ``doctest`` on any Python file.

.. code::

    pytest --doctest-modules file.py

``doctest`` searches for examples in the docstrings and executes them 
to verify that they function as written.

Using ``pytest`` Fixtures
~~~~~~~~~~~~~~~~~~~~~~~~~
To define a setup sequence before the ``doctest`` run or before a given 
module is tested, you use ``pytest`` fixtures. Because fixtures allow 
docstring examples to access shared objects, there is no need to repeat 
the setup in each example.

``pytest`` fixtures can be defined in a ``conftest.py`` file next to the source 
code. The following example shows a fixture that is run automatically for 
each ``doctest`` session.

.. code:: python

    import pytest

    from pyaedt import Desktop


    @pytest.fixture(autouse=True, scope="session")
    def start_aedt():
        desktop = Desktop("2021.1", NG=True)
        desktop.disable_autosave()

        # Wait to run doctest on docstrings
        yield desktop
        desktop.force_close_desktop()

Fixtures can also be defined in a separate Python file from 
``conftest.py``. This may help keep the fixtures more organized. Fixtures 
from other files need to be imported in the main ``conftest.py`` file. 

This example shows how to import fixtures defined in an 
``icepak_fixtures.py`` file under the ``doctest_fixtures`` folder.

.. code:: python

    import pytest

    from pyaedt import Desktop
    from pyaedt.doctest_fixtures import *

    # Import fixtures from other files
    pytest_plugins = [
        "pyaedt.doctest_fixtures.icepak_fixtures",
    ]


    @pytest.fixture(autouse=True, scope="session")
    def start_aedt():
        desktop = Desktop("2021.1", NG=True)
        desktop.disable_autosave()

        # Wait to run doctest on docstrings
        yield desktop
        desktop.force_close_desktop()

The ``doctest_namespace`` fixture built into ``doctest`` allows injecting
items from a fixture into the context of the ``doctest`` run. To use this
feature, the fixture needs to accept the ``doctest_namespace`` dictionary
as an argument. Then, objects can be added to the ``doctest_namespace``
dictionary and used directly in a docstring example.

This examples shows how the ``Icepak`` object can be stored in the
``doctest_namespace`` dictionary by adding the key ``icepak`` with the 
``Icepak`` object as the value. 

.. code:: python

    import pytest
    from pyaedt import Icepak


    @pytest.fixture(autouse=True, scope="module")
    def create_icepak(doctest_namespace):
        doctest_namespace["icepak"] = Icepak(projectname="Project1", designname="IcepakDesign1")

The ``Icepak`` object can then be used directly inside a docstring
example by referencing the key ``icepak``.

.. code:: python

    def assign_openings(self, air_faces):
        """Assign openings to a list of faces.

        Parameters
        ----------
        air_faces : list
            List of face names.

        Returns
        -------
        :class:`pyaedt.modules.Boundary.BoundaryObject`
            Boundary object when successful or ``None`` when failed.

        Examples
        --------

        Create an opening boundary for the faces of the "USB_GND" object.

        >>> faces = icepak.modeler.primitives["USB_GND"].faces
        >>> face_names = [face.id for face in faces]
        >>> boundary = icepak.assign_openings(face_names)
        pyaedt Info: Face List boundary_faces created
        pyaedt Info: Opening Assigned

        """

Useful ``doctest`` Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ellipses for Random Output
**************************
If the output of some operation in an example cannot be verified exactly,
an ellipsis (``...``) can be used in the expected output. This allows it
to match any substring in the actual output.

.. code ::

    Examples
    --------

    >>> desktop = Desktop("2021.1")
    pyaedt Info: pyaedt v...
    pyaedt Info: Python version ...

To support this, ``doctest`` must be run with the option set to allow ellipses.

.. code ::

    pytest --doctest-modules -o ELLIPSIS file.py

``doctest`` Skip
****************
The directive ``# doctest: +SKIP`` can be added to any line of a
docstring example so that it is not executed in ``doctest-modules``. 
This is useful for examples that cannot run within ``pytest`` or have 
side effects that will affect the other tests if they are run during 
the ``doctest`` session.

.. code :: python

    Examples
    --------

    >>> desktop = Desktop("2021.1") # doctest: +SKIP
