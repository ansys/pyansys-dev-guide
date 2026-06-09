.. _componentizing:

Componentizing Ansys packages
=============================

Componentization is the process of subdividing the functionality of large apps 
into multiple self-contained services with independent APIs. API creation surrounding 
existing Ansys products naturally aligns to publishing packages that mimic the full 
domain and scope of each product.

Emphasizing component libraries and services during API exposure sets a new paradigm
for Ansys product architecture that inherently breaks apart larger monolithic desktop
apps into subsets of functionality, with the expectation of compatibility and reusability
across the entire Ansys portfolio.

Many Ansys products already have a scripting solution in place, and wrapping that execution 
environment with a ``RunScript`` API endpoint is a low-barrier option to gain access to 
remote, programmatic execution. This solution lacks API granularity, however, as the abstraction
is simply an unvalidated script input and some blob output that must be parsed and evaluated 
without a prescribed response definition.

The documentation for the scripting environment still remains deep within the product and
each script execution request is hard to organize and maintain. Thus, there remains a
significant cognitive disconnect when consuming this API abstraction. The lack of API
definition within the top-level abstraction also makes data management difficult and direct 
compatibility with other PyAnsys libraries challenging. 

In addition to API clarity, the underlying product keeps a very large installation 
footprint that is a burden in modern, flexible cloud deployments. While avoiding re-architecting 
a product in the short-term can give a quick win, in most cases, it should only be used 
as a stopgap solution, providing a window of opportunity to learn more about how the user 
prefers to consume the individual functionalities of a product.

Creating well-architected component libraries maximizes product usage with these key benefits:

- Reusable shared components
- Improved API quality
- Package size reduction
- Product compatibility and composability
- Optimized, on-demand user solutions
