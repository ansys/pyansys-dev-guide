.. _development_practices:

Development Practices
=====================
This page explains how PyAnsys development is conducted. When
contributing directly to PyAnsys libraries, use these general 
coding paradigms:

#. Follow the `Zen of Python <https://www.python.org/dev/peps/pep-0020/>`__.
   As silly as core Python developers are sometimes, there's much to be
   gained by following the basic guidelines listed in PEP 20. As suggested
   in these guidelines, focus on making your additions intuitive, novel,
   and helpful for PyAnsys library users. When in doubt, use ``import this``.
   For Ansys code quality standards, see :ref:`coding_style`.

#. Document your contributions. Include a docstring for any added
   function, method, or class, following `numpydocs docstring <https://numpydoc.readthedocs.io/en/latest/format.html>`_
   guidelines and PyAnsys documentation standards <#Documentation Standards>.
   Always provide at least one simple use case for a new feature.

#. Test your contribution. Because Python is an interpreted language, if
   it's not tested, it's probably broken. At the minimum, include a unit
   test for each new feature within the ``tests`` directory. Ensure that
   each new method, class, or function has reasonable (>80%) coverage.
   See `Testing <#Testing>`__ for automating testing.

#. Do not include any datasets for which a license is not available
   or commercial use is prohibited.

#. Review our `Code of Conduct <https://github.com/pyansys/DPF-Core/blob/master/CODE_OF_CONDUCT.md>`_.

Contributing Through GitHub
---------------------------
To submit new code to a PyAnsys Library:

#. `Fork <https://docs.github.com/en/get-started/quickstart/fork-a-repo>`_
   the respective library's GitHub repository and then clone
   the forked repository to your computer. 

#. In your local repository, create a branch. See `Branching Model <#Branching Model>`__.

#. Add your new feature and commit it locally. Be sure to commit
   frequently as the ability to revert to past commits is often helpful,
   especially if your change is complex. 

#. Test often. See `Testing <#Testing>`__ for automating testing.

#. When you are ready to submit your code, create a pull request (PR)
   by following the steps in the next section.

Creating a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~
Once you have tested your branch locally, create a PR and target your
merge to ``main``. This will automatically run CI testing and verify
that your changes will work across all supported platforms.

For code verification, someone from the development team for the PyAnsys library
will review your code to verify that it meets our standards. Once your code
is approved, if you have write permission, you may merge the PR branch. If you
don't have write permission, the reviewer or someone else with write permission
will merge and delete the PR branch.

If your PR branch is a ``fix/`` branch, do not delete it because it may be necessary to
merge your PR branch with the current release branch. See the next section for branch
naming conventions.

.. _branch_naming:

Branch Naming Conventions
~~~~~~~~~~~~~~~~~~~~~~~~~
To streamline development, we have the following requirements for naming
branches. These requirements help core developers know what kind of
changes any given branch is introducing before looking at the code.

-  ``fix/``: any bug fixes, patches, or experimental changes that are
   minor
-  ``feat/``: any changes that introduce a new feature or significant
   addition
-  ``junk/``: for any experimental changes that can be deleted if gone
   stale
-  ``maint/``: for general maintenance of the repository or CI routines
-  ``doc/``: for any changes only pertaining to documentation
-  ``no-ci/``: for low-impact activity that should not trigger the CI
   routines
-  ``testing/``: improvements or changes to testing
-  ``release/``: releases (see below)

Testing
~~~~~~~
When making changes, periodically test locally before creating a PR.
Because the following tests are executed after any commit or PR, we
ask that you perform the following procedure locally to track down
any new issues from your changes.

#. Install requirements for testing:

.. code::

    pip install -r requirements_test.txt

#. Run the primary test suite and generate a coverage report:

.. code::

    pytest -v --cov _unittest

Spelling and Code Style
~~~~~~~~~~~~~~~~~~~~~~~
If you are using Linux or Mac OS, run spelling and coding style checks:

.. code::

    cd <local pyvista root directory>
    pip install -r requirements_style.txt
    make

Misspelled words will be reported. You can add words to be ignored to
the ``ignore_words.txt`` file. For example, for PyMAPDL, this file looks
like this: 

