.. _deprecating:

Deprecating a library
=====================

As time passes, some libraries may become outdated or replaced by better alternatives.
When this happens, it is important to deprecate the old library properly to ensure users
are aware of the change and can transition smoothly.

For the PyAnsys ecosystem, follow this specific process for deprecating libraries.
This process helps maintain clarity and consistency across the projects.

Maintainer tasks
----------------

If you are a maintainer of a library that is being deprecated, please follow these steps. As
an illustrative example, the deprecation of `PyAdditive Widgets <https://github.com/ansys/pyadditive-widgets>`_
is used in this guide.

1. **Inform the PyAnsys Core team**: Before proceeding with the deprecation, it is essential to
   inform the PyAnsys Core team. This can be done by sending an email to
   the team at `pyansys.core@ansys.com <pyansys_core_email_>`_. This step ensures that the
   deprecation is communicated effectively and that the team can assist with any necessary
   changes in the PyAnsys ecosystem.

2. **Close all open issues and pull requests**: Before deprecating the library, ensure that all
   open issues and pull requests in the library's repository are closed. This helps to avoid
   confusion and ensures that users are aware that the library is no longer actively maintained.
   You can close issues and pull requests with a comment explaining that the library is being
   deprecated and is no longer be supported.

3. **Create a deprecation issue**: Open an issue in the library's repository to announce the
   deprecation. This issue should explain why the library is being deprecated, what alternatives
   are available, and any relevant timelines. See a template below for the issue content.

   .. warning::

      Make sure to adapt the template to your specific library and situation.

   .. code:: markdown

      ## ⚠️ Project Deprecation Notice

      **This repository is no longer maintained as of [DATE].**

      ### Reason for deprecation
      [Explain briefly why the project is being deprecated — e.g. better alternatives, no time to maintain, outdated use case.]

      ### Alternatives
      If you're looking for a maintained alternative, consider:
      - [Alternative 1](https://...)
      - [Alternative 2](https://...)

      ### What this means
      - No further updates, bug fixes, or pull request reviews
      - Issues will be closed
      - The repository will be archived

      Thank you to everyone who contributed, used, or supported this project!

   This issue serves as a permanent record of the deprecation and provide users with
   necessary information about alternatives.

   Make sure to pin the issue to the top of the repository so that it is easily visible to users.
   This can be done by selecting the "Pin issue" option in the issue's right-side menu, on GitHub.

   See an example at `PyAdditive Widgets deprecation issue`_.

4. **Adapt the README**: Update the library's ``README`` file to reflect the deprecation.
   This should include a clear notice at the top of the ``README``, informing users that the
   library is deprecated. See an example at `PyAdditive Widgets README`_.

5. **(Optional) Add a warning in the code**: If applicable, add a warning in the code itself to inform users
   that the library is deprecated. This can be done using Python's `warnings` module. For example:
   
   .. note::

      Make sure to adapt the URL in the warning message.

   .. code:: python

      # At the top of your main module or package (i.e. src/ansys/<...>/__init__.py)

      import warnings

      warnings.warn(
          "This library is deprecated and will no longer be maintained. "
          "Please consider using alternatives. "
          "For more information check https://github.com/ansys/<repository>/issues/<number>",
          DeprecationWarning,
      )

   See an example at `PyAdditive Widgets deprecation warning`_.

6. **(Optional) Make a last release**: If you carried out step 5, consider making a final release
   of the library that includes the deprecation warning. This ensures that users who install
   the library in the future see the warning immediately.

7. **Archive the repository**: Once the deprecation issue is created and the ``README`` is updated,
   you can archive the repository. This prevents any further changes to the repository and
   signals to users that the library is no longer maintained. To archive a repository, go to the
   repository settings and select "Archive this repository."

These steps ensure that the deprecation process is clear and transparent, allowing users to
transition smoothly to alternatives while maintaining the integrity of the PyAnsys ecosystem.

.. note::

    The deprecation process may vary slightly depending on the specific library and its
    context. However, the core principles should remain consistent across all deprecations.

Core team tasks
---------------

The PyAnsys Core team is responsible for assisting with the deprecation process by:

- Reviewing the deprecation issue to ensure it meets the project's standards.
- Assisting with the above steps, if necessary.
- Remove from PyPI the configuration (PyPI token or trusted publisher) for the library.
- Archive the project on PyPI. See `PyAdditive Widgets PyPI archive`_.
- Removing the library from the `PyAnsys metapackage <metapackage_>`_, automation project
  and the ``pyansys-dev`` repository. See example pull requests:

  - `Metapackage deprecation PR`_
  - `PyAnsys Dev deprecation PR`_
  - `Automation project deprecation PR`_
