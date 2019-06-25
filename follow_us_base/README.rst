.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :alt: License: AGPL-3
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html

===============
FollowUs module
===============

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

* Comunitea
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
