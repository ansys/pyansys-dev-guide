.. _tables:

Tables
======

You can create four different types of tables in RST files:

- Grid tables: Create by drawing them.
- Simple tables: Create with the ``table`` directive.
- CSV tables: Create with the ``csv_table`` directive.
- List table: Create with the ``list-table`` directive.

The data in a table is always left-aligned. For all table types, you can
use reStructuredText syntax to format content and add links within the
table cells.

All tables created with directives support a title and optional attributes.
For more information, see `Tables <RST_table_directives_>`_ in
the section on reStructuredText directives in the `Docutils <Docutils_>`_
documentation.

Create a grid table
-------------------

You create a grid table by using plus (``+``), hyphen (``-``), and pipe or
vertical bar (``|``) characters to "draw" the table. You can also use the
equal sign (``=``) character to bold the column header text.

Here is a grid table with bold column header text::

  +-------------------+-------------------+-------------------+
  | Column A          | Column B          | Column C          |
  |                   |                   |                   |
  +===================+===================+===================+
  | Data 1            | Data 2            | Data 3            |
  +-------------------+-------------------+-------------------+
  | Data 4            | Data 5            | Data 6            |
  +-------------------+-------------------+-------------------+

Here is how this grid table is rendered in the documentation:

+-------------------+-------------------+-------------------+
| Column A          | Column B          | Column C          |
|                   |                   |                   |
+===================+===================+===================+
| Data 1            | Data 2            | Data 3            |
+-------------------+-------------------+-------------------+
| Data 4            | Data 5            | Data 6            |
+-------------------+-------------------+-------------------+

The length of the hyphen characters in each column determines the column width.
For example, assume that you want a table with a wider first column and, in the
second row, you want the data for the second column to span the third column.
You would add more hyphen characters in the corresponding header cell and, in the
second row, remove the pipe character indicating the column break between the second
and third columns::

  +---------------------------------------+-----------------+----------------+
  | Calumn A for wider first column       | Column B        | Column C       |
  +=======================================+=================+================+
  | Data 1                                | Data 2          | Data 3         |
  +---------------------------------------+-----------------+----------------+
  | Data 4                                | Data 5 with spanning text        |
  +---------------------------------------+----------------------------------+
  | Data 6                                | Data 7          | Data 8         |
  +---------------------------------------+-----------------+----------------+

Here is how this grid table is rendered in the documentation:

+---------------------------------------+-----------------+----------------+
| Column A for wider first column       | Column B        | Column C       |
+=======================================+=================+================+
| Data 1                                | Data 2          | Data 3         |
+---------------------------------------+-----------------+----------------+
| Data 4                                | Data 5 with spanning text        |
+---------------------------------------+-----------------+----------------+
| Data 6                                | Data 7          | Data 8         |
+---------------------------------------+-----------------+----------------+

Create a simple table
---------------------

You create a simple table using the ``table`` directive.

Here is a ``table`` directive for a simple table, where
column widths are automatically adjusted to fill the page based
on their content::

  .. table:: **Table title**
    :widths: auto

   +-------------+-------------+-------------+
   | Column A    | Column B    | Column C    |
   +=============+=============+=============+
   | Data 1      | Data 2      | Data 3      |
   +-------------+-------------+-------------+
   | Data 4      | Data 5      | Data 6      |
   +-------------+-------------+-------------+

Here is how this simple table is rendered in the documentation:

.. table:: **Table title**
  :widths: auto

  +-------------+-------------+-------------+
  | Column A    | Column B    | Column C    |
  +===========+=+=============+=============+
  | Data 1      | Data 2      | Data 3      |
  +-------------+-------------+-------------+
  | Data 4      | Data 5      | Data 6      |
  +-------------+-------------+-------------+

Create a CSV table
------------------

You create a CSV table using the ``csv_table`` directive. When using this
directive, you must be careful with the placement of commas (``,``).
When defining the column names and data, you must place a comma immediately
after the closing quotation marks. You must also place only one space between
each value. This directive provides no control over the merging of cells.
However, it does provide the ``widths`` attribute for specifying the width of
each column as a percentage.

Here is a ``csv_table`` directive that creates a table with three columns
and two rows, where the second and third columns are three times the width of the
first column::

  .. csv-table:: **Table title**
   :header: "Column A", "Column B", "Column C"
   :widths: 10, 30, 30

   "Data 1", "Data 2", "Data 3"
   "Data 4", "Data 5", "Data 6"

Here is how this CSV table is rendered in the documentation:

.. csv-table:: **Table title**
   :header: "Column A", "Column B", "Column C"
   :widths: 10, 30, 30

   "Data 1", "Data 2", "Data 3"
   "Data 4", "Data 5", "Data 6"

Create a list table
-------------------

You create a list table using the ``list-table`` directive. When using this directive,
you provide the table data in a *uniform* two-level bulleted list, where uniform means
that each sublist (second-level list) must contain the same number of items. This directive
uses asterisk (``*``) and hyphen (``-``) characters to define the table structure. When no
value is specified for the ``widths`` attribute, ``auto`` is the default.

This example of the ``list-table`` directive uses the ``widths`` attribute to specify
the widths of columns as percentage values::

  .. list-table:: **Table title**
   :widths: 15 35 50
   :header-rows: 1

   * - Column A
     - Column B
     - Column C
   * - Data 1
     - Data 2
     - Data 3
   * - Data 4
     - Data 5
     - Data 6

Here is how this list table is rendered in the documentation:

.. list-table:: **Table title**
   :widths: 15 35 50
   :header-rows: 1

   * - Column A
     - Column B
     - Column C
   * - Data 1
     - Data 2
     - Data 3
   * - Data 4
     - Data 5
     - Data 6
