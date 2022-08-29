.. _componentization:

Componentizing Ansys packages
=============================

Componentization is the process of subdividing the functionality of large applications 
into multiple self-contained services with independent APIs. API creation surrounding 
existing Ansys products naturally aligns to publishing packages that mimic the full 
domain and scope of each product. Emphasizing component libraries and services during 
API exposure sets a new paradigm for Ansys product architecture that inherently breaks 
apart larger monolithic desktop applications into subsets of functionality, with the 
expectation of compatibility and reusability across the entire Ansys portfolio.

Many Ansys products already have a scripting solution in place, and wrapping that execution 
environment with a '''RunScript''' API endpoint is a low-barrier option to gain access to 
remote, programmatic execution. This solution lacks API granularity, as the abstraction is 
simply an unvalidated script input and some blob output that must be parsed and evaluated 
without a prescribed response definition. The documentation for the scripting environment 
still remains deeper within the product and each script execution request is hard to organize 
and maintain, so there remains a significant cognitive disconnect when consuming this API 
abstraction. In addition to API clarity, the underlying product keeps a very large 
installation footprint that is a burden in modern, flexible cloud deployments. Avoiding 
re-architecting a product in the short-term can give a quick win, but in most cases 
should only be used as a stopgap solution, providing a window of opportunity to learn more 
about how the user prefers to consume the individual functionalities of a product.

Creating well-architected component libraries maximizes product usage with these key benefits:

- :ref:'API quality'
- :ref:'Package size reduction'
- :ref:'Product compatibility and composability'
- :ref:'Optimized, on-demand user solutions'

API quality
~~~~~~~~~~~

Discuss:
- Shared interfaces/contracts
- Object-oriented developer experience
- Separation of concern from underlying service implementation
- Top-level documentation
- Developer-driven control of data

Package size reduction
~~~~~~~~~~~~~~~~~~~~~~

Discuss:
- Package size requirements for modern cloud orchestration, including environmental and time impact
- Focused workloads

Dividing a multi-gigabyte application into many sub-gigabyte services enables a light-weight, 
efficient consumption model. Users can pull and deploy the exact packages needed for their current 
workload requirements.

Product compatibility and composability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Discuss:
- Data transfer compatibility between high-level APIs vs separate desktop installations
- Working with individual components from multiple existing products
- Organizing common functionality to share across the portfolio (meshing, geometry modeling, materials, etc)
- Easier compatibility with third party tools outside a walled installation


Optimized, on-demand user solutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Discuss:
- Deploying specific components to compute cluster environment
- Mixing components within a single container that would traditionally required the entire unified install
- User chosen environment and broad Linux support
- Solver/solution focused more than product focused

