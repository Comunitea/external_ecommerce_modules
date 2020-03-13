# -*- coding: utf-8 -*-

{
    'name': 'SEO Base',
    'version': '10.0.0.0.0',
    'summary': 'Module for Website SEO Optimization',
    'description': '',
    'category': 'Website',
    'author': 'Comunitea',
    'website': 'http://www.comunitea.com',
    'license': 'AGPL-3',
    'contributors': [
        'Rubén Seijas <ruben@comunitea.com>',
    ],
    'depends': [
        'product',
        'website',
        'website_sale',
        'website_sale_wishlist',
    ],
    'data': [
        'templates/layout.xml',
        'templates/product.xml',
        'templates/shop.xml',
        'views/product_view.xml',
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}
