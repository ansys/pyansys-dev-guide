Repository Directory Structure
------------------------------
The source for a PyAnsys library is hosted in an individual 
repository under the `PyAnsys Organization Account
<https://github.com/pyansys>`__.  The repository should contain 
the source, documentation, and unit testing of the library in
this directory structure:

::

   .ci/azure-pipelines.yml (optional)
   .github/workflows/ci.yml
   ansys/
       <product/service>/
           <feature>/
               __init__.py
               my_module.py
               my_other_module.py
   doc/
       conf.py
       index.rst
       requirements.txt
   LICENSE
   README.rst
   requirements.txt
   setup.py
   tests/
       requirements.txt
       test_basic.py
       test_advanced.py

