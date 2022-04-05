.. _python pkg lib diag:
.. graphviz::
    :caption: A Python library is a collection of packages.
    :alt: A Python library is a collection of packages.
    :align: center

     digraph "sphinx-ext-graphviz" {
         size="6,4";
         rankdir="LR";
         graph [
           fontname="Verdana", fontsize="10", color="black", fillcolor="white"
         ];
         node [
           fontname="Verdana", fontsize="10", style="filled", color="black", fillcolor="#ffc107"
         ];

         python_library [
           label="Python Library", shape="folder"
         ];

         pkg_A [
           label="Package A", shape="folder"
         ];

         pkg_B [
           label="Package B", shape="folder"
         ];

         pkg_other [
           label="...", shape="folder"
         ];

         python_library -> pkg_A
         python_library -> pkg_B
         python_library -> pkg_other

         sub_package [
           label="Sub-package A", shape="folder"
         ];

         init_file1 [
           label="__init__.py", shape="file"
         ];

         init_file2 [
           label="__init__.py", shape="file"
         ];

         module_foo [
           label="module_foo.py", shape="file"
         ];

         module_bar [
           label="module_bar.py", shape="file"
         ];

         pkg_A -> sub_package;
         pkg_A -> init_file1;
         pkg_A -> module_foo;

         sub_package -> init_file2;
         sub_package -> module_bar;

     }


