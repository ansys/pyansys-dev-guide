============
Contributing
============

Ansys welcomes all PyAnsys code contributions and wants you to
understand how to contribute. While we maintain PyAnsys libraries
and thoroughly review all submissions, we want to foster a community
that supports user questions and develops new features to make
our libraries powerful tools for all users. As such, we
encourage you to submit questions, report bugs, request new
features, contribute code, and start discussions.

This page provides general information about contributing to a
PyAnsys library. Contribution information specific to a particular
library appears on the ``Contributing`` page in the respective
library's documentation, including:

- Instructions for cloning the source repository from GitHub
- URL to the library's ``Issues`` page

For convenience, here are URLs for ``Issues`` pages for
Ansys product repositories:

- `PyAEDT Issues <https://github.com/pyansys/pyaedt/issues>`_
- `PyDPF-Core Issues <https://github.com/pyansys/pydpf-core/issues>`_
- `PyDPF-Post Issues <https://github.com/pyansys/pydpf-post/issues>`_
- `PyMAPDL Issues <https://github.com/pyansys/pymapdl/issues>`_
- `PyMAPDL-Reader Issues <https://github.com/pyansys/pymapdl-reader/issues>`_

You can reach the overall PyAnsys project support team at
'pyansys.support@ansys.com <pyansys.support@ansys.com>`_.

Submitting Questions
---------------------
For general or technical questions about a PyAnsys library, its
applications, or software usage, create issues on the respective
library's ``Issues`` page. This allows PyAnsys developers and
community members with the needed expertise to collectively address
them. It also makes their responses available to all users.

Reporting Bugs
--------------
If you encounter a bug or your workflow crashes while using a
PyAnsys library, create an issue on the respective library's 
``Issues`` page and tag it with an appropriate label so that it 
can be promptly addressed. In describing the issue, be as descriptive
as possible so that the issue can be reproduced. Whenever possible,
provide a traceback, screenshots, and sample files that might help
the community to address the issue.

Requesting New Features
-----------------------
We encourage you to submit ideas for improving PyAnsys libraries.
To suggest a new feature, create an issue on the respective library's
``Issues`` page and tag it with the ``Feature Request`` label. Use a 
descriptive title and provide ample background information to help the
community decide how the feature might be implemented. For example,
if you would like to see a reader added for a specific file format,
in the issue, provide a link to documentation for this file
format and possibly some sample files and screenshots. The community
will then use the issue thread to discuss the request and
provide feedback on how the feature might best be implemented.

Contributing New Code
---------------------
When you are ready to start contributing code, see:

- :ref:`development_practices` for information on how development is
  conducted in PyAnsys repositories
- :ref:`best_practices` for information on how to style and format your
  code to adhere to PyAnsys standards

Starting Discussions
--------------------
For general questions about development practices, you should create discussions
rather than issues. The repository for each PyAnsys library has its own
``Discussions`` page. For example, to ask a question about an PyMAPDL development
practice, you would create a discussion on this library's `Discussions <https://github.com/pyansys/pymapdl/discussions>`_
page. It is possible for discussions to lead to the creation of issues.

.. note::
    Because the ``Discussions`` feature is still in beta on GitHub, usage may
    change in the future.
    
Cloning the Source Repository
-----------------------------
As mentioned earlier, specific instructions for cloning a source
repository from GitHub appear on the ``Contributing`` page in the
respective library's documentation. In te following code for cloning and
installing the latest version of a PyAnsys repository, ``<pyansy-repository>``
is a placeholder for the name of the repository.

.. code::

    git clone https://github.com/pyansys/<pyansys-repository>
    cd <pyansys-repository>
    pip install -e .

For example, you would use this code to clone and installing the latest version
of PyMAPDL:

.. code::

    git clone https://github.com/pyansys/pymapdl
    cd pymapdl
    pip install -e .

If you want to eventually push a contribution to the official
PyAnsys repository, consider creating a `fork <https://docs.github.com/en/get-started/quickstart/fork-a-repo>`_
of the repository. For additional information, see :ref: dev_practices.

Licensing
---------
All contributed code will be licensed under the MIT License. For more information, see
for more information. The ``LICENSE`` file with the MIT License must be included in
the root directory of the repository for a PyAnsys library.

If you did not write the code that you are contributing yourself, it is your
responsibility to ensure that the existing license for this code is compatible and
included in the contributed files. You must obtain permission from the original
author to relicense the code.
