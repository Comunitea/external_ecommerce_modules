# -*- coding: utf-8 -*-
{
    'name': 'Ecommerce Basic Modules',
    'version': '11.0.1.1.0',
    'summary': 'This module contains modules dependencies for a basic installation of an e-commerce website.',
    'description': '',
    'category': 'Ecommerce',
    'author': 'Comunitea',
    'contributors': [
        'Pavel Smirnov <pavel@comunitea.com>',
        'Rubén Seijas <ruben@comunitea.com>',
    ],
    'website': 'https://www.comunitea.com',
    "support": "info@comunitea.com",
    'license': 'AGPL-3',
    "price": 0,
    "currency": "EUR",
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    'installable': True,
    'application': False,
    'data': [
        'templates/head.xml',
        'templates/footer.xml',
        'templates/contactus.xml',
        'views/website.xml',
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [],
    "live_test_url": "",
    "demo": [],
    "demo_title": "",
    "demo_addons": [],
    "demo_addons_hidden": [],
    "demo_url": "",
    "demo_summary": "",
    "demo_images": [],
    "external_dependencies": {"python": [], "bin": []},
    'depends': [
        # Real Dependencies
        'website',
        'website_crm',
        'website_crm_privacy_policy',
        # Website modules that should be installed for all websites
        'web',
        'web_decimal_numpad_dot',  # Allows using numpad dot to enter period decimal separator even where comma is used.
        'web_diagram',
        'web_dialog_size',  # Lets user expand/restore the dialog box size through a button in the upper right corner
        'web_editor',
        'web_export_view',  # Exporting custom data to CSV/XLS
        'web_kanban_gauge',
        'web_no_bubble',  # Removes from the web interface the bubbles introduced in the version 10.0 but not help boxes
        'web_planner',
        'web_refresher',  # Adds a button next to the pager (in trees/kanban views) to refresh the displayed list.
        'web_responsive',  # It provides a mobile compliant interface.
        'web_sheet_full_width',  # Get full width in the form view sheet
        'website_canonical_url',
        'website_crm',
        'website_crm_recaptcha',
        'website_crm_phone_validation',
        'website_cookie_notice',
        'website_form',
        'website_form_builder',
        'website_form_recaptcha',
        'website_legal_page',
        'website_mail',
        'website_mass_mailing',
        'website_menu_by_user_status',
        'website_odoo_debranding',
        'website_partner',
        'website_payment',
        'payment_redsys',
        'payment_paypal',
        'website_rating',
        'website_theme_install',  # Propose to install a theme on website installation
        'website_sale',
        'website_sale_delivery',
        'website_sale_management',
        'website_sale_options',
        'website_sale_require_legal',  # Forcing the user to accept your legal terms to checkout
        'website_sale_require_login',  # Force users to login before buying anything in the website
        'website_sale_stock_available_display',  # Allow to display available stock in website products
        'website_sale_stock',
        'website_sale_stock_options',
        'website_sale_suggest_create_account',  # suggest the buyer to log in or create an account, but without forcing
        'website_sale_wishlist',  # Let returning shoppers save products in a wishlist
        # Third parts with private licences
        'sgeede_infinite_scroll',  # Allow infinite scroll in Products without using pagination anymore
        'website_maintainance',  # Website Maintenance / Under Construction / Coming Soon
        # Third parts with free licences made by Comunitea
        'seo_base',
        'breadcrumbs_base_tmp',
        # Third parts with free licences made by others
        'muk_website_scroll_up',
    ],
}
