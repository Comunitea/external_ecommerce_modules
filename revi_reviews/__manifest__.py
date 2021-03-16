{
    'name': 'Revi Reviews',
    'version': '12.0.1.0.0',
    'summary': 'Integration with Revi Reviews Service',
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
        'website_sale'
    ],
    'data': [
        'views/revi_settings.xml',
        'views/revi_menu.xml',
        'views/account_invoice.xml',
        # 'views/sale_order.xml',
        'views/res_partner.xml'
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}
