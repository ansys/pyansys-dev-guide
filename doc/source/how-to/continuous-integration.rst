Using continuous integration
============================
Continuous Integration (CI) is the process of merging new changes into the main
code base while ensuring that these changes are functional and do not break the existing
logic. 

This process is automated as much as possible to alleviate the developer's workload
and ensure a quick development workflow.

Because ``PyAnsys`` projects are hosted in `GitHub <https://github.com>`_, the
`GitHub Actions <https://docs.github.com/en/actions>`_ framework is used.

 
Enable GitHub actions
---------------------
By default, ``Actions`` are enabled in new repositories and can be accessed
using the associated :ref:`GitHub repository sections`.

If ``Actions`` are not enabled, you can enable them by changing ``Actions
Permissions`` in ``Settings -> Actions -> General``.


Use GitHub actions
------------------
Actions to be executed in the CI process must be declared in a ``YML`` and
stored in the ``.github/workflows/`` directory. Although each action is
different, they all have a common structure:

- A ``name`` identifying the action.
- A collection of ``triggering events`` that run the action when required.
- A collection of ``concurrent`` workflows conditions to, for example, avoid running
  several workflows for the same branch. (Multiple consecutive pushes could lead to
  multiple ongoing workflows when you want only the last push to run).
- A collection of ``jobs`` with different steps to follow during the CI process. 

.. code-block:: yaml

    name: <Name of the action>
    
    on:
      <Trigering events and conditions>

    concurrency:
      <Avoid concurrent workflows to be run>

    jobs:
      <All jobs must be defined below this line>


Disable concurrent workflows
----------------------------

Handling hardware resources is a big deal, especially when running with self-hosted agents.
Also, if you are using public GitHub hardware for running your workflows, you should try to
care about the environment and sustainability.

Disabling concurrent CI workflows is a good way to do so. For example, imagine the following situation:

* You push some changes to your branch.
* The CI workflow kicks in and starts executing the different stages.
* You suddenly realize that there is a typo/file missing.
* You push the new commit to your PR.
* A new CI workflow kicks in and starts running.

At this moment, you probably have two parallel workflows running at the same time,
though you are only interested in the results from the last one.

One way to solve this is manually cancelling the oldest workflow. However, it is also possible to
automatically cancel pre-existing workflows for a certain branch/PR. To do so, prior to the
``jobs`` section, you should add the following lines to your workflow:

.. code-block:: yaml

  concurrency:
    group: ${{ github.workflow }}-${{ github.ref }}
    cancel-in-progress: true


Required workflows
------------------
These workflows are required for any ``PyAnsys`` project:

- :ref:`Coding style` workflow
- :ref:`Documentation style`, :ref:`Build documentation`, and :ref:`Deploying documentation` Workflows
- :ref:`Testing` and :ref:`Test code coverage` workflows
- :ref:`Releasing and publishing` workflow

You should collect all workflows under a common
``ci.yml`` file. For more information, see :ref:`Workflow examples`.


Parametrize workflows
---------------------
It is important to test a ``PyAnsys`` library on different operating systems
using different Python versions:

.. math::

    \text{Num. Workflows} = \text{Num. Operating Systems} \times \text{Num. Python Versions}

The most common operating systems are ``Windows``, ``macOS``, and ``Linux``. For
Python versions, see :ref:`Supporting Python versions`.

Because having a ``YML`` file for each workflow would be tedious, ``GitHub
Actions`` provides the ``matrix`` parameter inside the ``strategy``. For more
information, see `Using a Matrix for your Jobs
<https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs>`_.

Consider this example of a parametrized workflow example:

