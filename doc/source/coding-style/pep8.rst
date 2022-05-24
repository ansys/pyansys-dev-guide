PEP 8
=====

This section summarizes the key points from `PEP 8`_ and how they apply to PyAnsys
libraries. `PEP 8`_ style guideline were devised by the Python community
to increase the readability of Python code. `PEP 8`_ has been adopted by some of
the most popular libraries within the Python ecosystem, including: `NumPy`_,
`SciPy`_, and `pandas`_.

.. _PEP 8: https://www.python.org/dev/peps/pep-0008/
.. _NumPy: https://numpy.org/
.. _SciPy: https://www.scipy.org/
.. _pandas: https://pandas.pydata.org/


Imports
-------
Code style guidelines follow for ``import`` statements.

Import Location
~~~~~~~~~~~~~~~
Imports should always be placed at the top of the file, just after any
module comments and docstrings and before module globals and
constants.  This reduces the likelihood of an `ImportError`_ that
might only be discovered during runtime.

.. _ImportError: https://docs.python.org/3/library/exceptions.html#ImportError

.. tabs::

   .. tab:: Avoid

      .. code-block:: python

         def compute_logbase8(x):
             import math

             return math.log(8, x)

   .. tab:: Use

      .. code-block:: python

         import math


         def compute_logbase8(x):
             return math.log(8, x)


Imports Order
~~~~~~~~~~~~~
For better readability, group imports in this order:

#. Standard library imports
#. Related third-party imports
#. Local application-specific or library-specific imports

All imports within each import grouping should be performed in alphabetical order.

.. tabs::

   .. tab:: Avoid

      .. code-block:: python

         import sys
         import subprocess
         from mypackage import mymodule
         import math


         def compute_logbase8(x):
             return math.log(8, x)


   .. tab:: Use

      .. code-block:: python

         import math
         import subprocess
         import sys

         from mypackage import mymodule


         def compute_logbase8(x):
             return math.log(8, x)


Multiple Imports
~~~~~~~~~~~~~~~~
You should place imports in separate lines unless they are modules from the same
package.

.. tabs::

    .. tab:: Avoid

        .. code-block:: python
        
           import math, sys

           from my_package import my_module
           from my_package import my_other_module
        

           def compute_logbase8(x):
               return math.log(8, x)
    
    .. tab:: Use
    
        .. code-block:: python
        
           import math
           import sys

           from my_package import my_module, my_other_module
        

           def compute_logbase8(x):
               return math.log(8, x)


Import Namespaces
~~~~~~~~~~~~~~~~~
You should avoid using wildcards in imports because doing so can make it
difficult to detect undefined names.  For more information, see `Python
Anti-Patterns: using wildcard imports
<(https://docs.quantifiedcode.com/python-anti-patterns/maintainability/from_module_import_all_used.html>`_.

.. tabs::

    .. tab:: Avoid
    
        .. code-block:: python
        
            from my_package.my_module import *
    
    .. tab:: Use
    
        .. code-block:: python
        
            from my_package.my_module import myclass


Naming Conventions
------------------
To achieve readable and maintainable code, use concise and descriptive names for classes,
methods, functions, and constants. Regardless of the programming language, you must follow these
global rules to determine the correct names:

#. Choose descriptive and unambiguous names.
#. Make meaningful distinctions.
#. Use pronounceable names.
#. Use searchable names.
#. Replace magic numbers with named constants.
#. Avoid encodings. Do not append prefixes or type information.


Variables
~~~~~~~~~
Do not use the characters ``'l'``, ``'O'`` , or ``'I'`` as single-character
variable names. In some fonts, these characters are indistinguishable from the
numerals one and zero.


Packages and Modules
~~~~~~~~~~~~~~~~~~~~
Use a short, lowercase word or words for module names. Separate words
with underscores to improve readability. For example, use ``module.py``
or ``my_module.py``.

For a package name, use a short, lowercase word or words. Avoid
underscores as these must be represented as dashes when installing
from PyPi.

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


