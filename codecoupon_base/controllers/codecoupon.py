# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import json
from datetime import datetime
from odoo import http, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class CouponControl(http.Controller):

    # Return generate function
    def return_gen(self, message, flag, success, develop):
        values = {
            'message': message,
            'flag': flag,
            'success': success,
            'develop': develop
        }
        return json.dumps(values)

    @http.route(['/shop/codecoupon/check'], type='json', auth="public", methods=['POST'], website=True)
    def _coupon_check(self, coupon_code):

        # Return error message if module isn't active
        if not request.website.codecoupon_state:
            return self.return_gen(_("Coupon module is disabled"), "danger", False, False)

        # Set default values
        message = _("Coupon with code %s" % coupon_code)
        flag = "warning"
        success = False

        # Set developer mode
        develop = request.website.codecoupon_dev or False

        # Set message content
        #
        # Подтянуть сообщения об ошибках из настроек модуля
        #

        # Search the coupon to apply
        domain = [('code', '=', coupon_code)]
        coupon = request.env['codecoupon_base.coupons'].sudo().search(domain)

        if coupon and coupon.is_active:
            message += _(" exists and is active")
            flag = "success"
            # Set dates
            today = datetime.today()
            start_date = datetime.strptime(coupon.start_date, '%Y-%m-%d') if coupon.start_date else False
            end_date = datetime.strptime(coupon.end_date, '%Y-%m-%d') if coupon.end_date else False
            # Check dates
            if start_date and start_date > today:
                message += _(" <br/>- but is still not available")
                flag = "warning"
            elif end_date and end_date < today:
                message += _(" <br/>- but is expired")
                flag = "warning"
            # Check stock
            elif coupon.is_counted and coupon.total < 1:
                message += _(" <br/>- but there is no more in the stock")
                flag = "warning"
            else:
                message += _(" <br/>- and is available for use")
                success = True
        else:
            return self.return_gen(_("Coupon with code <strong>%s</strong> not found" % coupon_code),
                              "danger", False, develop)

        # Check user data
        session_user = request.env.user
        session_partner_id = session_user.partner_id.id

        if coupon.partner_ids and success:
            if coupon.partner_ids.ids.count(session_partner_id) > 0:
                message += _(" <br/>- and is available for current user")
            else:
                message += _(" <br/>- but is unavailable for current user")
                flag = "warning"
                success = False

        # Check cart data
        order = request.website.sale_get_order()
        product_ids = order.order_line

        if coupon.min_cart != 0 and coupon.min_cart > order.amount_untaxed and success:
            message += _(" <br/>- but your order total is too low")
            flag = "warning"
            success = False

        if coupon.max_cart != 0 and coupon.max_cart < order.amount_untaxed and success:
            message += _(" <br/>- but your order total is too high")
            flag = "warning"
            success = False

        # Check products data
        have_one = False
        discount_apply_sum = 0

        if coupon.coupon_type == 'product' and success:
            to_apply_list = coupon.product_ids.ids
            list = ''
            if len(to_apply_list) > 0:
                for res in product_ids:
                    if res.product_id.id in to_apply_list:
                        have_one = True
                        discount_apply_sum += res.price_subtotal
                        list += " [%s]," % res.product_id.name
                if have_one:
                    message += _(" <br/>- and it was applied for products: %s" % list)
            else:
                return self.return_gen(_("Invalid coupon!"), "danger", False, develop)

        if coupon.coupon_type == 'category' and success:
            to_apply_list = coupon.category_ids.ids
            list = ''
            if len(to_apply_list) > 0:
                for res in product_ids:
                    if res.product_id.public_categ_ids.id in to_apply_list and res.product_id.sale_ok:
                        have_one = True
                        discount_apply_sum += res.price_subtotal
                        list += " [%s]," % res.product_id.name
                if have_one:
                    message += _(" <br/>- and it was applied for products: %s" % list)
            else:
                return self.return_gen(_("Invalid coupon!"), "danger", False, develop)

        if coupon.coupon_type == 'all' and success:
            list = ''
            for res in product_ids:
                if res.product_id.sale_ok:
                    have_one = True
                    discount_apply_sum += res.price_subtotal
                    list += " [%s]," % res.product_id.name
            if have_one:
                message += _(" <br/>- and it was applied for products: %s" % list)

        if not have_one and success:
            message += _(" <br/>- but your order does not have products to apply")
            flag = "warning"
            success = False

        # Set coupon discount value
        discount_total = 0
        if coupon.discount_type == 'fixed' and coupon.value:
            discount_total = coupon.value
        elif coupon.discount_type == 'percentage' and coupon.value:
            discount_total = discount_apply_sum * (coupon.value / 100)

        # Search or create coupon product
        if have_one and discount_apply_sum and success:
            coupon_as_product = request.env['product.product'].sudo().search(
                [('default_code', '=', coupon.code)],
                limit=1
            )
            if coupon_as_product:
                coupon_as_product.product_tmpl_id.write({'list_price': -discount_total})
                message += _(" <br/>- and coupon product (id: %s) already existed" % coupon_as_product.id)
            else:
                coupon_as_product = request.env['product.product'].sudo().create({
                    'name': 'Discount coupon %s' % coupon.code,
                    'default_code': coupon.code,
                    'sale_ok': False,
                    'type': 'service',
                    'taxes_id': '',
                    'supplier_taxes_id': '',
                    'list_price': -discount_total
                })
                message += _(" <br/>- and coupon product (id: %s) was created" % coupon_as_product.id)

            # Set history element
            coupon_history = request.env['codecoupon_base.history'].sudo().search(
                [('order', '=', order.id)],
                limit=1
            )
            if not coupon_history:
                coupon_history = request.env['codecoupon_base.history'].sudo().create({
                    'name': coupon.id,
                    'order': order.id
                })
                message += _(" <br/>- and was added a history element with id %s" % coupon_history.id)

            # Update sale order
            order._cart_update(product_id=coupon_as_product.id, set_qty=1)
            order.write({'applied_coupon': coupon.id})
            message += _(" <br/>- and your discount is %s €" % discount_total)

            # Update coupon balance (if it's countable)
            if coupon.is_counted:
                coupon.write({'total': coupon.total - 1})
                message += _(" <br/>- rest of current coupons: %d" % coupon.total)

        # Set error message for developer or custom mode
        if not develop and not success:
            message = _("Coupon with code %s is invalid" % coupon_code)

        return self.return_gen(message, flag, success, develop)

    @http.route(['/shop/codecoupon/remove'], type='json', auth="public", methods=['POST'], website=True)
    def _coupon_remove(self, coupon_code):

        # Set default values
        message = _("Coupon with code %s" % coupon_code)
        flag = "warning"
        success = False

        # Set developer mode
        develop = request.website.codecoupon_dev or False

        # Set message content
        #
        # Подтянуть сообщения об ошибках из настроек модуля
        #

        # Search the coupon to remove
        domain = [('code', '=', coupon_code)]
        coupon = request.env['codecoupon_base.coupons'].sudo().search(domain)

        if coupon:
            coupon_to_remove = request.env['product.product'].sudo().search(
                [('default_code', '=', coupon.code)],
                limit=1
            )
            if coupon_to_remove:
                # Remove coupon from order
                order = request.website.sale_get_order()
                order._cart_update(product_id=coupon_to_remove.id, add_qty=-1)
                order.write({'applied_coupon': ''})
                message += _(" was eliminated")
                flag = "success"
                success = True

                # Delete the history element
                coupon_history = request.env['codecoupon_base.history'].sudo().search(
                    [('order', '=', order.id)],
                    limit=1
                )
                if coupon_history:
                    coupon_history.unlink()
                    message += _(" <br/>- and history element was deleted")

                # Update coupon balance (if it's countable)
                if coupon.is_counted:
                    coupon.write({'total': coupon.total + 1})
                    message += _(" <br/>- rest of current coupons: %d" % coupon.total)
            else:
                message += _(" not found")

        else:
            return self.return_gen(_("An error has occurred!"), "danger", False, develop)

        return self.return_gen(message, flag, success, develop)
