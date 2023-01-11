Project approval and public release
===================================
Most of the projects in PyAnsys expose the functionality of ANSYS, Inc.
products. Due to intellectual property reasons, the public release of a PyAnsys
library must undergo through a project approval process.


Approval process
----------------
The approval process is divided into three different parts:

.. grid:: 3
    
    .. grid-item-card:: :octicon:`file-badge` Managerial
       :link: managerial
       :link-type: ref

        Verifies that direct managers, GM/VP, CT or CTO are aware about the project and approve it.

    .. grid-item-card:: :octicon:`law` Legal
       :link: legal
       :link-type: ref

        Verifies that the project ships with the right legal framework to protect ANSYS, Inc. intellectual property.

    .. grid-item-card:: :octicon:`gear` Technical
       :link: technical
       :link-type: ref

        Verifies that the project is compliant with ANSYS, Inc. software guidelines and best practices.


.. important::

    An approval from each part is required to release a project into the public.


When releasing a project to the public, expect to:

* Coordinate with the product line development team, if applicable.
* Maintain the project by means of fixing bugs and providing support for new releases.
* Ensure the good reputation of ANSYS, Inc. in the open source community.


Managerial
^^^^^^^^^^
The managerial part of the approval process guarantees that direct manager (DM),
general managers (GM), vice presidents (VP), and chief technolofy officer (CTO)
are aware about the existence and the status of the project.

The amount of administrative reviews and approvals depends on the nature of the
project. A project can be classified in to the following categories:

.. grid:: 3
    
    .. grid-item-card:: :octicon:`repo` Documentation projects

        Documentation projects require direct manager approval, legal
        review, and documentation proofing. No source code other than
        documentation files is allowed.

    .. grid-item-card:: :octicon:`tools` Tools supporting products

        Tool projects require direct manager and business unit's GM/VP
        approval. No product source code is allowed.

    .. grid-item-card:: :octicon:`container` Libraries supporting products

        Library projects interfacing and wrapping any ANSYS, Inc. products
        require approval of the direct manager, product line, product line, and
        the CTO. No product source code is allowed.



Legal
^^^^^
The legal review and approval guarantees that the whole project is subjected
and protected by the ANSYS, Inc. legal framework.

Start by completing the legal review request form:

.. button-link:: https://ansys.sharepoint.com/:w:/r/sites/OpenSourceSoftwareOSSSuperintendence/_layouts/15/Doc.aspx?sourcedoc=%7B3296AD39-79EC-4F42-81C1-1DF988986800%7D&file=Open%20Source%20Policy_Request%20to%20Release%20Code_need%20GM%20sign-off_2021Sep.docx&action=default&mobileredirect=true
    :color: black
    :expand:

    **Open Source Code Release Request Form**

The following checks are required when performing the legal review of the project:

.. card:: |uncheck| The project contains the right licensing

    * The project contains the right license.
    * The contribution does not contain any strong encryption.
    * Ansys official logos and branding images are used in the project.
    * The ANSYS, Inc. copyright appears in the right location as required by the Legal department.
    * The copyright has the right formatting, that is ``Copyright (C) YYYY ANSYS, Inc.``.
    * The contribution does not embody any Ansys intellectual property that is not approved for open sourcing.
    * The contribution does not embody any invention for which Ansys has sought or received patent protection.
    * Any third-party open sources included in the contribution have been reviewed for security vulnerabilities and have had their license files included in the repository.

Open source dependencies that are not distributed as part of the project do not
need their licenses included in the Ansys repository. Examples include
dependent npm modules or Python packages from PyPI.


Technical
^^^^^^^^^
The technical review and approval guarantees that the project follows the best
and latest software development practices.

The following checks are required when performing the technical review of the project:

.. card:: |uncheck| The project contains the right metadata information
    
    * The name of the project follows naming convention.
    * The version of the project follows :ref:`Semantic versioning`.
    * The author of the project is ANSYS, Inc.
    * The maintainer of the project is ANSYS, Inc.
    * Contact and support information are provided in the project.
    * :ref:`The \`\`LICENSE\`\` file` is present and compliant with legal requirements.
    * :ref:`The \`\`CONTRIBUTING.md\`\` file` is present.

.. card:: |uncheck| The project is compliant with PyAnsys style guidelines

    * The layout of the project follows the :ref:`Packaging style` guidelines.
    * :ref:`Testing` guarantees at least 80% of code coverage.
    * The project follows the :ref:`Documentation style` guidelines.
    * The examples in the source code docstrings are tested.
    * Documentation examples are presented in the form of a gallery.
    * The package builds properly.
    * The project contains uses CI/CD with all the :ref:`Required workflows`.
    * The CI/CD pipeline generates project :ref:`artifacts`.

.. card:: |uncheck| The GitHub repository is properly secured

    * Repository is compliant with the :ref:`General configuration`.
    * :ref:`Branch protection` is enabled.
    * :ref:`Tag protection` is enabled.
    * :ref:`Workflow protection` is enabled.

.. note::

    Contact `support@pyansys.com <mailto:support@pyansys.com>`_ if you require
    support for being compliant with all previous requirements.


.. |check| raw:: html

    <input checked=""  type="checkbox">

.. |check_| raw:: html

    <input checked=""  disabled="" type="checkbox">

.. |uncheck| raw:: html

    <input type="checkbox">

.. |uncheck_| raw:: html

    <input disabled="" type="checkbox">
