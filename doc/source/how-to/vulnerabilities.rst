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

- **Vulnerabilities from PyAnsys library code**: Maintainers are responsible for deciding whether
  to address vulnerabilities. The priority of vulnerabilities can be escalated internally if they
  represent a roadblock for usage. The Ansys business unit in charge of the project should handle
  vulnerabilities on a case-by-case basis.

- **Vulnerabilities from external package dependencies**: When vulnerabilities exist in external
  packages used by PyAnsys libraries, such as NumPy or Matplotlib, Ansys should not address these
  vulnerabilities directly. Instead, raise an issue on the open source repository, pointing out
  the vulnerability and linking the applicable `CVE`_. At most, be mindful of deprecated packages
  and functions because they may not receive security patches and might introduce vulnerabilities
  into your codebase.

Vulnerability discovery and tracking
-------------------------------------

Leverage available security tools like dependency scanners or static analyzers (such as PyUp,
Safety, or Bandit) to automatically detect and remediate security vulnerabilities in Python
packages and dependencies.

The PyAnsys ecosystem has implemented automated mechanisms to track and report vulnerabilities
in the codebase. These tools are intended to be integrated into the CI/CD workflow of the
repositories.

The PyAnsys Core team has come up with a GitHub Action that can be used to automatically check
for vulnerabilities in the codebase. This action is based on the following tools:

- `Safety`_ : Checks installed dependencies for known security vulnerabilities.
- `Bandit`_: Attempts to find common security issues in Python code.

Safety addresses external dependencies, while Bandit focuses on the codebase itself. Both tools
have been integrated into the ``ansys/actions/check-vulnerabilities`` action.

.. note::

  The tools selected for the action are not definitive. The action can be modified to include
  other tools or to use different versions of the tools in the future.

For third-party packages, the PyAnsys Core team has listed a set of excluded advisories so that
the action does not fail. This is done to avoid false positives and to ensure that the action does
not block the CI/CD pipeline unnecessarily. You can find the list of excluded advisories in
`the check-vulnerabilities action documentation`_.

For potential vulnerabilities in the codebase, repositories can configure Bandit to ignore
specific advisories. This can be due to the code not being ready yet to be fixed or that the
advisory is not relevant to the codebase. However, it is important to note that ignoring
advisories should be done with caution, and developers should be aware of the potential risks
involved. Furthermore, repository maintainers should document the reasons for ignoring advisories
and ensure that they are regularly reviewed to determine if they can be addressed.

.. note::

  An example on how to document the ignored advisories can be found in the `PyACP security
  considerations`_ documentation page. This should be taken as a reference for documenting ignored
  advisories in other repositories.

.. warning::

  Testing the action locally before enabling it in the CI/CD workflow is recommended. Information
  on how to do this can be found in `the check-vulnerabilities action documentation`_.

Vulnerability remediation and reporting
----------------------------------------

When a vulnerability is detected, the action fails and reports the vulnerabilities found in the
codebase. Following that, these vulnerabilities are reported as draft security advisories in the
repository's **Security** tab. Maintainers are then responsible for reviewing the advisories and
deciding whether to address them or not. These advisories are monitored by the PyAnsys Core team
and are escalated internally if they represent a roadblock for usage.

Repositories should also have a process in place to handle vulnerabilities that are reported by
users or other developers. For that purpose, a ``SECURITY.md`` file should be created in the root
of the repository. This file should contain information on how to report vulnerabilities and the
process for handling them.

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

When a vulnerability is detected and a decision is made to address it, the repository maintainers
should create a private fork of the repository and create a pull request with the fix. Information
on how to create such a temporary fork to resolve a vulnerability can be found in `Github's
documentation`_. When opened, the pull request should be reviewed in depth and include tests to
ensure that the vulnerability is fixed. Once the pull request is merged, the repository
maintainers should create a new release with the fix and update the changelog accordingly.

The release should be tagged with a new version number where the patch value has been incremented,
and the changelog should include a note about the vulnerability and the fix. The note should
include this information:

