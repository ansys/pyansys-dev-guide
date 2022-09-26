"""
This is example-script
======================

This example doesn't do much, it is addition of elements in a list

- # This is commented python


- # This is a section header
  # ------------------------

In the built documentation, it will be rendered as rST. All rST lines
must begin with '# ' (note the space) including underlines below section
headers.

These lines won't be rendered as rST because there is a gap after the last
commented rST block. Instead, they'll resolve as regular Python comments.
"""
###############################################################################
# 1. Creating a List
# ~~~~~~~~~~~~~~~~~~

print("1. Creating a List") 
List = [] 
print("Intial blank List: ") 
print(List) 

###############################################################################
# 2. Addition of Elements in the List 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("Addition of Elements in the List")
List.append(1) 
List.append(2) 
List.append(4) 
print("Printing the List after Addition of Three elements: ") 
print(List) 

###############################################################################
# 3. Adding elements to the List using Iterator 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("3. Adding elements to the List using Iterator")
for i in range(1, 4): 
	List.append(i) 
print("List after Addition of elements from 1-3: ") 
print(List) 

###############################################################################
# Addition of List to a List
# ~~~~~~~~~~~~~~~~~~~~~~~~~~

print("4. Addition of List to a List") 
List2 = ['Stars', 'Moon'] 
List.append(List2) 
print("List after Addition of a List: ") 
print(List) 

###############################################################################
# Addition of Element at specific Position (using Insert Method)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("5. Addition of Element at specific Position (using Insert Method)") 
List.insert(3, 12) 
List2.insert(0, 'Terminator') 
print("List after performing Insert Operation: ") 
print(List) 

###############################################################################
# Addition of multiple elements to the List at the end (using Extend Method)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("6. Addition of multiple elements to the List at the end (using Extend Method)") 
List.extend([8, 'Diode', 'Transistor']) 
print("List after performing Extend Operation: ") 
print(List)

###############################################################################
# Adding Tuples to the List
# ~~~~~~~~~~~~~~~~~~~~~~~~~
print("7. Adding Tuples to the List") 
List.append((5, 6)) 
print("List after Addition of a Tuple: ") 
print(List)


###############################################################################
# Plotting sin function
# ~~~~~~~~~~~~~~~~~~~~~

import numpy as np
import matplotlib.pyplot as plt
# You can use modules local to the example being run, here we import

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel(r'$x$')
plt.ylabel(r'$\sin(x)$')
plt.show()