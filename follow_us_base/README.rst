==============
Follow Us Base
==============

.. |badge1| image:: https://img.shields.io/badge/maturity-Production-green.png
    :target: https://odoo-community.org/page/development-status
    :alt: Production
.. |badge2| image:: https://img.shields.io/badge/licence-LGPL--3-blue.png
    :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-Comunitea-gray.png?logo=github
    :target: https://github.com/Comunitea/
    :alt: Comunitea
.. |badge4| image:: https://img.shields.io/badge/github-Comunitea%2FFOLLOWUS-lightgray.png?logo=github
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/11.0/follow_us_base
    :alt: Comunitea / Follow Us
.. |badge5| image:: https://img.shields.io/badge/Spanish-Translated-F47D42.png
    :target: https://github.com/Comunitea/external_ecommerce_modules/blob/11.0/seo_base/i18n/es.po
    :alt: Spanish Translated


|badge1| |badge2| |badge3| |badge4| |badge5|

This module contains several modules for different optimizations on the website.

It is compatible with the multi-website.

**Table of contents**

.. contents::
   :local:

Add front-end users to mass_mailing list
----------------------------------------

This module adds **Follow us** page with a subscription form to the website.

The page with newsletter channel list has URL *EXAMPLE.COM/page/newsletter*

For put the newsletter horizontal banner you need to set this code to your template:

::

    <t t-call="follow_us_base.newsletter_banner">
        <t t-set="channel" t-value="CHANNEL_ID"/>           # required
        <t t-set="hash_tag" t-value="'YOUR_HASH_TAG'"/>     # optional
    </t>


Author
------

Developer: Comunitea, info@comunitea.com

Contributors
~~~~~~~~~~~~

* Pavel Smirnov, pavel@comunitea.com
* Rubén Seijas, ruben@comunitea.com

Maintainer
~~~~~~~~~~

This module is maintained by the Comunitea http://www.comunitea.com.

Disclaimer of Warranties
------------------------

    **Attention!**

    We provide this module as is, and we make no promises or guarantees about this correct working.

Comunitea provides this application without warranty of any kind.

Comunitea does not warrant that the module will meet your requirements;
that the current application will be uninterrupted, timely, secure, or error-free or that any defects or errors will be corrected.
