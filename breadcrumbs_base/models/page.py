# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, models, fields, _


class Page(models.Model):
    _inherit = 'website.page'

    name = fields.Char(string=_('Page name'), required=True, translate=True)
    parent_id = fields.Many2one('website.page', string=_("Parent page"))
