.. _development_practices:

Development Practices
=====================

This section explains how development is conducted in PyAnsys
repositories. Please follow the practices outlined here when
contributing directly to PyAnsys.


General Development Procedures
------------------------------

To submit new code to a PyAnsys, first `fork <https://docs.github.com/en/get-started/quickstart/fork-a-repo>`_ 
the repository (for example `PyMAPDL <https://github.com/pyansys/pymapdl>`_)
and then clone the forked repository to your computer. Next, create a new branch based on the
`Branch Naming Conventions Section <#branch-naming-conventions>`__ in
your local repository.

Next, add your new feature and commit it locally. Be sure to commit
often as it is often helpful to revert to past commits, especially if
your change is complex. Also, be sure to test often. See the `Testing
Section <#testing>`__ below for automating testing.

When you are ready to submit your code, create a pull request by
following the steps in `Creating a New Pull Request <#creating-a-new-pull-request>`__.

Be sure to review these topics:

#. `Branching Section <#Branching Model>`__
#. Testing standards.
#. Documentation standards. See :ref:`api_documentation`.
#. Code quality standards. See :ref:`coding_style`.


Guidelines
~~~~~~~~~~

Consider the following general coding paradigms when contributing:

1. Follow the `Zen of Python <https://www.python.org/dev/peps/pep-0020/>`__.
   As silly as the core Python developers are sometimes, there's much to
   be gained by following the basic guidelines listed in PEP 20.
   Without repeating them here, focus on making your additions
   intuitive, novel, and helpful for users.

   When in doubt, ``import this``.

2. **Document it**. Include a docstring for any function, method, or
   class added. Follow the `numpydocs docstring
   <https://numpydoc.readthedocs.io/en/latest/format.html>`_
   guidelines, and always provide an example of simple use cases for
   new features.

3. **Test it**. Because Python is an interperted language, if it's not
   tested, it's probably broken. At the minimum, include unit tests
   for each new feature within the ``tests`` directory. Ensure that
   each new method, class, or function has reasonable (>80%) coverage.

Additionally, do not include any data sets for which a license
is not available or commercial use is prohibited.

Licensing
~~~~~~~~~

All contributed code will be licensed under the MIT License found in
the repository. If you did not write the code yourself, it is your
responsibility to ensure that the existing license is compatible and
included in the contributed files. You must obtain permission from the
original author to relicense the code.

See :ref:`license_file` for more details.


Branching Model
---------------
This project has a branching model that enables rapid development of
features without sacrificing stability and closely follows the 
`Trunk Based Development <https://trunkbaseddevelopment.com/>`_ approach.

Descriptions follow for the main features of the branching model.

- The `main` branch is the main development branch. All features,
  patches, and other branches should be merged here. While all pull
  requests (PRs) should pass all applicable CI (Continuous Integration)
  checks, this branch might be functionally unstable if changes have
  introduced unintended side-effects or bugs that were not caught through
  unit testing.
- There will be one or many `release/` branches based on minor
  releases (for example, `release/0.2`) that contain a stable version
  of the code base that is also reflected on PyPi. Hotfixes from
  `fix/` branches should be merged both to main and to these
  branches. When creating a new patch release is necessary, these
  release branches will have their `__version__.py` updated and be
  tagged with a patched semantic version (for example, `0.2.1`). This
  triggers CI to push to PyPi and allow us to rapidly push hotfixes
  for past versions without having to worry about untested features.
- When a minor release candidate is ready, a new `release` branch will
  be created from `main` with the next incremented minor version
  (for example, `release/0.2`), This `release` branch will be thoroughly
  tested. When deemed stable, it will be tagged with the version (`0.2.0`
  in this case) and merged with `main` if any changes were pushed to it.
  Feature development then continues on `main` and any hotfixes will now
  be merged with this release. Older release branches should not be deleted
  so they can be patched as needed.

.. _release_procedures:

Release Procedures
------------------

Major and Minor
~~~~~~~~~~~~~~~
Procedures follow for major and minor releases.

#. Create a new branch from the `main` branch with name
    `release/MAJOR.MINOR`(for example, `release/0.2`).

#. Locally run all tests as outlined in :ref:`testing` and ensure all
   are passing.

#. Locally test and build the documentation with link checking to make
   sure no links are outdated. Be sure to run ``make clean`` to ensure no
   results are cached.

    .. code::

        cd doc
        make clean  # deletes the sphinx-gallery cache
        make html -b linkcheck

#. After building the documentation, open the local build and examine
   the examples for any obvious issues.

#. Update the version numbers in
   ``ansys/<product>/<library>/_version.py`` and commit it.  Push the
   branch to GitHub and create a new PR for this release that merges
   it to `main`. Development to `main` should be limited while
   effort is focused on the release.

#. The community and Ansys developers must now functionally test the
   new release. It is best to locally install this branch and use it in
   production. Any bugsidentified should have their hotfixes pushed to
   this release branch.

#. When the branch is deemed as stable for public release, the PR ismerged
   to `main` branch, which is then tagged with a `MAJOR.MINOR.0` release.
   The release branch will not be deleted.
   
   Tag the release with:

    .. code::

	git tag v<MAJOR.MINOR.0>
        git push origin --tags

#. Create a list of all changes for the release. It is often helpful
   to see the `GitHub's compare feature`_ differences from
   the last tag and the `main` branch.  Be sure to acknowledge new
   contributors by their GitHub username and place mentions where
   appropriate if a specific contributor is to be thanked for a new
   feature.

#. Place your release notes from step 8 in the release section with GitHub. See
   `GitHub Releases`_

.. _GitHub Releases: https://docs.github.com/en/github/administering-a-repository/releasing-projects-on-github/managing-releases-in-a-repository
.. _GitHub's compare feature: https://github.com/pyansys/pymapdl/compare


Patch Release Steps
~~~~~~~~~~~~~~~~~~~
Patch releases are for critical and important bug fixes that cannot or
should not wait until a minor release. These are the steps for a patch release:

1. Push the necessary bug fixes to the applicable release branch.
   This will generally be the latest release branch (`release/MAJOR.MINOR`).

2. Update ``__version__.py`` with the next patch increment
   (`MAJOR.MINOR.PATCH`), commit it, and open a PR to merge with the
   release branch. This gives the developers and community
   an opportunity to validate and approve the bug fix release.  Any
   additional hotfixes should be outside of this PR.

3. When approved, merge with the release branch, but not `main` as
   there is no reason to increment the version of the `main` branch.
   Then, create a tag from the release branch with the applicable
   version number (see above for the correct steps).

4. If deemed necessary, add a release notes page.


.. _testing:

Testing
-------
<Testing Section>
