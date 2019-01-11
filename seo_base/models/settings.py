# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Website(models.Model):
    _inherit = 'website'

    map_add_icon = fields.Boolean('Favicon.ico', default=False)
    map_add_robot = fields.Boolean('Robots.txt', default=False)
    map_add_pages = fields.Boolean('Static pages', default=False)
    map_add_cats = fields.Boolean('Product public categories', default=False)
    map_add_prods = fields.Boolean('Published products', default=False)
    map_add_blog = fields.Boolean('Blog pages', default=False)
    map_cache_time = fields.Selection(
        selection=[
            ("1second", "Developer mode"),
            ("12hours", "Normal mode")
        ], string="CACHE_TIME: ", default="1second"
    )
    map_freq_def = fields.Selection(
        selection=[
            ("daily", "Daily"),
            ("weekly", "Weekly"),
            ("monthly", "Monthly"),
        ], string="Change frequently", default="weekly"
    )
    map_prio_def = fields.Float("URL priority", default=0.5, help="Between 0,1 and 1,0")


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'sitemap_base.settings'

    def _default_website(self):
        return self.env['website'].search([], limit=1)

    website_id = fields.Many2one('website', string="website", default=_default_website, required=True)
    map_add_icon = fields.Boolean(related='website_id.map_add_icon')
    map_add_robot = fields.Boolean(related='website_id.map_add_robot')
    map_add_pages = fields.Boolean(related='website_id.map_add_pages')
    map_add_cats = fields.Boolean(related='website_id.map_add_cats')
    map_add_prods = fields.Boolean(related='website_id.map_add_prods')
    map_add_blog = fields.Boolean(related='website_id.map_add_blog')
    map_cache_time = fields.Selection(related='website_id.map_cache_time')
    map_freq_def = fields.Selection(related='website_id.map_freq_def')
    map_prio_def = fields.Float(related='website_id.map_prio_def')

    @api.constrains('map_prio_def')
    def _check_priority_value(self):
        for r in self:
            if r.map_prio_def < 0.1 or r.map_prio_def > 1:
                raise ValidationError(_('URL priority must be between 0,1 and 1,0'))
