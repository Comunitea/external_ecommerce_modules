========================
Website eCommerce Extend
========================

.. |badge1| image:: https://img.shields.io/badge/odoo-v12.0-a3478a
    :target: https://github.com/odoo/odoo/tree/12.0
    :alt: Odoo v12.0
.. |badge2| image:: https://img.shields.io/badge/maturity-Production-green.png
    :target: https://odoo-community.org/page/development-status
    :alt: Production
.. |badge3| image:: https://img.shields.io/badge/licence-LGPL--3-blue.png
    :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |badge4| image:: https://img.shields.io/badge/github-Comunitea-lightgray.png?logo=github
    :target: https://github.com/Comunitea/
    :alt: Comunitea
.. |badge5| image:: https://img.shields.io/badge/github-Comunitea%2FeCommerce-lightgray.png?logo=github
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/12.0/website_ecommerce_extend
    :alt: Comunitea / eCommerce
.. |badge6| image:: https://img.shields.io/badge/Spanish-Translated-F47D42.png
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/12.0/website_ecommerce_extend/i18n/es.po
    :alt: Spanish Translated

|badge1| |badge2| |badge3| |badge4| |badge5| |badge6|

Extend Website for eCommerce customization

**Table of contents**

.. contents::
   :local:

Content
-------
Extend Website for eCommerce customization.

Features
--------
All features that this module include are listed below.

Website Logo
~~~~~~~~~~~~
Change website logo for an image responsive without tittle and include alt tag.

Top Menu
~~~~~~~~
Add Header Top menu styles via bootstrap_overriden file. Take care about Affix Top Menu customize view.

You can define yours with:
    * $-header-logo-min-height: 6rem;
    * $-header-logo-affixed-min-height: 6rem;
    * $-header-logo-margin: 1rem 1rem 1rem 1rem;
    * $-header-logo-affixed-margin: 1rem 1rem 1rem 1rem;
    * $-header-nav-link-text-transform: uppercase;
    * $-header-nav-link-affixed-text-transform: uppercase;
    * $-header-nav-link-font-size: $font-size-base;
    * $-header-nav-link-affixed-font-size: $font-size-base;

My Cart and Wishlist Headers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Delete link texts

Website Menus
~~~~~~~~~~~~~
Add backend menus for best configuration and usage.

These menus are included into Website > Configuration > Products:

#. Websites
#. Menus

Templates
~~~~~~~~~
* Head
    * [ADD] Custom assets
* Footer
    * [ADD] Delayed charge of custom js at the end of pages
* Contact us
    * [ADD] Contact form e-mail JS validation
        * [ADD] Placeholder with fill info
        * [ADD] Error message with fill info
    * [ADD] Phone field set as required in customize view with activated to False by default
    * [UPD] Improve legal advice label style
* Portal My Details
    * Remove style display none for that the states will be available in select for user can change his state on his portal

Styles
~~~~~~
For Full Legal Acceptance on contact form to get a correct alignment.

Javascript
~~~~~~~~~~
- Add delayed own js charge at the end of pages.
- Add script to contact form e-mail validation.

    * `jQuery Validation Plugin <http://jqueryvalidation.org/>`_ - v1.16.0 - 12/2/2016
    * Copyright (c) 2016 Jörn Zaefferer; Licensed MIT

Author
------
Comunitea Servicios Tecnológicos S.L.

Contributors
~~~~~~~~~~~~
* Pavel Smirnov, pavel@comunitea.com
* Rubén Seijas, ruben@comunitea.com

Maintainer
~~~~~~~~~~
.. image:: https://comunitea.com/wp-content/uploads/2016/01/logocomunitea3.png
   :alt: Comunitea
   :target: https://comunitea.com

Comunitea Servicios Tecnológicos S.L.

For support and more information, please visit `<https://comunitea.com>`_.

Known issues
------------
You are welcome to report them. Just use the bug tracker instructions.

Bug Tracker
-----------
Bugs are tracked on `Comunitea Issues <https://github.com/Comunitea/external_ecommerce_modules/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`Feedback <https://github.com/Comunitea/external_ecommerce_modules/issues/new>`_.

Please, do not contact contributors directly about support or help with technical issues.

Disclaimer of Warranties
------------------------

    **Warning!**

    We provide this module as is, and we make no promises or guarantees about this correct working.

Comunitea provides this application without warranty of any kind.

Comunitea does not warrant that the module will meet your requirements;
that the current application will be uninterrupted, timely, secure, or error-free or that any defects or errors will be corrected.
