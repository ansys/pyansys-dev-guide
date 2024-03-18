.. _py_file_format:

PY file formatting
==================

Python's flexibility and object-oriented nature allows developers to create
and work with a wide range of custom objects and data structures.

Hierarchical order of Python objects
------------------------------------

The next several topics describe the fundamental objects in Python,
starting with the most primitive data types and ending with more complex abstractions.
For explanations of important terms, see the `Python Glossary <Python_glossary_>`_
in the official documentation published by the Python organization.

.. _py_file_primitive_data_types:

Primitive data types
~~~~~~~~~~~~~~~~~~~~

The primitive, or built-in, data types provided by Python represent simple values
that can be used to perform various operations and transformations to solve a wide
range of problems:

- **Integer**: Represents whole numbers, both positive and negative, that are used
  for simple arithmetic operations and counting. For example, ``5``, ``-3``, ``0``,
  and ``1000``. When defining this data type, ``int`` is used.
- **Float**: Represents numbers with decimal points that are used for calculations
  involving non-integer values. For example, ``3.14``, ``-0.5``, ``2.0``, and
  ``1.0e-5`` (scientific notation). When defining this data type, ``float`` is used.
  In PyAnsys libraries, parameters that specify angle, amplitude, capacitance,
  impedance, resistance, and voltage have ``float`` as their data types.
- **String**: Represents a sequence of characters, such as text, that are used for
  text processing, manipulations, and representation. For example, ``"Hello, World!"``,
  ``"Python"``, and ``"123"``. When defining this data type, ``str`` is used.
- **Boolean**: Represents binary values that are used to make logical decisions and
  control program flow. For example, ``True`` and ``False``. When defining this type
  of data, ``bool`` is used.

.. _py_file_collections:

Collections
~~~~~~~~~~~

Collections are data structures used in Python to group multiple values into a single
container so that the data can be organized and manipulated:

- **List**: An ordered collection of items separated by commas and enclosed in square
  brackets ``[]``. Lists can contain elements of different data types, including integers,
  floats, strings, and other objects. For example, ``[1, 2, 3, "apple", "banana"]``. Lists
  are mutable, meaning you can change their content (add, remove, or modify elements).
  When defining this data type, ``list`` is used.
- **Tuple**: An ordered collection of items separated by commas and enclosed in parentheses ``()``.
  For example, ``(1, "apple", 3.14)``. Tuples can contain elements of different data types,
  similar to lists. Tuples are immutable, meaning their content cannot be changed once created.
  When defining this data type, ``tuple`` is used.
- **Dictionary**: A collection of key-value pairs enclosed in curly braces ``{}``. For example,
  ``{"name": "John", "age": 30, "city": "New York"}``. Each key is associated with a value,
  creating a mapping between keys and their corresponding values. Dictionaries are unordered,
  meaning they don't guarantee the order of elements. When defining this data type, ``dict`` is used.
- **Set**: An unordered collection of unique elements enclosed in curly braces ``{}``. For example,
  ``{1, 2, 3, 4}``. Sets are useful for eliminating duplicate values from a list and performing set
  operations like union, intersection, and difference. When defining this data type, ``set`` is used.

In summary, both lists and tuples are used for ordered sequences, dictionaries for key-value mappings,
and sets for managing unique elements.

Also, collections can be nested within one another, creating more complex data structures.

Functions
~~~~~~~~~

Functions are at the same level in the Python object hierarchy as collections. Functions
are used to operate on collections.

Custom objects
~~~~~~~~~~~~~~
Developers define custom objects to create their own data structures and behaviors.
This allows them to model real-world entities, concepts, or abstract data types in
their programs, encapsulate data and behavior into reusable units, and create instances
of these custom objects to work with.

- **Class**: A blueprint or template for creating objects (instances). A class defines
  the structure and behavior of objects of that class. Encapsulating data and behavior
  into a single unit hides implementation details and makes managing and maintaining
  code easier. A class typically includes attributes (variables) to store data and methods
  (functions) to perform actions or operations related to the class. Classes are defined
  using the ``class`` keyword, followed by the class name. A class often includes an ``__init__``
  method to initialize object attributes.
- **Instance**: An individual object created from a class. An instance represents
  a specific occurrence or realization of the class's blueprint. Instances have their own
  unique data attributes and can perform actions using the methods defined in their class.
  You can create multiple instances of the same class, each with its own state and behavior.
- **Method**: A function defined within a class that is associated with instances of that class.
  Methods encapsulate behavior related to the class and can access and manipulate the
  object's attributes. Methods can be called on instances to perform specific operations or
  computations.
- **Attribute**: A variable defined within a class that is used to store data associated with
  instances of the class. Attributes can represent characteristics or properties of objects
  created from the class. They can be accessed and modified through instances or methods.
- **Enum**: A custom object (data type) that defines a fixed set of named, constant values that
  are meaningful and need to be represented symbolically. Enums (enumerations) are created by
  subclassing the ``enum`` module in Python and defining class attributes as the enum members,
  thereby providing a structured way to work with a set of symbolic names. Enums help improve
  code readability and maintainability by providing descriptive names for values, making the
  code more self-explanatory.

Modules
~~~~~~~

Modules are the PY files containing the Python code. They can include any of the preceding
objects. Modules, which use the UTF-8 encoding standard by default, organize the code into
reusable units that can be imported into other Python scripts. For example, this line of
code imports the PyAEDT :file:`layout.py` file::

  from pyaedt.edb_core import layout

The :file:`layout.py` file contains two classes, ``EdbLayout`` and ``Shape``. The ``EdbLayout``
class manages EDB methods for primitives accessible from the ``Edb.modeler`` property. The
``Shape`` class manages EDB methods for shapes. When you import this PY file into a Python
script, you can use all methods in these classes plus any functions defined in the file.

In a PY file, you should separate methods with one blank line and separate functions with two blank
lines. Think of this as keeping the members of a class together versus separating functions,
which are isolated.

Exceptions
~~~~~~~~~~

Exceptions can be raised during program execution to handle the error scenarios that can occur
when working with any of the preceding objects. Exceptions can be caught and handled to prevent
program crashes.

Docstrings
----------

When developers create Python objects, they write docstrings, which are enclosed in triple
quotation marks (``"""``), to describe these objects and explain how to use them programmatically.

For an overview of how PyAnsys libraries use NumPy-style docstrings, see :ref:`numpy_docstrings`.
This page links to descriptions for required docstring sections and provides general
information on how to format the content in each section. For comprehensive
information on NumPy-style docstrings and sections, see the `numpydoc Style guide <numpydoc_style_guide_>`_.

Because the docstrings for Python objects are read exponentially more by users than by
the developers who draft them, docstrings should be reviewed carefully, with suggestions in
PRs suggesting how to improve and consistently format them across this and other PyAnsys libraries.
By using the same docstring conventions and consistent docstring formatting, PyAnsys users
can quickly locate and fully understand how to use PyAnsys libraries.

.. tip::
    Because Python docstrings are written in reStructuredText syntax, they can
    contain lists, notices, links, italic and bold formatting, inline code entities,
    code blocks, and more, just like RST files.

For a summary of PyAnsys-specific docstring formatting rules, see :ref:`docstring_formatting_rules`.
