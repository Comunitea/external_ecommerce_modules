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

|badge1| |badge2| |badge3| |badge4|

**Table of contents**

.. contents::
   :local:

eCommerce Friendly Breadcrumbs
------------------------------
This module adds friendly multi-level breadcrumbs for your WEB.

**Attention!**

    This module don't have templates for front-end part of website.

    For correct front-end functionality you need to install additional module **breadcrumbs_base_tmp**.

How it works
~~~~~~~~~~~~
The Breadcrumbs generator is available to call in any template:

::

    <t t-call="breadcrumbs_base.breadcrumbs_bar"/>

Foreach template that contain it, then a breadcrumb will be created and activate by default.

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
#. Blog Post
#. Main object
    When there is nothing at all previous. Generate a breadcrumbs by main_object.
    If main_object have _description filed then is used
    like 'home / %s / %s' % (main_object._description, main_object.name).
    Otherwise 'home / %s' % main_object.name.

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
