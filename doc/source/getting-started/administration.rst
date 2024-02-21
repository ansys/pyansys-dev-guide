Project approval and public release
===================================

Most of the projects in PyAnsys expose the functionality of Ansys
products. Due to intellectual property reasons, the public release of a PyAnsys
library must go through a project approval process.

First steps
-----------

To trigger the public release process, project leads must fill in this form:

* `Release request workflow initiation form <https://ansys.typeform.com/ReleaseSupport?typeform-source=gz2idtcjsw2.typeform.com>`_

The form lets the different parties involved in the public release process know that
there is a request to release a project. If your intent is to release an Ansys Open
Source project, then continue to the next section.

Approval process
----------------

The approval process is divided into three parts:

.. grid:: 3
    
    .. grid-item-card:: :octicon:`file-badge` Managerial
       :link: managerial
       :link-type: ref

       Ensures that direct managers, general managers, and the chief technology
       officer are aware of the project and approve it.

    .. grid-item-card:: :octicon:`law` Legal
       :link: legal
       :link-type: ref

       Ensures that the project adheres to a legal framework that protects
       Ansys intellectual property.

    .. grid-item-card:: :octicon:`gear` Technical
       :link: technical
       :link-type: ref

       Ensures that the project complies with Ansys software guidelines and best practices.


.. important::

    An approval from each of these three parts is required to release a project to the public.

    Once approved, a project can be published to the :ref:`Public PyPI`.


When releasing a project to the public, you should:

* Coordinate with the product line development team, if applicable.
* Maintain the project by means of fixing bugs and providing support for new releases.
* Uphold Ansys' reputation in the open source community.

Once all three approvals have been awarded, project leads must complete
the next form:

* `OSS approval request form <https://ansys.typeform.com/ReleaseSupport?typeform-source=gz2idtcjsw2.typeform.com/OSSapproval>`_

This form serves as a final checklist to verify that all approvals have been processed
and to formalize the OSS approval process as a final record. You can find frequently
asked questions in :ref:`Questions asked in the OSS approval request form`.

Managerial
^^^^^^^^^^

The managerial part of the approval process ensures that the direct manager,
general managers, vice presidents, or the chief technology officer are aware of
the project's existence and status.

A project must be classified into one of these categories, determining the
number of administrative reviews and approvals needed:

.. grid:: 3
    
    .. grid-item-card:: :octicon:`repo` Documentation projects

        Documentation projects must have direct manager approval, legal review, and
        documentation proofing. No source code other than documentation files
        is allowed.

    .. grid-item-card:: :octicon:`tools` Tool projects

        Tool projects require direct manager and business unit's general
        manager approval. No product source code is allowed.

    .. grid-item-card:: :octicon:`container` Library projects

        Library projects interfacing and wrapping any Ansys products require
        approval from the direct manager, product line, and the chief
        technology officer. No product source code is allowed.

Legal
^^^^^

Legal review approval ensures that the entire project complies with Ansys'
legal policies.

Start by completing the legal review request form for open sourcing the code:

.. button-link:: https://github.com/ansys-internal/oss-approval-tracklist/issues/new?assignees=MaxJPRey%2C+RobPasMue%2C+jorgepiloto%2C+&labels=&projects=&template=oss_final_signature.yml&title=Name+of+the+package+to+release
    :color: black
    :expand:

    **Open Source Code Release Request Form**

The following checks are required when performing the legal review of the project:

.. card:: |uncheck| The project contains the right licensing.

    * The project has the correct license.
    * The contribution does not contain any strong encryption.
    * Ansys official logos and branding images are used in the project.
    * The Ansys copyright appears in the correct location as required by the
      Legal department.
    * The copyright has the proper formatting, which is:
      ``Copyright (C) YYYY ANSYS, Inc. and/or its affiliates.``.
    * The contribution does not embody any unapproved Ansys intellectual
      property for open sourcing.
    * The contribution does not embody any inventions for which Ansys has
      sought or received patent protection.
    * Any third-party open source code included in the contribution has been
      reviewed for security vulnerabilities and includes their license files in
      the repository.

Open source dependencies not distributed as part of the project do not need
their licenses included in the Ansys repository. Examples include dependent
Node Package Manager (``npm``) modules or Python packages from PyPI.

Technical
^^^^^^^^^

Technical approval ensures that the project follows the best and latest
software development practices. Request a technical review by sending an email
to `pyansys.core@ansys.com <mailto:pyansys.core@ansys.com>`_.

