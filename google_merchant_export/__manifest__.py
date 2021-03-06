{
    'name': 'Google Merchant Export',
    'version': '12.0.1.0.0',
    'summary': 'Product exportation for google merchant service',
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
        'website_sale',
        'website_seo_settings',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/feed.xml',
        'views/menu.xml',
        'templates/export.xml'
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'installable': True,
    'application': False,
}
