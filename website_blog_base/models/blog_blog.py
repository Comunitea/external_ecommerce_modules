# -*- coding: utf-8 -*-
#
# © 2018 Comunitea - Ruben Seijas <ruben@comunitea.com>
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import http, api, models, fields, _


class Blog(models.Model):
    _inherit = 'blog.blog'

    for_retailers = fields.Boolean(string=_("Available for retail B2B users"), default=True)
    for_customers = fields.Boolean(string=_("Available for B2C users"), default=True)
