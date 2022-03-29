.. _python pkg lib diagram:
.. graphviz::
    :caption: Difference between Python library and package
    :alt: Difference between Python library and package
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

     }


