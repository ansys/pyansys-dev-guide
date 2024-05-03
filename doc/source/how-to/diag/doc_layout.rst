.. _proposed doc layout:
.. graphviz::
    :caption: Hierarchical structure for PyAnsys library documentation.
    :alt: Hierarchical structure for PyAnsys library documentation.

     digraph "sphinx-ext-graphviz" {
         size="8,6";
         bgcolor="white"
         rankdir="LR";
         graph [
           fontname="Verdana", fontsize="10", color="black", fillcolor="white"
         ];
         node [
           fontname="Verdana", fontsize="10", style="filled", color="black", fillcolor="#ffc107"
         ];

         doc [
           label="doc", shape="folder"
         ]

         source [
           label="source", shape="folder"
         ]

         section_A [
           label="section_A", shape="folder"
         ]

         section_B [
           label="section_B", shape="folder"
         ]

         index_file [
           label="index.rst", shape="file"
         ]

         index_file_A [
           label="index.rst", shape="file"
         ]

         index_file_B [
           label="index.rst", shape="file"
         ]

         section_A_1 [
           label="page_1.rst", shape="file"
         ]

         section_A_2 [
           label="page_2.rst", shape="file"
         ]

         another_section [
           label="another_section", shape="file"
         ]

         conf_file [
           label="conf.py", shape="file"
         ]

         doc -> source;

         source -> conf_file;
         source -> index_file;
         source -> section_A;
         source -> section_B;

         section_A -> index_section_A;
         section_A -> page_A_1;
         section_A -> page_A_2;

         section_B -> index_section_B;
         section_B -> section_B_subsection;
     }


