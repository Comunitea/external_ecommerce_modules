{
    'name': 'Pagantis Payment Acquirer',
    'version': '12.0.1.0.0',
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
        'website_sale',
    ],
    'data': [
        'views/payment_views.xml',
        'views/payment_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    'installable': True,
    'application': False,
}
