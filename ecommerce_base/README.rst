=========================
Ecommerce Extend Features
=========================

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

This module contains some custom features for a basic installation of an e-commerce website.

**Table of contents**

.. contents::
   :local:

Content
-------
Some custom features for a basic installation of an e-commerce website.

Features
--------
All features that this module include are listed below.

Website Logo
~~~~~~~~~~~~
Change website logo for an image responsive without tittle and include alt tag.

    **Warning!**

    If not **``website_logo´´** module is installed then use default **``website.layout_logo_show´´** view

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
* For Full Legal Acceptance on contact form to get a correct alignment.

* Cookies Message Notice
    * Use Bootstrap default variables but you can override them ans also:
        * Add a new margin for content into panel
        * Always used border color same as btn color even in hover but with inverted colors
    * Just inside your custom styles, override this global variables as you wish:

    ::

        ::root {
            // Warning Panel
            --state-warning-text: your_value or #8a6d3b;
            --state-warning-bg: your_value or #fcf8e3;
            --state-warning-border: your_value or #fcf8e3;
            --state-warning-margin: your_value or 1.8rem 1.25rem;
            // Links
            --state-warning-link-color: your_value or darken(#428bca, 6.5%); // #337ab7;
            --state-warning-link-decoration: your_value or none;
            --state-warning-link-hover-color: your_value or darken(@state-warning-link-color, 15%);
            --state-warning-link-hover-decoration: your_value or underline;
            // Ok Button
            --state-warning-btn-color: your_value or @btn-primary-color;
            --state-warning-btn-bg: your_value or @btn-primary-bg;
            --state-warning-btn-hover-color: your_value or @btn-primary-bg;
            --state-warning-btn-hover-bg: your_value or @btn-primary-color;
        }

Javascript
~~~~~~~~~~
Add script to contact form e-mail validation.

    * `jQuery Validation Plugin <http://jqueryvalidation.org/>`_ - v1.16.0 - 12/2/2016
    * Copyright (c) 2016 Jörn Zaefferer; Licensed MIT

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

    **Warning!**

    We provide this module as is, and we make no promises or guarantees about this correct working.

Comunitea provides this application without warranty of any kind.

Comunitea does not warrant that the module will meet your requirements;
that the current application will be uninterrupted, timely, secure, or error-free or that any defects or errors will be corrected.
