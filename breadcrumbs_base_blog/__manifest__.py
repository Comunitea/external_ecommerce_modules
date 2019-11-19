# -*- coding: utf-8 -*-
{
    'name': 'Breadcrumbs Blog',
    'version': '1.0',
    'summary': 'Blog extension for Breadcrumbs Base module',
    'description': '',
    'category': 'eCommerce',
    'author': 'Comunitea',
    'website': 'http://www.comunitea.com',
    'license': 'AGPL-3',
    'contributors': [
        'Pavel Smirnov <pavel@comunitea.com>',
        'Rubén Seijas <ruben@comunitea.com>',
    ],
    'depends': [
        'breadcrumbs_base',
        'breadcrumbs_base_tmp',
        'website_blog'
    ],
    'data': [
        'templates/breadcrumbs_bar.xml',
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
}
