.. _private_dependencies:


Hosting Private Dependencies
============================
There will be cases in which it is necessary to host and pull packages that are
not ready to be hosted to the public `PyPI`_. For example, if a PyAnsys library
requires auto-generated gRPC interface files from an as-of-yet private feature
or service, this package should be hosted on a private PyPI repository.

Ansys has a private repository at `PyAnsys PyPI`_, and access is controlled via
a secret PAT, specified in the GitHub secret ``PYANSYS_PYPI_PRIVATE_PAT`` which
is only available to repositories within the `PyAnsys`_.

.. note::
   Forked GitHub repositories do not have access to GitHub secrets. This is
   designed to protect against PRs that could potentially scrape tokens from
   our CI/CD.


Upload
------
Packages can be uploaded to the private repository with the following short
bash script. If you are operating out of a GitHub CI pipeline, email the
PyAnsys Core team at pyansys.core@ansys.com for the PAT,
``PYANSYS_PYPI_PRIVATE_PAT``.

Assuming you are already in a Python repository containing your wheels and/or
source distribution within the ``dist`` directory:

.. code::

   pip install build twine pip -U

   REPOSITORY_URL="https://pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi/upload"
   python -m twine upload dist/* \
     -p ${{ secrets.PYANSYS_PYPI_PRIVATE_PAT }} \
     -u PAT \
     --repository-url $REPOSITORY_URL

Alternatively, you can use environment variables instead of CLI arguments for twine.

.. code::

   export TWINE_USERNAME=PAT
   export TWINE_PASSWORD=$PYANSYS_PYPI_PRIVATE_PAT
   export TWINE_REPOSITORY_URL="https://pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi/upload"

   python -m twine upload dist/*


Download
--------
To download the Python package from the `PyAnsys PyPI`_, use the following:

.. code::

   INDEX_URL=https://$PYANSYS_PYPI_PRIVATE_PAT@pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi/simple/
   pip install ansys-<product/tool>-<library> --index-url $INDEX_URL --no-dependencies

.. warning::
   Take care to always use the ``--index-url`` switch rather than the
   ``--extra-index-url`` switch. As noted in the `pip Documentation`_, the
   ``--index-url`` switch changes the Python Package Index, and forces ``pip``
   to only use packages from that package index.

   Our package index uses PyPI upstream, and therefore other users cannot
   inject packages from PyPI that would supersede our packages, even if they
   are of a higher version.

   This is not the case if you use ``--extra-index-url``, which adds rather
   than replaces the default package index. For security do not use
   ``--extra-index-url``.


.. _PyPI: https://pypi.org/
.. _PyAnsys PyPI: https://pkgs.dev.azure.com/pyansys/_packaging/pyansys/pypi
.. _PyAnsys: https://github.com/pyansys
.. _pip Documentation: https://pip.pypa.io/en/stable/cli/pip_install/
