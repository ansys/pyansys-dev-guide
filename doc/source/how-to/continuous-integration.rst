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

Disable concurrent workflows
----------------------------

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
- :ref:`Documentation building <Build documentation>`
- :ref:`Documentation deployment <Deploy documentation>`
- :ref:`Testing`
- :ref:`Test code coverage`
- :ref:`release_publish`

You should collect all workflows in a common ``ci.yml`` file. For more information,
see :ref:`Workflow examples`.

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
                    python: ['3.10', '3.11', '3.12', '3.13']
                    os: [windows-latest, macos-latest, ubuntu-latest]
                
                steps:
                  - echo "Running Python ${{ matrix.python }} in ${{ matrix.os }}"

    .. tab-item:: Actions log file

        .. code-block:: text

            Running Python 3.10 in windows-latest
            Running Python 3.11 in windows-latest
            Running Python 3.12 in windows-latest
            Running Python 3.13 in windows-latest
            Running Python 3.10 in macos-latest
            Running Python 3.11 in macos-latest
            Running Python 3.12 in macos-latest
            Running Python 3.13 in macos-latest
            Running Python 3.10 in ubuntu-latest
            Running Python 3.11 in ubuntu-latest
            Running Python 3.12 in ubuntu-latest
            Running Python 3.13 in ubuntu-latest

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
