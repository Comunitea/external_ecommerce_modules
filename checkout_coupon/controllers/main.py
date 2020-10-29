# -*- coding: utf-8 -*-


import json
import logging

from datetime import datetime

from odoo import http, _
from odoo.http import request

from odoo.addons.website_sale.controllers.main import WebsiteSale

_logger = logging.getLogger(__name__)


class CheckoutCoupon(http.Controller):

    @http.route(['/shop/checkout/couponcheck'], type='json', auth="public", methods=['POST'], website=True)
    def _coupon_check(self, coupon_code):

        if not request.website.use_osc_coupon:
            values = {
                "message": _("Coupon module is disabled"),
                "flags": "red",
                "success": False
            }
            values = json.dumps(values)
            return values

        domain = [('code', '=', coupon_code)]
        coupon = request.env['checkout_coupon.coupons'].sudo().search(domain)
        today = datetime.today()
        success = False

        if coupon.start_date:
            start_date = datetime.strptime(coupon.start_date, '%Y-%m-%d')
        if coupon.end_date:
            end_date = datetime.strptime(coupon.end_date, '%Y-%m-%d')

        if coupon and coupon.is_active:
            msg = _('The coupon exists')
            flags = 'green'
            if coupon.start_date and start_date > today:
                flags = 'yellow'
                msg += _(' but is still not available')
            elif coupon.end_date and end_date < today:
                flags = 'yellow'
                msg += _(' but is expired')
            elif coupon.is_counted and coupon.total < 1:
                flags = 'yellow'
                msg += _(' but there is no more in the stock')
            else:
                success = True
                msg += _(' and is available for use')
        else:
            msg = _('Invalid coupon!')
            flags = 'red'

        session_user = request.env.user
        session_partner_id = session_user.partner_id.id

        if coupon.partner_ids and success:
            if coupon.partner_ids.ids.count(session_partner_id) > 0:
                msg += _(' and is available for current user')
            else:
                msg += _(' but is unavailable for current user')
                flags = 'red'
                success = False

        order = request.website.sale_get_order()
        product_ids = order.order_line

        if coupon.min_cart_value and coupon.min_cart_value > order.amount_untaxed and success:
            msg += _(' but your order total is too low')
            flags = 'yellow'
            success = False

        if coupon.max_cart_value and coupon.max_cart_value < order.amount_untaxed and success:
            msg += _(' but your order total is too high')
            flags = 'yellow'
            success = False

        if success:
            coupon_as_product = request.env['product.product'].sudo().search(
                [('default_code', '=', coupon.code)],
                limit=1
            )
            line = coupon._prepare_order_line_discount(order)
            discount_apply_sum = 0
            _logger.info("Prepared Order Line for Coupon Discount %s", line)

            if coupon.coupon_type == 'all':
                msg += _(' and was applied for products: ')
                for res in product_ids:
                    if res.product_id.type == 'product':
                        if coupon.discount_type == 'percentage':
                            discount_apply_sum += (res.product_id.list_price * res.product_uom_qty) * (coupon.value / 100)
                        else:
                            discount_apply_sum += line['list_price'] * res.product_uom_qty
                        msg += _(' %s,' % res.product_id.id)

            elif coupon.coupon_type == 'category':
                msg += _(' and was applied for category %s with products: ' % coupon.discount_category_id.name)
                for res in product_ids:
                    if res.product_id.public_categ_ids.id == coupon.discount_category_id.id and res.product_id.type == 'product':
                        if coupon.discount_type == 'percentage':
                            discount_apply_sum += (res.product_id.list_price * res.product_uom_qty) * (coupon.value / 100)
                        else:
                            discount_apply_sum += line['list_price'] * res.product_uom_qty
                        msg += _(' %s,' % res.product_id.name)

            elif coupon.coupon_type == 'product':
                for res in product_ids:
                    if res.product_id.id == coupon.discount_product_id.id:
                        if coupon.discount_type == 'percentage':
                            discount_apply_sum += (res.product_id.list_price * res.product_uom_qty) * (coupon.value / 100)
                        else:
                            discount_apply_sum = line['list_price'] * res.product_uom_qty
                        msg += _(' and was applied for product %s' % res.product_id.id)

            if coupon_as_product:
                coupon_as_product.product_tmpl_id.write({
                    'list_price': -discount_apply_sum,
                    'taxes_id': [tax for tax in line['tax_id']]
                })
                msg += _(' and coupon product (id: %s) existed' % coupon_as_product.id)
            else:
                coupon_as_product = request.env['product.product'].sudo().create({
                    'name': 'Discount coupon %s' % coupon.code,
                    'default_code': coupon.code,
                    'sale_ok': False,
                    'type': 'service',
                    'taxes_id': [(4, coupon._default_tax_id().id, False)],
                    'supplier_taxes_id': '',
                    'list_price': -discount_apply_sum,
                })
                msg += _(' and coupon product (id: %s) was created' % coupon_as_product.id)

            if not coupon_as_product:
                msg += _(' but your order does not have products to apply')
                flags = 'yellow'
                success = False
                _logger.warning(msg)

            coupon_history = request.env['checkout_coupon.history'].sudo().search(
                [('order', '=', order.id)],
                limit=1
            )

            if not coupon_history:
                coupon_history = request.env['checkout_coupon.history'].sudo().create({
                    'name': coupon.id,
                    'order': order.id
                })
                msg += _(' and was added a history element with id %s' % coupon_history.id)

            order._cart_update(product_id=coupon_as_product.id, set_qty=1)
            order.write({'applied_coupon': coupon.id})
            msg += _(' and your discount is %s €' % line['list_price'])

            if coupon.is_counted:
                coupon.write({'total': coupon.total - 1})
                msg += _('; rest of current coupons: %s' % coupon.total)

        values = {
            "message": msg,
            "flags": flags,
            "success": success
        }

        _logger.info('%s' % msg)
        values = json.dumps(values)

        return values

    @http.route(['/shop/checkout/couponremove'], type='json', auth="public", methods=['POST'], website=True)
    def _coupon_remove(self, coupon_code):

        if not request.website.use_osc_coupon:
            values = {
                "message": _("Coupon module is disabled"),
                "flags": "red",
                "success": False
            }
            values = json.dumps(values)
            return values

        domain = [('code', '=', coupon_code)]
        coupon = request.env['checkout_coupon.coupons'].sudo().search(domain)
        success = False
        msg = _('Coupon %s' % coupon_code)
        flags = ''

        if coupon:
            coupon_to_remove = request.env['product.product'].sudo().search(
                [('default_code', '=', coupon.code)],
                limit=1
            )
            if coupon_to_remove:
                order = request.website.sale_get_order()
                coupon_history = request.env['checkout_coupon.history'].sudo().search(
                    [('order', '=', order.id)],
                    limit=1
                )
                order._cart_update(product_id=coupon_to_remove.id, add_qty=-1)
                order.write({'applied_coupon': ''})
                msg += _(' was eliminated')

                if coupon.is_counted:
                    coupon.write({'total': coupon.total + 1})
                    msg += _('; rest of current coupons: %s' % coupon.total)

                flags = 'green'
                success = True
                if coupon_history:
                    coupon_history.unlink()
                    msg += _('; and history element was deleted')
        else:
            msg += _(' not found')
            flags = 'red'

        values = {
            "message": msg,
            "flags": flags,
            "success": success
        }

        values = json.dumps(values)

        return values


