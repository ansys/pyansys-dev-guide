PEP 8
=====

This section summarizes important coding style guidelines from `PEP 8`_
and how they apply to PyAnsys libraries. The Python community devised PEP 8 
to increase the readability of Python code. Some of the most popular
packages within the Python ecosystem have adopted PEP 8,
including `NumPy`_, `SciPy`_, and `pandas`_.

Imports
-------

Code style guidelines follow for ``import`` statements.

Import location
~~~~~~~~~~~~~~~

Imports should always be placed at the top of the file, just after any
module comments and docstrings and before module global variables and
constants. This reduces the likelihood of an `ImportError`_ that
might only be discovered during runtime.

.. tab-set::

   .. tab-item:: Use

      .. code-block:: python

         import math


         def compute_logbase8(x):
             return math.log(8, x)

   .. tab-item:: Avoid

      .. code-block:: python

         def compute_logbase8(x):
             import math

             return math.log(8, x)

Import order
~~~~~~~~~~~~

For better readability, group imports in this order:

#. Standard library imports
#. Related third-party imports
#. Local app-specific or library-specific imports

All imports within each import grouping should be performed in alphabetical order
so that they are easily searchable.

.. tab-set::

   .. tab-item:: Use

      .. code-block:: python

         import math
         import subprocess
         import sys

         from mypackage import mymodule


         def compute_logbase8(x):
             return math.log(8, x)

   .. tab-item:: Avoid

      .. code-block:: python

         import sys
         import subprocess
         from mypackage import mymodule
         import math


         def compute_logbase8(x):
             return math.log(8, x)

Multiple imports
~~~~~~~~~~~~~~~~

You should place imports on separate lines unless they are modules from the same
package.

.. tab-set::

    .. tab-item:: Use
    
        .. code-block:: python
        
           import math
           import sys

           from my_package import my_module, my_other_module
        

           def compute_logbase8(x):
               return math.log(8, x)

    .. tab-item:: Avoid

        .. code-block:: python
        
           import math, sys

           from my_package import my_module
           from my_package import my_other_module
        

           def compute_logbase8(x):
               return math.log(8, x)
    

Absolute versus relative imports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You should use absolute imports over relative imports because they are 
more readable and reliable.

.. tab-set::

    .. tab-item:: Use
    
        .. code-block:: python

           from ansys.mapdl.core.plotting import general_plotter

    .. tab-item:: Avoid

        .. code-block:: python

           from .core.plotting import general_plotter


Import namespaces
~~~~~~~~~~~~~~~~~

You should avoid using wildcards in imports because doing so can make it
difficult to detect undefined names. For more information, see `using wildcard imports (from … import *)
<https://docs.quantifiedcode.com/python-anti-patterns/maintainability/from_module_import_all_used.html>`_.
in the *Python Anti-Patterns* documentation.

.. tab-set::

    .. tab-item:: Use
    
        .. code-block:: python
        
            from my_package.my_module import myclass

    .. tab-item:: Avoid
    
        .. code-block:: python
        
            from my_package.my_module import *

Naming conventions
------------------

To achieve readable and maintainable code, use concise and descriptive names for functions,
classes, methods, and constants. Regardless of the programming language, you must follow these
global rules to determine the correct names:

- Choose descriptive and unambiguous names.
- Make meaningful distinctions.
- Use pronounceable names.
- Use searchable names.
- Replace magic numbers with named constants.
- Avoid encodings. Do not append prefixes or type information.

Variables
~~~~~~~~~

Do not use the characters ``"l"``, ``"O"``, or ``"I"`` as single-character
variable names. In some fonts, these characters are indistinguishable from the
numerals one and zero.

Packages and modules
~~~~~~~~~~~~~~~~~~~~

Use a short, lowercase word or words for module names. Separate words
with underscores to improve readability. For example, use ``module.py``
or ``my_module.py``.

For a package name, use a short, lowercase word or words. Avoid
underscores as these must be represented as dashes when installing
from PyPI.

.. code::

   python -m pip install package

Classes
~~~~~~~

Use `camel case <https://en.wikipedia.org/wiki/Camel_case>`_ when naming
classes. Do not separate words with underscores. 

.. code:: python

   class MyClass:
       """Docstring for MyClass"""

       ...

Functions and methods
~~~~~~~~~~~~~~~~~~~~~

Use a lowercase word or words when naming Python functions or methods. To
improve readability, separate words with underscores.

When naming methods, follow these conventions:

- Enclose only `dunder methods`_ with double underscores.
- Start a method that is to be private with double underscores.
- Start a method that is to be protected with a single underscore.

