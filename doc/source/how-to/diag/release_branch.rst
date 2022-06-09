.. graphviz::
    :caption: Release branches are created based on minor releases.
    :alt: Release branches are created based on minor releases.
    :align: center

     digraph "sphinx-ext-graphviz" {
         size="8,6";
         bgcolor="transparent";
         rankdir="LR";
         node[width=0.15, height=0.15, shape=point, color=black];
         edge[weight=2, arrowhead=none, color=black];

         node[group=master];
         1 -> 2 -> 4 -> 5 -> 8 -> 9 -> 11 -> 12 -> 13 -> 14 -> 15;
         15[shape=box, label=main];

         node[group=release1];
         2 -> 6 -> 7 -> 10;
         10[shape=box, label="release\/0.1"]

         node[group=release2];
         13 -> 16;
         16[shape=box, label="release\/0.2"]
     }
