==========================
Breadcrumbs Base Templates
==========================

.. |badge1| image:: https://img.shields.io/badge/maturity-Production-green.png
    :target: https://odoo-community.org/page/development-status
    :alt: Production
.. |badge2| image:: https://img.shields.io/badge/licence-LGPL--3-blue.png
    :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-Comunitea-lightgray.png?logo=github
    :target: https://github.com/Comunitea/
    :alt: Comunitea
.. |badge4| image:: https://img.shields.io/badge/github-Comunitea%2FeCommerce-lightgray.png?logo=github
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/12.0/breadcrumbs_base_tmp
    :alt: Comunitea / eCommerce
.. |badge5| image:: https://img.shields.io/badge/Spanish-Translated-F47D42.png
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/12.0/breadcrumbs_base_tmp/i18n
    :alt: Spanish Translated

|badge1| |badge2| |badge3| |badge4| |badge5|

This module adds friendly multi-level breadcrumbs bar after "Main menu" block in all web pages.

**Table of contents**

.. contents::
   :local:

Templates
---------

This module adds friendly multi-level breadcrumbs bar in Header after "Main menu" and "Navbar Menu" block in all not Portal web pages, except "My portal Home".

    **Warning!**

    This module removes all other breadcrumb bars from the website but not my account part.

Usage
-----
Three customize views are provided with active by default.

#. No Portal Breadcrumbs
#. My Portal Breadcrumbs
#. Disable Product Breadcrumbs

    **Attention!**

    "No Portal Breadcrumbs" go side by side with "Product Breadcrumbs". There is not possible to be activated at the same time. Be carefully.
    "My Portal Breadcrumbs" view just only add breadcrumbs for my portal home page.


Customization
-------------
Listed below.

Views
~~~~~
This are the three views you can activate or deactivate from web editor to performance your experience.

These views are enabled by default. Just change that on web editor whatever you want.

#. No Portal Breadcrumbs
    - This view enabled Breadcrumbs Bar in all templates and pages except My Portal Home.
#. My Portal Breadcrumbs
    - This view enabled Breadcrumbs Bar in just for My Portal Home
#. Disable Product Breadcrumbs
    - Avoid duplicate breadcrumbs
    - Provide you a better experience working with SEO improvements.

Styles
~~~~~~
This module uses default Bootstrap colors and elements.

If you want to use this module in a theme but you do not like where it is rendered, you can simply
override default colors of this module adding these variables to the less of your theme:

For override default colors of this module **is necessary** to add these restrictions to the less of your theme:

::

        :root {
            --color-bg: you_color or $body-bg;
            --color-href: you_color or $secondary;
            --color-current: you_color or $body-color;
            --crumb-padding: your_padding or 0.75rem 1rem;
            --bar-border: your border or unset;
        }

This module uses default Bootstrap colors and elements.

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
