.. _continuous_integration:

Continuous integration
======================

Continuous integration (CI) is the process of merging new changes into the main
code base while ensuring that these changes are functional and do not break the existing
code. 

This process is automated as much as possible to alleviate the developer's workload
and ensure a quick development workflow.

Because PyAnsys projects are hosted in `GitHub <GitHub_>`_, the
`GitHub Actions`_ framework is used.

Enable GitHub actions
---------------------

By default, ``Actions`` are enabled in new repositories and can be accessed
using the associated :ref:`GitHub repository sections <github_repo_sections>`.

If ``Actions`` are not enabled, you can enable them. For more information, see
`Managing GitHub Actions permissions for your repository
<https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository>`_
in the GitHub documentation.

Use GitHub Actions
------------------

You must declare the GitHub Actions to be executed in the CI process in a
common ``ci.yml`` file in the ``.github/workflows`` directory. Although each
action is different, they all have a common structure:

- A name identifying the action.
- A collection of triggering events that run the action when required.
- A collection of concurrent workflows conditions to, for example, avoid running
  several workflows for the same branch. (Multiple consecutive pushes could lead to
  multiple ongoing workflows when you want only the last push to run).
- A collection of jobs with different steps to follow during the CI process. 

.. code-block:: yaml

    name: <Name of the action>
    
    on:
      <Triggering events and conditions>

    concurrency:
      <Avoid concurrent workflows to be run>

    jobs:
      <All jobs must be defined below this line>

Turn off concurrent workflows
-----------------------------

Handling hardware resources is a big deal, especially when running with self-hosted agents.
If you are using public GitHub hardware for running your workflows, disabling concurrent
CI workflows is a way to show that you care about the environment and sustainability.

For example, imagine the following situation:

* You push some changes to your branch.
* The CI workflow kicks in and starts executing the different stages.
* You suddenly realize that there is a typo or a file missing.
* You push the new commit to your PR.
* A new CI workflow kicks in and starts running.

At this moment, you probably have two parallel workflows running at the same time,
though you are only interested in the results from the last one.

One way to solve this is manually cancelling the oldest workflow. However, it is also possible to
automatically cancel pre-existing workflows for a PR. To do so, prior to the
``jobs`` section in the ``ci.yml`` file, add the following lines to your workflow:

.. code-block:: yaml

  concurrency:
    group: ${{ github.workflow }}-${{ github.ref }}
    cancel-in-progress: true


Required workflows
------------------

PyAnsys projects require workflows for performing these types of checks:

- :ref:`Code style <coding_style>`
- :ref:`Documentation style`
- `Security checks <check_vulnerabilities_>`_
- :ref:`Documentation building <Build documentation>`
- :ref:`Documentation deployment <Deploy documentation>`
- :ref:`Testing`
- :ref:`Test code coverage`
- :ref:`release_publish`

You should collect all workflows in a common ``ci.yml`` file in the ``.github/workflows``
directory. For more information, see :ref:`Workflow examples`.

Dependabot parametrization
--------------------------

PyAnsys projects use Dependabot to keep dependencies up to date.
Dependabot is a GitHub feature that automatically checks for outdated dependencies and creates
pull requests to update them.

Dependabot can be configured to run on different schedules, such as daily, weekly, or monthly.
To configure Dependabot, create a ``dependabot.yml`` file in the ``.github`` directory of your
repository. You can check the :ref:`Dependabot cooldown` section in :ref:`Repository protection` for
an example of a ``dependabot.yml`` file.

Parametrize workflows
---------------------

It is important to test a PyAnsys library on different operating systems
using different Python versions:

.. math::

    \text{Num. Workflows} = \text{Num. Operating Systems} \times \text{Num. Python Versions}

The most common operating systems are Windows, macOS, and Linux/UNIX. For supported
Python versions, see :ref:`Python versions`.

Because having a YML file for each workflow would be tedious, GitHub
Actions provides the ``matrix`` parameter inside the ``strategy``. For more
information, see `Using a matrix for your Jobs
<https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs>`_
in the GitHub documentation

Consider this example of a parametrized workflow:

