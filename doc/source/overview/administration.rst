Project Administration
######################
The PyAnsys project allows you to create your own workflows and 
interfaces to Ansys products using Ansys APIs. While using PyAnsys 
libraries requires that the relevant Ansys products are licensed 
either directly or indirectly, you can distribute your custom-made 
applications and workflows internally or externally.


Licensing and Approval
======================
To allow for commercial use, a PyAnsys library must use the MIT
license. Because this license falls in the BSD-style license class,
PyAnsys libraries can be used as a shared library with no
restrictions.  This follows the pattern of including a PyAnsys as a
dependency in ``install_requires`` in the ``setup.py``.

Should you choose to copy and include any PyAnsys project source uses,
all you have to do to to make your library suitable for commercial
use, is to a copy of the original PyAnsys MIT license in the reused
code.

To view this license, see the `LICENSE` file in the root directory 
of this repository. This file must be included in the root 
directory of the repository for every PyAnsys library.


Project Approval
================
Exposing new Ansys technologies through the PyAnsys project is subject
to an internal review and decision process. Please reach out to
Stephane Marguerin or Alexander Kaszynski for any requests.


Repository Management and Standards
===================================
Each PyAnsys repository should at the minimum be administrated by a
single individual with "Admin" permissions over the repository.  This
enables them to override any blocking pull requests or to change the
settings for that repository (e.g. GitHub pages, repository
description, managing branch protections).

Each repository is expected to follow a minimum set of standards:

- Minimum code standards following PEP8 and described in <REF Code
  Guidelines Section>
- CI/CD using GitHub actions or Azure Devops enforcing coding standards.
- Publicly hosted documentation detailing API with examples.  See
  :ref:`api_documentation`.
- Unit testing with at least 80% test coverage.
- Infrastructure in place to deploy the library as a package on `PyPi
  <https://pypi.org/>`_
- Proper license file and author (see :ref:`setup_file` and `ref:`license_file`)
