====================
Website Settings SEO
====================

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
.. |badge5| image:: https://img.shields.io/badge/github-Comunitea%2FSEO-lightgray.png?logo=github
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/12.0/website_seo_settings
    :alt: Comunitea / SEO
.. |badge6| image:: https://img.shields.io/badge/Spanish-Translated-F47D42.png
    :target: https://github.com/Comunitea/external_ecommerce_modules/blob/12.0/website_seo_settings/i18n/es.po
    :alt: Spanish Translated


|badge1| |badge2| |badge3| |badge4| |badge5| |badge6|

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
#. Access rules:
    * You can manage your shop access.
    * Shop open for public users by default. Otherwise, the access rules must be established.
        #. Only B2B users
        #. Only B2C users

    * Set this in Website > Configuration > SEO > General > Public Shop

#. Shop product list
    * Add new customize views:
        * Responsive View
            * Change table view with responsible divs
        * Responsive View full
            * Extend responsive view to expand container width
            * **Warning!** Needs 'Responsive View' active to work properly
        * Category Images
            * With or without collapse options

    * Border for product container in responsive views via bootstrap_overriden file:
        * $oe_product_border and/or $oe_product_detail_border

Cart
~~~~
#. Refactor Product Suggested view under cart buttons to separate from cart lines
#. Add Alternate Products view under cart buttons to separate from cart lines

Products
~~~~~~~~
#. Add customize view for default code
#. Add customize view to put name for price
#. Add customize view for promotions ribbons
#. Refactor view for Alternate Products
#. Add customize view for Product Suggested

For links on these views you can let use tag color or define yours via bootstrap_overriden file:
    * $oe-product-tag-link-color
    * $oe-product-tag-link-decoration
    * $oe-product-tag-link-padding: 0.375rem 0.75rem !default; // Ex for sm: 0.0625rem 0.3125rem
    * $oe-product-tag-link-font-size: 0.875rem !default; // Ex for sm: 0.75rem

For carousel image controls you can define yours via bootstrap_overriden file:
    * $carousel-control-color
    * $carousel-control-color-hover
    * $carousel-control-width
    * $carousel-control-opacity
    * $carousel-indicator-box-shadow
    * $carousel-indicator-margin
    * $carousel-indicator-max-width

Add shadow and border for product images in shop, product detail, alternate and suggested products but you can define yours via bootstrap_overriden file
    * $oe-product-border
    * $oe-product-border-hover
    * $oe-product-border-detail
    * $oe-product-border-detail-hover
    * $box-shadow-product (This change all with same shadow)
    * $box-shadow-product-hover (This change all with same shadow)
    * $box-shadow-product-list
    * $box-shadow-product-list-hover
    * $box-shadow-product-detail
    * $box-shadow-product-detail-hover
    * $box-shadow-product-alternate
    * $box-shadow-product-suggested

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
#. Products Tags
    * Add product template tags over categories on left side bar
    * Include metadata and slug fields with redirection
    * Works with website sale search
    * You can use this colors as well
        * 1: #dc3545,
        * 2: #fd7e14,
        * 3: #F7CD1F,
        * 4: #6CC1ED,
        * 5: #814968,
        * 6: #EB7E7F,
        * 7: #2C8397,
        * 8: #475577,
        * 9: #D6145F,
        * 10: #30C381,
        * 11: #9365B8,
#. Category Customize views
    * Add customize view for category list
    * Add customize view for category tag list
    * Include field color like as products tags
    * Category Images
        * With or without collapse options
#. Grid Style
    * Provide via bootstrap_overriden file some variables to apply same style that on products.
        * $oe-grid-before-border: $oe-product-border;
        * $oe-grid-before-border-hover: $oe-product-border-hover;
        * $oe-grid-before-padding: 1rem 0.2rem 0.5rem 1rem;
        * $oe-grid-before-box-shadow: $box-shadow-product;
        * $oe-grid-before-box-shadow-hover: $box-shadow-product-hover;
        * $oe-grid-before-title-border-bottom: 1px solid rgba(100, 100, 100, 1);
        * $oe-grid-before-categ-margin-top: if($oe-grid-before-border == $oe-product-border, 1rem, inherit);
    * Nav Items
        * $oe-grid-before-nav-item-link-padding: 0.6rem 0.2rem !default;
        * $oe-grid-before-nav-item-img-margin: 0.5rem 0.5rem 0.5rem 0.2rem !default;
        * $oe-grid-before-nav-item-img-border: $oe-product-border !default;
        * $oe-grid-before-nav-item-img-border-hover: $oe-product-border-hover !default;
        * $oe-grid-before-nav-item-img-box-shadow: if($oe-grid-before-nav-item-img-border == $oe-product-border, $box-shadow-product, unset) !default;
        * $oe-grid-before-nav-item-img-box-shadow-hover: if($oe-grid-before-nav-item-img-box-shadow == $box-shadow-product, $box-shadow-product-hover, unset) !default;
        * $oe-grid-before-nav-item-border-bottom: unset !default; // 1px solid rgba(100, 100, 100, 0.2);
        * $oe-grid-before-nav-item-border-bottom-hover: unset !default; // 1px solid $secondary;
        * $oe-grid-before-nav-item-border-top: unset !default; // 1px solid rgba(100, 100, 100, 0.2);
    * Just override and set to unset these variables if you do not want them:
        * $oe-grid-before-border: unset;
        * $oe-grid-before-border-hover: unset;
    *

::

    **Warning!**

    Product Tags are placed inside product_grid_before so Categories customize view have to enabled.


#. Include default code inside product item but truncate text for height style

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
------
Comunitea Servicios Tecnológicos S.L.

Contributors
------------
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

#. Responsive View full needs 'Responsive View' active to work properly.

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