Use a lowercase word or words for Python functions or methods. Separate words
with underscores to improve readability. When naming class methods, the
following conventions apply:

- Enclose only `dunder methods`_ with double underscores.
- Start a method that is to be considered private with double underscores.
- Start a method that is to be considered protected with a single underscore.

.. _dunder methods: https://docs.python.org/3/reference/datamodel.html#special-method-names

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
           unlike private methods, which names are 'mangled' to avoid
           these methods from being called from inherited classes.

           """
           # note how we can call private methods here
           self.__private_method()

       def public_method(self):
           """This method can be called external to this class."""
           self._value += 2


.. note:: 

   Remember that these are only conventions for naming functions and methods. In Python
   there are no private or protected members, meaning that you can always access even
   those members that start with underscores.

Variables
~~~~~~~~~
Use a lowercase single letter, word, or words when naming variables. Separate
words with underscores to improve readability.

.. code:: python

    my_variable = 5

Constants are variables that are set at the module level and are used by one or
more methods within that module. Use an uppercase word or words for constants.
Separate words with underscores to improve readability.

.. code:: python

    PI = 3.141592653589793
    CONSTANT = 4
    MY_CONSTANT = 8
    MY_OTHER_CONSTANT = 1000

Indentation and Line Breaks
---------------------------
Proper and consistent indentation is important to producing
easy-to-read and maintainable code. In Python, use four spaces per
indentation level and avoid tabs. 

Indentation should be used to emphasize:

 - Body of a control statement, such as a loop or a select statement
 - Body of a conditional statement
 - New scope block

.. code:: python

   class MyFirstClass:
       """MyFirstClass docstring."""


   class MySecondClass:
       """MySecondClass docstring."""


   def top_level_function():
       """Top level function docstring."""
       return

For improved readability, add blank lines or wrapping lines. Two
blank lines should be added before and after all class and function
definitions.

Inside a class, use a single line before any method definition.

.. code-block:: python

   class MyClass:
       """MyClass docstring."""

       def first_method(self):
           """First method docstring."""
           return

       def second_method(self):
           """Second method docstring."""
           return

To make it clear when a 'paragraph' of code is complete and a new section
is starting, use a blank line to separate logical sections.

Instead of:

.. tabs::

    .. tab:: Avoid
    
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
    
    .. tab:: Use
    
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


Maximum Line Length
-------------------
For source code lines, best practice is to keep the length at or below
100 characters. For docstrings and comments, best practice is to keep
the length at or below 72 characters.

Lines longer than these recommended limits might not display properly
on some terminals and tools or might be difficult to follow. For example,
this line is difficult to follow:


.. tabs::

    .. tab:: Avoid

        .. code:: python

            employee_hours = [schedule.earliest_hour for employee in self.public_employees for schedule in employee.schedules]

    .. tab:: Use

        .. code-block:: python
        
            employee_hours = [
                schedule.earliest_hour
                for employee in self.public_employees
                for schedule in employee.schedules
            ]

Alternatively, instead of writing a list comprehension, you can use a
classic loop.

Notice that sometimes it will not be possible to keep the line length below the
desired value without breaking the syntax rules.

Comments
--------
Because a PyAnsys library generally involves multiple physics domains,
users reading its source code do not have the same background as
the developers who wrote it. This is why it is important for a library
to have well commented and documented source code. Comments that
contradict the code are worse than no comments. Always make a priority
of keeping comments up to date with the code.

Comments should be complete sentences. The first word should be
capitalized, unless it is an identifier that begins with a lowercase
letter.

Here are general guidelines for writing comments:

#. Always try to explain yourself in code by making it
   self-documenting with clear variable names.
#. Don't be redundant.
#. Don't add obvious noise.
#. Don't use closing brace comments.
#. Don't comment out code that is unused. Remove it.
#. Use explanations of intent.
#. Clarify the code.
#. Warn of consequences.

Obvious portions of the source code should not be commented. 
For example, the following comment is not needed:

.. code:: python

   # increment the counter
   i += 1

However, an important portion of the behavior that is not self-apparent
should include a note from the developer writing it. Otherwise,
future developers may remove what they see as unnecessary. 

.. code:: python

   # Be sure to reset the object's cache prior to exporting. Otherwise,
   # some portions of the database in memory will not be written.
   obj.update_cache()
   obj.write(filename)


Inline Comments
~~~~~~~~~~~~~~~
Use inline comments sparingly. An inline comment is a comment on the
same line as a statement.

Inline comments should be separated by two spaces from the statement. 

.. code:: python

    x = 5  # This is an inline comment

Inline comments that state the obvious are distracting and should be
avoided:

.. code:: python

    x = x + 1  # Increment x


Focus on writing self-documenting code and using short but
descriptive variable names.  

.. tabs::

    .. tab:: Avoid

        .. code:: python
        
           x = "John Smith"  # Student Name

    .. tab:: Use
    
        .. code:: python
        
            user_name = "John Smith"


Docstring Conventions
~~~~~~~~~~~~~~~~~~~~~
A docstring is a string literal that occurs as the first statement in
a module, function, class, or method definition. A docstring becomes
the doc special attribute of the object.

Write docstrings for all public modules, functions, classes, and
methods. Docstrings are not necessary for private methods, but such
methods should have comments that describe what they do.

To create a docstring, surround the comments with three double quotes
on either side.

For a one-line docstring, keep both the starting and ending ``"""`` on the
same line: 

