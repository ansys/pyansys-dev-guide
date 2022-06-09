.. _tests structure diag:
.. graphviz::
    :caption: Minimum required PyAnsys project structure.
    :alt: Minimum required PyAnsys project structure.
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

         tests [
           label="tests", shape="folder"
         ];

         tests_package_A [
           label="tests_package_A", shape="folder"
         ];

         conftest [
           label="conftest.py", shape="file"
         ]

         pytest_ini [
           label="pytest.ini", shape="file"
         ]

         test_module_foo [
           label="test_module_foo.py", shape="file"
         ]

         test_module_bar [
           label="test_module_bar.py", shape="file"
         ]

         tests -> tests_package_A;
         tests -> test_module_foo;
         tests -> conftest;
         tests -> pytest_ini;
         tests_package_A -> test_module_bar;

     }


