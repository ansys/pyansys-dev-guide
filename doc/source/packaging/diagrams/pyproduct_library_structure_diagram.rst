.. _pyproduct library structure diagram:
.. graphviz::
    :caption: Minimum required PyAnsys project structure
    :alt: Minimum required PyAnsys project structure
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
           label="PyAnsys Project", shape="folder"
         ];

         doc [
           label="doc", shape="folder"
         ]

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

         tests [
           label="tests", shape="folder"
         ]

         readme [
           label="README.rst", shape="file"
         ]

         license [
           label="LICENSE", shape="file"
         ]

         pyproject [
           label="pyproject.toml", shape="file"
         ]

         setup [
           label="setup.py", shape="file"
         ]


         pyproduct_library -> doc;
         pyproduct_library -> src;
         pyproduct_library -> tests;
         pyproduct_library -> license;
         pyproduct_library -> readme;
         pyproduct_library -> pyproject;
         pyproduct_library -> setup;

         src -> ansys;
         ansys -> product;
         product -> library;
         library -> init_file;

     }


