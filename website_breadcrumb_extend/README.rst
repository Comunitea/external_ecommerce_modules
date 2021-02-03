=========================
Website Breadcrumb Extend
=========================

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
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/12.0/website_breadcrumb_extend
    :alt: Comunitea / eCommerce
.. |badge6| image:: https://img.shields.io/badge/Spanish-Translated-F47D42.png
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/12.0/website_breadcrumb_extend/i18n
    :alt: Spanish Translated

|badge1| |badge2| |badge3| |badge4| |badge5| |badge6|

This module adds friendly multi-level breadcrumbs over along of all website.

**Table of contents**

.. contents::
   :local:

eCommerce Friendly Breadcrumbs
------------------------------
This module adds friendly multi-level breadcrumbs over along of all website by two ways:
    #. Providing a template to be called from any template.
    #. Using customize views
        * This way is activated by default.

How it works
~~~~~~~~~~~~
Method One: The Breadcrumbs generator is available to call in any template:

::

    <t t-call="website_breadcrumb_extend.breadcrumbs_bar"/>

Foreach template that contain it, then a breadcrumb will be created and activate by default.

Method Two: Using customize views and they do it all for you.
    * This way is activated by default.
    * If you want use first method then deactivate customize views and call the breadcrumbs template

Settings
~~~~~~~~
You have a Breadcrumbs menu into Website Settings to manage your breadcrumbs.

Only published crumbs are visible in the website. You can also change the name.

You can set it in the Breadcrumbs menu.

Generated breadcrumbs
~~~~~~~~~~~~~~~~~~~~~
All models included for breadcrumbs are:

#. Product Templates
#. Product Tags
#. Ecommerce Categories
#. Website Pages
    Moreover, this module adds parent_id field to website.page model. This allows to add parent page for static pages.
#. Views
#. Blogs
#. Blog Post
#. Slides Channels
#. Slides
#. Main object
    When there is nothing at all previous. Generate a breadcrumbs by main_object.
    If main_object have _description filed then is used
    like 'home / %s / %s' % (main_object._description, main_object.name).
    Otherwise 'home / %s' % main_object.name.

Customize views
---------------
This module adds friendly multi-level breadcrumbs bar in Header after "Main menu" and "Navbar Menu" block in all pages including Portal part.

    **Warning!**

    This module removes all other breadcrumb bars from the website.

Usage
~~~~~
Customize views are provided with active by default.

#. No Portal Breadcrumbs
#. Portal Breadcrumbs
#. Disable Default Breadcrumbs

    **Warning!**

    "No Portal Breadcrumbs" go side by side with "Shop Breadcrumbs".
    There is not possible to be activated both at the same time. Be carefully.

Customization
-------------
Listed below.

Views
~~~~~
You can activate or deactivate views from web editor to performance your experience.

These views are enabled by default. Just change that on web editor whatever you want.

#. No Portal Breadcrumbs
    - This view enabled Breadcrumbs Bar in all templates and pages except My Portal Home.
#. Portal Breadcrumbs
    - This view enabled Breadcrumbs Bar in all Portal part
#. Disable Default Breadcrumbs
    - Avoid duplicate breadcrumbs
    - Provide you a better experience working with SEO improvements.

Styles
~~~~~~
This module uses default Bootstrap colors and elements.

If you want to use this module in a theme but you do not like where it is rendered, you can simply
override default colors of this module adding these variables in your theme:

    #. Breadcrumb wrap container
        * $breadcrumbs-wrap-color-bg: if(color("menu"), color("menu"), $body-bg) !default;
        * $breadcrumbs-wrap-margin-bottom: 2rem !default;
        * $breadcrumbs-wrap-border-top: unset;
        * $breadcrumbs-wrap-border-bottom: unset;
    #. Breadcrumbs
        * $breadcrumb-bg-color: unset !important !default;
        * $breadcrumb-padding: 0.75rem 1rem !important !default;
        * $breadcrumb-color-href: $o-enterprise-primary-color !default;
        * $breadcrumb-link-decoration: underline !default;
        * $breadcrumb-active-color: $gray-600 !default;
    #. Documents table list
        * $breadcrumb-portal-navbar-border: unset !important !default;

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
You are welcome to report them. Just follow the bug tracker instructions.

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
