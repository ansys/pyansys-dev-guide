Python versions
===============

Like other programming languages, Python evolves with time. New
features get added to the language, and other features get deprecated. For
more information, see `Status of Python versions
<https://devguide.python.org/versions/#versions>`_ in the *Python
Developer's Guide*.

+-------------+----------------+-----------------+---------------------------+------------+
| **Version** | **PEP**        | **Released**    | **Security support ends** | **Status** |
+-------------+----------------+-----------------+---------------------------+------------+
| 3.13        | `PEP 719`_     | 07 Oct 2024     |    Oct 2029               | Stable     |
+-------------+----------------+-----------------+---------------------------+------------+
| 3.12        | `PEP 693`_     | 02 Oct 2023     |    Oct 2028               | Stable     |
+-------------+----------------+-----------------+---------------------------+------------+
| 3.11        | `PEP 664`_     | 03 Oct 2022     |    Oct 2027               | Stable     |
+-------------+----------------+-----------------+---------------------------+------------+
| 3.10        | `PEP 619`_     | 04 Oct 2021     |    Oct 2026               | Stable     |
+-------------+----------------+-----------------+---------------------------+------------+

.. _PEP 719: https://peps.python.org/pep-0719/
.. _PEP 693: https://peps.python.org/pep-0693/
.. _PEP 664: https://peps.python.org/pep-0664/
.. _PEP 619: https://peps.python.org/pep-0619/

.. admonition:: Consider supporting stable Python versions.

   Python versions labeled as ``stable`` receive only security
   fixes. Versions labeled as ``dev`` are still receiving bug fixes.

Expect stable versions to be the most commonly used Python versions. Some
packages like `NumPy`_ drop support for older versions of
Python earlier than their end of life (EOL) as outlined in `NEP 29
<https://numpy.org/neps/nep-0029-deprecation_policy.html#support-table>`_.

You can still install an older version from PyPI using `pip`_ as
your package manager. When ``pip`` is used, it downloads and installs
the most recent version of the library that supports your version of Python. You
can enforce a minimum-required Python version within the ``setup.py`` file with
this code:

.. code:: python

    from setuptools import setup

    [...]

    setup(name="my_package_name", python_requires=">3.10", [...])


This helps ``pip`` to know which versions of your library
support which versions of Python. You can also impose an upper limit if you're
sure you don't support certain versions of Python. For example, if you only
support Python 3.10 through 3.13, your command would look like this: ``python_requires='>=3.10, <3.13'``.

Verify Python support
---------------------

The best way to validate whether a Python library supports a version of Python
is by :ref:`continuous_integration`. An example GitHub workflow testing Python
3.10 through Python 3.13 on Windows and Linux would start like this:

.. code-block:: yaml
   :linenos:
   :emphasize-lines: 8, 13

   jobs:
     tests:
       name: "Tests"
       runs-on: ${{ matrix.os }}
       strategy:
         matrix:
           os: [windows-latest, ubuntu-latest]
           python-version: ['3.10', '3.11', '3.12', '3.13']
       steps:
         - name: "Run tests using pytest"
           run: ansys/actions/test-pytest@v8
           with:
             python-version: ${{ matrix.os }}

The workflow would then list the tests to run.
