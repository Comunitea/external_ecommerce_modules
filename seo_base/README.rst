========================================
Website base module for SEO optimization
========================================

.. |badge1| image:: https://img.shields.io/badge/maturity-Production-green.png
    :target: https://odoo-community.org/page/development-status
    :alt: Production
.. |badge2| image:: https://img.shields.io/badge/licence-LGPL--3-blue.png
    :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-Comunitea-gray.png?logo=github
    :target: https://github.com/Comunitea/
    :alt: Comunitea
.. |badge4| image:: https://img.shields.io/badge/github-Comunitea%2FSEO-lightgray.png?logo=github
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/11.0/seo_base
    :alt: Comunitea / SEO
.. |badge5| image:: https://img.shields.io/badge/Spanish-Translated-F47D42.png
    :target: https://github.com/Comunitea/external_ecommerce_modules/blob/11.0/seo_base/i18n/es.po
    :alt: Spanish Translated


|badge1| |badge2| |badge3| |badge4| |badge5|

This module contains several modules for different optimizations on the website.

It is compatible with the multi-website.

**Table of contents**

.. contents::
   :local:

Analytics
~~~~~~~~~

Integration with analytical systems:

- Google Tag Manager
- Facebook Pixel

Set this in Website > SEO Configuration > Analytics

Shop access rules
~~~~~~~~~~~~~~~~~

You can manage your shop access. True by default.
If you wish may enable for user type (B2B or B2C).

Set this in Website > SEO Configuration > General > Public Shop

Sitemap.xml
~~~~~~~~~~~

This module creates a sitemap.xml file in the root path of the website.

You can use the back-end part for the configuration of this map.

Set this in Website > SEO Configuration > Sitemap.xml

Robots.txt
~~~~~~~~~~

This module creates a Robots.txt file in the root path of the website.

You can use the back-end part for the change of cache time and set robots.txt content.

Set this in Website > SEO Configuration > Robots.txt

ECommerce category & product friendly URL's
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Product and ECommerce public category redirecting from custom Odoo URL to new friendly URL by SLUG field.

This part works with shop access rules prevent redirection by user

- For products: **from** *EXAMPLE.COM/shop/product/sku-product-name-id* **to** *EXAMPLE.COM/product/product-name*
- For public categories: **from** *EXAMPLE.COM/shop/category/category-name-id* **to** *EXAMPLE.COM/category/category-name*

Product META fields
~~~~~~~~~~~~~~~~~~~

This module creates a product SEO fields:

- Title
- Description
- Keywords
- Friendly URL (slug)
- Product short description
- Product full description (with WYSIWYG / HTML editor)

Image meta-data
~~~~~~~~~~~~~~~

This module adds meta-attributes **alt** and **title** to the product images.

Also, change the URL structure and remove the *'unique'* part of the image URL.

Favicon
~~~~~~~

Show the favicon in the route *EXAMPLE.COM/favicon.ico* in case of *EXAMPLE.COM/web/image/website/WEBSITE_ID/favicon/*

Set current favicon link to the head.

Progressive web app
~~~~~~~~~~~~~~~~~~~

- Add Manifest.json;
- Add a **Service Worker** (with offline cache) to the Web App.

Set this in Website > SEO Configuration > Web App

__

    **Warning!**

    The Service Worker Offline cache part of this module can include several problems with cache,
    cookies and user sessions.


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
