Vulnerabilities
===============

.. contents::

Vulnerabilities refer to potential security flaws or weaknesses in PyAnsys packages.
Here are some examples of common vulnerabilities:
- Insufficient input validation or insecure handling of file paths can lead to unauthorized access
- Insecure code and command injection into the app
- remote code execution due to deserialization of untrusted code
- Disclose sensitive information due to weak exception handling

Vulnerability sources
---------------------

- **Vulnerabilities from PyAnsys libraries code itself**
  The maintainers are responsible for deciding whether to address vulnerabilities.
  The priority of vulnerabilities can be escalated internally if
  they represent a roadblock for business activity, such as.
  preventing some deal closures or the delivery of products.
  The Ansys business units in charge of the package should handle
  vulnerabilities case by case.

- **Vulnerabilities from PyAnsys packages external dependencies (for example numpy, matplotlib)**
  Ansys cannot address them directly. It would be an endless task.
  At most, be mindful of deprecated packages and functions, as they may not receive
  security patches and might introduce vulnerabilities into your codebase.

Vulnerability discovery and tracking
-------------------------------------

Leverage available security tools, such as dependency scanners or static
analyzers (such as Pyup Safety or Bandit), to automatically detect and
remediate security vulnerabilities in Python packages and dependencies.

**Continuously monitor and assess the project's security.**
Integrate security testing into the development life cycle using
continuous integration and deployment (CI/CD) pipelines to catch
potential vulnerabilities before they reach production systems.

.. note::

   ACE uses a tool across Ansys TFS to track vulnerabilities.
   The same tool could be used, but dedicated to the PyAnsys open source environment.
   This means using the tool in an environment isolated from the Ansys Azure codebase.

As a first step, these security tools are planned to be used within the `metapackage`_.
This `metapackage`_ contains PyAnsys packages pined to a certain version of the Ansys unified install.
This provides a full overview of the public PyAnsys packages vulnerabilities status.
When a flaw is detected in a PyAnsys package, an issue is opened in the repository associated to this package.
Then it is up to the maintainers of this repository to handle it as described previously.

Finally, if a vulnerability is fixed, a patch release must be created.

Vulnerability images
====================

To be discussed through a new meeting.


.. _metapackage: https://github.com/pyansys/pyansys