.. code:: python

   class MyClass:
       """Docstring for MyClass."""

       def __init__(self, value):
           """Constructor.

           Methods with double underscores on either side are called
           "dunder" methods and are special Python methods.

           """
           self._value = value

       def __private_method(self):
           """This method can only be called from ``MyClass``."""
           self._value = 0

       def _protected_method(self):
           """This method should only be called from ``MyClass``.

           Protected methods can be called from inherited classes,
           For private methods, which names are 'mangled' to prevent
           these methods from being called from inherited classes.

           """
           # note how private methods can be called here
           self.__private_method()

       def public_method(self):
           """This method can be called external to this class."""
           self._value += 2


.. note:: 

   Remember that these are only conventions for naming functions and methods. In Python,
   there are no private or protected members, meaning that you can always access even
   those members that start with underscores.

Variables
~~~~~~~~~

Use a lowercase single letter, word, or words when naming variables. To improve
readability, separate words with underscores.

.. code:: python

    my_variable = 5

Constants are variables that are set at the module level and are used by one or
more methods within that module. Use an uppercase word or words for constants.
To improve readability, separate words with underscores.

.. code:: python

    PI = 3.141592653589793
    CONSTANT = 4
    MY_CONSTANT = 8
    MY_OTHER_CONSTANT = 1000

Indentation and line breaks
---------------------------

Proper and consistent indentation is important to producing
easy-to-read and maintainable code. In Python, use four spaces per
indentation level and avoid tabs. 

Indentation should be used to emphasize:

- Body of a control statement, such as a loop or a select statement
- Body of a conditional statement
- New scope blocks

.. code:: python

   class MyFirstClass:
       """MyFirstClass docstring."""


   class MySecondClass:
       """MySecondClass docstring."""


   def top_level_function():
       """Top-level function docstring."""
       return

To improve readability, add blank lines and wrap lines. You
should add two blank lines before and after all function and class
definitions.

Inside a class, add a single blank line before any method definition.

.. code-block:: python

   class MyClass:
       """MyClass docstring."""

       def first_method(self):
           """First method docstring."""
           return

       def second_method(self):
           """Second method docstring."""
           return

To make it clear when a "paragraph" of code is complete and a new section
is starting, use a blank line to separate logical sections.

.. tab-set::

    .. tab-item:: Use
    
        .. code-block:: python

           if x < y:
               ...
           else:
               if x > y:
                   ...
               else:
                   ...

           if x > 0 and x < 10:
               print("x is a positive single digit.")
           elif x < 0:
               print("x is less than zero.")

    .. tab-item:: Avoid
    
        .. code-block:: python

           if x < y:
               ...

           else:
               if x > y:
                   ...

               else:
                   ...

           if x > 0 and x < 10:
               print("x is a positive single digit.")
    

Maximum line length
-------------------

For source code, best practice is to keep the line length at or below
100 characters. For docstrings and comments, best practice is to keep
the length at or below 72 characters.

Lines longer than these recommended limits might not display properly
on some terminals, and tools or might be difficult to follow. For example,
this line is difficult to follow:

.. tab-set::

    .. tab-item:: Use

        .. code-block:: python

            employee_hours = [
                schedule.earliest_hour
                for employee in self.public_employees
                for schedule in employee.schedules
            ]

    .. tab-item:: Avoid

        .. code-block:: python

            # fmt: off

            employee_hours = [schedule.earliest_hour for employee in self.public_employees for schedule in employee.schedules]

            # fmt: on

Alternatively, instead of writing a list comprehension, you can use a
classic loop.

Notice that sometimes it is not be possible to keep the line length below the
desired value without breaking the syntax rules.

Comments
--------

Because a PyAnsys library generally involves multiple physics domains,
people reading its source code do not have the same background as
the developers who wrote it. This is why it is important for a library
to have well commented and documented source code. Comments that
contradict the code are worse than no comments. Always make a priority
of keeping comments up to date with the code.

Comments should be complete sentences. The first word should be
capitalized, unless it is an identifier that begins with a lowercase
letter.

Here are general guidelines for writing comments:

- Always try to explain yourself in code by making it
  self-documenting with clear variable names.
- Don't be redundant.
- Don't add obvious noise.
- Don't use closing brace comments.
- Don't comment out code that is unused. Remove it.
- Use explanations of intent.
- Clarify the code.
- Warn of consequences.

Obvious portions of the source code should not be commented. 
For example, the following comment is not needed:

.. code:: python

   # increment the counter
   i += 1

