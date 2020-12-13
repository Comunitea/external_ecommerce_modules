# -*- coding: utf-8 -*-

{
    'name': 'Website Affix Top Menu',
    'version': '11.0.0.0.4',
    'summary': 'Module to affix top menu in header to top on the website '
               'when scrolling by customize view via web editor',
    'description': '',
    'category': 'eCommerce',
    'author': 'Comunitea',
    'contributors': [
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
    'application': True,
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
        'website',
    ],
    'data': [
        'templates/assets.xml',
        'templates/header.xml',
    ],
    'images': [
        '/static/description/icon.png',
    ],
}
