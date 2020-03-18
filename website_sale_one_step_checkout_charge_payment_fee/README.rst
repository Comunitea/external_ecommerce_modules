Charge Payment Fee in One Step Checkout (OSC)
=============================================

.. |badge1| image:: https://img.shields.io/badge/maturity-Production-green.png
    :target: https://odoo-community.org/page/development-status
    :alt: Production
.. |badge2| image:: https://img.shields.io/badge/licence-LGPL--3-blue.png
    :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-Comunitea-gray.png?logo=github
    :target: https://github.com/Comunitea/
    :alt: Comunitea
.. |badge4| image:: https://img.shields.io/badge/github-Comunitea%2FExternal%20Ecommerce-lightgray.png?logo=github
    :target: https://github.com/Comunitea/external_ecommerce_modules/tree/10.0/website_sale_one_step_checkout_charge_payment_fee
    :alt: Comunitea / Dismac
.. |badge5| image:: https://img.shields.io/badge/Spanish-Translated-F47D42.png
    :target: https://github.com/Comunitea/CMNT_00152_2018_DIS/tree/master/project-addons/theme_dismac/i18n/es.po
    :alt: Spanish Translated


|badge1| |badge2| |badge3| |badge4| |badge5|

**Table of contents**

.. contents::
   :local:

Allows to use payment fee in OSC.
---------------------------------

This is a module that allow to use payment fee in OSC.
And also allow to use this other Comunitea modules:

#. payment_acquirer_by_amount
#. payment_cash_on_delivery

Spinner on OSC
~~~~~~~~~~~~~~

When payment method is used sometimes reload page is required, then a spinner is show loading when payment button is hidden.

You can change the spinner image and the backgroung opacity easily, just define this variables in your archive css to override them:
::

    :root {
        --color-bg: your_bg_color or rgba(255,255,255,0.2);
        --url-bg: your_bg_url or url('/website_sale_one_step_checkout_charge_payment_fee/static/src/img/load-spinner.gif');
    }

Payment Method Info
~~~~~~~~~~~~~~~~~~~

Show an interactive panel info for payments if they have some payment amount restriction.
Also includes a panel footer to redirect for payment info page or contact message if page not exist.

Payment Method Panel
~~~~~~~~~~~~~~~~~~~~
Include a warning panel for choose a payment method if none is checked

Cart
~~~~
#. Include a line with Payment Fee Amount if exist.
#. Control for digital products.

Cash on Delivery Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. Exclude payment fee and packs lines if exist from cart and cart popover.
#. Hide cash on delivery order line and products packs in review order

Payment Acquirer by Amount
~~~~~~~~~~~~~~~~~~~~~~~~~~
#. Show error when just one acquirer is published and amounts conditions do not let select it
#. Show acquirers or not by amount conditions

Payment Buttons
~~~~~~~~~~~~~~~
Replace Configure button text from only transfer use to a generic payment acquirer.

Payment Mode
~~~~~~~~~~~~
Associate mode payment with payment method to link website orders if exist a relation ship if it is needed.

Credits
=======

Author
------

Developer: Comunitea, info@comunitea.com

Contributors
~~~~~~~~~~~~

Rubén Seijas, ruben@comunitea.com
Pavel Smirnov <pavel@comunitea.com>

Maintainer
~~~~~~~~~~

This module is maintained by Comunitea.

For support and more information, please visit https://comunitea.com.

Disclaimer of Warranties
------------------------

    **Attention!**

    We provide this module as is, and we make no promises or guarantees about this correct working.

Comunitea provides this application without warranty of any kind.

Comunitea does not warrant that the module will meet your requirements;
that the current application will be uninterrupted, timely, secure, or error-free or that any defects or errors will be corrected.
