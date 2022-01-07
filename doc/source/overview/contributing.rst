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

- Instrutions for cloning the source repository from GitHub
- URL to the library`s ``Issues`` page
- Email address for the library's support team

For convenience, here are URLs for the ``Issues`` page of
applicable repositories:

- `PyAEDT Issues <https://github.com/pyansys/pyaedt/issues>`_
- `PyDPF-Core Issues <https://github.com/pyansys/pydpf-core/issues>`_
- `PyDPF-Post Issues <https://github.com/pyansys/pydpf-post/issues>`_
- `PyMAPDL Issues <https://github.com/pyansys/pymapdl/issues>`_
- `PyMAPDL Reader Issues <https://github.com/pyansys/pymapdl-reader/issues>`_

The overall PyAnsys project support team can be reached at
pyansys.support@ansys.com. Someone will either respond or direct the
message to the respective libary's support team.

Submitting Questions
---------------------
For general or technical questions about a PyAnsys library, its
applications, or software usage, create issues on the respective
library's ``Issues`` page. This allows PyAEDT developers and
community members with the needed expertise to collectively address
them. It also makes their responses available to all users.

Reporting Bugs
--------------
If you encounter a bug or your workflow crashes while using a
PyAnsys library, create an issue on the respective library's 
``Issues`` page and tag it with an appropriate label so that it 
can be promptly addressed. When reporting an issue, be as descriptive
as possible so that the issue can be reproduced. Whenever possible,
provide a traceback, screenshots, and sample files to help us address
the issue.

Requesting New Features
-----------------------
We encourage you to submit ideas for improvements to PyAnsys libraries.
To suggest a new feature, create an issue on the respective library's
``Issues`` page and tag it with a ``Feature Request`` label. Use a 
descriptive title and provide ample background information to help the
community implement the desired functionality. For example, if you
would like a reader for a specific file format, provide a link to
documentation for this file format and possibly provide some sample files
and screenshots. We will use the issue thread as a place to discuss the
feature request and provide feedback.

Contributing New Code
---------------------
If you have an idea for improving a PyAnsys library, consider first
creating an issue for a new feature request. We will then use this thread
to discuss how best to implement the contribution.

Once you are ready to start coding, see:

- :ref:`dev_practices` for information on how development is conducted
  in PyAnsys repositories
- :ref:`best_practices` for information on how to style and format your
  code to adhere to PyAnsys standards

Starting Discussions
--------------------
General questions regarding development practices should be raised as
discussions in the repository for the respective PyAnsys library
rather than as issues. For example, general questions about PyMAPDL
should be raised in `PyMAPDL Discussions <https://github.com/pyansys/pymapdl/discussions>`_. 
Issues can be spun out of discussions depending on what is decided, but general
questions should start as discussions where possible.

.. note::
    The discussions feature is still in beta on GitHub, so this may
    change in the future.
    
Cloning the Source Repository
-----------------------------
As mentioned earlier, specific instructions for cloning a source
repository from GitHub appear on the ``Contributing`` page in the
respective library's documentation. Here is a summary of the code
for cloning and installing the latest version in development:

.. code::

    git clone https://github.com/pyansys/<pyansys-repository>
    cd <pyansys-repository>
    pip install -e .

For example, here is the code for cloning and installing the latest version
of PyMAPDL:

.. code::

    git clone https://github.com/pyansys/pymapdl
    cd pymapdl
    pip install -e .

Consider creating a `fork <https://docs.github.com/en/get-started/quickstart/fork-a-repo>`_
of the repository if you want to eventually push a contribution to the official
PyAnsys repository. For additional information, see :ref: dev_practices.

Licensing
---------
All contributed code will be licensed under the MIT License found in
the repository. If you did not write the code yourself, it is your
responsibility to ensure that the existing license is compatible and
included in the contributed files. You must obtain permission from the
original author to relicense the code.

See :ref:`license_file` for more information.