However, if code behavior is not apparent, it should be documented.
Otherwise, future developers might remove code that they see as unnecessary.

.. code:: python

   # Be sure to reset the object's cache prior to exporting. Otherwise,
   # some portions of the database in memory will not be written.
   obj.update_cache()
   obj.write(filename)

Inline comments
~~~~~~~~~~~~~~~

Use inline comments sparingly. An inline comment is a comment on the
same line as a statement.

Inline comments should be separated by two spaces from the statement: 

.. code:: python

    x = 5  # This is an inline comment

Inline comments that state the obvious are distracting and should be
avoided:

.. code:: python

    x = x + 1  # Increment x


Focus on writing self-documenting code and using short but
descriptive variable names.  

.. tab-set::

    .. tab-item:: Use
    
        .. code:: python
        
            user_name = "John Smith"

    .. tab-item:: Avoid

        .. code:: python
        
           x = "John Smith"  # Student Name

Docstrings
~~~~~~~~~~

A docstring is a string literal that occurs as the first statement in
a module, function, class, or method definition. A docstring becomes
the doc special attribute of the object.

Write docstrings for all public modules, functions, classes, and
methods. Docstrings are not necessary for private methods, but such
methods should have comments that describe what they do.

To create a docstring, surround the comments with three double quotation marks
on either side.

For a one-line docstring, keep both the starting and ending ``"""`` on the
same line: 

.. code:: python

    """This is a docstring."""

For a multi-line docstring, put the ending ``"""`` on a line by itself.

For more information on docstrings for PyAnsys libraries, see
:ref:`Documentation style`.

Programming recommendations
---------------------------

The following sections provide some `PEP 8
<https://www.python.org/dev/peps/pep-0008/>`_ recommendations for removing
ambiguity and preserving consistency. Additionally, they address some common
pitfalls that occur when writing Python code.

Booleans and comparisons
~~~~~~~~~~~~~~~~~~~~~~~~

Don't compare Boolean values to ``True`` or ``False`` using the
equivalence operator.

.. tab-set::

    .. tab-item:: Use

        .. code-block:: python
        
           if my_bool:
               return result

    .. tab-item:: Avoid

        .. code-block:: python
        
           if my_bool == True:
               return result

Because empty sequences are evaluated to ``False``, don't compare the
length of these objects but rather consider how they would evaluate
by using ``bool(<object>)``.

.. tab-set::

    .. tab-item:: Use
    
        .. code-block:: python
        
            my_list = []
            if not my_list:
                raise ValueError("List is empty")

    .. tab-item:: Avoid
    
        .. code-block:: python
    
            my_list = []
            if not len(my_list):
                raise ValueError("List is empty")


In ``if`` statements, use ``is not`` rather than ``not ...``. 

.. tab-set::

    .. tab-item:: Use
    
        .. code-block:: python
        
            if x is not None:
                return "x exists!"

    .. tab-item:: Avoid

        .. code-block:: python
        
            if not x is None:
                return x


Also, avoid ``if x:`` when you mean ``if x is not None:``.  This is
especially important when parsing arguments.

Handling strings
~~~~~~~~~~~~~~~~

Use the ``.startswith()`` and ``.endswith()`` functions instead of slicing.

.. tab-set:: 

    .. tab-item:: Use
    
        .. code-block:: python
        
           if word.startswith("cat"):
               print("The word starts with 'cat'.")
        
           if file_name.endswith(".jpg"):
               print("The file is a JPEG.")

    .. tab-item:: Avoid

        .. code-block:: python
        
           if word[:3] == "cat":
               print("The word starts with 'cat'.")
        
           if file_name[-4:] == ".jpg":
               print("The file is a JPEG.")

Reading the Windows registry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Never read the Windows registry or write to it because this is dangerous and 
makes it difficult to deploy libraries on different environments or operating
systems.

.. tab-set::

    .. tab-item:: Avoid

        .. code-block:: python

            self.sDesktopinstallDirectory = Registry.GetValue(
                "HKEY_LOCAL_MACHINE\Software\Ansoft\ElectronicsDesktop\{}\Desktop".format(
                    self.sDesktopVersion
                ),
                "InstallationDirectory",
                "",
            )

Duplicated code
~~~~~~~~~~~~~~~

Follow the DRY principle, which states that "Every piece of knowledge
must have a single, unambiguous, authoritative representation within a
system."  Follow this principle unless it overly complicates
the code. The following "Avoid" example converts Fahrenheit to Kelvin
twice, which now requires the developer to maintain two separate lines
that do the same thing.

