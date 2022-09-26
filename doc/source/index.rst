..
   Simply reuse the root readme

Version: |version|

**Download documentation**:
`PDF Version <https://github.com/pyansys/about/releases/latest/*.pdf>`_ 

.. grid:: 2

   .. grid-item::
   .. card:: Overview
      :img-top: _static/getting_started.svg
      
      New to PyAnsys?The PyAnsys project exposes Ansys technologies via 
      libraries in the Python ecosystem.Check out the overview for more 
      details about PyAnsys
      
      +++
      
      .. button-ref:: overview/index
         :expand:
         :color: secondary
         :click-parent:
         
         To the PyAnsys overview
   
   .. grid-item-card::
   .. card:: How-to
      :img-top: _static/user_guide.svg
      
      The How-to section describes several guidelines and best practices 
      for creating effective and efficient Python libraries to interface 
      with Ansys products and services.
      
      +++
      
      .. button-ref:: how-to/index
         :expand:
         :color: secondary
         :click-parent:

         To the user guide

   .. grid-item-card::
   .. card:: Packaging style
     :img-top: _static/api.svg

      The PyAnsys library eliminates the need to share snippets of code 
      that perform actions. Users can instead create workflows consisting of their 
      own Python modules and third-party libraries.

      +++

      .. button-ref:: packaging/index
         :expand:
         :color: secondary
         :click-parent:

         To the reference guide

   .. grid-item-card::
   .. card:: Coding style
      :img-top: _static/api.svg

      Coding style refers to the different rules defined in a software project
      that must be followed when writing source code. These rules ensure that
      all the source code looks the same across different files of the project..

      +++

      .. button-ref:: coding-style/index
         :expand:
         :color: secondary
         :click-parent:

         To the contributor's guide

.. include:: ../../README.rst

.. toctree::
   :hidden:
   :maxdepth: 3

   overview/index
   how-to/index
   packaging/index
   coding-style/index
   doc-style/index
   abstractions/index
