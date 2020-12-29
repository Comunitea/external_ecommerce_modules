========================
Website SEO Optimization
========================

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

This module contains several improves for different optimizations on the website.

It is compatible with the multi-website.

**Table of contents**

.. contents::
   :local:

Analytics
~~~~~~~~~

Integration with analytical systems:

* Google Tag Manager
* Facebook Pixel

Set this in Website > SEO Configuration > Analytics

Shop
~~~~
Access rules:

#. You can manage your shop access. True by default.
#. If you wish may enable for user type (B2B or B2C).

Set this in Website > SEO Configuration > General > Public Shop

Sitemap.xml
~~~~~~~~~~~

#. This module creates a sitemap.xml file in the root path of the website.
#. You can use the back-end part for the configuration of this map.

Set this in Website > SEO Configuration > Sitemap.xml

Robots.txt
~~~~~~~~~~

#. This module creates a Robots.txt file in the root path of the website.
#. You can use the back-end part for the change of cache time and set robots.txt content.

Set this in Website > SEO Configuration > Robots.txt

Friendly URL's
~~~~~~~~~~~~~~

Website
-------

In Website Builder, eCommerce, Blog, etc. Odoo add parameters in URLs, like category,
page or sorting. This is a bad thing for SEO because it creates DUST (Duplicate URL,
Same Text) and Duplicate Content. That is to say, multiple URLs that leads to the same
page search engine's index.

Because of this is includes website_canonical_url module dependency.

* Configuration

    #. Canonical URL is absolute. The domain name by default matches
    #. "Settings / Technical / System Parameters / web.base.url"
    #. This might not be enough to make sure that you have always one and only one URL to access your resources.
    #. You can force the domain by setting "Canonical domain" field into website settings.

ECommerce category & product
----------------------------
#. Product and ECommerce public category redirecting from custom Odoo URL to new friendly URL by SLUG field.
#. This part works with shop access rules prevent redirection by user
    * For products: **from** *EXAMPLE.COM/shop/product/sku-product-name-id* **to** *EXAMPLE.COM/product/product-name*
    * For public categories: **from** *EXAMPLE.COM/shop/category/category-name-id* **to** *EXAMPLE.COM/category/category-name*

Product
~~~~~~~

Guarantee
---------
Hide default guarantee text in product template.

META fields
-----------

This module creates a product SEO fields:

#. Title
#. Description
#. Keywords
#. Friendly URL (slug)
#. Product short description
#. Product full description (with WYSIWYG / HTML editor)

Image meta-data
~~~~~~~~~~~~~~~
#. This module adds meta-attributes **alt** and **title** to the product images.
#. Also, change the URL structure and remove the *'unique'* part of the image URL.

Favicon
~~~~~~~
* Show the favicon in the route *EXAMPLE.COM/favicon.ico* in case of *EXAMPLE.COM/web/image/website/WEBSITE_ID/favicon/*

Set current favicon link to the head.

Progressive web app
~~~~~~~~~~~~~~~~~~~
#. Add Manifest.json;
#. Add a **Service Worker** (with offline cache) to the Web App.

Set this in Website > SEO Configuration > Web App

    **Warning!**

    The Service Worker Offline cache part of this module can include several problems with cache,
    cookies and user sessions.

Author
~~~~~~
Developer: Comunitea, info@comunitea.com

Contributors
------------
* Pavel Smirnov, pavel@comunitea.com
* Rubén Seijas, ruben@comunitea.com

Maintainer
~~~~~~~~~~
.. image:: https://comunitea.com/wp-content/uploads/2016/01/logocomunitea3.png
   :alt: Comunitea
   :target: https://comunitea.com

Comunitea Servicios Tecnológicos S.L.

For support and more information, please visit `<https://comunitea.com>`_.

Known Issues
------------
By default uses Product Internal Description as Website Product Description instead 'website_description'.
Nothing happen if Internal Description is not used for internal purposes but if it is needed, then you have to:

* Override product views to change 'description' for 'website_description' in:
    * website_sale_product_add (Product Seo Base)
    * seo_base_product_meta (Seo base product meta fields)
* Delete or comment internal Description replacement in:
    * seo_base_product_meta (Seo base product meta fields)
        * <xpath expr="//group[@name='description_internal']" position="replace"/>
* Create an Scheduled Action like this to convert existing internal descriptions to HTML
    * model.description_plaintext2html()

        **Warning!**

        Descriptions are normalized to prevent different codifications.

        Depending of number of products to convert maybe you need run manually with flag --workers=0

.. image:: /seo_base/static/img/scheduled_actions.png
   :alt: Convert Product Internal Descriptions from PlainText to HTML

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