.. tab-set::

    .. tab-item:: Use
    
        .. code-block:: python
        
            def fahr_to_kelvin(fahr):
                """Convert temperature in Fahrenheit to Kelvin.

                Parameters
                ----------
                fahr : int or float
                    Temperature in Fahrenheit.

                Returns
                -------
                kelvin : float
                   Temperature in Kelvin.

                """
                return ((fahr - 32) * (5 / 9)) + 273.15


            new_temp = fahr_to_kelvin(55)
            new_temp_k = fahr_to_kelvin(46)

    .. tab-item:: Avoid
    
        .. code-block:: python
        
            temp = 55
            new_temp = ((temp - 32) * (5 / 9)) + 273.15

            temp2 = 46
            new_temp_k = ((temp2 - 32) * (5 / 9)) + 273.15

This is a trivial example, but you can apply this approach for a
variety of both simple and complex algorithms and workflows. Another
advantage of this approach is that you can implement unit testing
for this method.

.. code:: python

   import numpy as np


   def test_fahr_to_kelvin():
       np.testing.assert_allclose(12.7778, fahr_to_kelvin(55))

Now, you have only one line of code to verify. You can also use
a testing framework such as `pytest`_ to test that the method is
correct.

Nested blocks
~~~~~~~~~~~~~

Avoid deeply nested block structures (such as conditional blocks and loops)
within one single code block. 

.. code:: python

   def validate_something(self, a, b, c):
       if a > b:
           if a * 2 > b:
               if a * 3 < b:
                   raise ValueError
           else:
               for i in range(10):
                   c += self.validate_something_else(a, b, c)
                   if c > b:
                       raise ValueError
                   else:
                       d = self.foo(b, c)
                       # recursive
                       e = self.validate_something(a, b, d)

Aside from the lack of comments, this complex method
is difficult to debug and validate with unit testing. It would
be far better to implement more validation methods and join conditional
blocks.

For a conditional block, the maximum depth recommended is four. If you
think you need more for the algorithm, create small functions that are
reusable and unit-testable.

Loops
~~~~~

While there is nothing inherently wrong with nested loops, to avoid
certain pitfalls, steer clear of having loops with more than two levels. In
some cases, you can rely on coding mechanisms like list comprehensions 
to circumvent nested loops. 

.. tab-set::

   .. tab-item:: Use

        .. code-block:: python

            squares = [i * i for i in range(10)]


        .. code-block:: pycon

            >>> print(f"{squares = }")
            squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

   .. tab-item:: Avoid

        .. code-block:: python
        
            squares = []
            for i in range(10):
                squares.append(i * i)

        .. code-block:: pycon

            >>> print(f"{squares = }")
            squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

If the loop is too complicated for creating a list comprehension,
consider creating small functions and calling these instead. Assume
that you want to extract all consonants in a sentence.

.. tab-set::

    .. tab-item:: Use
    
        .. code-block:: python
    
            def is_consonant(letter):
                """Return ``True`` when a letter is a consonant."""
                vowels = "aeiou"
                return letter.isalpha() and letter.lower() not in vowels
        
        .. code-block:: pycon
            
            >>> sentence = "This is a sample sentence."
            >>> consonants = [letter for letter in sentence if is_consonant(letter)]
            >>> print(f"{consonants = }")

            consonants = ['T', 'h', 's', 's', 's', 'm', 'p', 'l', 's', 'n', 't', 'n', 'c']

    .. tab-item:: Avoid
    
        .. code-block:: python
        
            sentence = "This is a sample sentence."
            vowels = "aeiou"
            consonants = []
            for letter in sentence:
                if letter.isalpha() and letter.lower() not in vowels:
                    consonants.append(letter)
        
        .. code-block:: pycon 
        
            >>> print(f"{consonants = }")

            consonants = ['T', 'h', 's', 's', 's', 'm', 'p', 'l', 's', 'n', 't', 'n', 'c']

The "Use" approach is more readable and better documented. Additionally,
you could implement a unit test for ``is_consonant``.

Security considerations
-----------------------

Security, an ongoing process involving people and practices, ensures app confidentiality, integrity, and availability [#]_.
Any library should be secure and implement good practices that avoid or mitigate possible security risks.
This is especially relevant in libraries that request user input (such as web services).
Because security is a broad topic, you should review this useful Python-specific resource:

* `10 Unknown Security Pitfalls for Python <https://blog.sonarsource.com/10-unknown-security-pitfalls-for-python>`_ - By Dennis Brinkrolf - Sonar source blog

.. [#] Wikipedia - `Software development security <https://en.wikipedia.org/wiki/Software_development_security>`_. 