.. code:: python

    """This is a docstring."""

For a multi-line docstring, put the ending ``"""`` on a line by itself.

For more information on docstrings for PyAnsys libraries, see
:ref:`Documentation Style`.


Programming Recommendations
---------------------------
The following sections provide some `PEP8
<https://www.python.org/dev/peps/pep-0008/>`_ suggestions for removing
ambiguity and preserving consistency. They also address some common pitfalls 
when writing Python code.


Booleans and Comparisons
~~~~~~~~~~~~~~~~~~~~~~~~
Don't compare Boolean values to ``True`` or ``False`` using the
equivalence operator.

.. tabs::

    .. tab:: Avoid

        .. code-block:: python
        
           if my_bool == True:
               return result

    .. tab:: Use

        .. code-block:: python
        
           if my_bool:
               return result

Knowing that empty sequences are evaluated to ``False``, don't compare the
length of these objects but rather consider how they would evaluate
by using ``bool(<object>)``.

.. tabs::

    .. tab:: Avoid
    
        .. code-block:: python
    
            my_list = []
            if not len(my_list):
                raise ValueError('List is empty')

    .. tab:: Use
    
        .. code-block:: python
        
            my_list = []
            if not my_list:
               raise ValueError('List is empty')


In ``if`` statements, use ``is not`` rather than ``not ...``. 

.. tabs::

    .. tab:: Avoid

        .. code-block:: python
        
            if not x is None:
                return x

    .. tab:: Use
    
        .. code-block:: python
        
            if x is not None:
                return 'x exists!'


Also, avoid ``if x:`` when you mean ``if x is not None:``.  This is
especially important when parsing arguments.


Handling Strings
~~~~~~~~~~~~~~~~
Use ``.startswith()`` and ``.endswith()`` instead of slicing.


.. tabs:: 

    .. tab:: Avoid

        .. code-block:: python
        
           if word[:3] == "cat":
               print("The word starts with 'cat'.")
        
           if file_name[-4:] == ".jpg":
               print("The file is a JPEG.")

    .. tab:: Use
    
        .. code-block:: python
        
           if word.startswith("cat"):
               print("The word starts with 'cat'.")
        
           if file_name.endswith(".jpg"):
               print("The file is a JPEG.")


Reading the Windows Registry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Never read the Windows registry or write to it because this is dangerous and 
makes it difficult to deploy libraries on different environments or operating
systems.

.. tabs::

    .. tab:: Avoid

        .. code-block:: python

            self.sDesktopinstallDirectory = Registry.GetValue(
                "HKEY_LOCAL_MACHINE\Software\Ansoft\ElectronicsDesktop\{}\Desktop".format(
                    self.sDesktopVersion
                ),
                "InstallationDirectory",
                "",
            )


Duplicated Code
~~~~~~~~~~~~~~~
Follow the DRY principle, which states that "Every piece of knowledge
must have a single, unambiguous, authoritative representation within a
system."  Follow this principle unless it overly complicates
the code. For instance, the following example converts Fahrenheit to Kelvin
twice, which now requires the developer to maintain two separate lines
that do the same thing.


.. tabs::

    .. tab:: Avoid
    
        .. code-block:: python
        
            temp = 55
            new_temp = ((temp - 32) * (5 / 9)) + 273.15

            temp2 = 46
            new_temp_k = ((temp2 - 32) * (5 / 9)) + 273.15

   
    .. tab:: Use
    
        .. code-block:: python
        
            def fahr_to_kelvin(fahr)
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


This is a trivial example, but the approach can be applied for a
variety of both simple and complex algorithms and workflows. Another
advantage of this approach is that you can implement unit testing
for this method.

.. code:: python

   import numpy as np


   def test_fahr_to_kelvin():
       np.testing.assert_allclose(12.7778, fahr_to_kelvin(55))

Now, you have only one line of code to verify and can also use
a testing framework such as ``pytest`` to test that the method is
correct.


Nested Blocks
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

.. tabs::

    .. tab:: Avoid

        .. code-block:: python
        
            squares = []
            for i in range(10):
               squares.append(i * i)

        .. code-block:: pycon

            >>> print(f"{squares = }")
            squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


    .. tab:: Use

        .. code-block:: python

            squares = [i * i for i in range(10)]


        .. code-block:: pycon

            >>> print(f"{squares = }")
            squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


If the loop is too complicated for creating a list comprehension,
consider creating small functions and calling these instead. For
example to extract all consonants in a sentence:

.. tabs::

    .. tab:: Avoid
    
        .. code-block:: python
        
            sentence = 'This is a sample sentence.'
            vowels = 'aeiou'
            consonants = []
            for letter in sentence:
                if letter.isalpha() and letter.lower() not in vowels:
                    consonants.append(letter)
        
        .. code-block:: pycon 
        
            >>> print(f"{consonants = }")
            consonants = ['T', 'h', 's', 's', 's', 'm', 'p', 'l', 's', 'n', 't', 'n', 'c']
    
    
    .. tab:: Use
    
        .. code-block:: python
    
            def is_consonant(letter):
                """Return ``True`` when a letter is a consonant."""
                vowels = 'aeiou'
                return letter.isalpha() and letter.lower() not in vowels
       
        .. code-block:: pycon
    
            >>> sentence = "This is a sample sentence."
            >>> consonants = [letter for letter in sentence if is_consonant(letter)]
            >>> print(f"{consonants = }")
            consonants = ['T', 'h', 's', 's', 's', 'm', 'p', 'l', 's', 'n', 't', 'n', 'c']

The second approach is more readable and better documented. Additionally,
you could implement a unit test for ``is_consonant``.


Security Considerations
-----------------------

Security, an ongoing process involving people and practices, ensures application confidentiality, integrity, and availability [#]_.
Any library should be secure and implement good practices that avoid or mitigate possible security risks.
This is especially relevant in libraries that request user input (such as web services).
Because security is a broad topic, we recommend you review this useful Python-specific resource:

* `10 Unknown Security Pitfalls for Python <https://blog.sonarsource.com/10-unknown-security-pitfalls-for-python>`_ - By Dennis Brinkrolf - Sonar source blog

.. [#] Wikipedia - `Software development security <https://en.wikipedia.org/wiki/Software_development_security>`_. 
