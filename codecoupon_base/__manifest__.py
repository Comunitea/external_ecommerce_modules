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
    'name': 'CodeCoupon discount',
    'version': '1.1',
    'summary': 'Discount module for eCommerce WEB based on application of codes',
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
        'views/coupons.xml',
        'views/history.xml',
        'views/sale_order.xml',
        'views/settings.xml',
        'views/menu.xml',
        'templates/checkout.xml',
        'templates/head.xml'
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
}
