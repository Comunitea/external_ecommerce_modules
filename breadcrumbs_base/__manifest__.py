# -*- coding: utf-8 -*-

{
    'name': 'Breadcrumbs Base',
    'version': '11.0.2.0.0',
    'summary': 'Friendly breadcrumbs for eCommerce',
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
        'website_sale'
    ],
    'data': [
        'views/page_view.xml',
        'views/breadcrumbs_views.xml',
        'templates/breadcrumbs.xml',
        'security/ir.model.access.csv',
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
}
