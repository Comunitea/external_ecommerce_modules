# -*- coding: utf-8 -*-
#
# © 2018 Comunitea - Ruben Seijas <ruben@comunitea.com>
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).s.

from odoo import api, fields, models


class Company(models.Model):
    _inherit = "res.company"

    social_instagram = fields.Char(string='Instagram Account')

