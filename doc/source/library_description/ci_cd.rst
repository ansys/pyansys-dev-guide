.. _ci_cd:

CI/CD
#####
CI/CD (continuous integration/continuous delivery) is 
achieved using either public `Azure DevOps
<https://azure.microsoft.com/en-us/services/devops/>`_ or 
`GitHub Workflow Actions <https://github.com/features/actions>`_ 
for unit testing, release builds, and documentation builds. 
The selected method should also be used for branch protection. 
For more information, see :ref:`repository_management`.

Here are some good examples:

- `PyAnsys Sphinx documentation theme action <https://github.com/pyansys/pyansys-sphinx-theme/blob/main/.github/workflows/ci-build.yml>`_:
  Generates Ansys Python package documentation using the `PyAnsys Sphinx theme <https://sphinxdocs.pyansys.com/>`__.  
- `MAPDL documentation action <https://github.com/pyansys/pymapdl/blob/main/.github/workflows/ci-build.yml>`_: 
  Generates MAPDL documentation using product containers.
- `PyAEDT unit testing action <https://github.com/pyansys/PyAEDT/blob/main/.github/workflows/unit_tests.yml>`_: 
  Runs unit testing using an application preinstalled on a self-hosted agent.
- `MAPDL Azure DevOps action <https://github.com/pyansys/pymapdl/blob/main/.ci/azure-pipelines.yml>`_:
  Uses a containerized application to run unit testing for an Azure pipeline.
- `DPF-Core Azure DevOps action <https://github.com/pyansys/DPF-Core/blob/master/.ci/azure-pipelines.yml>`_:
  Uses a universal package to run unit testing.