.. tab-set::

    .. tab-item:: Workflow File

        .. code-block:: yaml
        
            jobs:
              example_matrix:
                strategy:
                  matrix:
                    python: ['3.7', '3.8', '3.9', '3.10']
                    os: [windows-latest, macos-latest, ubuntu-latest]
                
                steps:
                  - echo "Running Python ${{ matrix.python }} in ${{ matrix.os }}"

    .. tab-item:: Actions Log File

        .. code-block:: text

            Running Python 3.7 in windows-latest
            Running Python 3.8 in windows-latest
            Running Python 3.9 in windows-latest
            Running Python 3.10 in windows-latest
            Running Python 3.7 in macos-latest
            Running Python 3.8 in macos-latest
            Running Python 3.9 in macos-latest
            Running Python 3.10 in macos-latest
            Running Python 3.7 in ubuntu-latest
            Running Python 3.8 in ubuntu-latest
            Running Python 3.9 in ubuntu-latest
            Running Python 3.10 in ubuntu-latest


Workflow examples
-----------------
Workflow examples are provided for checking :ref:`Coding style`,
:ref:`Documenting`, :ref:`Testing`, and :ref:`Releasing and publishing`.

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

  Secrets are encrypted variables that you create in an organization, repository, or repository environment. The secrets that you create are available to use in GitHub Actions workflows. 

  From `GitHub documentation <https://docs.github.com/en/actions/security-guides/encrypted-secrets>`_


You can use secrets to pass sensible data such as passwords, token or IPs to your workflows.

By default, ``Ansys`` and ``Ansys-internal`` organizations provide certain secrets to help you to automatize/unify certain tasks such as release.

Actions secrets
~~~~~~~~~~~~~~~

+-------------------------------------+-------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------+
| **SECRET**                          | **Repository access**               | **Value**                            | **Description**                                                                              |
+=====================================+=====================================+======================================+==============================================================================================+
| ``BOT_APPLICATION_ID``              | All repositories                    | *Secret*                             | Username of bot app                                                                          |
+-------------------------------------+-------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------+
| ``BOT_APPLICATION_PRIVATE_KEY``     | All repositories                    | *Secret*                             | Bot private key (see :ref:`organization_bot`)                                                |
+-------------------------------------+-------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------+
| ``HUGO_THEME_TOKEN``                | All repositories                    | *Secret*                             |                                                                                              |
+-------------------------------------+-------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------+
| ``LICENSE_SERVER``                  | All repositories                    | *Secret*                             | IP address of license server                                                                 |
+-------------------------------------+-------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------+
| ``MULTIPR_DEPENDABOT``              | All repositories                    | Token ``PYANSYS_CI_BOT_TOKEN``       | Token to be passed to bot to allow multiple library updates in one pull request.             |
+-------------------------------------+-------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------+
| ``PYANSYS_CI_BOT_PACKAGE_TOKEN``    | Private and internal repositories   |                                      | Token to publish (write) packages in `ghcr.io <ghcr.io>`_ registry.                          |
+-------------------------------------+-------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------+
| ``PYANSYS_CI_BOT_TOKEN``            | All repositories                    |                                      |                                                                                              |
+-------------------------------------+-------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------+
| ``PYANSYS_PYPI_PRIVATE_PAT``        | All repositories                    |                                      |                                                                                              |
+-------------------------------------+-------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------+
| ``PYPI_TOKEN``                      | All repositories                    |                                      |                                                                                              |
+-------------------------------------+-------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------+
| ``PYPI_TESTING_TOKEN``              | Private and internal repositories   |                                      |                                                                                              |
+-------------------------------------+-------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------+
| ``TWINE_TOKEN``                     | Private and internal repositories   |                                      |                                                                                              |
+-------------------------------------+-------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------+

Dependabot secrets
~~~~~~~~~~~~~~~~~~

These secrets in most of the cases a replica of the `Actions secrets`_. 

+-------------------------------------+---------------------------------------------+----------------------------------------+----------------------------------------------+
| **SECRET**                          | **Repository access**                       | **Token**                              | **Description**                              |
+=====================================+=============================================+========================================+==============================================+
| ``BOT_APPLICATION_ID``              | Same as `Actions secrets`_ equivalent                                                                                               |
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

Organization Tokens
-------------------

To facilitate certain taks such as autentication, ``Ansys`` and ``Ansys-internal`` organizations provide to the developer with certain tokens or personal access tokens (PATs). These tokens are confidential and for internal use only.
Some of these tokens can be used as GitHub secrets, others must be requested to pyansys.core@ansys.com.

