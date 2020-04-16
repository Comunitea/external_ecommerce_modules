==========================
Breadcrumbs Base Templates
==========================

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
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/11.0/breadcrumbs_base_tmp
    :alt: Comunitea / eCommerce

|badge1| |badge2| |badge3| |badge4|

This module adds friendly multi-level breadcrumbs bar after "Main menu" block in all web pages.

**Table of contents**

.. contents::
   :local:

How it works
------------

This module adds friendly multi-level breadcrumbs bar after "Main menu" block in all web pages.

    **Attention!**

    This module removes all other breadcrumb bars from the website and my account part by default.

    Otherwise you have to disabled them in the web editor

Customize views
~~~~~~~~~~~~~~~
This are the three views you can activate or deactivate from web editor to performance your experience.

These views are enabled by default. Just change that on web editor whatever you want.

#. Breadcrumbs Bar
    - This view enabled Breadcrumbs Bar in all templates and pages.
#. Disable Shop Breadcrumbs Bar
    - This view removes default shop Breadcrumbs Bar.
    - Avoid duplicate breadcrumbs
    - Provide you a better experience working with SEO improvements.
#. Disable My Portal Breadcrumbs Bar
    - This view removes default portal Breadcrumbs Bar.
    - Avoid duplicate breadcrumbs
    - Provide you a better experience working with SEO improvements.
    - Include always a reference for My portal Home and not to loose that reference when you navigate into your documents.
    - Include a Home link integrated with My Portal Home link

Styles
~~~~~~
This module uses default Bootstrap colors and elements.

For override default colors of this module **is necessary** to add these restrictions to the less of your theme:

::

    :root {
        --color-bg: you_color or #fff;
        --color-href: you_color or #337ab7;
        --color-current: you_color or #777;
    }

Author
------
.. image:: https://comunitea.com/wp-content/uploads/2016/01/logocomunitea3.png
   :alt: Comunitea
   :target: https://comunitea.com

Comunitea Servicios Tecnológicos S.L.

For support and more information, please visit `<https://comunitea.com>`_.

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
