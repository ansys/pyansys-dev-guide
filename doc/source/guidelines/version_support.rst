Python Version Support
======================

When creating Python libraries, plan on supporting the oldest actively supported
version of Python. For a quick reference, visit `Python EOL
<https://endoflife.date/python>`_. Here is 2022 summary:

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

Expect these to be the most commonly used Python versions. Note that recently dropped versions (Python 3.6) will no longer have wheels built for popular libraries like `numpy <https://numpy.org/>`_. You can still install the older version from PyPI via ``pip`` since version support tends to gradually "drop off" rather than cease entirely when security support exits.

You can enforce a minimum required Python version within ``setup.py`` with:

.. code:: python

   from setuptools import setup

   [...]

   setup(name="my_package_name",
         python_requires='>3.6',
   [...]
   )

This helps the package manager ``pip`` to know which versions of your library
support which versions of Python. You can also impose an upper limit if you're
sure you don't support certain versions of Python. For example, if you only
support Python 3.6 through 3.9: ``python_requires='>=3.6, <3.10'``.
