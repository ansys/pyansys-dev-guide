.. graphviz::
    :caption: The main branch is the primary development branch. 
    :alt: The main branch is the primary development branch. 
    :align: center

     digraph "sphinx-ext-graphviz" {
         size="8,6";
         bgcolor="white";
         rankdir="LR";
         node[width=0.15, height=0.15, shape=point, color=black];
         edge[weight=2, arrowhead=none, color=black];
         node[group=master];
         1 -> 2 -> 4 -> 5;
         5[shape=box, label=main];
         node[group=branch];
         2 -> 6 -> 7 -> 4;
     }
