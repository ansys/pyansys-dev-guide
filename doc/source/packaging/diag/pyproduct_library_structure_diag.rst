.. _pyproduct library structure diag:
.. graphviz::
    :caption: Minimum required PyAnsys project structure.
    :alt: Minimum required PyAnsys project structure.
    :align: center

     digraph "sphinx-ext-graphviz" {
         size="8,6";
         rankdir="LR";
         bgcolor="white";
         graph [
           fontname="Verdana", fontsize="10", color="black", fillcolor="white", splines=ortho
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

         source [
           label="source", shape="folder"
         ]

         src [
           label="src", shape="folder"
         ]

         conf_file [
           label="conf.py", shape="file"
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

         authors [
           label="AUTHORS", shape="file"
         ]

         changelog [
           label="CHANGELOG.md", shape="file"
         ]

         code_of_conduct [
           label="CODE_OF_CONDUCT.md", shape="file"
         ]

         contributing [
           label="CONTRIBUTING.md", shape="file"
         ]

         contributors [
           label="CONTRIBUTORS.md", shape="file"
         ]

         license [
           label="LICENSE", shape="file"
         ]

         readme [
           label="README.rst", shape="file"
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
         pyproduct_library -> authors;
         pyproduct_library -> license;
         pyproduct_library -> changelog;
         pyproduct_library -> code_of_conduct;
         pyproduct_library -> contributing;
         pyproduct_library -> contributors;
         pyproduct_library -> readme;
         pyproduct_library -> pyproject;
         pyproduct_library -> setup;

         doc -> source;
         source -> conf_file;

         src -> ansys;
         ansys -> product;
         product -> library;
         library -> init_file;

     }


