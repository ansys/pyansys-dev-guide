.. _proposed doc layout:
.. graphviz::
    :caption: Generic structure for the PyAnsys library documentation.
    :alt: Generic structure for the PyAnsys library documentation.
    :align: center

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
           label="source", shape="folder"
         ]

         source [
           label="source", shape="folder"
         ]

         chapter_A [
           label="chapter_A", shape="folder"
         ]

         chapter_B [
           label="chapter_B", shape="folder"
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
           label="section_1.rst", shape="file"
         ]

         section_A_2 [
           label="section_2.rst", shape="file"
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
         source -> chapter_A;
         source -> chapter_B;

         chapter_A -> index_file_A;
         chapter_A -> section_A_1;
         chapter_A -> section_A_2;

         chapter_B -> index_file_B;
         chapter_B -> another_section;
     }


