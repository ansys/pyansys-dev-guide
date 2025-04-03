.. _release_publish:

Releasing and publishing
========================

Releasing a new version is a critical procedure. It should be automated as much
as possible to avoid human error.

This sections explains the :ref:`Git` workflow and steps that you must follow
to create a successful release.

.. attention::

   A project must be authorized to be publicly released. For an explanation
   of the process, see :ref:`Project approval and public release`.

Semantic versioning
-------------------

PyAnsys library releases are managed through both automated and manual review
processes.

PyAnsys follows `Semantic Versioning`_, which produces release names in the
form of ``X.Y.Z``, where each letter corresponds to an integer value. This
notation can also be understand as ``MAJOR.MINOR.PATCH``:

* A ``MAJOR`` version is when you make incompatible API changes.
* A ``MINOR`` version is when you add a feature in a backwards-compatible manner.
* A ``PATCH`` version is when you make backwards-compatible bug fixes.

To match the versioning methodology used by the "big three" data science Python
packages, `NumPy`_, `SciPy`_, and `pandas`_, ``MAJOR`` versions of PyAnsys
packages are not released when any incompatible API change is made but rather
when major, globally breaking API changes are made. 

Note that ``0.MINOR.PATCH`` packages are expected to have fluid APIs and should
be solidified at the ``1.MINOR.PATCH`` release. At that point, APIs are expected
to be much more stable.

