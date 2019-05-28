# -*- coding: utf-8 -*-
#
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# See README.rst file on addon root folder for more details
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
    'name': 'SEO Base',
    'version': '11.0.1.0.0',
    'summary': 'Website with basic functions for SEO optimization. \
        This module contains several configurations for different optimizations on the website. \
        It is compatible with the multi-website modules.',
    'category': 'Website',
    'author': 'Comunitea, ' 'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/website',
    'license': 'AGPL-3',
    'contributors': [
        'Pavel Smirnov <pavel@comunitea.com>',
        'Rubén Seijas <ruben@comunitea.com>',
        'Juan Vázquez Moreno <vmjuan90@gmail.com>',
    ],
    'depends': [
        'website',
        'website_sale',
        'sgeede_infinite_scroll'
    ],
    'data': [
        'views/product_meta.xml',
        'views/public_category.xml',
        'views/settings.xml',
        'views/menu.xml',
        'templates/favicon.xml',
        # 'templates/head.xml', # Only one-company webs
        'templates/product.xml',
        'templates/robots.xml',
        'templates/seo.xml',
        'templates/sitemap.xml',
        'templates/shop.xml',
        'templates/webapp.xml',
    ],
    'images': [
        '/static/description/icon.png',
    ],
    'installable': True,
    'application': True,
}
