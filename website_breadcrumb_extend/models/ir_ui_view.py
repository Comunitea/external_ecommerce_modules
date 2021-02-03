# -*- coding: utf-8 -*-

from odoo import models, fields, _


class IrUiView(models.Model):
    _inherit = 'ir.ui.view'

    name = fields.Char(string=_('View Name'), required=True, translate=True)
