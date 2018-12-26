# -*- coding: utf-8 -*-
#
# © 2018 Comunitea
# Pavel Smirnov <pavel@comunitea.com>
# Rubén Seijas <ruben@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#
##############################################################################
#
#    Copyright (C) {year} {company} All Rights Reserved
#    ${developer} <{mail}>$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'E-commerce base modules',
    'version': '1.0',
    'summary': 'Website base e-commerce additional and customization theme',
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
        'web_sheet_full_width',
        'l10n_es',
        'website',
        'website_mail',
        'website_theme_install',
        'website_cookie_notice',
        'website_crm',
        'website_crm_recaptcha',
        'website_crm_privacy_policy',
        'website_crm_phone_validation',
        'website_sale',
        'website_sale_management',
        'website_sale_stock',
        'website_sale_stock_options',
        'website_sale_comparison',
        # 'website_sale_hide_price',
        'website_sale_product_brand',
        'website_sale_wishlist',
        'website_sale_delivery',
        'website_payment',
        'website_sale_require_login',
        'website_sale_require_legal',
    ],
    'data': [
        'templates/head.xml',
        'templates/footer.xml',
        'templates/contactus.xml',
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
}
