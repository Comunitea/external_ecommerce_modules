# -*- coding: utf-8 -*-
# © 2019 Comunitea - Pavel Smirnov <pavel@comunitea.com> & Ruben Seijas <ruben@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models, _


class Website(models.Model):
    _inherit = 'website'

    revi_api_key = fields.Char(string=_("Revi API key"))
    revi_def_state = fields.Selection([
        ('skip', _("Don't send")),
        ('open', _("Open invoice"))], string=_("State for send data to Revi"), default='skip')
    # revi_send_back = fields.Boolean(string=_("Use back-end"))
    revi_auto_send = fields.Boolean(string=_("Automatic sending of invitation emails"), default=False)
