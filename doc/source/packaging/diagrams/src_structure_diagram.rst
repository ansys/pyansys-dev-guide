.. _src structure diagram:
.. graphviz::
    :caption: Generic structure for the src/ directory
    :alt: Generic structure for the src/ directory
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

         src [
           label="src", shape="folder"
         ];

         ansys [
           label="ansys", shape="folder"
         ]

         product [
           label="product", shape="folder"
         ]

         library [
           label="library", shape="folder"
         ]

         pkg_A [
           label="Package A", shape="folder"
         ]

         init_file_pkgA [
           label="__init__.py", shape="file"
         ]

         other_files_pkgA [
           label="...", shape="file"
         ]

         init_file [
           label="__init__.py", shape="file"
         ]

         other_files [
           label="...", shape="file"
         ]

         src -> ansys;
         ansys -> product;
         product -> library;
         library -> init_file;
         library -> other_files;
         library -> pkg_A;
         pkg_A -> init_file_pkgA;
         pkg_A -> other_files_pkgA;

     }


