# -*- coding: utf-8 -*-
{
    'name': 'Pagantis Payment Acquirer',
    'version': '1.0',
    'summary': 'Añade el método de pago: Pagantis',
    'description': '',
    'category': 'Accounting',
    'author': 'Comunitea',
    'website': 'http://www.comunitea.com',
    'license': 'AGPL-3',
    'contributors': [
        "Ruben Seijas <ruben@comunitea.com>"
    ],
    'depends': [
        'payment',
        'website_sale',  # For default checkout
        # 'website_sale_one_step_checkout'  # For OSC checkout
    ],
    'data': [
        'views/payment_views.xml',
        'views/payment_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    'images': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
}