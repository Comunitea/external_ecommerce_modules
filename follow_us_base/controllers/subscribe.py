# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import json
from odoo import http, _
from odoo.http import request


def search_channel(channel):
    mailing_list_ids = request.env['mail.mass_mailing.list']
    domain = [('id', '=', channel)]
    return mailing_list_ids.sudo().search(domain, limit=1)


class SubscribeActions(http.Controller):

    @http.route(['/followus/subscribe'], type="json", auth="public", methods=['POST'], website=True)
    def subscribe(self, email, channel):
        success = False

        if not channel:
            # If channel is not established
            return json.dumps({'success': success})

        # Search the current channel
        mailing_list = search_channel(channel)

        # Search a partner with current email
        partner_list = request.env['res.partner']
        domain = ['&', ('email', '=', email), ('active', '=', True)]
        partner = partner_list.search(domain, limit=1)

        mail_contacts = request.env['mail.mass_mailing.contact'].sudo()

        if partner:
            already_exist = mail_contacts.search([('email', '=', email)])
            if already_exist:
                # If the contact already exists, add it as a follower for the newsletter channel
                list_ids = already_exist.list_ids.ids
                list_ids.append(mailing_list.id)
                update = already_exist.write({'list_ids': [(6, 0, list_ids)]})
                if update:
                    success = True
            else:
                # Create a new follower based on partner information
                create = mail_contacts.create({
                    'name': partner.name,
                    'company_name': partner.parent_id.name or '',
                    'email': partner.email,
                    'list_ids': [(4, mailing_list.id)]
                })
                if create:
                    success = True
        else:
            # Create a new follower
            self.ensure_one()
            create = self.add_to_list(email, mailing_list.id)
            if create:
                success = True

        values = {
            'success': success,
        }
        return json.dumps(values)

    @http.route(['/followus/unsubscribe'], type="json", auth="public", methods=['POST'], website=True)
    def un_subscribe(self, email, channel):
        success = False

        # Search the current channel
        mailing_list = search_channel(channel)

        # Search current follower in the list of channel members
        domain = ['&', ('list_ids', 'ilike', mailing_list.id), ('email', '=', email)]
        follower = request.env['mail.mass_mailing.contact'].sudo().search(domain, limit=1)

        # Delete current channel
        if follower:
            list_ids = follower.list_ids.ids
            list_ids.remove(mailing_list.id)
            update = follower.write({'list_ids': [(6, 0, list_ids)]})
            if update:
                success = True

        values = {
            'success': success,
        }
        return json.dumps(values)
