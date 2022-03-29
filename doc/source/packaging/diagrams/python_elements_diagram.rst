.. _python elements diagram:
.. graphviz::
    :caption: Differences between Python modules, sub-packages and, packages
    :alt: Differences between Python modules, sub-packages and, packages
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

         package [
           label="Package A", shape="folder"
         ];

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
           label="foo.py", shape="file"
         ];

         module_bar [
           label="bar.py", shape="file"
         ];

         package -> sub_package;
         package -> init_file1;
         package -> module_bar;

         sub_package -> init_file2;
         sub_package -> module_foo;

     }


