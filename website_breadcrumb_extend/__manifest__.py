# -*- coding: utf-8 -*-
{
    'name': 'Website Breadcrumb Extend',
    'version': '12.0.0.0.0',
    'summary': 'Add friendly breadcrumbs over along of all website.',
    'category': 'eCommerce',
    'author': 'Comunitea',
    'contributors': [
        'Pavel Smirnov <pavel@comunitea.com>',
        'Rubén Seijas <ruben@comunitea.com>',
    ],
    'website': 'http://www.comunitea.com',
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
        'website_sale',
    ],
    'data': [
        'templates/breadcrumb_bar.xml',
        'views/assets.xml',
        'views/website_page_view.xml',
        'views/breadcrumb_view.xml',
        'views/customize_views.xml',
        'security/ir.model.access.csv',
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [
    ],
}
