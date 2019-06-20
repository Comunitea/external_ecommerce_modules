# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import json
from odoo import http, _
from odoo.http import request


def search_channel(channel_ids):
    mailing_list_ids = request.env['mail.mass_mailing.list']
    domain = [('id', 'in', channel_ids)]
    return mailing_list_ids.sudo().search(domain)


class SubscribeActions(http.Controller):

    @http.route(['/followus/subscribe'], type="json", auth="public", methods=['POST'], website=True)
    def subscribe(self, email, channel_ids):
        success = False
        message = ''

        if not channel_ids:
            # If channel is not established
            return json.dumps({'success': success, 'message': 'Empty channel list'})

        # Search the current channel
        mailing_list_ids = search_channel(channel_ids)

        for mailing_list in mailing_list_ids:
            # Search a partner with current email
            partner_list = request.env['res.partner']
            domain = ['&', ('email', '=', email), ('active', '=', True)]
            partner = partner_list.search(domain, limit=1)

            mail_contacts = request.env['mail.mass_mailing.contact'].sudo()

            if partner:
                already_exist = mail_contacts.search([('email', '=', email)])
                # If the contact already exists
                if already_exist:
                    list_ids = already_exist.list_ids.ids

                    # Add it as a follower if the contact isn't already on the list of channel
                    if mailing_list.id not in list_ids:
                        list_ids.append(mailing_list.id)
                        update = already_exist.write({'list_ids': [(6, 0, list_ids)]})
                        if update:
                            success = True
                            message += 'The partner was added as a follower to channel %s<br/>\n' % mailing_list.name
                    else:
                        success = True
                        message += 'The partner is already in channel %s<br/>\n' % mailing_list.name
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
                        message += 'The partner was added as a NEW follower to channel %s<br/>\n' % mailing_list.name
            else:
                # Create a new follower
                create = mail_contacts.create({
                        'name': email,
                        'email': email,
                        'list_ids': [(4, mailing_list.id)]
                    })
                if create:
                    success = True
                    message += 'The follower was created and added to channel %s<br/>\n' % mailing_list.name

        values = {
            'success': success,
            'message': message
        }

        return json.dumps(values)

    @http.route(['/followus/unsubscribe'], type="json", auth="public", methods=['POST'], website=True)
    def un_subscribe(self, email, channel_ids):
        success = False
        message = ''

        # Search the current channel
        mailing_list_ids = search_channel(channel_ids)

        for mailing_list in mailing_list_ids:
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
                    message += 'The follower was deleted from channel %s<br/>\n' % mailing_list.name
            else:
                success = True
                message += 'The follower was not fount in channel %s<br/>\n' % mailing_list.name

        values = {
            'success': success,
            'message': message
        }

        return json.dumps(values)
