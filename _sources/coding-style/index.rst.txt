

.. _coding_style:

Coding style
============

Coding style refers to the different rules defined in a software project that
must be followed when writing source code. These rules ensure that all
source code looks the same across different files of the project.

Because the PyAnsys ecosystem consists of many projects, coding style rules
are critical. Their use helps to achieve these goals:

- Prevent against common programming errors
- Limit product complexity
- Provide an easily readable, understandable, and maintainable product
- Establish a consistent style
- Implement an objective basis for code review

All PyAnsys libraries are expected to follow `PEP 8`_ and be consistent in style and
formatting with the libraries for the "big three" data science packages: `NumPy`_,
`SciPy`_, and `pandas`_. 

The purpose of this section is not to repeat coding style documentation
but rather to describe coding best practices applicable to the `PyAnsys`_ project when there are any
delineations, clarifications, or additional procedures above and
beyond PEP 8. For example, this section provides a topic on deprecation
best practices because there is no official guidance on deprecating features
within Python. 

.. toctree::
   :hidden:
   :maxdepth: 3

   pep8
   formatting-tools
   required-standard
   deprecation
