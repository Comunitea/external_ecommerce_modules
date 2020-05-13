================
Breadcrumbs Base
================

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
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/11.0/breadcrumbs_base
    :alt: Comunitea / eCommerce
.. |badge5| image:: https://img.shields.io/badge/Spanish-Translated-F47D42.png
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/11.0/breadcrumbs_base/i18n
    :alt: Spanish Translated

|badge1| |badge2| |badge3| |badge4| |badge5|

**Table of contents**

.. contents::
   :local:

eCommerce Friendly Breadcrumbs
------------------------------
This module adds friendly multi-level breadcrumbs for your website but just providing a template to be called from any template.

If you wish have a complete experience you must install additional module **'breadcrumbs_base_tmp'** provided as well.

    **Warning!**

    This module don't have templates for front-end part of website.

    For correct front-end functionality you need to install additional module **'breadcrumbs_base_tmp'**.

How it works
~~~~~~~~~~~~
The Breadcrumbs generator is available to call in any template:

::

    <t t-call="breadcrumbs_base.breadcrumbs_bar"/>

Foreach template that contain it, then a breadcrumb will be created and activate by default.

    **Warning!**

    If you call it from any portal templates you have to install **'breadcrumbs_base_tmp'** module and
    disable **'Disable My Account Breadcrumbs Bar'** view on web editor.
    Otherwise you will have two breadcrumbs at the same time, this and portal default breadcrumbs.

Style
_____
Add a shadow with a border bottom when scrolling to differentiate the body content of the breadcrumbs bar

Portal
~~~~~~
Include always a reference for My portal Home and not to loose that reference when you navigate into your documents.

Also include a Home link integrated with My Portal Home link.

Settings
~~~~~~~~

You have a Breadcrumbs menu into Website Settings to manage your breadcrumbs.

Only published crumbs are visible in the website. You can also change the name.

You can set it in the Breadcrumbs menu.

Generated breadcrumbs
~~~~~~~~~~~~~~~~~~~~~
All models included for breadcrumbs are:

#. Product Templates
#. Product Tags
#. Ecommerce Categories
#. Website Pages
    Moreover, this module adds parent_id field to website.page model. This allows to add parent page for static pages.
#. Views
#. Blogs
#. Blog Posts
#. Slides Channels
#. Slides
#. Main object
    When there is nothing at all previous. Generate a breadcrumbs by main_object.
    If main_object have _description filed then is used
    like 'home / %s / %s' % (main_object._description, main_object.name).
    Otherwise 'home / %s' % main_object.name.

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

    **Warning!**

    We provide this module as is, and we make no promises or guarantees about this correct working.

Comunitea provides this application without warranty of any kind.

Comunitea does not warrant that the module will meet your requirements;
that the current application will be uninterrupted, timely, secure, or error-free or that any defects or errors will be corrected.
