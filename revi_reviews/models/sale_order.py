import json
import logging
import requests
import unicodedata

from odoo import api, fields, models, _

from odoo.http import request

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    revi_use = fields.Boolean(string=_("Use Revi service"), default=False)
    revi_state = fields.Selection([
        ('skip', _("Don't send")),
        ('waiting', _("Waiting for send")),
        ('error', _("Error of send")),
        ('sent', _("Already sent"))
    ], string=_("Opinion state"), default='waiting', help=_("Revi mail state for this order"))

    @api.model
    def create(self, vals):
        website = request.env['website'].get_current_website()
        partner_id = vals.get('partner_id', False)
        partner = request.env['res.partner'].sudo().search([('id', '=', partner_id)], limit=1)
        sales_team = vals.get('team_id', False)
        website_salesteam = website.salesteam_id

        def set_revi_state(use, state):
            return vals.update({
                'revi_use': use,
                'revi_state': state
            })

        # Check order type
        if website.revi_def_state != 'skip' and partner.revi_use:
            if website_salesteam.id == sales_team:
                # From front-end
                set_revi_state(True, 'waiting')
            else:
                # From back-end
                if website.revi_send_back:
                    set_revi_state(True, 'waiting')
        else:
            set_revi_state(False, 'skip')

        return super(SaleOrder, self).create(vals)

    @api.multi
    def write(self, values):
        for res in self:
            next_step = False
            revi_state = values.get('revi_state', False)
            if not revi_state:
                revi_state = res.revi_state

            website = request.env['website'].get_current_website()
            language = website.default_lang_id.iso_code
            # root = request.httprequest.url_root
            root = request.env['ir.config_parameter'].sudo().get_param('web.base.url') + '/'
            partner = res.partner_id

            # Change partner in the order
            partner_id = values.get('partner_id', False)
            if partner_id:
                new_partner = request.env['res.partner'].sudo().search([('id', '=', partner_id)], limit=1)
                if new_partner:
                    partner = new_partner
                    # Set new Revi data on partner change
                    if website.revi_def_state != 'skip' and partner.revi_use:
                        res.sudo().write({
                            'revi_use': True,
                            'revi_state': 'waiting'
                        })

            if revi_state not in ['skip', 'sent']:
                next_step = True

            if next_step and res.revi_use and partner.revi_use and partner.email:
                next_step = True
            else:
                next_step = False

            # Control of order state change
            state = res.state
            new_state = values.get('state', False)
            """
            We need to send order data to Revi only if state of order was changed and is SENT or SALE:
                1. If order has state SENT and Revi default state is SENT
                2. If order has state SALE and Revi default state is SENT
                3. If order has state SALE and Revi default state is SALE
            """
            if next_step and new_state in ['sent', 'sale'] and new_state != state:
                state_to_send = website.revi_def_state
                if state_to_send == 'sent' or (state_to_send == 'sale' and state_to_send == new_state):
                    next_step = True
                else:
                    next_step = False
            else:
                next_step = False

            # Check the Revi API settings
            if website.revi_def_state == 'skip' or not website.revi_api_key:
                next_step = False

            # Generate order & order_line data to send
            if next_step:
                # Set order data
                _logger.info('REVI - Preparing Sale Order %s', res.id)
                order_data = {
                    'orders': [{
                        'id_order': '%s' % res.id,
                        'lang': language,
                        'customer_name': partner.name,
                        'email': partner.email,
                        'currency': res.currency_id.name,
                        'taxes': '%s' % res.amount_tax,
                        'total_products': '%s' % len(res.order_line.filtered(lambda x: x.product_id.type == 'product')),
                        'total_paid': '%s' % res.amount_total,
                        'status': 'ready' if website.revi_auto_send else 'pending',
                        'order_date': res.date_order,
                        'date_status_upd': res.write_date
                    }]
                }

                def _gen_product_data(product):
                    return {
                        'id_product': product.id,
                        'ean': product.barcode or '',
                        'price': product.lst_price if 'hide_website_price' not in dir(product)
                                                      or ('hide_website_price' in dir(product)
                                                          and not product.hide_website_price) else 'N/D',
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

                order_lines = res.order_line.filtered(lambda x: x.product_id.type == 'product')
                for order in order_lines:
                    product = order.product_id.product_tmpl_id
                    # if there are more than one order line no matter because always be the same product
                    # Tickets by POS has not order_line, then order_line must will be False
                    order_line = order.sale_line_ids and order.sale_line_ids[0] or False
                    # Only want refer for published products and products packs, never pack content
                    # If not order_line is a POS Ticket, then no problem because there are packs, never pack content
                    if product.website_published and (not order_line or (
                            order_line and 'pack_parent_line_id' in dir(order_line)
                            and not order_line.pack_parent_line_id)):
                        product_data['products'].append(_gen_product_data(product))
                        products_to_link.append({'id_product': '%d' % product.id})
                    else:
                        if order_line and 'pack_parent_line_id' in dir(order_line) \
                                and order_line.pack_parent_line_id:
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
                success = False

                def post_send(url, data, headers):
                    _logger.debug('REVI - Sending data to url: %s', url)
                    _logger.debug('REVI - headers: %s', headers)
                    _logger.debug('REVI - data: %s', data)
                    return requests.post(url, data=json.dumps(data), headers=headers)

                def post_success(request):
                    code = request.status_code
                    #
                    # There is an error with the json response data on the Revi server's part
                    #
                    # response = request.json().get('success')
                    # if code in [200, 201] and response is True:
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
                if post_success(hello_call):
                    # Send order
                    _logger.info('REVI: Sending order data...')
                    create_order = post_send(revi_order_url, order_data, headers)
                    if post_success(create_order):
                        # Send products (order_line)
                        _logger.info('REVI: Sending product data...')
                        create_products = post_send(revi_product_url, product_data, headers)
                        if post_success(create_products):
                            # Link products to orders
                            _logger.info('REVI: Sending product order linked data...')
                            link_products = post_send(revi_link_url, link_data, headers)
                            if post_success(link_products):
                                success = True

                # Set new Revi state for changed order
                if success:
                    _logger.info('REVI - Changed Revi state to sent for Sale Order %s', res.id)
                    res.sudo().write({'revi_state': 'sent'})
                else:
                    _logger.error('REVI - Changed Revi state to error for Sale Order %s', res.id)
                    res.sudo().write({'revi_state': 'error'})

            return super(SaleOrder, res).write(values)
