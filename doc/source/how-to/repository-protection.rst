Repository protection
=====================

Handling repositories also implies handling sensitive information, especially
when looking into workflows. Access to private servers to acquire Ansys product
licenses, secrets handling and so on. Thus, it is important that the PyAnsys
libraries have good protection rules implemented.

In the following sections, different safety measures are presented.

General configuration
---------------------

Being an owner/admin of a repository gives you access to the ``Settings`` menu.
One accesses the *General configuration* of the repository by:

    ``Repository`` >> ``Settings`` >> ``General``

The PyAnsys team recommends the following measures in the **Pull Requests** (PRs) section:

* **Only allow for** ``Squash merging``: this option forces all commits of a PR
  to be condensed into a single commit. That way, in case a PR was not successful
  for some reason, or wants to be reverted, it is easier to just revert that commit.
* **Enable the** ``Default to PR title for squash merge commits`` **checkbox**:
  this provides a uniform way of naming PRs and merging them to the main branch.
* **Enable the** ``Always suggest updating pull request branches`` **checkbox**:
  though this can be enforced (as it is explained in upcoming sections), it is
  recommended to always have your branch updated to the ``main`` branch before merging.
* **Enable the** ``Automatically delete head branches`` **checkbox**: this is more
  intended for cleaning purposes. Once a PR is merged into the ``main`` branch, the
  PR-related branch should be deleted so that only active branches are available in
  the repository.

Branch protection
-----------------

Branch protection is critical in terms of avoiding malicious code insertion and access
to confidential data. If one accesses:

    ``Repository`` >> ``Settings`` >> ``Code and automation`` >> ``Branches``

You are presented with the Branch protection menu. On the ``Branch protection
rules`` please click on the ``Add rule`` button.

On the ``Branch name pattern`` box, one should include the name of the branch
to be protected (usually ``main``, but one could also protect other branches,
such as ``gh-pages``). Regular expressions (also known as ``regex``) are also
accepted (for example, if protection on all ``release/*`` branches is wanted).

The PyAnsys team recommends to set the following rules for the ``main`` branch:

* **Enable the** ``Require a pull request before merging`` **checkbox**: that way,
  no one (except for owners/admins) should be able to directly merge to ``main``.
* **Enable the** ``Require approvals`` **checkbox**: this ensures
  that all PRs are reviewed and nobody goes *riding solo* (again, except for owners).
* **Enable the** ``Require review from Code Owners`` **checkbox**: this is intended for
  workflow protection as well. That way, it is ensured that no malicious code is
  merged into the main branch. Code owners should be capable of identifying pieces
  of code which should not be allowed, though it forces them to review all PRs.
* **It is recommended to create an Owners/Admins team**: this team should contain
  multiple members, so that if somebody is not available, others can still approve
  and merge.
* **Enable the** ``Require status checks to pass before merging`` **checkbox**: this
  is the sole purpose of CI/CD. Only code which compiles, passes tests, is formatted
  accordingly etc. should be allowed to merge.
* **Enable the** ``Require branches to be up to date before merging`` **checkbox**:  this
  is an important concept, since sometimes, somebody may have merged into ``main`` a
  certain piece of code which clashes with your own developments. By activating this,
  it is ensured that all code which is merged has been tested and is compatible with
  the current ``main`` branch.
* **Enable the** ``Status Checks required`` **checkbox**: whenever possible, all workflow
  stages should be included, but at least: ``Style``, ``Documentation
  Style Check``, ``Build and Unit testing``, ``Documentation build``, and ``Smoke tests``
  should be activated.
* **Enable the** ``Require conversation resolution before merging`` **checkbox**:
  this forces assignees to actually go through all comments. It is just a safety
  measure so that at least any comment left by reviewers is read (and hopefully applied).


Tag protection
--------------

Tags should also be protected, so that only code owners/admins can create them. This can
be done by accessing:

    ``Repository`` >> ``Settings`` >> ``Tags``

Once inside, and following the PyAnsys tagging convention, the following tags should be
protected:

    ``v*``

Workflow protection
-------------------

Finally, workflows can also be protected.

    ``Repository`` >> ``Settings`` >> ``Actions`` >> ``General``

Once inside, focus should be set on the ``Fork pull request workflows from outside collaborators``.
In this case, the PyAnsys team suggests the following:

* **Enable the** ``Require approval for all outside collaborators`` **checkbox when going public**.
* **Enable the** ``Require approval for first-time contributors`` **while still internal/private**.

Workflows contain sensitive information and it is important to preserve security and control over it.
However, these rules are more flexible. For example, if you have a common outside collaborator, which
has been contributing for a time doing you may consider adding it as a member/collaborator of the
repository so that its PR workflows do not have to be accepted every time he is intending to run it.
