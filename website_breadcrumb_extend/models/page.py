# -*- coding: utf-8 -*-

from odoo import api, models, fields, _


class Page(models.Model):
    _inherit = 'website.page'

    name = fields.Char(string=_('Page name'), required=True, translate=True)
    parent_id = fields.Many2one('website.page', string=_("Parent page"))
