"""
This is an example
==================
Problem Descrption:

"""
# Python program to demonstrate Addition of elements in a List
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###############################################################################
# 1. Creating a List
# ~~~~~~~~~~~~~~~~~~

print("\n1. Creating a List") 
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

print("\n3. Adding elements to the List using Iterator")
for i in range(1, 4): 
	List.append(i) 
print("\nList after Addition of elements from 1-3: ") 
print(List) 

###############################################################################
# Addition of List to a List
# ~~~~~~~~~~~~~~~~~~~~~~~~~~

print("\n4. Addition of List to a List") 
List2 = ['Stars', 'Moon'] 
List.append(List2) 
print("\nList after Addition of a List: ") 
print(List) 

###############################################################################
# Addition of Element at specific Position (using Insert Method)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("\n5. Addition of Element at specific Position (using Insert Method)") 
List.insert(3, 12) 
List2.insert(0, 'Terminator') 
print("\nList after performing Insert Operation: ") 
print(List) 

###############################################################################
# Addition of multiple elements to the List at the end (using Extend Method)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("\n6. Addition of multiple elements to the List at the end (using Extend Method)") 
List.extend([8, 'Diode', 'Transistor']) 
print("\nList after performing Extend Operation: ") 
print(List)

###############################################################################
# Adding Tuples to the List
# ~~~~~~~~~~~~~~~~~~~~~~~~~
print("\n7. Adding Tuples to the List") 
List.append((5, 6)) 
print("\nList after Addition of a Tuple: ") 
print(List) 