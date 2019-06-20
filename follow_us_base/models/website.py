# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, models, fields, _
from odoo.http import request


class Website(models.Model):
    _inherit = 'website'

    newsletter_ids = fields.Many2many('mail.mass_mailing.list', string=_("Newsletter channels"))

    @api.multi
    def check_follower(self, channel):
        # Set user data
        user = request.env.user
        partner = user.partner_id

        # Search of current channel
        mailing_list_ids = request.env['mail.mass_mailing.list']
        domain = [('id', '=', channel)]
        mailing_list = mailing_list_ids.sudo().search(domain, limit=1)

        # Search current user in the list of channel members
        domain = ['&', ('list_ids', 'ilike', mailing_list.id), ('email', '=', partner.email)]
        is_follower = request.env['mail.mass_mailing.contact'].sudo().search(domain)

        return is_follower

    @api.multi
    def default_channel(self):
        channel = request.env['mail.mass_mailing.list'].search([], limit=1)
        return channel.id if channel else False