.. tab-set::

    .. tab-item:: Workflow file

        .. code-block:: yaml
        
            jobs:
              example_matrix:
                strategy:
                  matrix:
                    python: ['3.10', '3.11', '3.12', '3.13', '3.14']
                    os: [windows-latest, macos-latest, ubuntu-latest]
                
                steps:
                  - echo "Running Python ${{ matrix.python }} in ${{ matrix.os }}"

    .. tab-item:: Actions log file

        .. code-block:: text

            Running Python 3.10 in windows-latest
            Running Python 3.11 in windows-latest
            Running Python 3.12 in windows-latest
            Running Python 3.13 in windows-latest
            Running Python 3.14 in windows-latest
            Running Python 3.10 in macos-latest
            Running Python 3.11 in macos-latest
            Running Python 3.12 in macos-latest
            Running Python 3.13 in macos-latest
            Running Python 3.14 in macos-latest
            Running Python 3.10 in ubuntu-latest
            Running Python 3.11 in ubuntu-latest
            Running Python 3.12 in ubuntu-latest
            Running Python 3.13 in ubuntu-latest
            Running Python 3.14 in ubuntu-latest

Workflow examples
-----------------

Workflow examples are provided for various checks, such as :ref:`code style <coding_style>`,
:ref:`tests <testing>`, :ref:`documentation style <documenting_developers>`,
:ref:`documentation building <Build documentation>`, and :ref:`releasing <release_publish>`.

.. tab-set::

    .. tab-item:: style.yml
        
        .. literalinclude:: code/style.yml     
           :language: yaml

    .. tab-item:: tests.yml
        
        .. literalinclude:: code/tests.yml     
           :language: yaml

    .. tab-item:: docs.yml
        
        .. literalinclude:: code/docs.yml     
           :language: yaml

    .. tab-item:: build.yml
        
        .. literalinclude:: code/build.yml     
           :language: yaml

    .. tab-item:: release.yml
        
        .. literalinclude:: code/release.yml     
           :language: yaml


.. _organization_secrets:

Organization secrets
--------------------

According to `Encrypted secrets <https://docs.github.com/en/actions/security-guides/encrypted-secrets>`_
in the GitHub Docs, "Secrets are encrypted variables that you create in an organization,
repository, or repository environment. The secrets that you create are available to use in
GitHub Actions workflows." 

You can use secrets to pass sensitive data such as passwords, tokens, or IP addresses to your workflows.

The ``ansys`` and ``ansys-internal`` organizations provide certain secrets by default to
help you to automate or unify certain tasks, such as releasing a package.

Secrets for GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------+------------------------------------+---------------------------------------+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| **Secret**                          | **Repository access**              | **Token**                             | **Value**                                 | **description**                                                                                         |
+=====================================+====================================+=======================================+===========================================+=========================================================================================================+
| ``BOT_APPLICATION_ID``              | All repositories                   | No                                    | *Secret*                                  | Username of bot app                                                                                     |
+-------------------------------------+------------------------------------+---------------------------------------+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``BOT_APPLICATION_PRIVATE_KEY``     | All repositories                   | No                                    | *Secret*                                  | Bot private key (see :ref:`organization_bot`)                                                           |
+-------------------------------------+------------------------------------+---------------------------------------+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``HUGO_THEME_TOKEN``                | All repositories                   | Yes                                   | *Secret*                                  |                                                                                                         |
+-------------------------------------+------------------------------------+---------------------------------------+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``LICENSE_SERVER``                  | All repositories                   | No                                    | *Secret*                                  | IP address of license server                                                                            |
+-------------------------------------+------------------------------------+---------------------------------------+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``MULTIPR_DEPENDABOT``              | All repositories                   | :ref:`Yes (GitHub) <github_tokens>`   | Token ``PYANSYS_CI_BOT_TOKEN``            | Bot token to pass to bot to allow multiple library updates in one pull request.                         |
+-------------------------------------+------------------------------------+---------------------------------------+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``PYANSYS_CI_BOT_PACKAGE_TOKEN``    | Private and internal repositories  | :ref:`Yes (GitHub) <github_tokens>`   | Token ``PYANSYS_CI_BOT_PACKAGE_TOKEN``    | Bot token to publish (write) packages in `ghcr.io <ghcr.io>`_ registry.                                 |
+-------------------------------------+------------------------------------+---------------------------------------+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``PYANSYS_CI_BOT_TOKEN``            | All repositories                   | :ref:`Yes (GitHub) <github_tokens>`   | Token ``PYANSYS_CI_BOT_TOKEN``            | Bot token for general purpose. It has repository read/write permissions and package read permission.    |
+-------------------------------------+------------------------------------+---------------------------------------+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``PYANSYS_PYPI_PRIVATE_PAT``        | All repositories                   | :ref:`Yes (PyPI) <pypi_tokens>`       | Token ``PYANSYS_PYPI_PRIVATE_PAT``        | Token to publish to Ansys private PyPI channel.                                                         |
+-------------------------------------+------------------------------------+---------------------------------------+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``PYPI_TOKEN``                      | Private and internal repositories  | :ref:`Yes (PyPI) <pypi_tokens>`       | **Empty**                                 | This token should be overwritten in each repository after the first public release.                     |
+-------------------------------------+------------------------------------+---------------------------------------+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``PYPI_TESTING_TOKEN``              | Private and internal repositories  | :ref:`Yes (PyPI) <pypi_tokens>`       | *Secret*                                  | Token for testing publication to PyPI.                                                                  |
+-------------------------------------+------------------------------------+---------------------------------------+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``TWINE_TOKEN``                     | Private and internal repositories  | :ref:`Yes (PyPI) <pypi_tokens>`       | **Empty**                                 | This token should be overwritten in each repository after the first public release.                     |
+-------------------------------------+------------------------------------+---------------------------------------+-------------------------------------------+---------------------------------------------------------------------------------------------------------+

