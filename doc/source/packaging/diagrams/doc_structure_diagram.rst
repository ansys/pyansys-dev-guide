.. _doc structure diagram:
.. graphviz::
    :caption: Generic structure for the ``doc/`` directory
    :alt: Generic structure for the ``doc/`` directory
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

         doc [
           label="doc", shape="folder"
         ];

         build [
           label="_build", shape="folder"
         ]

         source [
           label="source", shape="folder"
         ]

         make_bat [
           label="make.bat", shape="file"
         ]

         makefile [
           label="Makefile", shape="file"
         ]

         static [
           label="_static", shape="folder"
         ]

         index_file [
           label="index.rst", shape="file"
         ]

         conf_file [
           label="conf.py", shape="file"
         ]

         doc -> build;
         doc -> source;
         doc -> make_bat;
         doc -> makefile;

         source -> conf_file;
         source -> index_file;
         source -> static;
     }