class AutoRemoveCoupon(WebsiteSale):

    @staticmethod
    def _remove_coupon(sale_order):

        coupon = sale_order.applied_coupon
        coupon_to_remove = request.env['product.product'].sudo().search(
            [('default_code', '=', coupon.code)],
            limit=1
        )
        sale_order._cart_update(product_id=coupon_to_remove.id, add_qty=-1)

        if coupon.is_counted:
            coupon.write({'total': coupon.total + 1})

        coupon_history = request.env['checkout_coupon.history'].sudo().search(
            [('order', '=', sale_order.id)],
            limit=1
        )
        coupon_history.unlink()

        sale_order.write({'applied_coupon': ''})

    """
    Auto remove of coupon in the cart if the cart has been changed
    """
    @http.route(['/shop/cart/update_json'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update_json(self, product_id, line_id=None, add_qty=None, set_qty=None, display=True):

        sale_order = request.website.sale_get_order()

        if sale_order.applied_coupon:
            self._remove_coupon(sale_order)

        return super(AutoRemoveCoupon, self).cart_update_json(product_id, line_id=line_id, add_qty=add_qty,
                                                              set_qty=set_qty, display=display)

    """
    Auto remove of coupon in the cart if the module is disabled
    """
    @http.route(['/shop/checkout'], type='http', auth="public", website=True)
    def checkout(self, **post):

        sale_order = request.website.sale_get_order()

        if sale_order.applied_coupon and not request.website.use_osc_coupon:
            self._remove_coupon(sale_order)

        return super(AutoRemoveCoupon, self).checkout(**post)
