Vulnerabilities
===============

.. contents::

Vulnerabilities refer to potential security flaws or weaknesses in PyAnsys packages.
Here are some examples of common vulnerabilities:
- Insufficient input validation or insecure handling of file paths can lead to unauthorized access
- Insecure code and command injection into the app
- Remote code execution due to deserialization of untrusted code
- Disclosure of sensitive information due to weak exception handling

Vulnerability sources
---------------------

- **Vulnerabilities from PyAnsys library code**
  The maintainers are responsible for deciding whether to address vulnerabilities.
  The priority of vulnerabilities can be escalated internally if
  they represent a roadblock for usage.
  The Ansys business unit in charge of the project should handle
  vulnerabilities on a case-by-case basis.

- **Vulnerabilities from external package dependencies**
  When vulnerabilities exist in external packages used by PyAnsys libraries, such as numpy or matplotlib,
  Ansys should not address these vulnerabilities directly. Instead, it is best to raise an issue on
the open source repository, pointing out the vulnerability and linking the applicable `CVE`_.
  At most, be mindful of deprecated packages and functions, because they may not receive
  security patches and might introduce vulnerabilities into your codebase.

Vulnerability discovery and tracking
-------------------------------------

Leverage available security tools, such as dependency scanners or static
analyzers (such as PyUp, Safety or Bandit), to automatically detect and
remediate security vulnerabilities in Python packages and dependencies.

**Continuously monitor and assess the project's security.**
Integrate security testing into the development life cycle using
continuous integration and deployment (CI/CD) pipelines to catch
potential vulnerabilities before they reach production systems.

.. note::

   The Ansys Customer Excellence (ACE) team uses a scanner tool called *snyk* to track vulnerabilities.
   The same tool could be used, but dedicated to the PyAnsys open source environment.
   This means using the tool in an environment isolated from the Ansys Azure codebase.

As a first step, these security tools are planned to be used within the `metapackage`_ repository.
This repository contains PyAnsys packages pinned to a certain version of the Ansys unified installation.
This provides a full overview of the vulnerability status for all public PyAnsys packages.
When a flaw is detected in a PyAnsys package, an issue is opened in the repository associated with this package.
It is then up to the maintainers of this repository to handle it as described previously.

Finally, if a vulnerability is fixed, a patch release must be created.



.. _metapackage: https://github.com/pyansys/pyansys
.. _CVE: https://www.cve.org/