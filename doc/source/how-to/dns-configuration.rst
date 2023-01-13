DNS configuration
=================

As explained in :ref:`Documenting`, PyAnsys projects publish their documentation
online under the following canonical name (CNAME) convention:

``https://<product>.docs.pyansys.com``

To request a CNAME for the ``pyansys.com`` domain, contact
`Maxime Rey`_, `Roberto Pastor Muela`_ or `Alex Kaszynski`_. Any of these members
can handle the creation of the requested PyAnsys subdomain.

Once the CNAME is created, repository administrators can configure their published
documentation in GitHub pages to be exposed through it. To configure the CNAME
for your documentation, refer to `Managing a custom domain for your GitHub Pages site`_.

PyAnsys verified domains
------------------------

In the `PyAnsys GitHub organization`_, these domains have been verified:

* ``pyansys.com``
* ``docs.pyansys.com``

.. warning::

    Only CNAME requests with **one** subdomain before the previous verified
    domains are allowed. The reasons behind this measure are explained in
    :ref:`DNS protection measures`.

DNS protection measures
-----------------------

The rationale behind choosing the previous CNAME convention is due to cybersecurity reasons.
As explained in `Verifying a domain for your organization site`_, GitHub provides for
verifying domains for users and organizations.

**Having a verified domain prevents users external to the organization from
taking over existing direct subdomains**. However, GitHub does not verify
deeper subdomains.

This is better explained with the following examples:

Case scenario - **protected** subdomain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Consider that the domain ``pyansys.com`` has been verified for the `PyAnsys GitHub organization`_.
- This CNAME is requested: ``subdomain.pyansys.com``.

This CNAME can only be used by repositories inside the `PyAnsys GitHub organization`_.
Any attempt by an external user to take over this CNAME is identified and rejected by GitHub.

Case scenario - **vulnerable** subdomain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- The domain ``pyansys.com`` has been verified for the `PyAnsys GitHub organization`_.
- This CNAME is requested: ``subsubdomain.subdomain.pyansys.com``.

This CNAME **can** be used by external users for their repositories. For this reason,
you must avoid creating CNAME requests that are not verified by the organization.


Preventing CNAME takeover
-------------------------

CNAME values have been taken over in the past by external users, typically due to
these reasons:

* Ansys GitHub organizations had no domain verification set up.
* A CNAME created did not follow the recommended CNAME guidelines.
* More than one level of subdomain depth under the verified domain had been requested.
* Long time lapses occurred between CNAME creation and assignment to GitHub pages.

Thus, it is important that you follow these guidelines:

* Ensure that your GitHub organization has verified domains for hosting GitHub pages.
* Check that the CNAME that you request does not have a subdomain depth larger than **1** with respect to the verified domains.
* Request a CNAME only when needed, which is just prior to publishing the site.
* Request deletion of the CNAME once it is no longer used to prevent others from hosting
their sites on it.


..
   Links

.. _PyAnsys DNS Zones: https://portal.azure.com/#@ansys.com/resource/subscriptions/2870ae10-53f8-46b1-8971-93761377c38b/resourceGroups/pyansys/providers/Microsoft.Network/dnszones/pyansys.com/overview
.. _Maxime Rey: https://teams.microsoft.com/l/chat/0/0?users=maxime.rey@ansys.com
.. _Roberto Pastor Muela: https://teams.microsoft.com/l/chat/0/0?users=roberto.pastormuela@ansys.com
.. _Alex Kaszynski: https://teams.microsoft.com/l/chat/0/0?users=alexander.kaszynski@ansys.com
.. _PyAnsys GitHub organization: https://github.com/pyansys
.. _Managing a custom domain for your GitHub Pages site: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
.. _Verifying a domain for your organization site: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages#verifying-a-domain-for-your-organization-site