Vulnerabilities
===============

.. contents::

Vulnerabilities refer to potential security flaws or weaknesses in PyAnsys packages.
Here are some examples of common vulnerabilities:

- Insufficient input validation or insecure handling of file paths leading to unauthorized access
- Insecure code and command injection into the app
- Remote code execution due to deserialization of untrusted code
- Disclosure of sensitive information due to weak exception handling

Vulnerability sources
---------------------

- **Vulnerabilities from PyAnsys library code**: Maintainers are responsible for deciding whether to
  address vulnerabilities. The priority of vulnerabilities can be escalated internally if they represent
  a roadblock for usage. The Ansys business unit in charge of the project should handle
  vulnerabilities on a case-by-case basis.

- **Vulnerabilities from external package dependencies**: When vulnerabilities exist in external packages
  used by PyAnsys libraries, such as NumPy or Matplotlib, Ansys should not address these vulnerabilities
  directly. Instead, raise an issue on the open source repository, pointing out the
  vulnerability and linking the applicable `CVE`_. At most, be mindful of deprecated packages and functions
  because they may not receive security patches and might introduce vulnerabilities into your codebase.

Vulnerability discovery and tracking
-------------------------------------

Leverage available security tools like dependency scanners or static
analyzers (such as PyUp, Safety, or Bandit) to automatically detect and
remediate security vulnerabilities in Python packages and dependencies.

The PyAnsys ecosystem has implemented automated mechanisms to track and
report vulnerabilities in the codebase. These tools are intended to be integrated
into the CI/CD workflow of the repositories.

The PyAnsys Core team has come up with a GitHub Action that can be used to
automatically check for vulnerabilities in the codebase. This action is based on
the following tools:

- `Safety`_ : Checks installed dependencies for known security vulnerabilities.
- `Bandit`_: Attempts to find common security issues in Python code.

Safety addresses external dependencies, while Bandit focuses on the codebase itself.
Both tools have been integrated into the ``ansys/actions/check-vulnerabilities`` action.

.. note::

  The tools selected for the action are not definitive. The action can be modified to include
  other tools or to use different versions of the tools in the future.

For third-party packages, the PyAnsys Core team has listed a set of excluded advisories so
that the action does not fail. This is done to avoid false positives and to ensure that the action
does not block the CI/CD pipeline unnecessarily. You can find the list of excluded advisories
in `the action's documentation`_.

For potential vulnerabilities in the codebase, repositories can configure Bandit to ignore specific
advisories. This can be due to the code not being ready yet to be fixed or that the advisory is not relevant
to the codebase. However, it is important to note that ignoring advisories should be done with caution,
and developers should be aware of the potential risks involved. Furthermore, repository maintainers should
document the reasons for ignoring advisories and ensure that they are regularly reviewed to determine if they
can be addressed.

.. note::

  An example on how to document the ignored advisories can be found in the `PyACP security considerations`_
  documentation page. This should be taken as a reference for documenting ignored advisories in other repositories.

.. warning::

  Testing the action locally before enabling it in the CI/CD workflow is recommended. Information on how
  to do this can be found in `the action's documentation`_.

Vulnerability remediation and reporting
----------------------------------------

When a vulnerability is detected, the action fails and reports the vulnerabilities found in the codebase.
Following that, these vulnerabilities are reported as draft security advisories in the repository's
**Security** tab. Maintainers are then responsible for reviewing the advisories and deciding whether to address
them or not. These advisories are monitored by the PyAnsys Core team and are escalated internally if they
represent a roadblock for usage.

Repositories should also have a process in place to handle vulnerabilities that are reported by users or
other developers. For that purpose, a ``SECURITY.md`` file should be created in the root of the repository.
This file should contain information on how to report vulnerabilities and the process for handling them.

Here is an example of a ``SECURITY.md`` file:

.. code-block:: markdown

 ## Reporting a vulnerability

 > [!CAUTION]
 > Do not use GitHub issues to report any security vulnerabilities.

 If you detect a vulnerability, contact the [PyAnsys Core team](mailto:pyansys.core@ansys.com),
 mentioning the repository and the details of your finding. The team will address it as soon as possible.

 Provide the PyAnsys Core team with this information:

 - Any specific configuration settings needed to reproduce the problem
 - Step-by-step guidance to reproduce the problem
 - The exact location of the problematic source code, including tag, branch, commit, or a direct URL
 - The potential consequences of the vulnerability, along with a description of how an attacker could take advantage of the issue

Vulnerability disclosure
------------------------

When a vulnerability is detected and a decision is made to address it, the repository maintainers should
create a private fork of the repository and create a pull request with the fix. Information on
how to create such a temporary fork to resolve a vulnerability can be found in `Github's documentation`_.
When opened, the pull request should be reviewed in depth and include tests to ensure that the
vulnerability is fixed. Once the pull request is merged, the repository maintainers should create a new
release with the fix and update the changelog accordingly.

The release should be tagged with a new version number where the patch value has been incremented,
and the changelog should include a note about the vulnerability and the fix. The note should include
this information:

- The CVE number of the vulnerability (if applicable)
- A description of the vulnerability and its potential consequences
- A description of the fix and how it addresses the vulnerability
- A link to the pull request that fixed the vulnerability

Additionally, the security advisory should be published on the repository's **Security** tab.
This advisory should include the same information as the changelog note, in other words the
CVE number, the date of the advisory, and the status of the advisory (such as published or withdrawn).

A reference of a published security advisory can be found here: `PyAnsys Geometry subprocess advisory`_.
This advisory was published in the PyAnsys Geometry repository and includes information about a vulnerability
in which users could execute arbitrary code on the system by using one of this library's functions.

Ensuring compliance across the PyAnsys ecosystem
------------------------------------------------

The PyAnsys Core team is responsible for ensuring that the ``ansys/actions/check-vulnerabilities`` action is up to date and that it is
being used in all PyAnsys repositories considered as libraries (that is, Python packages shipped to PyPI).
Repository maintainers are responsible for ensuring that the action is implemented correctly and that the
results are reviewed regularly.