To obtain the values of secrets, email `pyansys.core@ansys.com <pyansys.core@ansys.com>`_.

Dependabot secrets
~~~~~~~~~~~~~~~~~~

Dependabot secrets are generally replicas of the `Secrets for GitHub Actions`_. 

+-------------------------------------+---------------------------------------------+----------------------------------------+----------------------------------------------+
| **Secret**                          | **Repository access**                       | **Token**                              | **Description**                              |
+=====================================+=============================================+========================================+==============================================+
| ``BOT_APPLICATION_ID``              | `Secrets for GitHub Actions`_ equivalent                                                                                            |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``BOT_APPLICATION_PRIVATE_KEY``     | Same as `Actions secrets`_ equivalent                                                                                               |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``LICENSE_SERVER``                  | Same as `Actions secrets`_ equivalent                                                                                               |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``MULTIPR_DEPENDABOT``              | Same as `Actions secrets`_ equivalent                                                                                               |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``PYANSYS_PYPI_PRIVATE_PAT``        | Same as `Actions secrets`_ equivalent                                                                                               |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+


.. _organization_tokens:

Organization tokens
-------------------

To facilitate certain tasks such as authentication, the ``ansys`` and ``ansys-internal`` organizations provide developers with certain tokens or personal access tokens (PATs).
These tokens are confidential and for internal use only.
Some of these tokens can be used as GitHub Actions secrets. Others must be requested
by emailing `pyansys.core@ansys.com <pyansys.core@ansys.com>`_.


.. _github_tokens:

GitHub Actions tokens
~~~~~~~~~~~~~~~~~~~~~
GitHub Actions tokens are used within GitHub to provide access and permissions to different tasks and repositories.

Fine-grained tokens
*******************

