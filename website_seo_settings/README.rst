====================
Website Settings SEO
====================

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
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/12.0/website_seo_settings
    :alt: Comunitea / SEO
.. |badge5| image:: https://img.shields.io/badge/Spanish-Translated-F47D42.png
    :target: https://github.com/Comunitea/external_ecommerce_modules/blob/12.0/website_seo_settings/i18n/es.po
    :alt: Spanish Translated


|badge1| |badge2| |badge3| |badge4| |badge5|

This app contains several improvements for SEO optimizations on the website settings.

**Table of contents**

.. contents::
   :local:

Analytics
~~~~~~~~~

Add integration with analytical system:

* Facebook Pixel

Set this in Website > SEO Configuration > Analytics

Including modules dependence to put all SEO settings in the same place.

    #. Google Analytics
        * Technical name: website
    #. Google Tag Manager
        * Technical name: website_google_tag_manager

Shop
~~~~
Access rules:

* You can manage your shop access.
* Shop open for public users by default. Otherwise, the access rules must be established.
    #. Only B2B users
    #. Only B2C users

Set this in Website > Configuration > SEO > General > Public Shop

Sitemap.xml
~~~~~~~~~~~

* Improve and update the sitemap.xml file in the root path of the website.
* You can configure what is included/excluded and also view your sitemap in website settings.
    #. Favicon
    #. Blog pages and blog posts
    #. Products and categories
    #. Include images for Products and categories
    #. Let set update frequency and urls priority
    #. Robots.txt

Set this in Website > Configuration > SEO > Sitemap.xml

Robots.txt
~~~~~~~~~~

* Create a Robots.txt file in the root path of the website.
* You can configure what is included and view your sitemap.

Set this in Website > Configuration > SEO > Robots.txt

    This field not support html tags. Just plain text.
    Make sure you only put a resource by line and press enter

Friendly URL's
~~~~~~~~~~~~~~

Let you enable set your slug field length between 20 and 99 characters.

    In Website Builder, eCommerce, Blog, etc. Odoo add parameters in URLs, like category,
    page or sorting. This is a bad thing for SEO because it creates DUST (Duplicate URL,
    Same Text) and Duplicate Content. That is to say, multiple URLs that leads to the same
    page search engine's index.

    Because of this is includes website_canonical_url module dependency.

    Configuration

    #. Canonical URL is absolute. The domain name by default matches
    # Set it in: Website > Settings > Website > Canonical domain
    #. Check it in: Settings > Technical > System Parameters > web.base.url
    #. This might not be enough to make sure that you have always one and only one URL to access your resources.
    #. You can force the domain by setting "Canonical domain" field into website settings.
    #. More info: https://support.google.com/webmasters/answer/139066

ECommerce Public Categories and Products
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Product and ECommerce public category redirecting from custom Odoo URL to new friendly URL by SLUG field.
#. This part works with shop access rules prevent redirection by user

    * For products: **from** *EXAMPLE.COM/shop/product/sku-product-name-id* **to** *EXAMPLE.COM/product/product-name*
    * For public categories: **from** *EXAMPLE.COM/shop/category/category-name-id* **to** *EXAMPLE.COM/category/category-name*

Guarantee
---------
Hide default guarantee text in product template.

META fields
-----------

Add SEO meta fields that work with main_object and his metadata workflow in website layout

#. Title
#. Description
#. Keywords
#. Friendly URL (Slug) with a maximum length
#. Product short description
#. Product full description (with WYSIWYG / HTML editor)

Image meta-data
~~~~~~~~~~~~~~~

#. Adds meta-attribute **title** to the product images in product detail carousel.
#. Also, change the URL structure and remove the *'unique'* part of the image URL.

Favicon
~~~~~~~

* Show the favicon in the route *EXAMPLE.COM/favicon.ico* in case of *EXAMPLE.COM/web/image/website/WEBSITE_ID/favicon/*

Set current favicon link to the head.

Web Progressive App (WPA)
~~~~~~~~~~~~~~~~~~~~~~~~~

#. Add a manifest.json at the project root
#. Add a **Service Worker** to the Web Progressive App.
#. You can set your app design (Name, description, logo, color, ...)
#. Activate or deactivate cache and console messages
#. Add to cache any resources
#. Add to manifest your onw code
#. Add a link for Add to Home Screen dialog inside user menu

Set this in Website > Configuration > SEO > Web Progressive App

    **Warning!**

    The Service Worker Offline cache part of this module can include several problems with cache,
    cookies and user sessions.
    Because of this, you can activate or deactivate it.
    Also you can activate or deactivate cache and console messages to debugger it.

Author
~~~~~~

Developer: Comunitea, info@comunitea.com

Contributors
------------

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
