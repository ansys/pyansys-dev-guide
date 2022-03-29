.. _high level pyansys structure:
.. graphviz::
    :caption: High-level structure of a PyAnsys project
    :alt: High-level structure of a PyAnsys project
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

         pyansys_project [
           label="PyAnsys Project", shape="folder"
         ];

         python_library [
           label="Python Library", shape="folder"
         ];

         other_files [ 
           label="Other Files", shape="node"
         ];

         pyansys_project -> python_library;
         pyansys_project -> other_files;

     }


