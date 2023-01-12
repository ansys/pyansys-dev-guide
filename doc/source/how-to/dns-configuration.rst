DNS configuration
=================

As explained in :ref:`Documenting`, PyAnsys projects publish their documentation
online under the following canonical name (CNAME) convention:

``https://<product>.docs.pyansys.com``

To request a CNAME for the ``pyansys.com`` domain, please contact
`Maxime Rey`_, `Roberto Pastor Muela`_ or `Alex Kaszynski`_. Any of these members
can handle the creation of the requested PyAnsys subdomain.

Once the CNAME is created, repository administrators can configure their published
documentation in GitHub pages to be exposed through it. To configure the CNAME
for your documentation, please refer to GitHub's online documentation:
`Managing a custom domain for your GitHub Pages site`_.

PyAnsys verified domains
------------------------

In the `PyAnsys GitHub organization`_, the following domains have been verified:

* ``pyansys.com``
* ``docs.pyansys.com``

.. warning::

    Only CNAME requests with **one** subdomain before the previous verified
    domains are allowed. The reasons behind this measure are explained in
    :ref:`DNS protection measures`.

DNS protection measures
-----------------------

The rationale behind choosing the previous CNAME convention is due to cybersecurity reasons.
GitHub allows to verify domains for users and organizations, see `Verifying a domain for your organization site`_.

Once an organization has a verified domain, **this prevents external users to the organization from
taking over existing direct subdomains**. However, deeper subdomains are no longer verified by
GitHub.

This is better explained with the following examples:

Case scenario - **protected** subdomain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Consider that the domain ``pyansys.com`` has been verified for the `PyAnsys GitHub organization`_.
#. A CNAME as follows is requested: ``subdomain.pyansys.com``

The CNAME requested can only be used by projects/repositories inside the `PyAnsys GitHub organization`_.
Any attempt by external users/organizations of taking over the previous CNAME is identified and rejected by GitHub.

Case scenario - **vulnerable** subdomain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Consider that the domain ``pyansys.com`` has been verified for the `PyAnsys GitHub organization`_.
#. A CNAME as follows is requested: ``subsubdomain.subdomain.pyansys.com``

The CNAME requested **can** be used by external user/organization repositories. For this reason,
it must be avoided to create CNAME requests that are not verified by the organization.


Preventing CNAME takeover
-------------------------

From past experience, CNAME values have been taken over by external users/organizations. This has typically
occurred due to the following reasons:

* Ansys GitHub organizations had no domain verification set up.
* A CNAME created did not follow the recommended CNAME guidelines.
* More than one level of subdomain depth under the verified domain had been requested.
* Long lead times between CNAME creation and assignment to GitHub pages occurred.

Thus, it is important that the following guidelines are followed:

* Ensure that your GitHub organization has verified domains for hosting GitHub pages.
* Check that whatever CNAME requested does not have a subdomain depth larger than **1** with respect to the verified domains.
* Request a CNAME only when needed - that is, right before publishing the site.
* Request CNAME deletion once it is no longer used to prevent others from hosting their sites on it.


..
   Links

.. _PyAnsys DNS Zones: https://portal.azure.com/#@ansys.com/resource/subscriptions/2870ae10-53f8-46b1-8971-93761377c38b/resourceGroups/pyansys/providers/Microsoft.Network/dnszones/pyansys.com/overview
.. _Maxime Rey: https://teams.microsoft.com/l/chat/0/0?users=maxime.rey@ansys.com
.. _Roberto Pastor Muela: https://teams.microsoft.com/l/chat/0/0?users=roberto.pastormuela@ansys.com
.. _Alex Kaszynski: https://teams.microsoft.com/l/chat/0/0?users=alexander.kaszynski@ansys.com
.. _PyAnsys GitHub organization: https://github.com/pyansys
.. _Managing a custom domain for your GitHub Pages site: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
.. _Verifying a domain for your organization site: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages#verifying-a-domain-for-your-organization-site