.. admonition:: PyAnsys library versions should not match product versions.

    PyAnsys libraries are expected to be developed outside the product
    release cycle in a rapid CI/CD manner. Thus, library versions should
    not match product versions. For example, PyMAPDL library (``ansys-mapdl-core``)
    might have the version ``0.59.0`` whereas the product (Ansys Parametric
    Design Language (APDL) might have the version is ``22.2`` (2022 R2).

Branching model
---------------

The branching model for a PyAnsys project enables rapid development of
features without sacrificing stability. The model closely follows the
`trunk-based development <https://trunkbaseddevelopment.com/>`_ approach:

- The ``main`` branch is the primary development branch. All features,
  patches, and other branches should be merged here. While all PRs
  should pass all applicable CI checks, this branch might be functionally
  unstable if changes have introduced unintended side effects or bugs
  that were not caught through unit testing. The version is always suffixed
  with ``.dev0`` in the ``main`` branch.

  .. include:: diag/main_branch.rst

- When a minor release candidate is ready, a new ``release`` branch is
  created from ``main`` with the next incremented minor version
  (for example, ``release/0.2``). This ``release`` branch is thoroughly
  tested. When deemed stable, it is tagged with the version (``0.2.0``
  in this case). Older release branches should not be deleted so that they can be
  patched as needed.

- There is one or more ``release/`` branches based on minor releases (for
  example, ``release/0.2``) that contain a stable version of the code base that
  is also reflected on PyPI. Hotfixes from ``fix/`` branches should be
  integrated both to ``main`` and to these branches. When creating a new patch
  release is necessary, these release branches have their version updated
  and are tagged with a patched :ref:`Semantic versioning` (for example,
  ``0.2.1``).  This triggers CI to push to PyPI so that hotfixes for past
  versions can be rapidly push without having to worry about untested features.

  .. include:: diag/release_branch.rst

New releases
------------

Releasing is the process of creating a version of the software that developers
consider useful for customers or other developers. Releases are usually labeled
with *tags*. These tags are used to quickly identify a release in the version
control system.

.. card:: Release checklist

    | |uncheck| Your main or release branch is up to date.
    | |uncheck| All code and documentation style checks are passing successfully.
    | |uncheck| All tests are passing successfully.
    | |uncheck| All documentation builds successfully.
    | |uncheck| The project builds successfully.

.. dropdown:: Release major and minor versions

    Before performing a release, you must verify that your ``origin main`` branch is up to date
    with these commands:
    
    .. code-block:: text
    
       git checkout main
       git fetch origin main 
       git rebase origin/main
    
    If you encounter any issues when running the preceding commands, solve them before
    continuing with the release. Ensure that your style, tests, and documentation
    checks are passing too.
    
    Create a new branch for the version that you want to release with this command:
    
    .. code-block:: text
    
       git checkout -b release/X.Y
    
    Update ``X`` or ``Y`` version numbers in your project and replace the ``dev0``
    with a ``0``.
    
    Check all locations, including
    :ref:`The \`\`setup.py\`\` file`, :ref:`The \`\`pyproject.toml\`\` file`, and any
    ``__init__.py`` or ``__version__.py`` files that your project may contain.
    
    Stage and commit previous changes with these commands:
    
    .. code-block:: text
    
       git add <files-edited-for-version-number-change>
       git commit -m "Bump version X.Y.0"
    
    Tag the previous commit with this command:
    
    .. code-block:: text
    
       git tag vX.Y.0
    
    Push the commit and the tag it with these commands:
    
    .. code-block:: text
    
       git push -u origin release/X.Y
       git push origin vX.Y.0


.. dropdown:: Release patched versions

    Patched versions allow you to fix issues discovered in published releases by
    cherry-picking these fixes from the ``main`` branch. For more information, see
    the `get-cherry-pick <https://git-scm.com/docs/git-cherry-pick>`_ description
    in the Git documentation.

    Before performing a patch release, you must first identify which
    ``release/X.Y`` branch it belongs to with these commands.
    
    .. code-block:: text
    
       git checkout release/X.Y
       git fetch origin release/X.Y
       git reset --hard origin/release/X.Y
    
    Next, use the following code to cherry-pick the fix commit from the ``main``
    branch, which solves for the bug. Do not merge changes from the
    ``main`` branch into the release branch. Always cherry-pick them:
    
    .. code-block:: text
       
       git cherry-pick <commit hash>
    
    Ensure that your style, tests, and documentation checks are also passing.
    
    Increase by one unit the value of ``Z`` in your project version. Stage and
    amend these new changes with these commands:
    
    .. code-block:: text
    
       git add <files-edited-for-version-number-change>
       git commit --amend -m "Bump version X.Y.Z"
    
    Tag the previous commit with this command:
    
    .. code-block:: text
    
       git tag vX.Y.Z
    
    Push the commit and the tag it using this command:
    
    .. code-block:: text
    
       git push -u origin release/X.Y
       git push origin vX.Y.Z

Artifact publication
--------------------

When a new version is released, some artifacts are provided with it. In Python,
these :ref:`Artifacts` are typically *wheel* and *source* files.
Documentation in the form of HTML and PDF files are also considered artifacts.

.. attention:: 

   Do not distribute artifacts without approval. 

   A project must be authorized to be publicly released. For an explanation
   of the process, see :ref:`Project approval and public release`.

There are three possible places where artifacts can be published:

.. grid:: 3
    
    .. grid-item-card:: :octicon:`lock` Private PyPI
       :link: private-pypi
       :link-type: ref

       This is a private index used to share artifacts across the company
       while making sure that projects remain private.

    .. grid-item-card:: :octicon:`unlock` Public PyPI
       :link: public-pypi
       :link-type: ref

       This is the public PyPI used by the Python community to distribute
       libraries. A project requires Ansys authorization before being
       published in this index.

    .. grid-item-card:: :octicon:`mark-github` GitHub
       :link: github
       :link-type: ref

       This is a section created by GitHub within a project repository where
       artifacts can be published. A project requires Ansys authorization
       before being public in GitHub.


.. _private-pypi:

Private PyPI
~~~~~~~~~~~~

It is sometimes necessary to host and pull packages that are not ready to be
hosted on the public `PyPI`_. For example, if a PyAnsys library requires
auto-generated gRPC interface files from a feature or service that is still
private, this package should be hosted on a private PyPI repository.

ANSYS, Inc. has a private repository at `PyAnsys PyPI`_. You must have the proper
credentials for publishing to this private repository:

+---------------------------------------------+-------------------------------------------------------------------------+
| Credentials                                 | Value                                                                   |
+=============================================+=========================================================================+
| Username                                    | ``__token__``                                                           |
+---------------------------------------------+-------------------------------------------------------------------------+
| Password                                    | ``PYANSYS_PYPI_PRIVATE_PAT``                                            |
+---------------------------------------------+-------------------------------------------------------------------------+
| repository-url                              | ``https://pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi/upload``   |
+---------------------------------------------+-------------------------------------------------------------------------+

The ``PYANSYS_PYPI_PRIVATE_PAT`` is a password in the form of a GitHub secret
that is available only to `PyAnsys projects <PyAnsys_>`_. This secret is
available during the execution of the CI/CD. Its value is never shown or shared
in the log files.

When using `Twine <https://twine.readthedocs.io/>`_ from the command line, you must
add in ``--repository-url`` as an extra option. Otherwise, Twine attempts to upload
the package to the public PyPI repository.

Forked GitHub repositories do not have access to GitHub secrets. This is
designed to protect against pull requests that could potentially scrape
tokens from the PyAnsys CI/CD.

Here's a cross-platform, one-line command for using Twine to upload a package:

.. code::

   python -m twine upload dist/* --repository-url https://pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi/upload -u __token__ -p <TOKEN-REDACTED>

Replace ``<TOKEN-REDACTED>`` with the private PyPI token.

.. dropdown:: Use GitHub Actions

    The following code lets you publish Python :ref:`Artifacts` in
    the ``dist`` directory to the private PyPI. This code is expected to be included when you
    :ref:`Use GitHub Actions`:
    
    .. code-block:: yaml
    
        release-pypi-private:
          name: "Release to private PyPI"
          runs-on: ubuntu-latest
          if: github.event_name == 'push' && contains(github.ref, 'refs/tags')
          steps:
            - uses: ansys/actions/release-pypi-private@v8
              with:
                library-name: "ansys-<product>-<library>"
                twine-username: "__token__"
                twine-token: ${{ secrets.PYANSYS_PYPI_PRIVATE_PAT }}


.. dropdown:: Use the command line

    Alternatively, instead of command-line tool arguments for Twine, you can use environment variables:
    
    .. tab-set::
    
        .. tab-item:: Windows
    
            .. tab-set::
    
                .. tab-item:: CMD
    
                    .. code-block:: text
    
                        set TWINE_USERNAME=__token__
                        set TWINE_PASSWORD=<PYANSYS_PYPI_PRIVATE_PAT>
                        set TWINE_REPOSITORY_URL=https://pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi/upload
    
                .. tab-item:: PowerShell
    
                    .. code-block:: text
    
                        $env:TWINE_USERNAME=__token__
                        $env:TWINE_PASSWORD=<PYANSYS_PYPI_PRIVATE_PAT>
                        $env:TWINE_REPOSITORY_URL=https://pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi/upload
    
        .. tab-item:: macOS
    
            .. code-block:: text
    
                export TWINE_USERNAME=__token__
                export TWINE_PASSWORD=<PYANSYS_PYPI_PRIVATE_PAT>
                export TWINE_REPOSITORY_URL="https://pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi/upload"
    
        .. tab-item:: Linux/UNIX
    
            .. code-block:: text
    
                export TWINE_USERNAME=__token__
                export TWINE_PASSWORD=<PYANSYS_PYPI_PRIVATE_PAT>
                export TWINE_REPOSITORY_URL="https://pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi/upload"
    
    
    Finally, run this command:
    
    .. code-block:: text
    
       python -m twine upload dist/*

.. _public-pypi:

Public PyPI
~~~~~~~~~~~

Publishing :ref:`Artifacts` to `PyPI`_ is the way of distributing :ref:`Python
libraries`. Before being publicly released, projects must follow the process
:ref:`Project approval and public release` to obtain public release
authorization. Once authorized, contact the
`PyAnsys Core team <pyansys_core_email_>`_ to get support during the first
release of the project.

Publishing to `PyPI`_ can be performed following the 
`Trusted Publisher <PyPI Trusted Publisher_>`_ approach or the
`API token <PyPI API token_>`_ approach. When possible, it is recommended
to use the Trusted Publisher as it provides enhanced security and simplifies
the management of authentication credentials. Existing repositories
currently using the API Token approach are encouraged to transition to the
Trusted Publisher approach to benefit from its security and management
improvements.

Publish with trusted publisher
******************************

Publishing with `Trusted Publisher <PyPI Trusted Publisher_>`_ requires an
initial setup to configure OIDC trust between PyPI and Github. This action is
performed by the `PyAnsy core team <pyansys_core_email_>`_ which adds your
project to the list of authorized repositories to release as a Trusted
Publisher.

It is recommended to create en environment in your Github repository to manage
deployments. Environments provide a way to configure deployment-specific
setting and ensure that sensitive operations are performed in a controller
manner. For more information, see the
`Environment documentation <Github environment documentation_>`_. Contact the
`PyAnsys Core team <pyansys_core_email_>`_  in case of doubts.

.. dropdown:: Use GitHub Actions

    The following code lets you publish any Python :ref:`Artifacts` contained in
    the ``dist`` directory to the public PyPI. It is expected to be included when you
    :ref:`Use GitHub Actions`.
    
    .. code-block:: yaml

        release-pypi-public:
          name: Release project to public PyPI
          runs-on: ubuntu-latest
          if: ${{ github.event_name == 'push' && contains(github.ref, 'refs/tags') }}
          # Specifying a GitHub environment is optional, but strongly encouraged
          environment: release
          permissions:
            id-token: write
            contents: write
          steps:
            - uses: ansys/actions/release-pypi-public@v8
              with:
                library-name: "ansys-<product>-<library>"
                use-trusted-publisher: true

Publish with API token
**********************

Publishing with `API token <PyPI API token_>`_ requires a username and a
password:

+-----------------------------------------------+----------------+
| **Credentials for publishing to public PyPI** | **Value**      |
+===============================================+================+
| Username                                      | ``__token__``  |
+-----------------------------------------------+----------------+
| Password                                      | ``PYPI_TOKEN`` |
+-----------------------------------------------+----------------+

The ``PYPI_TOKEN`` is a password in the form of a GitHub secret. This secret is
unique to each project. It can only be obtained after the first release to the
public PyPI. The `PyAnsys Core team <pyansys_core_email_>`_ enables the custom
``PYPI_TOKEN`` once your project has been successfully released for the first
time. For future releases, everything is automated.

Here's a cross-platform, one-line command for using Twine to download a package:

.. code::

   python -m pip install <PACKAGE-NAME> --index-url <TOKEN-REDACTED>@pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi/simple/

Replace ``<PACKAGE-NAME>`` and ``<TOKEN-REDACTED>`` with the package name and private PyPI token respectively.

.. dropdown:: Use GitHub Actions

    The following code lets you publish any Python :ref:`Artifacts` contained in
    the ``dist`` directory to the public PyPI. It is expected to be included when you
    :ref:`Use GitHub Actions`.
    
    .. code-block:: yaml
    
        release-pypi-public:
          name: "Release to public PyPI"
          runs-on: ubuntu-latest
          if: github.event_name == 'push' && contains(github.ref, 'refs/tags')
          steps:
            - uses: ansys/actions/release-pypi-public@v8
              with:
                library-name: "ansys-<product>-<library>"
                twine-username: "__token__"
                twine-token: ${{ secrets.PYPI_TOKEN }}

.. _GitHub_releasing:

GitHub
~~~~~~

You can publish :ref:`Artifacts` to GitHub, which makes them available in
the ``https://github.com/ansys/project-name/releases`` section. The
visibility of these artifacts follows the one in the repository. Visibility can
be private, internal, or public.

For enabling public visibility of a repository, follow the process explained in
:ref:`Project approval and public release`.

.. dropdown:: Use GitHub Actions

    The following code lets you publish any Python :ref:`Artifacts` contained in
    the ``dist`` directory to the GitHub release created. It is expected to be included
    when you :ref:`Use GitHub Actions`:
    
    .. code-block:: yaml
    
        release-github:
          name: "Release to GitHub"
          runs-on: ubuntu-latest
          if: github.event_name == 'push' && contains(github.ref, 'refs/tags')
          steps:
            - uses: ansys/actions/release-github@v8
              with:
                library-name: "ansys-<product>-<library>"

.. _artifact_download:

Artifact download
-----------------

You can download artifacts from the Ansys private PyPI, public PyPI, and GitHub. 

.. dropdown:: Download artifacts from the Ansys private PyPI

    Request the value of the ``PYANSYS_PYPI_PRIVATE_READ_PAT`` token by sending an
    email to the `pyansys.core@ansys.com <pyansys.core@ansys.com>`_ email.

    Create an environment variable named ``PYANSYS_PYPI_PRIVATE_READ_PAT`` in your
    local machine an assign it the value of the token.

    .. warning::
       Take care to always use the ``--index-url`` switch rather than the
       ``--extra-index-url`` switch. As noted in `pip Documentation`_, the
       ``--index-url`` switch changes the Python Package Index, which forces ``pip``
       to use only packages from that package index.
    
       The Ansys package index uses PyPI upstream. This prevents other users from being able to
       inject packages from PyPI that would supersede Ansys packages, even if they
       are of a higher version.
    
       This is not the case if you use ``--extra-index-url``, which adds to rather
       than replaces the default package index. For security, do not use
       ``--extra-index-url``.

    .. tab-set::
    
        .. tab-item:: Windows
    
            .. tab-set::
    
                .. tab-item:: CMD
    
                    .. code-block:: bat
    
                        set PYANSYS_PYPI_PRIVATE_READ_PAT=<REDACTED>
                        set INDEX_URL=https://%PYANSYS_PYPI_PRIVATE_READ_PAT%@pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi/simple/
                        python -m pip install ansys-<product/tool>-<library> --index-url %INDEX_URL% --no-dependencies
    
                .. tab-item:: PowerShell
    
                    .. code-block:: powershell
    
                        $env:INDEX_URL="https://$env:PYANSYS_PYPI_PRIVATE_READ_PAT@pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi/simple/"
                        python -m pip install ansys-<product/tool>-<library> --index-url $env:INDEX_URL --no-dependencies
    
        .. tab-item:: macOS
    
            .. code-block:: text
    
                export INDEX_URL="https://$PYANSYS_PYPI_PRIVATE_READ_PAT@pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi/simple/"
    
                python -m pip install ansys-<product/tool>-<library> \
                --index-url $INDEX_URL \
                --no-dependencies
    
        .. tab-item:: Linux/UNIX
    
            .. code-block:: text
    
                export INDEX_URL="https://$PYANSYS_PYPI_PRIVATE_READ_PAT@pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi/simple/"
    
                python -m pip install ansys-<product/tool>-<library> \
                --index-url $INDEX_URL \
                --no-dependencies

.. dropdown:: Download artifacts from the public PyPI

    Downloading artifacts from the public PyPI can be done by using ``pip``:

    .. code-block:: bash

        python -m pip install <package-name>

.. dropdown:: Download artifacts from GitHub

    Downloading artifacts from GitHub can be done by checking the
    ``https://github.com/ansys/project-name/releases`` section.

    Note that if you download the wheel of a Python package, you must manually install
    it with a command like this:
    
    .. code-block:: bash

        python -m pip install path/to/package/wheel.whl



.. |check| raw:: html

    <input checked=""  type="checkbox">

.. |check_| raw:: html

    <input checked=""  disabled="" type="checkbox">

.. |uncheck| raw:: html

    <input type="checkbox">

.. |uncheck_| raw:: html

    <input disabled="" type="checkbox">
