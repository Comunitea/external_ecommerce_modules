.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :alt: License: AGPL-3
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html

===============
SEO base module
===============

Website base module for SEO optimization
----------------------------------------

This module contains several modules for different optimizations on the website.

It is compatible with the multi-website.

Sitemap.xml
~~~~~~~~~~~

This module creates a sitemap.xml file in the root path of the website.

You can use the back-end part for the configuration of this map.

Robots.txt
~~~~~~~~~~

This module creates a Robots.txt file in the root path of the website.

You can use the back-end part for the change of cache time and set robots.txt content.

ECommerce category & product friendly URL's
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Product and ECommerce public category redirecting from custom Odoo URL to new friendly URL en base of SLUG field.

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

__

    **Warning!**

    The Service Worker Offline cache part of this module can include several problems with cache,
    cookies and user sessions.


Infinite product scroll
~~~~~~~~~~~~~~~~~~~~~~~

Add the SGEEDE Infinite Scroll module.

You can activate or deactivate this function in the front-end editor.

Javascript front-end
~~~~~~~~~~~~~~~~~~~~

    **Warning!**
    Test mode

Move links of Odoo javascript attachments from HEAD to FOOTER for more productivity and faster page loading speed.

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
