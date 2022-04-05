.. _grpc structure diag:
.. graphviz::
    :caption: Namespace convention for gRPC interface packages.
    :alt: Namespace convention for gRPC interface packages. 
    :align: center

     digraph "sphinx-ext-graphviz" {
         size="8,6";
         rankdir="LR";
         graph [
           fontname="Verdana", fontsize="10", color="black", fillcolor="white",splines=ortho
         ];
         node [
           fontname="Verdana", fontsize="10", style="filled", color="black", fillcolor="#ffc107"
         ];

         ansys_api_product [
           label="ansys-api-product", shape="folder"
         ];

         ansys [
           label="ansys", shape="folder"
         ];

         api [
           label="api", shape="folder"
         ];

         product [
           label="product", shape="folder"
         ];

         version [
           label="VERSION", shape="file"
         ];

         v0 [
           label="v0", shape="folder"
         ];

         proto_files [
           label="\*.proto", shape="file"
         ];


         ansys_api_product -> ansys;
         ansys -> api;
         api -> product;
         product -> version;
         product -> v0;
         v0 -> proto_files;

     }


