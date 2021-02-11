=======================
Website Megamenu Extend
=======================

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
    :target: https://github.com/comunitea/external_ecommerce_modules
    :alt: Comunitea / eCommerce
.. |badge5| image:: https://img.shields.io/badge/Spanish-Translated-F47D42.png
    :target: https://github.com/comunitea/external_ecommerce_modules/website_megamenu_extend/i18n/es.po
    :alt: Spanish Translated


|badge1| |badge2| |badge3| |badge4| |badge5|

**Table of contents**

.. contents::
   :local:

This module is just an extension features of **website_megamenu** OCA module.

Usage
-----
It the same as original module. You can use new features or not.

New Features
------------
#. Add a new unique custom snippet template for different usages
    * **<template id="mega_menu_category_and_products" name="Multi-Menus Custom">**

#. The custom snippet render columns dynamically in based on the number of categories to display
    * col-lg-3 empty at the end and the beginning for 2
    * col-lg-4 for 3
    * col-lg-3 otherwise

#. Add new fields over model **website.menu** to configure the snippet throw model **website** methods:
    #. mega_menu_module_name (To use yor custom snippet. Default empty)
    #. mega_menu_template_name (To use yor custom snippet. Default empty)
    #. mega_menu_hierarchy (To only get parent categories with child_ids. Default True)
    #. mega_menu_product_categories (To include product categories inside categories too. Default False)
    #. mega_menu_category_domain (Pass a custom domain for add categories to default domain. Default empty)
    #. mega_menu_category_domain_only_child (Define if you want show only categories parent or only categories chlid for custom domain. Default False)

#. Default domain just retrieve the published categories for current website

#. XML Sample:

::

    <record id="menu_name_menu" model="website.menu">
        <field name="name">Menu Name</field>
        <field name="parent_id" ref="website.main_menu"/>
        <field name="sequence" type="int">30</field>
        <field name="website_id" ref="website.default_website"/>
        <field name="is_mega_menu">True</field>
        <field name="mega_menu_module_name" eval="'your_module_name'"/>
        <field name="mega_menu_template_name" eval="'your_template_name'"/>
        <field name="mega_menu_hierarchy">True</field>
        <field name="mega_menu_product_categories">False</field>
        <field name="mega_menu_category_domain" eval="['&amp;', ('id', '!=', obj(ref('record_id')).id), ('id', '!=', obj(ref('record_id')).id)]" model="product.public.category"/>
        <field name="mega_menu_category_domain_only_child">False</field>
    </record>

How it works
------------
Now you can available to create a dynamics mega menus by categories with/without products and they remain editable on web editor.

By default, if you do not configure your custom menu, it creaye one with all parents categories that have some child.

If you do not fill your custom snippet template and change hierarchy to **False**, then use **website_megamenu** default snippet.

When you use your custom domain probably you want hierarchy to **False** too (By default). Also admit one OR or AND condition.

In your custom domain you have to indicate how you want normalize with default domain with ('|') or ('&amp;'). It will be replace before normalize.

Snippet Template
----------------
Control over len of categories to keep template structure.

    * Max two rows
    * Max four columns per row
    * Min and Max three subcategories per category in hierarchy cases
    * Max sixteen subcategories per category in NOT hierarchy cases

Credits
-------

Author
~~~~~~
Comunitea Servicios Tecnológicos S.L.

Contributors
~~~~~~~~~~~~
Rubén Seijas, ruben@comunitea.com

Maintainer
~~~~~~~~~~
This module is maintained by Comunitea.

For support and more information, please visit https://comunitea.com.

.. image:: https://comunitea.com/wp-content/uploads/2016/01/logocomunitea3.png
   :alt: Comunitea
   :target: https://comunitea.com

Known Issues / Roadmap
----------------------
* When you delete a menu record then on module update all menus will be computed not only deleted one.

Your are welcome to reported any other issue.

Bug Tracker
-----------
Bugs are tracked on `Comunitea Issues <https://github.com/Comunitea/external_ecommerce_modules/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`Feedback <https://github.com/Comunitea/external_ecommerce_modules/issues/new>`_.

Please, do not contact contributors directly about support or help with technical issues.

Disclaimer of Warranties
~~~~~~~~~~~~~~~~~~~~~~~~

    **Warning!**

    We provide this module as is, and we make no promises or guarantees about this correct working.

Comunitea provides this application without warranty of any kind.

Comunitea does not warrant that the module will meet your requirements;
that the current application will be uninterrupted, timely, secure, or error-free or that any defects or errors will be corrected.
