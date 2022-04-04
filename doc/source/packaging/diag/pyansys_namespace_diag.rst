.. _pyansys_namespace_diag:
.. graphviz::
    :caption: Namespace convention for PyAnsys projects
    :alt: Namespace convention for PyAnsys projects
    :align: center

     digraph "sphinx-ext-graphviz" {
         size="8,6";
         rankdir="LR";
         graph [
           fontname="Verdana", fontsize="10", color="black", fillcolor="white"
         ];
         node [
           fontname="Verdana", fontsize="10", style="filled", color="black", fillcolor="#ffc107"
         ];

         pyproduct_library [
           label="pyproduct-library", shape="folder"
         ];

         src [
           label="src", shape="folder"
         ]

         ansys [
           label="ansys", shape="folder"
         ]

         product [
           label="product", shape="folder"
         ]

         library [
           label="library", shape="folder"
         ]

         init_file [
           label="__init__.py", shape="file"
         ]

         pyproduct_library -> src;
         src -> ansys;
         ansys -> product;
         product -> library;
         library -> init_file;

     }


