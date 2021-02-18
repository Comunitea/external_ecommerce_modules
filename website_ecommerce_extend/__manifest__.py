# -*- coding: utf-8 -*-
{
    'name': 'Website eCommerce Extend',
    'version': '12.0.1.2.2',
    'summary': 'Extend Website for eCommerce customization',
    'category': 'eCommerce',
    'author': 'Comunitea',
    'contributors': [
        'Pavel Smirnov <pavel@comunitea.com>',
        'Rubén Seijas <ruben@comunitea.com>',
    ],
    'website': 'http://www.comunitea.com',
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
    "live_test_url": "",
    "demo": [],
    "demo_title": "",
    "demo_addons": [],
    "demo_addons_hidden": [],
    "demo_url": "",
    "demo_summary": "",
    "demo_images": [],
    "external_dependencies": {
        "python": [], "bin": []
    },
    'depends': [
        'website',
        'website_crm',
        'website_crm_privacy_policy',
        'website_sale_wishlist',
    ],
    'data': [
        'templates/assets.xml',
        'templates/contactus.xml',
        'templates/footer.xml',
        'templates/header.xml',
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [
    ],
}
