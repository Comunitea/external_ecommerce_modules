# -*- coding: utf-8 -*-
#
# © 2018 Comunitea
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import http, api, models, fields, _
from odoo.http import request
from odoo.addons.seo_base.models.settings import _default_website


class Website(models.Model):

    _inherit = 'website'

    refunds_contact = fields.Boolean(string="Request refunds in my portal", default=False,
                                     help="Active it to receive refund petitions of portal users from my portal account through refund form")