- The CVE number of the vulnerability (if applicable)
- A description of the vulnerability and its potential consequences
- A description of the fix and how it addresses the vulnerability
- A link to the pull request that fixed the vulnerability

Additionally, the security advisory should be published on the repository's **Security** tab. This
advisory should include the same information as the changelog note, in other words the CVE number,
the date of the advisory, and the status of the advisory (such as published or withdrawn).

A reference of a published security advisory can be found here: `PyAnsys Geometry subprocess
advisory`_. This advisory was published in the PyAnsys Geometry repository and includes
information about a vulnerability in which users could execute arbitrary code on the system by
using one of this library's functions.

Ensuring compliance across the PyAnsys ecosystem
------------------------------------------------

The PyAnsys Core team is responsible for ensuring that the ``ansys/actions/check-vulnerabilities``
action is up to date and that it is being used in all PyAnsys repositories considered as libraries
(that is, Python packages shipped to PyPI). Repository maintainers are responsible for ensuring
that the action is implemented correctly and that the results are reviewed regularly.


Addressing common vulnerabilities in Python libraries and applications
----------------------------------------------------------------------

When developing Python applications, it is essential to be aware of common vulnerabilities that can
occur in the codebase. These vulnerabilities can lead to security risks, data breaches, and other
serious issues.

The `Bandit` tool provides a blacklist of known vulnerable functions and methods that should
not be used in Python code. Using these functions can lead to security vulnerabilities and
should be avoided. Refer to the `blacklists Bandit documentation`_ for detailed information on
`Bandit` tool outputs.


**Bandit blacklist**

The `Bandit` tool provides a blacklist of known vulnerable functions and methods that should
not be used in Python code. Using these functions can lead to security vulnerabilities and
should be avoided.

Address each requested changes proposed by `Bandit` to ensure that your code is secure.
You can find information on how to improve your code in the `blacklists Bandit documentation`_.


**subprocess command injection**

The `subprocess` module can be vulnerable to command injection if user input is not properly
sanitized. This can lead to arbitrary command execution, which is a significant security risk.

To mitigate this risk, you should:

- avoid using the `subprocess` module to execute shell commands with user input, as it can lead
  to command injection vulnerabilities.
- if the previous point is not possible, you need to disable the `shell=True` argument in 
  `subprocess.run()` or similar functions, as it allows for shell injection attacks.

By removing the `shell=True` argument, a list is needed to pass the command and its
arguments directly, which is safer. This way, user input is not executed as a shell command,
and the risk of command injection is significantly reduced.

.. tab-set::

    .. tab-item:: Risk of `subprocess` command injection

        .. code:: python

          import subprocess

          user_input = "malicious_command; rm -rf /"  # User input that could be malicious
          subprocess.run(f"echo {user_input}", shell=True)  # Vulnerable to command injection

    .. tab-item:: Reduced risk of `subprocess` command injection

        .. code:: python

          import subprocess

          user_input = "malicious_command; rm -rf /"  # User input that could be malicious
          # Removing shell=True and using a list
          subprocess.run(["echo", user_input])  # User input is not executed as a shell command

.. note::

  Bandit warning remains even after deactivating the `shell=True` argument.
  If you are sure that the command is safe, you can ignore the Bandit warning. Please
  check the `Ignore Bandit warnings`_ section for more information on how to do so.



**try except continue statements**

Using `try except continue` statements can lead to silent failures, making it difficult to debug
issues and potentially allowing vulnerabilities to go unnoticed. Instead, you should handle
exceptions explicitly and log or raise them as needed.

.. tab-set::

    .. tab-item:: `try except continue` without handling exceptions

        .. code:: python

          try:
              risky_operation()  # Some code that might raise an exception
          except:
              continue  # This will silently ignore all the exceptions and continue execution

    .. tab-item:: `try except continue` with explicit exception handling

        .. code:: python

          try:
              risky_operation()
          except SpecificException as e:
              continue  # Handle specific exceptions and continue
          except AnotherSpecificException as e:
              log_error(e)  # Log the error for debugging
              raise  # Raise the exception to notify the caller


