# -*- coding: utf-8 -*-
{
    'name': 'Breadcrumbs Base Templates',
    'version': '12.0.0.1.0',
    'summary': 'Add customize templates and styles for Breadcrumbs Base module',
    'description': '',
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
        'breadcrumbs_base'
    ],
    'data': [
        'templates/breadcrumbs_bar.xml',
        'templates/head.xml',
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [
    ],
}