+----------------------------------------------------------------+----------------------------------------+
|   **TOKEN NAME**                                               | ``dependabot-multi-pr``                |
+================================================================+========================================+
|   **Repository access**                                        |  Public repositories (read-only)       |
+----------------------------------------------------------------+----------------------------------------+
|   **Permissions**                                              |                                        |
+----------------------------------------------------------------+----------------------------------------+
|      **Block another user**                                    |  No access                             |
|       View and manage users who you've blocked.                |                                        |
+----------------------------------------------------------------+----------------------------------------+
|      **Codespaces user secrets**                               |  No access                             |
|       Manage Codespaces user secrets.                          |                                        |
+----------------------------------------------------------------+----------------------------------------+
|      **email addresses**                                       |  No access                             |
|       Manage a user's email addresses.                         |                                        |
+----------------------------------------------------------------+----------------------------------------+
|      **Followers**                                             |  No access                             |
|       A user's followers.                                      |                                        |
+----------------------------------------------------------------+----------------------------------------+
|      **GPG keys**                                              |  No access                             |
|       View and manage a user's GPG keys.                       |                                        |
+----------------------------------------------------------------+----------------------------------------+
|      **gists**                                                 |  No access                             |
|       Create and modify a user's gists and comments.           |                                        |
+----------------------------------------------------------------+----------------------------------------+
|      **Git SSH keys**                                          |  No access                             |
|       Git SSH keys.                                            |                                        |
+----------------------------------------------------------------+----------------------------------------+
|      **Interaction limits**                                    |  No access                             |
|       Interaction limits on repositories.                      |                                        |
+----------------------------------------------------------------+----------------------------------------+
|      **Plan**                                                  |  No access                             |
|       View a user's plan.                                      |                                        |
+----------------------------------------------------------------+----------------------------------------+
|      **Private repository invitations**                        |  No access                             |
|       View a user's invitations to private repositories.       |                                        |
+----------------------------------------------------------------+----------------------------------------+
|      **Profile**                                               |  No access                             |
|       Manage a user's profile settings.                        |                                        |
+----------------------------------------------------------------+----------------------------------------+
|      **SSH signing keys**                                      |  No access                             |
|       View and manage a user's SSH signing keys.               |                                        |
+----------------------------------------------------------------+----------------------------------------+
|      **Starring**                                              |  No access                             |
|       List and manage repositories a user is starring.         |                                        |
+----------------------------------------------------------------+----------------------------------------+
|      **Watching**                                              |  No access                             |
|       List and change repositories a user is subscribed to.    |                                        |
+----------------------------------------------------------------+----------------------------------------+

Classic tokens
**************

.. table:: 
  :class: longtable

  +-------------------------------------------------------------------------------------+------------------------+
  | **Permission**                                                                      | **Status**             |
  +=====================================================================================+========================+
  | ``repo``                                                                            | ✅                     |
  |  Full control of private repositories.                                              |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``repo:status``                                                                     | ❌                     |
  |  Access commit status.                                                              |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``repo_deployment``                                                                 | ❌                     |
  |  Access deployment status.                                                          |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``public_repo``                                                                     | ❌                     |
  |  Access public repositories.                                                        |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``repo:invite``                                                                     | ❌                     |
  |  Access repository invitations.                                                     |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``security_events``                                                                 | ❌                     |
  |  Read and write security events.                                                    |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``workflow``                                                                        | ❌                     |
  |  Update GitHub Action workflows.                                                    |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``write:packages``                                                                  | ❌                     |
  |  Upload packages to GitHub Package Registry.                                        |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``read:packages``                                                                   | ❌                     |
  |  Download packages from GitHub Package Registry.                                    |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``delete:packages``                                                                 | ❌                     |
  |  Delete packages from GitHub Package Registry.                                      |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``admin:org``                                                                       | ❌                     |
  |  Full control of organizations and teams, read, and write organization projects.    |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``write:org``                                                                       | ❌                     |
  |  Read and write org and team membership, read, and write org projects.              |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``read:org``                                                                        | ❌                     |
  |  Read org and team membership, read, org projects.                                  |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``manage_runners:org``                                                              | ❌                     |
  |  Manage org runners and runner groups.                                              |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``admin:public_key``                                                                | ❌                     |
  |  Full control of user public keys.                                                  |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``write:public_key``                                                                | ❌                     |
  |  Write user public keys.                                                            |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``read:public_key``                                                                 | ❌                     |
  |  Read user public keys.                                                             |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``admin:repo_hook``                                                                 | ❌                     |
  |  Full control of repository hooks.                                                  |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``write:repo_hook``                                                                 | ❌                     |
  |  Write repository hooks.                                                            |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``read:repo_hook``                                                                  | ❌                     |
  |  Read repository hooks.                                                             |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``admin:org_hook``                                                                  | ❌                     |
  |  Full control of organization hooks.                                                |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``gist``                                                                            | ❌                     |
  |  Create gists.                                                                      |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``notifications``                                                                   | ❌                     |
  |  Access notifications.                                                              |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``user``                                                                            | ❌                     |
  |  Update **all** user data.                                                          |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``read:user``                                                                       | ❌                     |
  |  Read ALL user profile data.                                                        |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``user:email``                                                                      | ❌                     |
  |  Access user email addresses (read-only).                                           |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``user:follow``                                                                     | ❌                     |
  |  Follow and unfollow users.                                                         |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``delete_repo``                                                                     | ❌                     |
  |  Delete repositories.                                                               |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``write:discussion``                                                                | ❌                     |
  |  Read and write team discussions.                                                   |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``read:discussion``                                                                 | ❌                     |
  |  Read team discussions.                                                             |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``admin:enterprise``                                                                | ❌                     |
  |  Full control of enterprises.                                                       |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``manage_runners:enterprise``                                                       | ❌                     |
  |  Manage enterprise runners and runner groups.                                       |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``manage_billing:enterprise``                                                       | ❌                     |
  |  Read and write enterprise billing data.                                            |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``read:enterprise``                                                                 | ❌                     |
  |  Read enterprise profile data.                                                      |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``audit_log``                                                                       | ❌                     |
  |  Full control of audit log.                                                         |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``read:audit_log``                                                                  | ❌                     |
  |  Read access of audit log.                                                          |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``codespace``                                                                       | ❌                     |
  |  Full control of codespaces.                                                        |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``codespace:secrets``                                                               | ❌                     |
  |  Ability to create, read, update, and delete codespace secrets.                     |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``project``                                                                         | ❌                     |
  |  Full control of projects.                                                          |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``read:project``                                                                    | ❌                     |
  |  Read access of projects.                                                           |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``admin:gpg_key``                                                                   | ❌                     |
  |  Full control of public user GPG keys.                                              |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``write:gpg_key``                                                                   | ❌                     |
  |  Write public user GPG keys.                                                        |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``read:gpg_key``                                                                    | ❌                     |
  |  Read public user GPG keys.                                                         |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``admin:ssh_signing_key``                                                           | ❌                     |
  |  Full control of public user SSH signing keys.                                      |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``write:ssh_signing_key``                                                           | ❌                     |
  |  Write public user SSH signing keys.                                                |                        |
  +-------------------------------------------------------------------------------------+------------------------+
  | ``read:ssh_signing_key``                                                            | ❌                     |
  |  Read public user SSH signing keys.                                                 |                        |
  +-------------------------------------------------------------------------------------+------------------------+