... code::

    codespell ./ "*.pyc,*.txt,*.gif,*.png,*.jpg,*.js,*.html,*.doctree,*.ttf,*.woff,*.woff2,*.eot,*.mp4,*.inv,*.pickle,*.ipynb,flycheck*,./.git/*,./.hypothesis/*,*.yml,./doc/build/*,./doc/images/*,./dist/*,*~,.hypothesis*,./doc/source/examples/*,*cover,*.dat,*.mac,\#*,build,./docker/mapdl/v211,./factory/*,./ansys/mapdl/core/mapdl_functions.py,PKG-INFO" -I "ignore_words.txt"

Documentation
-------------
Documentation for a PyAnsys library is generated from three sources:

- Docstrings from the library's classes, functions, and modules using
  `sphinx.ext.autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_.
- reStructuredText (RST) files from ``doc/``
- Examples from ``examples/``

General usage information and API descriptions should be placed within
``doc/source`` and docstrings. Full examples should be placed in
``examples/``.

Adding a New Example
~~~~~~~~~~~~~~~~~~~~
Examples come in two formats:

- Basic code snippets demonstrating some functionality
- Full-fledged standalone examples meant to be run as individual downloadable scripts

While basic code snippets should be placed in the ``doc/source`` directory, full-fledged
standalone examples must be placed in the ``examples`` directory at the root of the repository.

When adding a standalone example, you add it to an applicable subfolder in the ``examples``
directory. If none of the existing directories match the category of your example, create
a new subfolder with a ``README.txt`` file describing the new category. As these examples
are built using the Sphinx gallery extension, you must follow `Sphinx gallery coding guidelines <https://sphinx-gallery.github.io/stable/index.html>_`.

PyMAPDL provides a self-demonstrating example of how to `add an example reference key <https://mapdldocs.pyansys.com/examples/03-tips-n-tricks/00-example-template.html#ref-how-to-add-an-example-reference-key>`_. 

Documentation Style and Organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Docstrings should follow `numpydocs docstring <https://numpydoc.readthedocs.io/en/latest/format.html>`_
guidelines. Documentation within the ``doc/`` directory use the reStructuredText.
(RST) format. Examples within the ``examples/`` directory should be PEP 8-compliant
and will be compiled dynamically during the build process. Always ensure that
examples run properly locally because they will be verified through the CI performed
via GitHub Actions.

Documentation for the latest stable release of a PyAnsys libary is accessible
from its repository. You can access the latest development version of the
documentation tracking the ``main`` branch by adding the prefix ``dev.`` to
the URL for the latest stable release. For example, the URL for the latest
stable release of the PyAEDT documentation is
`<https://dev.aedtdocs.pyansys.com/>`_, and the URL for the latest development 
version of this documentation is `<https://dev.aedtdocs.pyansys.com/>`_. The
latest development version is kept up-to-date automatically via GitHub actions.

Building the Documentation Locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can build and verify a library's HTML documentation locally by installing
Sphinx and other documentation build dependencies.

#. Optionally install the library in development mode:

.. code::

   pip install -e .

#. Install the build requirements for documentation:

.. code::

   pip install -r requirements_docs.txt


#. If running on Linux/Mac OS, build the documentation:

.. code::

    make -C doc html

Otherwise, if running on Windows, build the documentation:

.. code::

   cd doc
   make.bat html

#. After documentation builds successfully locally, use your
   browser to open the file ``index.html`` in ``doc/_build/html/`` 
   to review it.

Continuous Integration and Continuous Delivery (CI/CD)
------------------------------------------------------

A PyAnsys library uses continuous integration (CI) and continuous delivery (CD)
to automate building, testing, and deployment tasks. The CI pipeline is
deployed on both GitHub Actions and Azure Pipelines and performs the following
tasks:

- Module wheel build
- Core API testing
- Spelling and style verification
- Documentation build

Branching Model
---------------
The branching model for a PyAnsys library enables rapid development of
features without sacrificing stability. The model closely follows the 
`Trunk Based Development <https://trunkbaseddevelopment.com/>`_ approach:

