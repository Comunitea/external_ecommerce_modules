# © 2019 Comunitea - Pavel Smirnov <pavel@comunitea.com> & Ruben Seijas <ruben@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class WebsiteConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    revi_api_key = fields.Char(related='website_id.revi_api_key',
                               readonly=False)
    revi_def_state = fields.Selection(related='website_id.revi_def_state',
                                      readonly=False)
    # revi_send_back = fields.Boolean(related='website_id.revi_send_back')
    revi_auto_send = fields.Boolean(related='website_id.revi_auto_send',
                                    readonly=False)
    revi_url = fields.Selection(related='website_id.revi_url',
                                readonly=False)
