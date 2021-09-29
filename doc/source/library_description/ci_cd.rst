CI/CD Methods
#############
CI/CD (continuous integration/continuous delivery) is 
achieved using either public `Azure DevOps
<https://azure.microsoft.com/en-us/services/devops/>`_ or public
`GitHub Workflow Actions <https://github.com/features/actions>`_ 
for unit testing, release builds, and documentation builds. 
The selected method should also be used for branch protection. 
For more information, see `Repository Management`.

Here are some good examples:

- The `PyAnsys Sphinx documentation theme action <https://github.com/pyansys/pyansys-sphinx-theme/blob/main/.github/workflows/ci-build.yml>`_ 
  generates Ansys Python package documentation using the `PyAnsys Sphinx theme <https://sphinxdocs.pyansys.com/>`__.  
- The `MAPDL documentation action <https://github.com/pyansys/pymapdl/blob/main/.github/workflows/ci-build.yml>`_ 
  generates MAPDL documentation using product containers.
- The `PyAEDT unit testing action <https://github.com/pyansys/PyAEDT/blob/main/.github/workflows/unit_tests.yml>`_ 
  runs unit testing using an application preinstalled on a self-hosted agent.
- The `MAPDL Azure DevOps action <https://github.com/pyansys/pymapdl/blob/main/.ci/azure-pipelines.yml>`_ 
  uses a containerized application to run unit testing for an Azure pipeline.
- The `DPF-Core Azure DevOps action <https://github.com/pyansys/DPF-Core/blob/master/.ci/azure-pipelines.yml>`_ 
  uses a universal package to run unit testing.
