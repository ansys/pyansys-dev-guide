Repository protection
=====================

Handling repositories implies handling sensitive information, especially
when configuring workflows to access private servers. Because workflows
acquire Ansys product licenses and handle secrets, it is important to
implement good protection rules.

In the following sections, different safety measures are presented.

General configuration
---------------------

Being an owner or an administrator of a repository gives you access to the
**Settings** menu. To access the general configuration settings for the repository,
select **Settings > General**.

The PyAnsys core team recommends choosing these settings in the **Pull Requests**
section:

* Select **Allow squash merging** to force all commits of a pull request (PR)
  to be condensed into a single commit. This way, if a PR is not successful, it can
  be reverted easily.
* Select **Default to pull request title for squash merge commits** to
  provide a uniform way of naming PRs and merging them to the ``main`` branch.
* Select **Always suggest updating pull request branches** to update
  your branch to the ``main`` branch before merging. (This can be
  enforced as explained later.)
* Select **Automatically delete head branches** for cleanup purposes.
  Once a PR is merged into the ``main`` branch, the PR-related branch is
  deleted so that the repository contains only active branches.


Rulesets
--------

Rulesets can be used to protect branches and tags. These can
be imported and exported from GitHub. The PyAnsys core team provides
template files for the branch protection and tag protection rulesets.

Ruleset files:
:download:`Main branch protection ruleset <../_rulesets/main.json>`
:download:`Branch naming protection ruleset <../_rulesets/branch_naming.json>`
:download:`Tag create <../_rulesets/tag-create.json>`
:download:`Tag delete <../_rulesets/tag-delete.json>`

Please refer to the `GitHub documentation <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/managing-rulesets-for-a-repository#importing-a-ruleset>`_
to learn how to import and export rulesets.

.. note::
    You still need to manually set the rules for the required status checks
    as described below, as they usually are specific to the repository.

Branch protection
-----------------

Branch protection is critical in terms of avoiding malicious code insertion and access
to confidential data. To access the branch protection rulesets for the repository,
select **Settings > Code and automation > Branches**.

Next to **Branch protection rules**, click **Add rule**.

Under **Branch name pattern**, type the name of the branch that you want to protect
(usually ``main``, but you can also protect other branches, such as ``gh-pages``).
Regular expressions (also known as ``regex``) are
accepted. For example, you might want to protect all ``release/`` branches.

The PyAnsys core team recommends setting these rules for the ``main`` branch:

* Select **Require a pull request before merging** so that only owners
  or administrators are able to directly merge to the ``main`` branch.
* Select **Require approvals** to ensure that all PRs are reviewed. (PRs
  created by owners or administrators do not require approval.)
* Select **Require review from Code Owners** so that code owners are forced to review
  all PRs to prevent malicious code from being merged into the ``main`` branch.
  Code owners should be able to identify pieces of code that are not allowed.
  To ensure a code owner is always available to approve and merge PRs, creating an
  **Owners/Admins** team with multiple members is recommended.
* Select **Require status checks to pass before merging** so that only
  code that compiles, passes tests, and is formatted correctly can be merged. This
  is the sole purpose of CI/CD.
* Select **Require branches to be up to date before merging** to ensure
  that all code has been tested and is compatible with the ``main`` branch
  before it can be merged. This is an important concept because someone may have merged
  code into the ``main`` branch that clashes with your code.
* Select **Require status checks to pass before merging** so that the PR
  cannot be merged until all workflow checks are successful. The minimal checks to
  implement are for code style, documentation style, build and unit testing,
  documentation building, and smoke tests.
* Select **Require conversation resolution before merging** to force reviewers to
  go through and resolve all comments. This ensures that all comments are read and
  possibly applied.

For other branches, conventional commits can be enforced by creating a rule
with the following parameters:

- Enforcement status: ``Active``
- Target branches:
  - Include: ``All branches``
  - Exclude: ``main``, ``gh-pages``

- Restrict branch names:
    - Applies to: ``Branch name``
    - Requirement: ``Must match a given regex pattern``
    - Matching pattern: ``^(feat|fix|chore|docs|style|refactor|test|perf|ci|build|dependabot|release|maint)\/.*``
    - Description: ``Branch name must match the conventional commits pattern``

Tag protection
--------------

Protect tags so that only code owners and administrators can create them.
To access the tag protection settings for the repository, select **Settings >
Code and automation > Tags**.

Following the PyAnsys tagging convention, protect the  ``v*`` tag.

Workflow protection
-------------------

Protect workflows in the settings for actions. The focus here is on forks,
which let you make changes to a project without affecting the original repository. To
access the actions settings for the repository, select **Settings > Actions > General**.

Under **Fork pull request workflows from outside collaborators**, the preferred option
is **Require approval for all outside collaborators** for repositories that are to be
released publicly. The minimum option is **Require approval for first-time contributors**.

Because workflows contain sensitive information, it is important to preserve security and control.
The rules for workflows are more flexible. For example, if you have common outside collaborators who
has been contributing for some time, you may want to add them as members of the repository so that
their PR workflows do not have to be accepted every time that they intend to run them.

Internal and private repositories are only available to organization users and repository members,
respectively. Thus, no specific rules for outside collaborators are needed.
