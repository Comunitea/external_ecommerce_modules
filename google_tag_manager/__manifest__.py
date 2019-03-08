# Copyright 2018 Pierre Faniel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Google Tag Manager',
    'category': 'Website',
    'summary': 'Google Tag Manager - Odoo integration',
    'version': '1.0.0',
    'license': 'AGPL-3',
    'description': '''
        Includes Google Tag Manager HTML elements in the website metadata
    ''',
    'author': 'Pierre Faniel',
    'depends': [
        'website',
    ],
    'data': [
        'templates/website_layout.xml',
        'views/website_config_settings.xml',
    ],
    'images': [
        'static/description/google_tag_manager.png',
    ],
    'installable': True,
    'application': False,
}


