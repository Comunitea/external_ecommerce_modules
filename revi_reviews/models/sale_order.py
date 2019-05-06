# -*- coding: utf-8 -*-
# © 2019 Comunitea - Pavel Smirnov <pavel@comunitea.com> & Ruben Seijas <ruben@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import json
import requests
from odoo import api, fields, models, _
from odoo.http import request
import ipdb


class SaleOrder(models.Model):
    _inherit = "sale.order"

    revi_use = fields.Boolean(string=_("Use Revi service"))
    revi_state = fields.Selection([
        ('skip', _("Don't send")),
        ('waiting', _("Waiting for send")),
        ('error', _("Error of send")),
        ('sent', _("Already sent"))
    ], string=_("Opinion state"), default='waiting', help=_("Revi mail state for this order"))

    @api.multi
    def create(self, values):

        # ipdb.set_trace()

        return super(SaleOrder, self).create(values)

    @api.multi
    def write(self, values):
        for res in self:
            next_step = False
            revi_state = values.get('revi_state', False)
            if not revi_state:
                revi_state = res.revi_state

            website = request.env['website'].get_current_website()
            language = website.default_lang_id.iso_code
            root = request.httprequest.url_root
            partner = res.partner_id

            if revi_state not in ['skip', 'sent']:
                next_step = True

            if next_step and res.revi_use and partner.revi_use and partner.email:
                next_step = True
            else:
                next_step = False

            if next_step and website.revi_api_key and website.revi_def_state != 'skip':

                # Set order data
                order_data = {
                    'orders': [{
                        'id_order ': res.id,
                        'lang ': language,
                        'customer_name ': partner.name,
                        'email ': partner.email,
                        'currency ': res.currency_id.name,
                        # 'shipping_cost ': '',
                        # 'total_discount ': '',
                        'taxes ': res.amount_tax,
                        # 'vat ': '',
                        'total_products ': len(res.order_line.filtered(lambda x: x.product_id.type == 'product')),
                        'total_paid ': res.amount_total,
                        #
                        #
                        # Change to 'ready' in production!
                        'status ': 'pending',
                        #
                        #
                        'order_date ': res.confirmation_date,
                        'date_status_upd ': res.write_date
                    }]
                }

                def _gen_product_data(product):
                    return {
                        'id_product': product.id,
                        'price': product.lst_price,
                        'sku': product.default_code,
                        'lang': language,
                        'name': product.name,
                        'description ': '',
                        'url': '%sshop/product/%d' % (root, product.id),
                        'photo_url': '%swebsite/image/product.template/%d/image/' % (root, product.id)
                    }

                # Set products data
                product_data = {
                    'products': []
                }
                orders_products = {
                    'id_order': res.id,
                    'products': []
                }

                order_lines = res.order_line.filtered(lambda x: x.product_id.type == 'product')
                for order in order_lines:
                    product = order.product_id.product_tmpl_id
                    product_data['products'].append(_gen_product_data(product))
                    orders_products['products'].append({'id_product': product.id})

                # Set data for link products with order
                link_data = {
                    'orders_products': []
                }
                if orders_products:
                    link_data['orders_products'] = orders_products

                headers = {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'X-API-KEY': website.revi_api_key
                }

                hello_data = {
                    'test': 'Hello Revi!'
                }

                hello_call = requests.post('https://test.revi.io/api/v1/hello_world',
                                           data=json.dumps(hello_data), headers=headers)

                if hello_call.status_code == 200 and hello_call.json().get('success') is True:
                    ipdb.set_trace()
                #     create_order = requests.post('https://test.revi.io/api/v1/orders',
                #                                  data=json.dumps(order_data), headers=headers)

            return super(SaleOrder, res).write(values)
