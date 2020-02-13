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
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/12.0/breadcrumbs_base_tmp
    :alt: Comunitea / eCommerce

|badge1| |badge2| |badge3| |badge4|

**Table of contents**

.. contents::
   :local:

Additional templates for Breadcrumbs Base Module
------------------------------------------------

This module adds friendly multi-level breadcrumbs bar in Header after "Main menu" and "Navbar Menu" block in all not Portal web pages, except "My portal Home".

    **Attention!**

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
If you want to use this module in a theme but you do not like where it is rendered, you can simply
override default colors of this module adding these variables to the less of your theme:

::

        :root {
            --color-bg: you_color; (#fff by default)
            --color-href: you_color; (#337ab7 by default)
            --color-current: you_color; (#777 by default)
        }

This module uses default Bootstrap colors and elements.

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
