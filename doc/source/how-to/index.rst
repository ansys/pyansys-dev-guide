How-to
======

This section describes how to create effective and efficient Python libraries
for interfacing with Ansys products and services. It also explains how apps
and complex services expose functionalities such as logging, data transfer,
and app APIs.

.. rubric:: Prerequisites

.. grid:: 3

    .. grid-item-card:: :fas:`fa-regular fa-screwdriver-wrench` Environment setup
      :link: setting-up
      :link-type: doc
      :padding: 2 2 2 2

      How to configure your Python environment before contributing to a PyAnsys project.

    .. grid-item-card:: :fas:`fa-solid fa-people-group` Contributing
      :link: contributing
      :link-type: doc
      :padding: 2 2 2 2

      How to follow PyAnsys coding standards, branching, and the contribution workflow.

.. rubric:: Library Development

.. grid:: 3

    .. grid-item-card:: :fas:`fa-solid fa-code-compare` Python versions
      :link: supporting-python-versions
      :link-type: doc
      :padding: 2 2 2 2

      How to define which Python versions your library supports and configure CI accordingly.

    .. grid-item-card:: :fas:`fa-solid fa-box-open` Packaging
      :link: packaging
      :link-type: doc
      :padding: 2 2 2 2

      How to package and distribute a PyAnsys library for end users.

    .. grid-item-card:: :fas:`fa-solid fa-cubes` gRPC API packages
      :link: grpc-api-packages
      :link-type: doc
      :padding: 2 2 2 2

      How to structure gRPC API packages following PyAnsys conventions.

    .. grid-item-card:: :fas:`fa-solid fa-bars-staggered` Logging
      :link: logging
      :link-type: doc
      :padding: 2 2 2 2

      How to add structured logging to a PyAnsys library.

    .. grid-item-card:: :fas:`fa-solid fa-file` Documenting
      :link: documenting
      :link-type: doc
      :padding: 2 2 2 2

      How to write and maintain documentation following PyAnsys style guidelines.

.. rubric:: Quality Assurance

.. grid:: 3

    .. grid-item-card:: :fas:`fa-solid fa-flask-vial` Testing
      :link: testing
      :link-type: doc
      :padding: 2 2 2 2

      How to write unit and integration tests and measure code coverage.

    .. grid-item-card:: :fas:`fa-solid fa-code-merge` Continuous integration
      :link: continuous-integration
      :link-type: doc
      :padding: 2 2 2 2

      How to automate testing, linting, and builds with GitHub Actions.

.. rubric:: Security and Maintenance

.. grid:: 3

    .. grid-item-card:: :fas:`fa-solid fa-umbrella` Repository protection
      :link: repository-protection
      :link-type: doc
      :padding: 2 2 2 2

      How to secure branches, tags, and secrets in your GitHub repository.

    .. grid-item-card:: :fas:`fa-solid fa-shield-halved` Vulnerabilities
      :link: vulnerabilities
      :link-type: doc
      :padding: 2 2 2 2

      How to find and fix security vulnerabilities in a PyAnsys package.

    .. grid-item-card:: :fas:`fa-solid fa-circle-nodes` Product compatibility
      :link: compatibility
      :link-type: doc
      :padding: 2 2 2 2

      How to manage compatibility across different Ansys product versions.

    .. grid-item-card:: :fas:`fa-solid fa-bug` Deprecating a library
      :link: deprecating
      :link-type: doc
      :padding: 2 2 2 2

      How to retire a library cleanly and guide users to alternatives.

.. rubric:: Release & Publish

.. grid:: 3

    .. grid-item-card:: :fas:`fa-solid fa-server` DNS configuration
      :link: dns-configuration
      :link-type: doc
      :padding: 2 2 2 2

      How to set up the documentation domain for your PyAnsys library.

    .. grid-item-card:: :fas:`fa-solid fa-upload` Releasing and publishing
      :link: releasing
      :link-type: doc
      :padding: 2 2 2 2

      How to create and publish a versioned release to PyPI.

    .. grid-item-card:: :fas:`fa-solid fa-lightbulb` Tutorials and best practices
      :link: tutorials/index
      :link-type: doc
      :padding: 2 2 2 2

      How to use Python libraries effectively and efficiently.

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Prerequisites

   setting-up
   contributing

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Library Development

   supporting-python-versions
   packaging
   grpc-api-packages
   logging
   documenting

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Quality Assurance

   testing
   continuous-integration

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Security and Maintenance

   repository-protection
   vulnerabilities
   compatibility
   deprecating
   tutorials/index.rst

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Release & Publish

   dns-configuration
   releasing
