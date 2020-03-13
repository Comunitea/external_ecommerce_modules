# -*- coding: utf-8 -*-

import json
import logging
import requests
import unicodedata

from odoo import api, fields, models, _

from odoo.http import request

_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    revi_use = fields.Boolean(string=_("Use Revi service"), default=False)
    revi_state = fields.Selection([
        ('skip', _("Don't send")),
        ('waiting', _("Waiting for send")),
        ('error', _("Error of send")),
        ('sent', _("Already sent"))
    ], string=_("Opinion state"), default='waiting', help=_("Revi data state for this order"))

    @api.model
    def create(self, vals):
        website = request.env['website'].get_current_website()
        partner_id = vals.get('partner_id', False)
        partner = request.env['res.partner'].sudo().search([('id', '=', partner_id)], limit=1)

        def set_revi_state(use, state):
            return vals.update({
                'revi_use': use,
                'revi_state': state
            })

        # Check order type
        if website.revi_def_state != 'skip' and partner.revi_use and (
                vals.get('type', False) and vals['type'] == 'out_invoice'):
            set_revi_state(True, 'waiting')
        else:
            set_revi_state(False, 'skip')

        return super(AccountInvoice, self).create(vals)

    @api.multi
    def write(self, values):
        """
        We need to send invoice data to Revi only if state of invoice was changed and is OPEN.
        OR
        We need to send data if last attempt to send the data has FAILED (has state ERROR).
        """
        resp = super(AccountInvoice, self).write(values)
        website = request.env['website'].get_current_website()
        language = website.default_lang_id.iso_code
        # root = request.httprequest.url_root
        root = request.env['ir.config_parameter'].sudo().get_param('web.base.url') + '/'

        if values.get('state', False) and values['state'] == 'open':
            for res in self:
                partner = res.partner_id
                # Generate order & order_line data to send
                if res.revi_use and ('waiting' in res.revi_state or 'error' in res.revi_state) \
                        and partner.revi_use and partner.email and website.revi_api_key:
                    # Set order data
                    _logger.info('REVI - Preparing Invoice %s from %s', res.display_name, res.origin)
                    order_data = {
                        'orders': [{
                            'id_order': '%s' % res.id,
                            'lang': language,
                            'customer_name': partner.name,
                            'email': partner.email,
                            'currency': res.currency_id.name,
                            'taxes': '%s' % res.amount_tax,
                            'total_products': '%s' % len(res.invoice_line_ids.filtered(
                                lambda x: x.product_id.type == 'product' or x.product_id.type == 'service')),
                            'total_paid': '%s' % res.amount_total,
                            'status': 'ready' if website.revi_auto_send else 'pending',
                            'order_date': res.create_date,
                            'date_status_upd': res.write_date
                        }]
                    }

                    def _gen_product_data(product):
                        return {
                            'id_product': product.id,
                            'ean': product.barcode or '',
                            'price': product.lst_price if not product.hide_website_price else 'N/D',
                            'sku': product.default_code or '',
                            'locale': [{
                                'lang': language,
                                'name': unicodedata.normalize('NFKD', product.name).encode(
                                    'ascii', 'ignore').decode('ascii'),
                                'url': '%sshop/product/%d' % (root, product.id),
                                'photo_url': '%swebsite/image/product.template/%d/image/' % (root, product.id),
                                'description': unicodedata.normalize('NFKD', product.description_short
                                                                     or product.product_meta_description
                                                                     or product.description_sale or product.name)
                                .encode('ascii', 'ignore').decode('ascii'),
                            }]
                        }

                    # Set products data
                    product_data = {
                        'products': []
                    }
                    products_to_link = []

                    invoice_lines = res.invoice_line_ids.filtered(
                        lambda x: x.product_id.type == 'product' or x.product_id.type == 'service')
                    for line in invoice_lines:
                        product = line.product_id.product_tmpl_id
                        # if there are more than one order line no matter because always be the same product
                        # Tickets by POS has not order_line, then order_line must will be False
                        order_line = line.sale_line_ids and line.sale_line_ids[0] or False
                        # Only want refer for published products and products packs, never pack content
                        # If not order_line is a POS Ticket, then no problem because there are packs, never pack content
                        if product.website_published and (
                                not order_line or (order_line and 'pack_parent_line_id' not in dir(order_line))):
                            product_data['products'].append(_gen_product_data(product))
                            products_to_link.append({'id_product': '%d' % product.id})
                        else:
                            if order_line and 'pack_parent_line_id' in dir(order_line):
                                _logger.warning('REVI - No send product because belong to a pack: %s - %s',
                                                product.id, product.display_name)
                            elif not product.website_published:
                                _logger.warning('REVI - No send product because is not published: %s - %s',
                                                product.id, product.display_name)
                            else:
                                _logger.warning('REVI - No send product: %s - %s', product.id, product.display_name)

                    # Set data for link products with order
                    link_data = {
                        'orders_products': [{
                            'id_order': '%s' % res.id,
                            'products': products_to_link
                        }]
                    }

                    headers = {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'X-API-KEY': website.revi_api_key
                    }

                    # Set API URL's
                    revi_base_url = website.revi_url
                    revi_hello_url = '%s/api/v1/hello_world' % revi_base_url
                    revi_order_url = '%s/api/v1/orders' % revi_base_url
                    revi_product_url = '%s/api/v1/products' % revi_base_url
                    revi_link_url = '%s/api/v1/orders_products' % revi_base_url

                    hello_data = {
                        'test': 'Hello Revi!'
                    }

                    def post_send(url, data, headers):
                        _logger.debug('REVI - Sending data to url: %s', url)
                        _logger.debug('REVI - headers: %s', headers)
                        _logger.debug('REVI - data: %s', data)
                        return requests.post(url, data=json.dumps(data), headers=headers)

                    def post_success(request):
                        code = request.status_code
                        if code in [200, 201]:
                            _logger.info('REVI - Send result: SUCCESSFULLY')
                            return True
                        else:
                            _logger.error('REVI - Send result: ERROR %s', code)
                            return False

                    # Test post call
                    _logger.info('REVI: Sending hello test data...')
                    hello_call = post_send(revi_hello_url, hello_data, headers)

                    # Send data
                    success = False
                    if post_success(hello_call):
                        # Send order
                        _logger.info('REVI: Sending invoice data...')
                        create_order = post_send(revi_order_url, order_data, headers)
                        if post_success(create_order):
                            # Send products (order_line)
                            _logger.info('REVI: Sending product data...')
                            _logger.info(product_data['products'])
                            create_products = post_send(revi_product_url, product_data, headers)
                            if post_success(create_products):
                                # Link products to orders
                                _logger.info('REVI: Sending product invoice linked data...')
                                link_products = post_send(revi_link_url, link_data, headers)
                                if post_success(link_products):
                                    success = True

                    # Set new Revi state for changed account invoice
                    if success:
                        _logger.info('REVI - Changed Revi state to sent for Invoice %s from %s',
                                     res.display_name, res.origin)
                        res.sudo().write({'revi_state': 'sent'})
                    else:
                        _logger.error('REVI - Changed Revi state to error for Invoice %s from %s',
                                      res.display_name, res.origin)
                        res.sudo().write({'revi_state': 'error'})

        return resp
