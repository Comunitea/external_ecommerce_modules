=======================
Ecommerce Basic Modules
=======================

.. |badge1| image:: https://img.shields.io/badge/maturity-Production-green.png
    :target: https://odoo-community.org/page/development-status
    :alt: Production
.. |badge2| image:: https://img.shields.io/badge/licence-LGPL--3-blue.png
    :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-Comunitea-gray.png?logo=github
    :target: https://github.com/Comunitea/
    :alt: Comunitea
.. |badge4| image:: https://img.shields.io/badge/github-Comunitea%2FEcommerce-lightgray.png?logo=github
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/11.0/ecommerce_base
    :alt: Comunitea / Ecommerce
.. |badge5| image:: https://img.shields.io/badge/Spanish-Translated-F47D42.png
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/11.0/ecommerce_base/i18n
    :alt: Spanish Translated

|badge1| |badge2| |badge3| |badge4| |badge5|

This module contains modules dependencies for a basic installation of an e-commerce website.

Also include some custom features than can see below.

**Table of contents**

.. contents::
   :local:

Content
-------
This module contains modules dependencies for a basic installation of an e-commerce website.

Also include some custom features and modules made by: Third parts, Odoo, OCA and Comunitea.

Features
--------
All features that this module include are listed below

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
Add delayed own js charge at the end of pages.
Add script to contact form e-mail validation.

* `jQuery Validation Plugin <http://jqueryvalidation.org/>`_ - v1.16.0 - 12/2/2016
* Copyright (c) 2016 Jörn Zaefferer; Licensed MIT

Third parts modules
-------------------

Infinite Scroll
~~~~~~~~~~~~~~~
Add the SGEEDE Infinite Scroll module.

License
=======
LGPL-3

How it works
============
SGEEDE Infinite Scroll. Allow infinite scroll in Products without using pagination anymore.

Usage
=====
Allow infinite scroll in Products without using pagination anymore.

Configuration
=============
You can activate or deactivate this function in the front-end web editor views.

    **Warning!!**

    Note that it is used then indeed pagination views must will be deactivated.

Author & Maintainer
===================
This module is maintained by the `SGEEDE <http://www.sgeede.com>`_.

If you want to get in touch please contact us via mail (sale@mukit.at) or visit our website (https://mukit.at).

Contributors
============
Mathias Markl <mathias.markl@mukit.at>

Website Scroll Up
~~~~~~~~~~~~~~~~~
Add the MuK Scroll Up Button

License
=======
GNU AFFERO GENERAL PUBLIC LICENSE

Version 3, 19 November 2007

How it works
============
Adds a button to the bottom of the page to jump back up to the top of the page.
The button can be customized using the following attributes.

Usage
=====
Switch to your website and the scroll up button will appear on the bottom of your page.

Configuration
=============
No additional configuration is needed to use this module.

Author & Maintainer
===================
This module is maintained by the `MuK IT GmbH <https://www.mukit.at/>`_.

If you want to get in touch please contact us via mail (sale@mukit.at) or visit our website (https://mukit.at).

Contributors
============
Mathias Markl <mathias.markl@mukit.at>

Odoo and OCA Modules
--------------------

Real Dependencies
~~~~~~~~~~~~~~~~~
#. website
#. website_crm
#. website_crm_privacy_policy

Others that should be installed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. web
#. web_decimal_numpad_dot
#. web_diagram
#. web_dialog_size
#. web_editor
#. web_export_view
#. web_kanban_gauge
#. web_no_bubble
#. web_planner
#. web_refresher
#. web_responsive
#. web_sheet_full_width
#. website_canonical_url
#. website_crm
#. website_crm_recaptcha
#. website_crm_phone_validation
#. website_cookie_notice
#. website_form
#. website_form_builder
#. website_form_recaptcha
#. website_legal_page
#. website_mail
#. website_mass_mailing
#. website_menu_by_user_status
#. website_odoo_debranding
#. website_partner
#. website_payment
#. payment_redsys
#. payment_paypal
#. website_rating
#. website_theme_install
#. website_sale
#. website_sale_delivery
#. website_sale_management
#. website_sale_options
#. website_sale_require_legal
#. website_sale_require_login
#. website_sale_stock_available_display
#. website_sale_stock
#. website_sale_stock_options
#. website_sale_suggest_create_account
#. website_sale_wishlist

Comunitea Modules
-----------------
#. seo_base
#. breadcrumbs_base_tmp

Others interesting modules that could be installed
--------------------------------------------------
Working on it. Coming soon!

Author
------
.. image:: https://comunitea.com/wp-content/uploads/2016/01/logocomunitea3.png
   :alt: Comunitea
   :target: https://comunitea.com

Comunitea Servicios Tecnológicos S.L.

For support and more information, please visit `<https://comunitea.com>`_.

Contributors
~~~~~~~~~~~~
Pavel Smirnov, pavel@comunitea.com

Rubén Seijas, ruben@comunitea.com

Maintainer
~~~~~~~~~~
.. image:: https://comunitea.com/wp-content/uploads/2016/01/logocomunitea3.png
   :alt: Comunitea
   :target: https://comunitea.com

Comunitea Servicios Tecnológicos S.L.

For support and more information, please visit `<https://comunitea.com>`_.

Bug Tracker
-----------
Bugs are tracked on `Comunitea Issues <https://github.com/Comunitea/external_ecommerce_modules/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`Feedback <https://github.com/Comunitea/external_ecommerce_modules/issues/new>`_.

Please, do not contact contributors directly about support or help with technical issues.

Disclaimer of Warranties
------------------------

    **Attention!**

    We provide this module as is, and we make no promises or guarantees about this correct working.

Comunitea provides this application without warranty of any kind.

Comunitea does not warrant that the module will meet your requirements;
that the current application will be uninterrupted, timely, secure, or error-free or that any defects or errors will be corrected.