- The `main` branch is the primary development branch. All features,
  patches, and other branches should be merged here. While all PRs
  should pass all applicable CI checks, this branch might be functionally
  unstable if changes have introduced unintended side effects or bugs
  that were not caught through unit testing.
- There will be one or many ``release/`` branches based on minor
  releases (for example, ``release/0.2``) that contain a stable version
  of the code base that is also reflected on PyPI. Hotfixes from
  ``fix/`` branches should be merged both to ``main`` and to these
  branches. When creating a new patch release is necessary, these
  release branches will have their ``__version__.py`` file updated and
  be tagged with a patched semantic version (for example, ``0.2.1``).
  This triggers CI to push to PyPi and allow us to rapidly push hotfixes
  for past versions without having to worry about untested features.
- When a minor release candidate is ready, a new ``release`` branch will
  be created from ``main`` with the next incremented minor version
  (for example, ``release/0.2``). This ``release`` branch will be thoroughly
  tested. When deemed stable, it will be tagged with the version (``0.2.0``
  in this case) and merged with ``main`` if any changes were pushed to it.
  Feature development then continues on ``main`` and any hotfixes will now
  be merged with this release. Older release branches should not be deleted
  so they can be patched as needed.

.. _release_procedures:

Release Procedures
------------------

Major and Minor Release Steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Release procedures follow for major and minor releases.

#. Create a new branch from the ``main`` branch with the name
   ``release/MAJOR.MINOR`` (for example, ``release/0.2``).

#. Locally run all tests as outlined in `Testing <#Testing>`_ and
   ensure that all are passing.

#. Locally test and build the documentation with link checking to
   ensure that no links are outdated.
   
#. Run ``make clean`` to ensure that no results are cached.

    .. code::

        cd doc
        make clean  # deletes the sphinx-gallery cache
        make html -b linkcheck

#. After building the documentation, open the local build and examine
   the examples for any obvious issues.

#. Update the version numbers in
   ``ansys/<product>/<library>/_version.py`` and commit this file.  Push the
   branch to GitHub and create a new PR for this release that merges
   it to ``main``. While effort is focused on the release, development
   to ``main`` should be limited.

#. Wait for the PyAnsys developers and community to functionally test the
   new release. Testors should locally install this branch and use it in
   production. Any bugs that they identify should have their hotfixes pushed to
   this release branch.

   When the branch is deemed as stable for public release, the PR is merged
   to ``main``, which must then be tagged with a ``MAJOR.MINOR.0`` release.
   The release branch will not be deleted.

#. Tag the release:

    .. code::

	     git tag v<MAJOR.MINOR.0>
        git push origin --tags

#. Create a list of all changes for the release. It is often helpful
   to leverage GitHub's compare feature to see the differences from
   the last tag and the ``main`` branch. Be sure to acknowledge new
   contributors by their GitHub usernames and place mentions where
   appropriate if specific contributors are to be thanked for new
   features.

#. Place your release notes from the previous step in ``Releases`` 
   in the GitHub repository. See `GitHub Releases`_.

.. _GitHub Releases: https://docs.github.com/en/github/administering-a-repository/releasing-projects-on-github/managing-releases-in-a-repository
.. _GitHub's compare feature: https://github.com/pyansys/pymapdl/compare


Patch Release Steps
~~~~~~~~~~~~~~~~~~~
Patch releases are for critical and important bug fixes that cannot or
should not wait until a minor release. These are the steps for a patch release:

#. Push the necessary bug fixes to the applicable release branch.
   This will generally be the latest release branch (for example,
   ``release/MAJOR.MINOR``).

#. Update the ``__version__.py`` file with the next patch increment
   (``MAJOR.MINOR.PATCH``), commit it, and open a PR to merge with the
   release branch. This gives the PyAnsys developers and community
   an opportunity to validate and approve the bug fix release. Any
   additional hotfixes should be outside of this PR.

#. When the PR is approved, merge it with the release branch, but not with
   ``main`` as there is no reason to increment the version of the ``main`` branch.

#. Create a tag from the release branch with the applicable version number
   as described in the previous section.

4. If deemed necessary, create and add release notes as described in the
   previous section.
