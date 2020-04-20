# -*- coding: utf-8 -*-
{
    'name': 'Ecommerce Basic Modules',
    'version': '11.0.1.3.0',
    'summary': 'Some custom features for a basic installation of an e-commerce website.',
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
    'data': [
        'templates/head.xml',
        'templates/portal.xml',
        'templates/footer.xml',
        'templates/contactus.xml',
        'views/website.xml',
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [],
    'depends': [
        'portal',
        'website',
        'website_crm',
        'website_crm_privacy_policy',
    ],
}
