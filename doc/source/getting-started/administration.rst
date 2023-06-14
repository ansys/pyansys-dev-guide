Project approval and public release
===================================
Most of the projects in PyAnsys expose the functionality of Ansys
products. Due to intellectual property reasons, the public release of a PyAnsys
library must go through a project approval process.

First steps
-----------
In order to trigger the public release process, project leads should fill in the following
form:

* `Release request workflow intitiation form <https://gz2idtcjsw2.typeform.com/to/qVujtwSR>`_

This form lets the different parties involved in the public release process know that
there is a will to release a project. If your selected option was to release an Ansys Open
Source project, then please continue to the next section.

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


Once all these three approvals have been awarded, project leads are requested to fill
in the next form:

* `OSS approval request form <https://gz2idtcjsw2.typeform.com/OSSapproval>`_

This form serves as a final checklist to verify that all approvals have been processed
and to formalize the OSS approval process, as a final record. You can find the questions
to be asked in :ref:`OSS approval request form questions`.

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

.. button-link:: https://ansys.sharepoint.com/:w:/r/sites/OpenSourceSoftwareOSSSuperintendence/_layouts/15/Doc.aspx?sourcedoc=%7B3296AD39-79EC-4F42-81C1-1DF988986800%7D&file=Open%20Source%20Policy_Request%20to%20Release%20Code_need%20GM%20sign-off_2021Sep.docx&action=default&mobileredirect=true
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
    * The copyright has the proper formatting, which is ``Copyright (C) YYYY ANSYS, Inc.``.
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
    * :ref:`The \`\`AUTHORS.md\`\` file` is present and contains the project lead and main contributors.
    * :ref:`The \`\`LICENSE\`\` file` is present and compliant with legal requirements.
    * :ref:`The \`\`CONTRIBUTING.md\`\` file` is present.

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

OSS approval request form questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When filling in the `OSS approval request form`_, project leads will have to
answer the following questions (they might be of different nature: fill in,
yes/no, multiple-choice...). Be ready to answer them once you start completing
the form.

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
    * Have you confirmed that any IP is removed from the code, docs, and examples?
    * I and my legal reviewer as well as my product and PM reviewer have confirmed that
      there is no business interest in keeping this code confidential.
    * I and my legal reviewer confirm there is no business interest in enforcing copyright
      protection for this code.
    * I and my legal reviewer confirm that the code does not contain any 3rd party material
      (open source, proprietary, partner, customer, or otherwise).
    * I and my legal reviewer confirm that the code does not include any invention on which
      the company has, or might want to seek a patent.
    * Have you cleaned up the comments/issues/PRs/etc. to remove any potentially bad things?
    * My legal reviewer and I have checked the dependencies and validated they do not
      impose any licensing difficulties?
    * I and my legal reviewer confirm there is NO encryption present in the code.
    * The repository that hosts the code will be generally accessible to the public with no
      time limits or access restrictions.
    * This tool or library is not meant for use in any specific industry, platform, or
      process and is meant for use by general customers.

.. card:: |uncheck| Technical questions

    * Who verified your technical review?
    * Was your documentation for usage/installation/pre-reqs reviewed by the docs team?
    * Has your source code documentation been reviewed?
    * Completed end user testing?
    * Pull request testing complete?
    * Minimum of 80% testing coverage verified?
    * Your usage and installation examples are ready?
    * Package definition ready and PyPi packaging completed?
    * GitHub Repository has the contribution guidance and CLA set up and ready.

.. card:: |uncheck| Business questions

    * Who did you get from the PMM/DevEco team to check your readiness?
    * Did you tell ACE and the BU you are at this point?
    * Is there something public that is already called the same thing you want to call your project?
    * Did you get Product Marketing Manager (PMM) signoff?
    * Did you let DevEco know so they can update links from the DevPortal to your new OSS project?
    * Did you let Product Management know that your library is nearing release?
