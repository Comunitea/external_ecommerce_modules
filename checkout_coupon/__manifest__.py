# -*- coding: utf-8 -*-
{
    'name': 'Discount Coupons',
    'version': '10.0.1.0.0',
    'summary': 'Discount Coupons for Checkout',
    'description': '',
    'category': 'Ecommerce',
    'author': 'Comunitea',
    'website': 'http://www.comunitea.com',
    'license': 'AGPL-3',
    'contributors': [
        'Pavel Smirnov <pavel@comunitea.com>',
        "Ruben Seijas <ruben@comunitea.com>",
    ],
    'depends': [
        'website',
        'website_sale',
        'website_sale_charge_payment_fee',
    ],
    'data': [
        'views/coupons.xml',
        'views/history.xml',
        'views/sale_order.xml',
        'views/settings.xml',
        'views/menu.xml',
        'views/links.xml',
        'templates/checkout.xml',
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
