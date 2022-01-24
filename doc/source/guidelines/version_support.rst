Python Version Support
======================

When creating Python libraries, plan on supporting the oldest actively supported
version of Python. For a quick reference, visit `Status of Python Branches
<https://devguide.python.org/#status-of-python-branches>`_. Here is a summary as
of 2022:

+---------+-------------+-----------------------+
| Version | Released    | Security Support Ends |
+---------+-------------+-----------------------+
| 3.10    | 04 Oct 2021 | 04 Oct 2026           |
+---------+-------------+-----------------------+
| 3.9     | 05 Oct 2020 | 05 Oct 2025           |
+---------+-------------+-----------------------+
| 3.8     | 14 Oct 2019 | 14 Oct 2024           |
+---------+-------------+-----------------------+
| 3.7     | 27 Jun 2018 | 27 Jun 2023           |
+---------+-------------+-----------------------+

Expect these to be the most commonly used Python versions. Note that some
libraries like `NumPy <https://numpy.org/>`_ drop support for older versions of
Python earlier than their end of life (EOL) as outlined in `NEP 29
<https://numpy.org/neps/nep-0029-deprecation_policy.html#support-table>`_.

Realize that users can still install the older version from PyPI via ``pip`` as
the package manager (``pip``). When ``pip`` is used, it downloads and installs the most recent version
of THE library that supports your version of Python. You can enforce a minimum-
required Python version within ``setup.py`` with:

.. code:: python

   from setuptools import setup

   [...]

   setup(name="my_package_name",
         python_requires='>3.6',
   [...]
   )

This helps ``pip`` to know which versions of your library
support which versions of Python. You can also impose an upper limit if you're
sure you don't support certain versions of Python. For example, if you only
support Python 3.6 through 3.9: ``python_requires='>=3.6, <3.10'``.


Verifying Support
-----------------
The best way to validate whether a Python library supports a version of
Python is to validate it via unit testing within CI/CD. An example
GitHub workflow testing Python 3.6 through Python 3.10 on Windows and Linux
would would start with::

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
             ...

