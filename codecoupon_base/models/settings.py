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


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'codecoupon_base.settings'

    website_id = fields.Many2one('website', string="website", default=_default_website, required=True)
    codecoupon_state = fields.Boolean(related='website_id.codecoupon_state')
    codecoupon_length = fields.Integer(related='website_id.codecoupon_length')
    codecoupon_dev = fields.Boolean(related='website_id.codecoupon_dev')

    def activate_codecoupon(self):
        for r in self:
            r.write({'codecoupon_state': True})

    def deactivate_codecoupon(self):
        for r in self:
            r.write({'codecoupon_state': False})