**requests.get() without timeout**

Using `requests.get()` without a timeout can lead to hanging requests, which can be exploited
by attackers to cause denial of service (DoS) conditions. Always specify a timeout value to
prevent this issue.

.. tab-set::

    .. tab-item:: `requests.get()` without timeout

        .. code:: python

          import requests

          response = requests.get("https://example.com")  # No timeout specified

    .. tab-item:: `requests.get()` with timeout

        .. code:: python

          import requests

          response = requests.get("https://example.com", timeout=5)  # Timeout set to 5 seconds


**random insecure functions**

Using insecure functions from the `random` module can lead to predictable random number
generation, which can be exploited by attackers. Instead, use the `secrets` module, which
provides a secure way to generate random numbers.

.. tab-set::

    .. tab-item:: Insecure random functions

        .. code:: python

          import random

          random_number = random.randint(1, 100)  # Predictable random number generation
          random_letter = random.choice(["a", "b", "c"])  # Predictable choice from a list

    .. tab-item:: Secure random functions

        .. code:: python

          import secrets

          secure_random_number = secrets.randbelow(100)  # Secure random number generation
          secure_random_letter = secrets.choice(["a", "b", "c"])  # Secure choice from a list


Ignore Bandit warnings
~~~~~~~~~~~~~~~~~~~~~~

In-line comment
+++++++++++++++

When using Bandit, you may encounter warnings that you believe are not relevant to your codebase
or that you have already addressed. In such cases, you can ignore specific Bandit warnings by
adding a comment to the end of the line that triggers the warning. The comment should be in the
format ``# nosec <warning_id>``, where ``<warning_id>`` is the ID of the warning you want to ignore.

When you ignore a Bandit warning, it is essential to provide a clear comment explaining why
the warning is being ignored. This helps maintainers and other developers understand the context
and rationale behind the decision.

For example, to ignore the B404 warning, you would add `# nosec B404` to the end of the line:

.. code:: python

  # Subprocess is needed to start the backend. But
  # the input is controlled by the library. Excluding bandit check.
  import subprocess  # nosec B404


.. warning::

  Please note that ignoring Bandit warnings should be done with caution, and you should ensure
  that the code is safe and does not introduce any security risks. It is recommended to review the
  `bandit documentation`_ for more information on each warning and the potential risks involved.


Security considerations file
++++++++++++++++++++++++++++

In addition to ignoring specific Bandit warnings, it is a good practice to document the ignored
advisories in a dedicated file. You can find an example of such a file in the `PyACP security
considerations`_ documentation page. This way, you can provide to the users a clear overview of
the vulnerabilities that need to be taken into account when using the library.

Addressing common vulnerabilities in Github Actions
---------------------------------------------------
Vulnerabilities can exist in continuous integration (CI) pipelines just as they can in a codebase.
To reduce the risk of security breaches and supply chain attacks, it is important to secure your
GitHub Actions workflows against known vulnerabilities.

`zizmor`_ is a static analysis tool that audits GitHub Actions CI/CD setups. It detects common
vulnerabilities and, in some cases, can automatically fix them. For detailed information about
the rules that zizmor applies when auditing workflows, see `zizmor audit rules`_.

Auditing CI/CD setups in the PyAnsys ecosystem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For PyAnsys ecosystem projects, the recommended way to audit workflows is to use the
``ansys/actions/check-actions-security`` action. The action wraps ``zizmor`` and provides
additional functionality and configuration tailored to PyAnsys projects. For setup instructions,
see `the check-actions-security action documentation`_.

Fixing common issues detected by ``zizmor``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This section describes how to fix common workflow vulnerabilities.
For practical examples, see these pull requests with fixes already applied in the PyAnsys ecosystem:

- `Ansys actions security fixes 1`_
- `Ansys actions security fixes 2`_
- `Ansys actions security fixes 3`_
- `PyConverter-XML2Py security fixes`_

For vulnerabilities not listed here, refer to `zizmor audit rules`_ for remediation steps.
For additional examples of fixes, see the `zizmor trophy case`_.

**artipacked**

.. tab-set::


  .. tab-item:: Before

    .. code:: yaml

      # See https://docs.zizmor.sh/audits/#artipacked for more information.
      steps:

      - name: "Checkout project" # actions/checkout persists git credentials by default.
        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2


  .. tab-item:: After

    .. code:: yaml

      # See https://docs.zizmor.sh/audits/#artipacked for more information.
      steps:
  
      - name: "Checkout project"
        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
        with: # Unless needed for git operations in subsequent steps, do not persist credentials.
          persist-credentials: false

.. note::

  When you run git commands that require persisted credentials in subsequent steps within the same job,
  you can ignore this audit finding. For details, see `ignoring zizmor results`_

**unpinned-uses**

.. tab-set::


  .. tab-item:: Before

    .. code:: yaml

      # See https://docs.zizmor.sh/audits/#unpinned-uses for more information.
      steps:

      - name: "Upload distribution artifacts to GitHub artifacts"
        uses: actions/upload-artifact@v4 # The commit a tag-pinned action points to can change due to various factors.
        with:
          name: ${{ env.LIBRARY_NAME }}-artifacts
          path: ~/${{ env.LIBRARY_NAME }}/dist/


  .. tab-item:: After

    .. code:: yaml

      # See https://docs.zizmor.sh/audits/#unpinned-uses for more information.
      steps:

      - name: "Upload distribution artifacts to GitHub artifacts"
        uses: actions/upload-artifact@4cec3d8aa04e39d1a68397de0c4cd6fb9dce8ec1 # v4.6.1 # Pinning with a SHA prevents this.
        with:
          name: ${{ env.LIBRARY_NAME }}-artifacts
          path: ~/${{ env.LIBRARY_NAME }}/dist/

.. tip::

  You can use the `pinact`_ tool to automatically pin versions of actions and reusable workflows.

.. note::

  The ``ansys/actions/check-actions-security`` action has a ``trust-ansys-actions`` option that
  allows you to use tags for ``ansys/actions``.
  When this option is enabled, you only need to pin external actions.

**github-env**

