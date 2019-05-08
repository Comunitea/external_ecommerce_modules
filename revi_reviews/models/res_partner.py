# -*- coding: utf-8 -*-
# © 2019 Comunitea - Pavel Smirnov <pavel@comunitea.com> & Ruben Seijas <ruben@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models, _


class Partner(models.Model):
    _inherit = "res.partner"

    revi_use = fields.Boolean(string=_("Sent Revi mails"), default=True,
                              help=_("Send a Revi opinion mail to the current user when he making a purchase"))
