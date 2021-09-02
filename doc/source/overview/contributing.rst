==============================
Contributing - Getting Started
==============================

This is intended to be a quick start guide for those who want to start
contributing to a PyAnsys library.

We welcome all code contributions and hope that this guide facilitate
an understanding of the PyAnsys code repository. It is important to
note that while PyAnsys libaries is maintained by Ansys and all
submissions are reviewed thoroughly before merging, our goal is to
foster a community that can support user questions and develop new
features to make PyAnsys libaries a powerful tool for all users. As
such, we welcome and encourage the submittal of questions and code to
this repository.


Contributing New Code
---------------------
If you have an idea for improving a PyAnsys library, consider first
creating an issue as a feature request. We will then use this thread
to discuss how best to implement the contribution.

Once you are ready to start coding, see the
:ref:`development_practices` section for more information on how to
develop your code and adhere to PyAnsys repository standards.


Feature Requests
----------------
We encourage users to submit ideas for improvements to PyAEDT. To
suggest an improvement, create an issue on the respective Issues page with
a ``Feature Request`` label. Use a descriptive title and provide ample
background information to help the community implement the desired
functionality. For example, if you would like a reader for a specific
file format, provide a link to documentation of this file format and
possibly provide some sample files and screenshots. We will use the
issue thread as a place to discuss and provide feedback.


Reporting Bugs
--------------
If you encounter a bugs or your workflow crashes while using a PyAnsys
library, please create an issue on the respective `issues`_ page with an
appropriate label so that it can be promptly addressed. When reporting
an issue, be as descriptive as possible so that the issue can be
reproduced. Whenever possible, provide a traceback, screenshot, and
sample files to help us address the issue.


.. _issues:

Issues
------
For general or technical questions about pyAEDT, its applications, or
about software usage, you can create issues for the applicable respsitory at:

- `PyAEDT Issues <https://github.com/pyansys/pyaedt/issues>`_
- `PyMAPDL Issues <https://github.com/pyansys/pymapdl/issues>`_
- `DPF-Core Issues <https://github.com/pyansys/DPF-Core/issues>`_

This way, the community or PyAnsys developers can collectively address
them. The project support team can be reached at
pyansys.support@ansys.com, and someone will respond or direct the
message accordingly.


Discussions
~~~~~~~~~~~
General questions regarding development practices should be raised in
the correspoinding repository (for example `Discussions
<https://github.com/pyansys/pymapdl/discussions>`_) rather than as
issues themselves. Issues can be spun out of discussions depending on
what is decided, but general Q&A content should start as discussions
where possible.


Installing from Source
----------------------
You can clone the source repository from GitHub and install the
latest version in development mode by running:

.. code::

    git clone https://github.com/pyansys/<pyansys-repository>
    cd <pyansys-repository>
    pip install -e .

For example:

.. code::

    git clone https://github.com/pyansys/pymapdl
    cd pymapdl
    pip install -e .

Consider creating a fork of the repository if you wish to eventually
push a contribution to the offical PyAnsys repository.

.. https://docs.github.com/en/get-started/quickstart/fork-a-repo


Licensing
---------

All contributed code will be licensed under the MIT License found in
the repository. If you did not write the code yourself, it is your
responsibility to ensure that the existing license is compatible and
included in the contributed files. You must obtain permission from the
original author to relicense the code.

See :ref:`license_file` for more details.
