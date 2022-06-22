Supporting Python versions
==========================
Like other programming languages, Python evolves with time. New
features get added to the language, and others get deprecated. For
more information, see `Status of Python branches
<https://devguide.python.org/#status-of-python-branches>`_.

+---------+------------+-------------+-----------------------+--------+
| Version | PEP        | Released    | Security Support Ends | Status |
+---------+------------+-------------+-----------------------+--------+
| 3.11    | `PEP 664`_ | 03 Oct 2022 | 03 Oct 2027           | Dev    |
+---------+------------+-------------+-----------------------+--------+
| 3.10    | `PEP 619`_ | 04 Oct 2021 | 04 Oct 2026           | Dev    |
+---------+------------+-------------+-----------------------+--------+
| 3.9     | `PEP 596`_ | 05 Oct 2020 | 05 Oct 2025           | Stable |
+---------+------------+-------------+-----------------------+--------+
| 3.8     | `PEP 569`_ | 14 Oct 2019 | 14 Oct 2024           | Stable |
+---------+------------+-------------+-----------------------+--------+
| 3.7     | `PEP 537`_ | 27 Jun 2018 | 27 Jun 2023           | Stable |
+---------+------------+-------------+-----------------------+--------+

.. _PEP 664: https://peps.python.org/pep-0664/
.. _PEP 619: https://peps.python.org/pep-0619/
.. _PEP 596: https://peps.python.org/pep-0596/
.. _PEP 569: https://peps.python.org/pep-0569/
.. _PEP 537: https://peps.python.org/pep-0537/

.. admonition:: Consider supporting stable Python versions.

   Python versions labeled as ``stable`` receive only security
   fixes. Versions labeled as ``dev`` are still receiving bug fixes.

Expect stable versions to be the most commonly used Python versions. Some
libraries like `NumPy <https://numpy.org/>`_ drop support for older versions of
Python earlier than their end of life (EOL) as outlined in `NEP 29
<https://numpy.org/neps/nep-0029-deprecation_policy.html#support-table>`_.

You can still install an older version from PyPI using ``pip`` as
your package manager. When ``pip`` is used, it downloads and installs
the most recent version of the library that supports your version of Python. You
can enforce a minimum-required Python version within ``setup.py`` with:

.. code:: python

    from setuptools import setup

    [...]

    setup(name="my_package_name", python_requires=">3.6", [...])


This helps ``pip`` to know which versions of your library
support which versions of Python. You can also impose an upper limit if you're
sure you don't support certain versions of Python. For example, if you only
support Python 3.6 through 3.9, your command would look like this: ``python_requires='>=3.6, <3.10'``.


Verifying support
-----------------
The best way to validate whether a Python library supports a version of Python
is by :ref:`Using Continuous Integration`. An example GitHub
workflow testing Python 3.7 through Python 3.10 on Windows and Linux would
start with:

.. code:: yaml
   :linenos:
   :emphasize-lines: 8, 13-16

   jobs:
     unittest:
       name: Unit Testing
       runs-on: ${{ matrix.os }}
       strategy:
         matrix:
           os: [windows-latest, ubuntu-latest]
           python-version: ['3.7', '3.8', '3.9', '3.10']

       steps:
         - uses: actions/checkout@v2

         - name: Set up Python ${{ matrix.python-version }}
           uses: actions/setup-python@v2
           with:
             python-version: ${{ matrix.python-version }}

         - name: Unit testing
           run: |

The workflow would then list the tests to run.
