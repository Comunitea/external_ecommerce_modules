# -*- coding: utf-8 -*-

{
    'name': 'Payment Acquirer By Amount',
    'version': '12.0.1.0.0',
    'summary': 'Set amounts to show payment acquirer in your website by these amounts',
    'description': '',
    'category': 'Ecommerce',
    'author': 'Comunitea',
    'website': 'http://www.comunitea.com',
    'license': 'AGPL-3',
    'contributors': [
        "Ruben Seijas <ruben@comunitea.com>"
    ],
    'depends': [
        'payment',
        'website_sale',  # For default checkout
    ],
    'data': [
        'views/payment_view.xml',
        'views/payment_templates.xml'
    ],
    'images': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
}