.. _pypi_tokens:

PyPI tokens
~~~~~~~~~~~

.. _pypi_private_token:

``PYANSYS_PYPI_PRIVATE_PAT``
****************************

The ``PYANSYS_PYPI_PRIVATE_PAT`` token is used for authentication when uploading
libraries to the private Ansys PyPI index. This token can be used as the password for
the `twine <https://twine.readthedocs.io/en/stable/>`_ library.

.. _pypi_token:

``PYPI_TOKEN``
**************

The value of the ``PYPI_TOKEN`` token is unique for each repository. 
This token is used for authentication when uploading libraries to the public PyPI index.


``PYPI_TESTING_TOKEN``
**********************

The ``PYPI_TESTING_TOKEN`` token is used for testing uploads to the public PyPI index.


Other tokens
~~~~~~~~~~~~



``TWINE_TOKEN``
***************

The ``TWINE_TOKEN`` token is used for authentication when uploading libraries to PyPI.
Its value might change across repositories.
Depending if the library is uploaded to a public PyPI index or the Ansys private PyPI index, its value matches
:ref:`pypi_private_token` or :ref:`pypi_token`.



.. _organization_bot:

Organization bot
----------------

Because the usage of personal access tokens (PATs) is discouraged, the ``ansys``
and ``ansys-internal`` organizations provide a bot named ``ansys-bot`` to
perform certain tasks that require authentication. For example, this bot provides
for publishing GitHub pages or logging into a Docker image registry.

To use the bot for these tasks, you must use the bot tokens provided through secrets. For
more information, see :ref:`organization_secrets`. For an overview of each token's permissions,
see :ref:`organization_tokens`.

By default, the bot has access to **all repositories** and has the following permissions:

* **Read and write** permission to **actions, code, packages, and pull requests**
* **Read** permission to **metadata and organization secrets**

.. vale off

These permissions can be obtained using a temporal token obtained from
the ``BOT_APPLICATION_PRIVATE_KEY`` token and the
`peter-murray/workflow-application-token-action <https://github.com/peter-murray/workflow-application-token-action>`_.
For an example, see :ref:`deploying_to_another_repo`.

.. vale on