.. tab-set::


  .. tab-item:: Before

    .. code:: yaml

      # See https://docs.zizmor.sh/audits/#github-env for more information.
      steps:

      - name: "Decompose tag into components"
        shell: bash
        run: |
          if [[ ${{ github.ref_name }} =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
            IFS='.' read -ra PARTS <<< "${{ github.ref_name }}"
            echo "V_AND_MAJOR=${PARTS[0]}" >> $GITHUB_ENV # When used in workflows with dangerous triggers, such as pull_request_target
            echo "MINOR=${PARTS[1]}" >> $GITHUB_ENV # and workflow_run, GITHUB_ENV and GITHUB_PATH can be an arbitrary code execution risk.
            echo "PATCH=${PARTS[2]}" >> $GITHUB_ENV
          else
            echo "Invalid tag format. Expected vX.Y.Z but got ${{ github.ref_name }}"
            exit 1
          fi

      - name: "Check tag is valid for current branch"
        shell: bash
        run: |
          V_AND_MAJOR=${{ env.V_AND_MAJOR }}
          MAJOR="${V_AND_MAJOR#v}"
          echo "MAJOR=${MAJOR}" >> $GITHUB_ENV
          if [[ ${{ github.event.base_ref }} != "refs/heads/release/$MAJOR.${{ env.MINOR }}" ]]; then
            echo "::error::Tag ${{ github.ref_name }} does not match branch version. wrong branch."
            exit 1
          fi

      - name: "Remove v${{ env.MAJOR }} tag"
        shell: bash
        run: |
          git push --delete origin v${{ env.MAJOR }} && \
            echo "Deleted v${{ env.MAJOR }} tag" || \
            echo "Tag v${{ env.MAJOR }} not found"

      - name: "Remove v${{ env.MAJOR }}.${{ env.MINOR }} tag"
        shell: bash
        run: |
          git push --delete origin v${{ env.MAJOR }}.${{ env.MINOR }} && \
            echo "Deleted v${{ env.MAJOR }}.${{ env.MINOR }} tag" || \
            echo "Tag v${{ env.MAJOR }}.${{ env.MINOR }} not found"

      - name: "Create new tags"
        shell: bash
        run: |
          git tag v${{ env.MAJOR }}.${{ env.MINOR }}
          git tag v${{ env.MAJOR }}
          git push origin v${{ env.MAJOR }}.${{ env.MINOR }}
          git push origin v${{ env.MAJOR }}


  .. tab-item:: After

    .. code:: yaml

      # See https://docs.zizmor.sh/audits/#github-env for more information.
      steps:

      - name: "Decompose tag into components"
        id: tag-components
        shell: bash
        run: |
          if [[ ${{ github.ref_name }} =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
            IFS='.' read -ra PARTS <<< "${{ github.ref_name }}"
            echo "V_AND_MAJOR=${PARTS[0]}" >> $GITHUB_OUTPUT # Writing to GITHUB_OUTPUT is safe.
            echo "MINOR=${PARTS[1]}" >> $GITHUB_OUTPUT # Writing to GITHUB_OUTPUT is safe.
            echo "PATCH=${PARTS[2]}" >> $GITHUB_OUTPUT # Writing to GITHUB_OUTPUT is safe.
          else
            echo "Invalid tag format. Expected vX.Y.Z but got ${{ github.ref_name }}"
            exit 1
          fi

      - name: "Check tag is valid for current branch"
        id: current-branch-tag-validity
        shell: bash
        env:
          V_AND_MAJOR: ${{ steps.tag-components.outputs.V_AND_MAJOR }} # Then share information between steps
          MINOR: ${{ steps.tag-components.outputs.MINOR }} # through the env block.
        run: |
          MAJOR="${V_AND_MAJOR#v}"
          echo "MAJOR=${MAJOR}" >> $GITHUB_OUTPUT
          if [[ ${{ github.event.base_ref }} != "refs/heads/release/${MAJOR}.${MINOR}" ]]; then
            echo "::error::Tag ${{ github.ref_name }} does not match branch version. wrong branch."
            exit 1
          fi

      - name: "Remove v${{ steps.current-branch-tag-validity.outputs.MAJOR }} tag"
        shell: bash
        env:
          MAJOR: ${{ steps.current-branch-tag-validity.outputs.MAJOR }}
        run: |
          git push --delete origin v${MAJOR} && \
            echo "Deleted v${MAJOR} tag" || \
            echo "Tag v${MAJOR} not found"

      - name: "Remove v${{ steps.current-branch-tag-validity.outputs.MAJOR }}.${{ steps.tag-components.outputs.MINOR }} tag"
        shell: bash
        env:
          MAJOR: ${{ steps.current-branch-tag-validity.outputs.MAJOR }}
          MINOR: ${{ steps.tag-components.outputs.MINOR }}
        run: |
          git push --delete origin v${MAJOR}.${MINOR} && \
            echo "Deleted v${MAJOR}.${MINOR} tag" || \
            echo "Tag v${MAJOR}.${MINOR} not found"

      - name: "Create new tags"
        shell: bash
        env:
          MAJOR: ${{ steps.current-branch-tag-validity.outputs.MAJOR }}
          MINOR: ${{ steps.tag-components.outputs.MINOR }}
        run: |
          git tag v${MAJOR}.${MINOR}
          git tag v${MAJOR}
          git push origin v${MAJOR}.${MINOR}
          git push origin v${MAJOR}

.. note::

  The trick is to pass state between steps using ``GITHUB_OUTPUT`` instead of ``GITHUB_ENV`` or ``GITHUB_PATH``.
  On Windows runners, the same principle applies when running commands in ``cmd`` or ``pwsh``; only the syntax differs.

**template-injection**

.. tab-set::


  .. tab-item:: Before

    .. code:: yaml

      # See https://docs.zizmor.sh/audits/#template-injection for more information.
      name: Example reusable workflow

      on:
        workflow_call:
          inputs:
            user-input:
              required: false
              type: string
              default: "user input"

        workflow_dispatch:
          inputs:
            required: false
            type: string
            default: "user input"

      jobs:
        example-job:
          name: "Example job"
          runs-on: ubuntu-latest
          steps:

          - name: "Inspect context variables and workflow input"
            run: |
              echo ${{ github.workspace }} # Template expansions are resolved before workflows and jobs run. These expansions
              echo ${{ runner.temp }} # insert their results directly into the context, which can accidentally introduce shell injection risks.
              echo ${{ input.user-input }} # This is especially through when such expansion is from a user input.


  .. tab-item:: After

    .. code:: yaml

      # See https://docs.zizmor.sh/audits/#template-injection for more information.
      name: Example reusable workflow

      on:
        workflow_call:
          inputs:
            user-input:
              required: false
              type: string
              default: "user input"

        workflow_dispatch:
          inputs:
            required: false
            type: string
            default: "user input"

      jobs:
        example-job:
          name: "Example job"
          runs-on: ubuntu-latest
          steps:

          - name: "Inspect context variables and workflow input"
            env:
              USER_INPUT: ${{ inputs.user-input }} # Expand inputs and relevant context variables in the env block.
            run: |
              echo ${USER_INPUT} # Then use that directly within the run block.
              echo ${RUNNER_TEMP} # Also, most Github context variables have equivalent environment variables
              echo ${GITHUB_WORKSPACE} # that can be directly used in place of template expansions.

.. note::

  Notice that ``RUNNER_TEMP`` and ``GITHUB_WORKSPACE`` were not explicitly set in the ``env`` block.
  Some GitHub context variables automatically map to environment variables, such as
  ``runner.temp`` to ``RUNNER_TEMP`` and ``github.workspace`` to ``GITHUB_WORKSPACE``.
  
  If a corresponding environment variable is not automatically available, you must set it in the ``env``
  block of the job or step where it is needed before you can use it.

**excessive-permissions**

.. tab-set::


  .. tab-item:: Before

    .. code:: yaml

      # See https://docs.zizmor.sh/audits/#excessive-permissions for more information.
      name: Github CI

      on:
        pull_request:
        push:
          tags:
            - "*"
          branches:
            - main

      env:
        MAIN_PYTHON_VERSION: '3.12'
        DOCUMENTATION_CNAME: 'actions.docs.ansys.com'

      # When not specified, the default permission assigned to workflows might be too excessive
      # for what the jobs need to do. Furthermore, all job steps automatically inherit this
      # default permission

      concurrency:
        group: ${{ github.workflow }}-${{ github.ref }}
        cancel-in-progress: true

      jobs:
        doc-build:
          name: "Doc build"
          runs-on: ubuntu-latest
          steps:
            - uses: ansys/actions/doc-build@v10.1.0a0
              with:
                skip-install: true
                python-version: ${{ env.MAIN_PYTHON_VERSION }}
                use-python-cache: false
                needs-quarto: true

        doc-deploy-dev:
          name: "Deploy development documentation"
          runs-on: ubuntu-latest
          needs: [doc-build]
          steps:
            - uses: ansys/actions/doc-deploy-dev@v10.1.0a0
              with:
                cname: ${{ env.DOCUMENTATION_CNAME }}
                token: ${{ secrets.GITHUB_TOKEN }}
                bot-user: ${{ secrets.PYANSYS_CI_BOT_USERNAME }}
                bot-email: ${{ secrets.PYANSYS_CI_BOT_EMAIL }}


  .. tab-item:: After

    .. code:: yaml

      # See https://docs.zizmor.sh/audits/#excessive-permissions for more information.
      name: Github CI

      on:
        pull_request:
        push:
          tags:
            - "*"
          branches:
            - main

      env:
        MAIN_PYTHON_VERSION: '3.12'
        DOCUMENTATION_CNAME: 'actions.docs.ansys.com'

      permissions: {} # Zero permissions can be granted at the workflow level if not all jobs require permissions.
                      # As a good rule of thumb, this normally includes jobs that don't use secrets.

      concurrency:
        group: ${{ github.workflow }}-${{ github.ref }}
        cancel-in-progress: true

      jobs:
        doc-build:
          name: "Doc build"
          runs-on: ubuntu-latest
          steps:
            - uses: ansys/actions/doc-build@v10.1.0a0
              with:
                skip-install: true
                python-version: ${{ env.MAIN_PYTHON_VERSION }}
                use-python-cache: false
                needs-quarto: true

        doc-deploy-dev:
          name: "Deploy development documentation"
          runs-on: ubuntu-latest
          needs: [doc-build]
          permissions:
            contents: write # The specific permission type needed is set for a job that actually needs it.
          steps:
            - uses: ansys/actions/doc-deploy-dev@v10.1.0a0
              with:
                cname: ${{ env.DOCUMENTATION_CNAME }}
                token: ${{ secrets.GITHUB_TOKEN }}
                bot-user: ${{ secrets.PYANSYS_CI_BOT_USERNAME }}
                bot-email: ${{ secrets.PYANSYS_CI_BOT_EMAIL }}

**anonymous-definition**

.. tab-set::


  .. tab-item:: Before

    .. code:: yaml

      # See https://docs.zizmor.sh/audits/#anonymous-definition for more information.
      on: push # This workflow has no name.

      jobs:
        build:
          runs-on: ubuntu-latest
          steps:
            - run: echo "Hello!"


  .. tab-item:: After

    .. code:: yaml

      # See https://docs.zizmor.sh/audits/#anonymous-definition for more information.
      name: Echo Test # It is good practice to always name workflows.
      on: push

      jobs:
        build:
          runs-on: ubuntu-latest
          steps:
            - run: echo "Hello!"

.. note::

  This finding has no security impact and is more of reinforcing good practices.

Ignoring ``zizmor`` findings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One-off comments
++++++++++++++++
While auditing workflows with ``zizmor``, you might need to ignore findings that are not relevant to your workflows.  
You can ignore ``zizmor`` audits by adding a YAML comment on any line within the span of the finding.

Use the following format:

.. code:: yaml

  # zizmor: ignore[<rule-name>]

For example, to ignore the ``artipacked`` rule:

.. code:: yaml

  # zizmor: ignore[artipacked]

To ignore multiple rules in the same span, separate them with commas:

.. code:: yaml

  # zizmor: ignore[github-env,template-injection]

For more information, see `ignoring zizmor results`_.

``zizmor.yml`` configuration file
+++++++++++++++++++++++++++++++++
If you need to ignore multiple findings or entire files, a ``zizmor.yml`` configuration file is
easier to maintain than one-off comments.

A ``zizmor.yml`` file might look like this:

.. code:: yaml

  rules:
    unpinned-uses:
      config:
        policies:
          ansys/*: ref-pin
          actions/*: hash-pin
    template-injection:
      ignore:
        - safe.yml
        - somewhat-safe.yml:123
        - one-exact-spot.yml:123:456

This configuration file achieves the following:

- Declares that ``ansys/actions`` can be pinned with tags, but ``actions/*`` must be pinned with a SHA.
- Ignores all ``template-injection`` findings in ``safe.yml``, regardless of line or column location.
- Ignores any ``template-injection`` findings in ``somewhat-safe.yml`` that occur on line 123.
- Ignores one ``template-injection`` finding in ``one-exact-spot.yml`` that occurs on line 123, column 456.

For more information, see `ignoring zizmor results`_.