The technical review of the project verifies the following:

.. card:: |uncheck| The project contains the right metadata information.
    
    * The project name follows naming conventions.
    * The project version follows :ref:`Semantic versioning`.
    * The project author is ANSYS, Inc.
    * The project maintainer is ANSYS, Inc.
    * Contact and support information is provided in the project.
    * :ref:`The \`\`AUTHORS\`\` file` is present and compliant with legal requirements.
    * :ref:`The \`\`LICENSE\`\` file` is present and compliant with legal requirements.
    * :ref:`The \`\`CONTRIBUTING.md\`\` file` is present.
    * :ref:`The \`\`CONTRIBUTORS.md\`\` file` is present and contains the project lead and main contributors.

.. card:: |uncheck| The project is compliant with PyAnsys style guidelines.

    * The project layout follows the :ref:`Packaging style` guidelines.
    * :ref:`Testing` guarantees at least 80% code coverage.
    * The project adheres to the :ref:`Documentation style` guidelines.
    * The source code docstring examples have been tested.
    * The documentation examples are presented as a gallery.
    * The documentation receives the documentation team's approval.
    * The package builds properly.
    * The project uses CI/CD, including all the :ref:`Required workflows`.
    * The CI/CD pipeline generates project :ref:`artifacts`.

.. card:: |uncheck| The GitHub repository is properly secured.

    * The repository adheres to the :ref:`General configuration`.
    * :ref:`Branch protection` is enabled.
    * :ref:`Tag protection` is enabled.
    * :ref:`Workflow protection` is enabled.


.. |check| raw:: html

    <input checked=""  type="checkbox">

.. |check_| raw:: html

    <input checked=""  disabled="" type="checkbox">

.. |uncheck| raw:: html

    <input type="checkbox">

.. |uncheck_| raw:: html

    <input disabled="" type="checkbox">

Questions asked in the OSS approval request form
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When filling in the `OSS approval request form`_, project leads must
supply responses to several types of questions:

.. card:: |uncheck| General questions

    * What is the name of your project?
    * Who is the project maintainer?
    * Who is the lead from the product team?
    * Who is the Product Management contact?
    * Who is the ACE/AFT owner?

.. card:: |uncheck| Legal questions

    * Who validated your legal readiness?
    * Provided there are no issues with the MIT license, have you correctly applied
      it to the GitHub Repository for your project?
    * Is the copyright header correctly applied to your files in GitHub?
    * Have you confirmed that any intellectual property is removed from the code, docs,
      and examples?
    * I and my legal reviewer, as well as my product and PM reviewer, have confirmed that
      there is no business interest in keeping this code confidential.
    * I and my legal reviewer confirm there is no business interest in enforcing copyright
      protection for this code.
    * I and my legal reviewer confirm that the code does not contain any third-party material
      (open source, proprietary, partner, customer, or otherwise).
    * I and my legal reviewer confirm that the code does not include any invention on which
      the company has, or might want to seek, a patent.
    * Have you cleaned up comments, issues, and pull requests to remove any potentially bad content?
    * My legal reviewer and I have checked the dependencies and validated that they do not
      impose any licensing difficulties.
    * I and my legal reviewer confirm there is NO encryption present in the code.
    * The repository that hosts the code is generally accessible to the public with no
      time limits or access restrictions.
    * This tool or library is not meant for use in any specific industry, platform, or
      process but rather for use by general customers.

.. card:: |uncheck| Technical questions

    * Who verified your technical review?
    * Has your library documentation been reviewed by a documentation team member?
    * Has your source code documentation been reviewed by a developer team member?
    * Has end user testing been completed?
    * Has CI/CD testing been implemented?
    * Has a minimum test coverage of 80% been achieved?
    * Are usage and installation examples included and tested?
    * Is the package definition ready and PyPi packaging completed?
    * Does the GitHub repository supply contribution guidance and have CLA set up?

.. card:: |uncheck| Business questions

    * Who on the Product Marketing Manager (PMM) or Developer Ecosystem (DevEco)
      team checked your project for readiness?
    * Did you tell ACE and your Business Unit lead that you are ready for release?
    * Is there something public that already has the same name as your project?
    * Did you get PMM signoff?
    * Did you ask the DevEco team to update links from the Developer Portal to your
      new OSS project?
    * Did you let the PMM team know that your library is nearing release?
