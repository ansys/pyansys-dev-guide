Using Continuous Integration
============================
Continuous Integration (CI) is the process of merging new changes into the main
code-base while making sure these are functional and do not break the existing
logic. 

This process is automated as much as possible to alleviate developer's workload
and ensuring a quick development workflow.

Since ``PyAnsys`` projects are hosted in `GitHub <https://github.com>`_, the
`GitHub Actions <https://docs.github.com/en/actions>`_ framework is used.

 
Enabling GitHub Actions
-----------------------
By default, ``Actions`` are enabled in new repositories and can be accessed
using the associated :ref:`GitHub Repository Sections`.

In case ``Actions`` are not enabled, you can enable those by changing ``Actions
Permissions`` in ``Settings -> Actions -> General``.


Using GitHub Actions
--------------------
Actions to be executed in the CI process must be declared in a ``YML`` and
stored in the ``.github/workflows/`` directory. Although each action is
different, they all have a common structure:

- A ``name`` identifying the action.
- A collection of ``triggering events`` which run the action when required.
- A collection of ``jobs`` with different steps to be followed during the CI process. 

.. code-block:: yaml

    name: <Name of the action>
    
    on:
      <Trigering events and conditions>

    jobs:
      <All jobs must be defined below this line>


Required Workflows
------------------
The following workflows are required for any ``PyAnsys`` project:

- :ref:`Coding Style` workflow.
- :ref:`Documentation Style`, :ref:`Building Documentation`, and :ref:`Deploying Documentation` Workflows.
- :ref:`Testing` and :ref:`Testing Code Coverage` workflows.
- :ref:`Releasing and Publishing` workflow.

It is recommended that all these workflows are collected under a common
``ci.yml`` file. Visit :ref:`Workflow Examples` for a quick reference


Parametrizing Workflows
-----------------------
It is convenient to test a ``PyAnsys`` library in different operating systems
and Python versions. Notice that, this leads to:

.. math::

    \text{Num. Workflows} = \text{Num. Operating Systems} \times \text{Num. Python Versions}

The most common operating systems are ``Windows``, ``macOS``, and ``Linux``. For
Python version, visit :ref:`Supporting Python Versions`.

Since having a ``YML`` file per workflow would be a tedious task, ``GitHub
Actions`` provides the ``matrix`` parameter inside the ``strategy``, see `Using
a Matrix for your Jobs
<https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs>`_

As an example of usage, consider the following workflow:

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


Workflow Examples
-----------------
Workflow examples are provided for checking :ref:`Coding Style`,
:ref:`Documenting`, :ref:`Testing`, :ref:`Automating Release Process`.

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
