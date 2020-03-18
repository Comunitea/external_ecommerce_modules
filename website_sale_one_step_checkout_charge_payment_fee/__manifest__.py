# -*- coding: utf-8 -*-
{
    'name': 'External: Charge payment fee in one step checkout',
    'version': '10.0.1.0.0',
    'summary': 'Allows to use payment fee in OSC.',
    "development_status": "Production",
    'author': 'Comunitea Servicios Tecnológicos S.L.',
    'contributors': [
        "Ruben Seijas <ruben@comunitea.com>",
        "Pavel Smirnov <pavel@comunitea.com>",
    ],
    'website': 'http://www.comunitea.com',
    'license': 'AGPL-3',
    'category': 'eCommerce',
    'depends': [
        'payment_acquirer_by_amount',
        'website_sale_one_step_checkout',
        'website_sale_charge_payment_fee',
        'seo_base',
    ],
    'data': [
        'views/templates.xml',
        'views/acquirer_payment_mode_view.xml',
    ],
    'images': [
    ],
    'installable': True,
}
