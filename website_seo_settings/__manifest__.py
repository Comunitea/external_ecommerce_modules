# -*- coding: utf-8 -*-

{
    'name': 'Website SEO Settings',
    'version': '1.0',
    'summary': 'Website settings improvements for SEO optimization',
    'description': '',
    'category': 'Website',
    'author': 'Comunitea',
    'website': 'http://www.comunitea.com',
    'license': 'AGPL-3',
    'contributors': [
        'Pavel Smirnov <pavel@comunitea.com>',
        'Rubén Seijas <ruben@comunitea.com>',
    ],
    'depends': [
        'website',
        'website_sale',
        'website_canonical_url',
        'website_google_tag_manager',
    ],
    'data': [
        'templates/access.xml',
        'templates/head.xml',
        'templates/product.xml',
        'templates/robots.xml',
        'templates/shop.xml',
        'templates/sitemap.xml',
        'templates/webapp.xml',
        'views/product_views.xml',
        'views/public_category_views.xml',
        'views/settings_views.xml',
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}
