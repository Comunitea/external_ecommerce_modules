# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class IrUiView(models.Model):
    _inherit = 'ir.ui.view'

    name = fields.Char(string='View Name', required=True, translate=True)
