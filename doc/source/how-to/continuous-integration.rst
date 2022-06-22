Using continuous integration
============================
Continuous Integration (CI) is the process of merging new changes into the main
code base while ensuring that these changes are functional and do not break the existing
logic. 

This process is automated as much as possible to alleviate the developer's workload
and ensure a quick development workflow.

Because ``PyAnsys`` projects are hosted in `GitHub <https://github.com>`_, the
`GitHub Actions <https://docs.github.com/en/actions>`_ framework is used.

 
Enabling GitHub actions
-----------------------
By default, ``Actions`` are enabled in new repositories and can be accessed
using the associated :ref:`GitHub Repository Sections`.

If ``Actions`` are not enabled, you can enable them by changing ``Actions
Permissions`` in ``Settings -> Actions -> General``.


Using GitHub actions
--------------------
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


Disabling concurrent workflows
------------------------------

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

- :ref:`Coding Style` workflow
- :ref:`Documentation Style`, :ref:`Building Documentation`, and :ref:`Deploying Documentation` Workflows
- :ref:`Testing` and :ref:`Testing Code Coverage` workflows
- :ref:`Releasing and Publishing` workflow

You should collect all workflows under a common
``ci.yml`` file. For more information, see :ref:`Workflow Examples`.


Parametrizing workflows
-----------------------
It is important to test a ``PyAnsys`` library on different operating systems
using different Python versions:

.. math::

    \text{Num. Workflows} = \text{Num. Operating Systems} \times \text{Num. Python Versions}

The most common operating systems are ``Windows``, ``macOS``, and ``Linux``. For
Python versions, see :ref:`Supporting Python Versions`.

Because having a ``YML`` file for each workflow would be tedious, ``GitHub
Actions`` provides the ``matrix`` parameter inside the ``strategy``. For more
information, see `Using a Matrix for your Jobs
<https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs>`_.

Consider this example of a parametrized workflow example:

.. tabs::

    .. tab:: Workflow File

        .. code-block:: yaml
        
            jobs:
              example_matrix:
                strategy:
                  matrix:
                    python: ['3.7', '3.8', '3.9', '3.10']
                    os: [windows-latest, macos-latest, ubuntu-latest]
                
                steps:
                  - echo 'Running Python ${{ matrix.python }} in ${{ matrix.os }}'

    .. tab:: Actions Log File

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
Workflow examples are provided for checking :ref:`Coding Style`,
:ref:`Documenting`, :ref:`Testing`, and :ref:`Automating The Release Process`.

.. tabs::

    .. tab:: style.yml
        
        .. literalinclude:: code/style.yml     
           :language: yaml

    .. tab:: tests.yml
        
        .. literalinclude:: code/tests.yml     
           :language: yaml


    .. tab:: docs.yml
        
        .. literalinclude:: code/docs.yml     
           :language: yaml


    .. tab:: build.yml
        
        .. literalinclude:: code/build.yml     
           :language: yaml


    .. tab:: release.yml
        
        .. literalinclude:: code/release.yml     
           :language: yaml
