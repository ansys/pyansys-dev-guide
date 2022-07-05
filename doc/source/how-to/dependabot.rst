Dependabot
==========

Dependabot is a built-in tool which allows to keep project dependencies updated,
by informing of latest releases of the packages being used.

The ``dependabot.yml`` file
---------------------------

Dependabot version updates are performed by checking a ``dependabot.yml``
configuration file into your repository. In this file, one should specify the
location of the project's requirement files, so that Dependabot knows where
to look.

.. code:: yaml

    # To get started with Dependabot version updates, you'll need to specify which
    # package ecosystems to update and where the package manifests are located.
    # Please see the documentation for all configuration options:
    # https://docs.github.com/github/administering-a-repository/configuration-options-for-dependency-updates

    version: 2
    updates:
    - package-ecosystem: "pip" # See documentation for possible values
        directory: "/requirements" # Location of package manifests
        schedule:
            interval: "daily"

This file should be located in the ``.github`` folder of your repository for
GitHub to detect it automatically. As it can be seen there are several main options:

* **package-ecosystem**: which lets Dependabot know what your package manager is.
  PyAnsys projects typically use ``pip``, but another example could be ``conda``.
* **directory**: which lets Dependabot where your requirement files are located.
  PyAnsys projects typically contain all their requirements inside a ``requirements``
  folder. Other directories could be provided.
* **schedule**: which lets Dependabot know the frequency at which its subroutines
  should be performed for checking for updates.

.. caution::

    At the moment, Dependabot only works for requirement files. Support for ``setup.py``
    and ``pyproject.toml`` files is not yet enabled, as it can be seen in this issue
    opened some time ago: `Standard Python support <https://github.com/dependabot/dependabot-core/issues/3290>`_.
    While this feature is still coming, remember to update whatever dependencies are
    defined in other package configuration files **by hand**.

Dependabot updates
------------------

Dependabot determines (using semantic versioning) whether a requirement should
be updated due to the existence of a newer version. When Dependabot identifies
an outdated dependency, it raises a Pull Request to update these requirement
files.

Dependabot allows for two different types of updates:

* **Dependabot security updates**: automated pull requests that help update
  dependencies with known vulnerabilities.
* **Dependabot version updates**: automated pull requests that keep dependencies updated,
  even when they don’t have any vulnerabilities. To check the status of version updates,
  navigate to the ``Insights`` tab of your repository, then ``Dependency Graph``,
  and ``Dependabot``.


.. caution::

    Dependabot only works for *pinned-down* versions of requirements (or, at most, versions
    with an *upper-limits* requirement such as ``pyvista <= 0.34.0``). However, this is not
    a best practice for *run-time* dependencies (that is, the usage of a package should support
    the oldest available version, if possible). Thus, it is only recommended to fully pin
    **documentation** and **testing** requirements (that is, using ``==``). Having the latest
    dependencies available in your requirements **testing**  files allows to test the
    *latest* packages against your library.

Dependabot version updates
~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to enable version updates for your repository, please go to
`Enabling Dependabot version updates
<https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#enabling-dependabot-version-updates>`_.

Dependabot security updates
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dependabot security updates make it easier for you to fix vulnerable dependencies in your
repository. If you enable this feature, when a Dependabot alert is raised for a vulnerable
dependency in the dependency graph of your repository, Dependabot automatically tries to fix it.

In order to enable security updates and notifications for your repository, please go to
`Enabling or disabling Dependabot security updates for an individual repository
<https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#enabling-or-disabling-dependabot-security-updates-for-an-individual-repository>`_.