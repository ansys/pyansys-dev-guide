Vulnerabilities
===============
Vulnerabilities refer to potential security flaws or weaknesses in PyAnsys packages.
Here are some examples of common vulnerabilities:
- Insufficient input validation or insecure handling of file paths can lead to unauthorized access
- Insecure code and commands injection into the application
- remote code execution due to deserialization of untrusted code
- Disclose sensitive information due to weak exception handling

2 types of sources for the vulnerabilities:
-------------------------------------------
- **Vulnerabilities from Pyansys libraries code itself**
  The maintainers take the responsibility to address them or not.
  Those vulnerabilities priorities could be escalated internally if
  they represent roadblock for business activity.
  For instances, if they prevent some deal closures or the delivery of products in
  In that case, the BUs in charge of the package will handle it case by case.

- **Vulnerabilities from PyAnsys packages external dependencies (numpy, matplotlib...)**
  Ansys cannot address them directly. It would be an endless task.
  At most, be mindful of deprecated packages and functions, as they may not receive
  security patches and might introduce vulnerabilities into your codebase.


Strategy to discover and track vulnerabilities:
-----------------------------------------------
Leverage available security tools, such as dependency scanners or static
analyzers (such as Pyup Safety or Bandit), to automatically detect and
remediate security vulnerabilities in our Python packages and dependencies.

**We must continuously monitor and assess the project's security.**
Integrate security testing into the development life cycle using
continuous integration and deployment (CI/CD) pipelines to catch
potential vulnerabilities before they reach production systems.

.. note:: 
   ACE uses a tool across Ansys TFS to track vulnerabilities.
   We could use the same but dedicated to the PyAnsys open source environment.
   This means using the tool in an environment isolated from the Ansys Azure codebase.

As a first step, we will use those security tools within the `metapackage`_.
This `metapackage`_ contains PyAnsys packages pined to a certain version of the Ansys unified install.
This will provide us with a full overview of the PyAnsys packages vulnerabilities status.
When a flaw is detected in a PyAnsys package, an issue will be open in the repository associated to this package.
Then it will be up to the maintainers of this repository to handle it as described previously.


Finally, if a vulnerability is fixed, a patch release must be created.



Images vulnerabilities
======================

To be discussed through a new meeting.




.. _metapackage: https://github.com/pyansys/pyansys