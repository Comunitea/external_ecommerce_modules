# -*- coding: utf-8 -*-
{
    'name': 'Product Brand Extend',
    'version': '12.0.0.0.0',
    'summary': 'Extension features of website_sale_product_brand OCA module',
    'category': 'eCommerce',
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
        'product_brand',
        'website_sale_product_brand',
        "website_menu_by_user_status",
    ],
    'data': [
        'data/website_menu.xml',
        'templates/product_brand.xml',
        'views/assets.xml',
        'views/product_brand_views.xml',
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [
    ],
}
