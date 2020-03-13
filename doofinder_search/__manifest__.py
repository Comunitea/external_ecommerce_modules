# -*- coding: utf-8 -*-

{
    'name': 'Doofinder search',
    'version': '10.0.1.0.0',
    'summary': 'Integration with Doofinder search engine',
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
        'seo_base',
    ],
    'data': [
        'templates/feed.xml'
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
}
