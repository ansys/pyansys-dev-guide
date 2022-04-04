.. _build system diag:
.. mermaid::
   :caption: Maintainers use the build system to create artifacts
   :alt: Maintainers use the build system to create artifacts
   :align: center

   flowchart LR

     maintainers[Maintainers]

     subgraph build_system[Build System]
       direction LR

       subgraph frontend[Frontend]
           direction LR
           setuptools
           flit
           poetry
       end

       subgraph backend[Backend]
           direction LR
           setuptools.build_back
           flit_core.api
           poetry.masonry.api
       end

       subgraph project[PyAnsys Project]
           direction LR
           sourcefiles[src/ tests/ doc/ ]
           metadata[LICENSE README.rst]
           pyproject.toml
       end

     end

     subgraph artifacts[Artifacts]
       direction LR
       *.whl
       *.tar.gz
     end

     %% Link definitions
     maintainers-- Trigger -->build_system
     frontend-- Calls -->backend
     project-- Read by -->backend
     build_system-- Generates -->artifacts
     *.whl --- *.tar.gz

     %% Define style for nodes and subgraphs
     classDef NodeStyle stroke:black,color:black,fill:white,stroke-width:2px,font-size:12pt;
     classDef SubgraphStyle stroke:black,color:black,fill:white,stroke-width:2px,font-size:14pt,font-weight:bold;

     %% Assign style to elements
     class maintainers,setuptools,flit,poetry,setuptools.build_back,flit_core.api,poetry.masonry.api,pyproject.toml,metadata,sourcefiles,*.whl,*.tar.gz NodeStyle;
     class build_system,frontend,backend,project,artifacts SubgraphStyle;

     %% HACK: add some space between subgraph header and its nodes
     linkStyle 1 fill:none,color:black,stroke:black;
     linkStyle 2 fill:none,color:black,stroke:black;
     linkStyle 3 fill:none,color:black,stroke:black;
     linkStyle 4 fill:none,color:white,stroke:white;
