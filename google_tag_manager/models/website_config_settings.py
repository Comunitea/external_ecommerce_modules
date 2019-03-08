# -*- coding: utf-8 -*-
# Copyright 2018 Pierre Faniel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class WebsiteConfigSettings(models.TransientModel):
    _inherit = 'website.config.settings'

    google_tag_manager_key = fields.Char(related='website_id.google_tag_manager_key')
