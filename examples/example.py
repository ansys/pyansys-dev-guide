"""
This is example-script
======================

This example is addition of elements in a list and basic plotting.
This forms the header and description section.To embed rST in the Python
examples, include a line of >= 20 # symbols, #%%, or # %%.
"""
###############################################################################
# 1. Creating a List  #This is section header
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# This line won't be rendered as rST because there's a space after the last block.
print("1. Creating a List")
# This will print the output in out code cell.
List = []
print("Initial blank List: ")
print(List)
# This is the end of the 'code block'. All code within
# this block can be easily executed all at once.

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
# Plotting figure using matplotlib
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import matplotlib.pyplot as plt

# You can use local modules to import for the example being run.

# Create Figure and Subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4), sharey=True, dpi=120)

# Plot
ax1.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 10], "go")  # greendots
ax2.plot([1, 2, 3, 4, 5], [2, 3, 4, 5, 11], "b*")  # bluestart

# Title, X and Y labels, X and Y Lim
ax1.set_title("Scatterplot Green dots")
ax2.set_title("Scatterplot Blue stars")
ax1.set_xlabel("X")
ax2.set_xlabel("X")  # x label
ax1.set_ylabel("Y")
ax2.set_ylabel("Y")  # y label
ax1.set_xlim(0, 6)
ax2.set_xlim(0, 6)  # x axis limits
ax1.set_ylim(0, 12)
ax2.set_ylim(0, 12)  # y axis limits

# ax2.yaxis.set_ticks_position('none')
plt.tight_layout()
plt.show()
