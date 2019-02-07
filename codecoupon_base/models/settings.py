# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models, _


def _default_website(self):
    return self.env['website'].search([], limit=1)


class Website(models.Model):
    _inherit = "website"

    codecoupon_state = fields.Boolean(_("CodeCoupon module is active"), default=False)
    codecoupon_length = fields.Integer(_("Default coupon min length"), default=6)
    codecoupon_dev = fields.Boolean(_("Developer mode"), default=False,
                                    help=_("This option will be used to read the LOG messages"))
    codecoupon_form_title = fields.Char(_("Coupon form title"), default=_("Have a discount coupon?"))
    codecoupon_appl_title = fields.Char(_("Applied coupon form title"), default=_("You have a coupon applied"))
    codecoupon_form_text = fields.Char(_("Coupon form input title"), default=_("Put it in this field and apply"))
    codecoupon_err_msg = fields.Char(_("Error message"),
                                     help=_("This message will be displayed in case of any error"),
                                     default=_("Invalid coupon!"))
    codecoupon_adv_msg = fields.Text(_("Advice of auto elimination"),
                                     help=_("This message will be displayed how advice of "
                                            "auto coupon elimination in case of cart change"),
                                     default=_("It will be eliminated with a some change in the cart"))


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'codecoupon_base.settings'

    website_id = fields.Many2one('website', string="website", default=_default_website, required=True)
    codecoupon_state = fields.Boolean(related='website_id.codecoupon_state')
    codecoupon_length = fields.Integer(related='website_id.codecoupon_length')
    codecoupon_dev = fields.Boolean(related='website_id.codecoupon_dev')
    codecoupon_form_title = fields.Char(related='website_id.codecoupon_form_title')
    codecoupon_appl_title = fields.Char(related='website_id.codecoupon_appl_title')
    codecoupon_form_text = fields.Char(related='website_id.codecoupon_form_text')
    codecoupon_err_msg = fields.Char(related='website_id.codecoupon_err_msg')
    codecoupon_adv_msg = fields.Text(related='website_id.codecoupon_adv_msg')

    def activate_codecoupon(self):
        for r in self:
            r.write({'codecoupon_state': True})

    def deactivate_codecoupon(self):
        for r in self:
            r.write({'codecoupon_state': False})
