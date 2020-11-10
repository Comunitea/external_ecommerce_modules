# -*- coding: utf-8 -*-

{
    'name': 'Website Blog Extend',
    'version': '11.0.1.0.0',
    'summary': 'Friendly blog extension for eCommerce',
    'description': '',
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
    'qweb': [],
    "live_test_url": "",
    "demo": [],
    "demo_title": "",
    "demo_addons": [],
    "demo_addons_hidden": [],
    "demo_url": "",
    "demo_summary": "",
    "demo_images": [],
    'depends': [
        'website_blog',
        'website_legal_page',
        'website_mail',
    ],
    'data': [
        'views/blog_blog.xml',
        'views/blog_post_view.xml',
        'views/snippets.xml',
        'templates/access.xml',
        'templates/assets.xml',
        'templates/blog.xml',
        'templates/latest_posts.xml'
    ],
    'images': [
        '/static/description/icon.png',
    ],
}
