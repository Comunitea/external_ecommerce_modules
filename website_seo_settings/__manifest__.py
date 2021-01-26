# -*- coding: utf-8 -*-

{
    'name': 'Website SEO Settings',
    'version': '12.0.3.0.0',
    'summary': 'Website settings improvements for SEO optimization',
    'description': '',
    'category': 'Website',
    'author': 'Comunitea',
    'website': 'http://www.comunitea.com',
    'license': 'AGPL-3',
    'contributors': [
        'Rubén Seijas <ruben@comunitea.com>',
    ],
    'depends': [
        'portal',
        'website',
        'website_sale',
        'website_canonical_url',
        'website_google_tag_manager',
        'product_template_tags'
    ],
    'data': [
        'templates/access.xml',
        'templates/assets.xml',
        'templates/product.xml',
        'templates/robots.xml',
        'templates/shop.xml',
        'templates/sitemap.xml',
        'templates/webapp.xml',
        'views/product_views.xml',
        'views/public_category_views.xml',
        'views/settings_views.xml',
        'security/tag_security.xml'
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}
