# -*- coding: utf-8 -*-

{
    'name': 'Website SEO Optimization',
    'version': '11.0.0.0.0',
    'summary': 'This module contains several improves for different '
               'optimizations on the website.',
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
    ],
    'data': [
        'views/product_meta.xml',
        'views/public_category.xml',
        'views/settings.xml',
        'views/menu.xml',
        'templates/favicon.xml',
        'templates/head.xml',
        'templates/product.xml',
        'templates/robots.xml',
        'templates/seo.xml',
        'templates/sitemap.xml',
        'templates/shop.xml',
        'templates/webapp.xml',
        'templates/access.xml',
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}