GithHub tokens
~~~~~~~~~~~~~~
To be used within GitHub.

+----------------------------------------------------------------+----------------------------------------+
| | **TOKEN NAME**                                               | ``PYANSYS_CI_BOT_TOKEN``               |
+================================================================+========================================+
| | **Repository access**                                        |  Public Repositories (read-only)       |
+----------------------------------------------------------------+----------------------------------------+
| | **Permissions**                                              |                                        |
+----------------------------------------------------------------+----------------------------------------+
| |    **Block another user**                                    |  No access                             |
| |     View and manage users blocked by the user.               |                                        |
+----------------------------------------------------------------+----------------------------------------+
| |    **Codespaces user secrets**                               |  No access                             |
| |     Manage Codespaces user secrets.                          |                                        |
+----------------------------------------------------------------+----------------------------------------+
| |    **Email addresses**                                       |  No access                             |
| |     Manage a user's email addresses.                         |                                        |
+----------------------------------------------------------------+----------------------------------------+
| |    **Followers**                                             |  No access                             |
| |     A user's followers                                       |                                        |
+----------------------------------------------------------------+----------------------------------------+
| |    **GPG keys**                                              |  No access                             |
| |     View and manage a user's GPG keys.                       |                                        |
+----------------------------------------------------------------+----------------------------------------+
| |    **Gists**                                                 |  No access                             |
| |     Create and modify a user's gists and comments.           |                                        |
+----------------------------------------------------------------+----------------------------------------+
| |    **Git SSH keys**                                          |  No access                             |
| |     Git SSH keys                                             |                                        |
+----------------------------------------------------------------+----------------------------------------+
| |    **Interaction limits**                                    |  No access                             |
| |     Interaction limits on repositories                       |                                        |
+----------------------------------------------------------------+----------------------------------------+
| |    **Plan**                                                  |  No access                             |
| |     View a user's plan.                                      |                                        |
+----------------------------------------------------------------+----------------------------------------+
| |    **Private repository invitations**                        |  No access                             |
| |     View a user's invitations to private repositories        |                                        |
+----------------------------------------------------------------+----------------------------------------+
| |    **Profile**                                               |  No access                             |
| |     Manage a user's profile settings.                        |                                        |
+----------------------------------------------------------------+----------------------------------------+
| |    **SSH signing keys**                                      |  No access                             |
| |     View and manage a user's SSH signing keys.               |                                        |
+----------------------------------------------------------------+----------------------------------------+
| |    **Starring**                                              |  No access                             |
| |     List and manage repositories a user is starring.         |                                        |
+----------------------------------------------------------------+----------------------------------------+
| |    **Watching**                                              |  No access                             |
| |     List and change repositories a user is subscribed to.    |                                        |
+----------------------------------------------------------------+----------------------------------------+


PyPI tokens
~~~~~~~~~~~



Other tokens
~~~~~~~~~~~~


``HUGO_THEME_TOKEN``
********************

This token is used to ... # todo: to be added


``TWINE_TOKEN``
***************

This token is used to ... # todo: to be added



.. _organization_bot:

Organization bot
----------------

Because the usage of user personal access tokens (PATs) is discouraged, ``Ansys`` and ``Ansys-internal``
organizations provide with a bot called ``ansys-bot`` to perform certain tasks which requires autentification,
for example github pages publication or docker image registry login.

To use the bot for these tasks, you need to use the bot tokens provided through secrets (see :ref:`organization_secrets`).
To get a better overview of the permissions of each token see :ref:`organization_tokens`.

By default, the bot has access to **all repositories** and has the following permissions:

* **Read and write** access to **actions, code, packages, and pull requests**
* **Read** access to **metadata and organization secrets**

Those permissions can be obtained using a temporal token obtained from the ``BOT_APPLICATION_PRIVATE_KEY`` token
and the `peter-murray/workflow-application-token-action <https://github.com/peter-murray/workflow-application-token-action>`_.
Visit :ref:`deploying_to_another_repo` for a documented example.