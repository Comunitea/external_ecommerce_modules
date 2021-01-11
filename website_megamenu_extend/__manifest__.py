# -*- coding: utf-8 -*-
{
    "name": "Website Megamenu Extend",
    'version': '12.0.0.0.0',
    "summary": "Extension features of website_megamenu OCA module",
    'description': '',
    "category": "Menu/Megamenu",
    'author': 'Comunitea',
    'contributors': [
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
        # OCA / Odoo
        'website',
        'website_megamenu',
        # Comunitea
        'website_seo_settings',
    ],
    'data': [
        'templates/snippets.xml'
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [
    ],
}
