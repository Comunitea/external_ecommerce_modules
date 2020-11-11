======================
Website Affix Top Menu
======================

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
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/11.0/website_sale_affix_header
    :alt: Comunitea / Affix Header
.. |badge5| image:: https://img.shields.io/badge/Spanish-Translated-F47D42.png
    :target: https://github.com/Comunitea/external_ecommerce_modules/blob/11.0/website_blog_base/i18n/es.po
    :alt: Spanish Translated

|badge1| |badge2| |badge3| |badge4| |badge5|

This module let you affix the top menu in header to top on the website when scrolling by customize view on web editor.

**Table of contents**

.. contents::
   :local:

What it does
------------
This module let you affix the top menu in header to top on the website when scrolling by customize view on web editor.

    **Warning**

    This view is deactivated by default.

    You have to activate it to make it works.

How it works
------------
Log into your website as an web editor user.

- Go to Customize > Main Layout > Affix Header
    * Activate customize view

When the view is active then the header will be affix on the top of the page and always will be visible.

Animations
----------
When scrolling and the menu is fixed then add an animated shadow on the bottom.

Integrations
------------
It works with Breadcrumbs Extend module ('breadcrumbs_base') created by 'Comunitea Servicios Tecnológicos S.L.'

Shadow Animation
~~~~~~~~~~~~~~~~
When Breadcrumbs Extend module ('breadcrumbs_base') is installed then shadow animation is used by this module
otherwise is provided by this module.

Even if  Breadcrumbs Extend module ('breadcrumbs_base') is installed but is no present in any page then
shadow animation will works anyway.

How to customize it
-------------------

    **Warning!**

    By defauft include an animation to became transparent when scrolling

    Put 'none' on global variables to override it and not use it.

Just inside your custom styles, override this global variables as you wish:

::

    :root {
        --affix-header-bg-color: your_color or #f8f8f8; // navbar default color
        --affix-header-z-index: your_index or 999;
        --affix-header-animation-name: your_animation_name or opacity_frame or none;
        --affix-header-animation-duration: your_animation_duration or 0.3s or none;
        --affix-header-animation-delay: your_animation_delay or 0s or none;
    }

Also you can create your owns animations and placed them by global variables like this:

::

    @keyframes opacity_frame {
      from {opacity: 1;}
      to {opacity: 0;}
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
Rubén Seijas (ruben@comunitea.com)

Maintainer
~~~~~~~~~~
.. image:: https://comunitea.com/wp-content/uploads/2016/01/logocomunitea3.png
   :alt: Comunitea
   :target: https://comunitea.com

Comunitea Servicios Tecnológicos S.L.

For support and more information, please visit `<https://comunitea.com>`_.

Known issues / Roadmap
----------------------

This module has the following limitations:

 * It will not work as long as cookies are not accepted.
 * When cookies are already accepted you need to change the page or manually reload it to see the header affix on the top of the page.
 * TODO: Be able to establish the position of the scroll from which you want to affix the header.

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

    `Comunitea <https://comunitea.com>`_ provides this application without warranty of any kind.

    `Comunitea <https://comunitea.com>`_ does not warrant that the module will meet your requirements;
    that the current application will be uninterrupted, timely, secure, or error-free or that any defects or errors will be corrected.
