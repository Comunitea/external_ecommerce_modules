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
.. |badge4| image:: https://img.shields.io/badge/github-Comunitea%2FeCommerce-lightgray.png?logo=github
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/10.0/seo_base
    :alt: Comunitea / eCommerce
.. |badge5| image:: https://img.shields.io/badge/Spanish-Translated-F47D42.png
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/10.0/seo_base/i18n/es.po
    :alt: Spanish Translated

|badge1| |badge2| |badge3| |badge4| |badge5|

This module contains some SEO optimizations on the website.

**Table of contents**

.. contents::
   :local:

Products
--------

#. Add new fields.

    * description_short
        * Added in product detail template before description_sale. Only used there.
    * description
        * An effective an complete HTML description added in product detail template instead website_description.
    * hide_website_price
        * If selected, hide price and 'add to cart', 'add to wishlist' and 'add qty' buttons. 'N/D' is shown instead.

#. Replace Website group in Sales Page in Product Form and add all Website features in New Website Page in Product Form

Product Public Categories
-------------------------

Add slug field for Friendly URL Redirection.

Friendly URL's
--------------

Add a slug field for Products and Product Public Categories for Friendly URL Redirection.

* It is included into Forms and Tree Views.
* Have a slug validation
* It is automatic placed on create and write based on object name

TODO
~~~~

Located and replace all links for products and categories. Replace by some like this:

* '/product/{}'.format(product.slug) if product.slug else keep('/shop/product/%s' % slug(product))

Author
------

Developer: Comunitea, info@comunitea.com

Contributors
~~~~~~~~~~~~

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
