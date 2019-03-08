# -*- coding: utf-8 -*-
# Copyright 2018 Pierre Faniel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class Website(models.Model):
    _inherit = 'website'

    google_tag_manager_key = fields.Char('Google Tag Manager Key')
