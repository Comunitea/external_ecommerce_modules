# -*- coding: utf-8 -*-

{
    'name': 'Breadcrumbs Base',
    'version': '11.0.2.1.0',
    'summary': 'Friendly breadcrumbs for eCommerce',
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
    'depends': [
        'website',
        'website_sale'
    ],
    'data': [
        'views/page_view.xml',
        'views/breadcrumbs_views.xml',
        'templates/breadcrumbs.xml',
        'security/ir.model.access.csv',
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [
    ],
    "live_test_url": "",
    "demo": [],
    "demo_title": "",
    "demo_addons": [],
    "demo_addons_hidden": [],
    "demo_url": "",
    "demo_summary": "",
    "demo_images": [],
    "external_dependencies": {"python": [], "bin": []},
}
