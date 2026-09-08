DNS configuration
=================

As explained in :ref:`documenting_developers`, documentation for PyAnsys libraries is published
online following canonical name (CNAME) convention:

``https://<product>.docs.pyansys.com``

To request a CNAME for the ``pyansys.com`` domain, contact the
`PyAnsy core team <pyansys_core_email_>`_. They handle the creation of all PyAnsys subdomains.

Once the CNAME is created, repository administrators can configure their published
documentation in GitHub pages to be exposed through it. To configure the CNAME
for your documentation, see `Managing a custom domain for your GitHub Pages site`_
in the GitHub documentation.

DNS TXT verification
--------------------

Once a CNAME is registered under the ``pyansys.com`` domain, the next step is
to perform a DNS TXT verification. All PyAnsys subdomains are required by the Ansys
IT department to provide a DNS TXT verification. To verify a new CNAME for an
organization, see `Verifying a domain for your organization site`_ in the GitHub
documentation. This article shows how to create DNS TXT verification elements
for GitHub Pages sites.

.. warning::

    Only users with privilege access to the ``pyansys.com`` DNS zone can
    perform a DNS TXT verification. If assistance is needed, contact the
    `PyAnsy core team <pyansys_core_email_>`_.

PyAnsys-verified domains
------------------------

In the Ansys GitHub organization, these domains have been verified:

* ``pyansys.com``
* ``docs.pyansys.com``

.. warning::

    Only CNAME requests with **one** subdomain before the previous verified
    domains are allowed. For more information, see :ref:`DNS protection measures`.

DNS protection measures
-----------------------

The rationale behind choosing the previous CNAME convention is related to cybersecurity.
As the `Verifying a domain for your organization site`_ article explains, GitHub provides for
verifying domains for users and organizations.

**Having a verified domain prevents users external to the organization from
taking over existing direct subdomains**.

However, GitHub does not verify deeper subdomains.

This is better explained with the following examples:

Scenario for a **protected** subdomain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- The ``docs.pyansys.com`` domain has been verified for the Ansys GitHub organization.
- This CNAME is requested: ``subdomain.docs.pyansys.com``.

This CNAME can only be used by repositories inside the Ansys GitHub organization.
Any attempt by an external user to take over this CNAME is identified and rejected by GitHub.

Scenario for a **vulnerable** subdomain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- The domain ``docs.pyansys.com`` has been verified for the Ansys GitHub organization.
- This CNAME is requested: ``subsubdomain.subdomain.docs.pyansys.com``.

This CNAME **can** be used by external users for their repositories. For this reason,
you must avoid creating CNAME requests that are not verified by the Ansys GitHub organization.

CNAME takeover prevention
-------------------------

CNAME values have been taken over in the past by external users, typically due to
these reasons:

* The Ansys GitHub organizations had no domain verification set up.
* A CNAME created did not follow the recommended CNAME guidelines.
* More than one level of subdomain depth under the verified domain had been requested.
* Long time lapses occurred between CNAME creation and assignment to GitHub pages.

Thus, it is important that you follow these guidelines:

* Ensure that your GitHub organization has verified domains for hosting GitHub pages.
* Check that the CNAME that you request does not have a subdomain depth larger than **one** with respect to the verified domains.
* Request a CNAME only when needed, which is just prior to publishing the site.
* Request deletion of the CNAME once it is no longer used to prevent others from hosting
  their sites on it.

.. Links

.. _PyAnsys DNS Zones: https://portal.azure.com/#@ansys.com/resource/subscriptions/2870ae10-53f8-46b1-8971-93761377c38b/resourceGroups/pyansys/providers/Microsoft.Network/dnszones/pyansys.com/overview
.. _Managing a custom domain for your GitHub Pages site: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
.. _Verifying a domain for your organization site: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages#verifying-a-domain-for-your-organization-site