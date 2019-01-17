# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


def _default_website(self):
    return self.env['website'].search([], limit=1)


class Website(models.Model):
    _inherit = 'website'

    cache_mode = fields.Selection(
        selection=[
            ("1second", "Developer mode"),
            ("12hours", "Normal mode")
        ], string="CACHE_TIME: ", default="1second"
    )
    console_mode = fields.Selection(
        selection=[
            ("dev", "Developer mode"),
            ("usr", "Normal mode")
        ], string="Browser console mode: ", default="usr"
    )
    map_add_icon = fields.Boolean('Favicon.ico', default=False)
    map_add_robot = fields.Boolean('Robots.txt', default=False)
    map_add_pages = fields.Boolean('Static pages', default=False)
    map_add_cats = fields.Boolean('Product public categories', default=False)
    map_add_prods = fields.Boolean('Published products', default=False)
    map_add_blog = fields.Boolean('Blog pages', default=False)
    map_freq_def = fields.Selection(
        selection=[
            ("daily", "Daily"),
            ("weekly", "Weekly"),
            ("monthly", "Monthly")
        ], string="Change frequently", default="weekly"
    )
    map_prio_def = fields.Float("URL priority", default=0.5, help="Between 0,1 and 1,0")
    robots_txt_content = fields.Text(_("Robots.txt content"))
    slug_length = fields.Integer("Friendly URL max length", default=40)
    web_app_icon = fields.Binary("App icon", required=True)
    web_app_name = fields.Char("App name", help="Icon name on the homescreen of device")
    web_app_short_name = fields.Char("App short name")
    web_app_description = fields.Char("App short description")
    web_app_start_url = fields.Char("App start URL")
    web_app_background_color = fields.Char("App background color", help="In the HEX format, ex: #7c7bad")
    web_app_theme_color = fields.Char("App theme color", help="In the HEX format, ex: #7c7bad")
    web_app_display = fields.Selection(selection=[
        ("standalone", "Standalone native app"),
        ("fullscreen", "Fullscreen"),
        ("browser", "Standart")
    ], string="App display mode", default="browser")
    web_app_code = fields.Text("Manifest additional code")
    sw_offline = fields.Boolean("Use service worker offline cache", default=False)
    sw_code = fields.Text("Service worker cache list")


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'sitemap_base.settings'

    website_id = fields.Many2one('website', string="website", default=_default_website, required=True)
    map_add_icon = fields.Boolean(related='website_id.map_add_icon')
    map_add_robot = fields.Boolean(related='website_id.map_add_robot')
    map_add_pages = fields.Boolean(related='website_id.map_add_pages')
    map_add_cats = fields.Boolean(related='website_id.map_add_cats')
    map_add_prods = fields.Boolean(related='website_id.map_add_prods')
    map_add_blog = fields.Boolean(related='website_id.map_add_blog')
    map_freq_def = fields.Selection(related='website_id.map_freq_def')
    map_prio_def = fields.Float(related='website_id.map_prio_def')

    @api.constrains('map_prio_def')
    def _check_priority_value(self):
        for r in self:
            if r.map_prio_def < 0.1 or r.map_prio_def > 1:
                raise ValidationError(_('URL priority must be between 0,1 and 1,0'))


class RobotsConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'robots_txt.settings'

    website_id = fields.Many2one('website', string="website", default=_default_website, required=True)
    robots_txt_content = fields.Text(related='website_id.robots_txt_content')


class SeoGeneralConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'seo_general.settings'

    website_id = fields.Many2one('website', string="website", default=_default_website, required=True)
    slug_length = fields.Integer(related='website_id.slug_length')
    cache_mode = fields.Selection(related='website_id.cache_mode')
    console_mode = fields.Selection(related='website_id.console_mode')

    @api.constrains('slug_length')
    def _check_slug_length_value(self):
        for r in self:
            if r.slug_length < 20 or r.slug_length > 99:
                raise ValidationError(_('Friendly URL max length must be between 20 and 99'))


class WebAppConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'web_app.settings'

    website_id = fields.Many2one('website', string="website", default=_default_website, required=True)
    web_app_icon = fields.Binary(related='website_id.web_app_icon')
    web_app_name = fields.Char(related='website_id.web_app_name')
    web_app_short_name = fields.Char(related='website_id.web_app_short_name')
    web_app_description = fields.Char(related='website_id.web_app_description')
    web_app_start_url = fields.Char(related='website_id.web_app_start_url')
    web_app_background_color = fields.Char(related='website_id.web_app_background_color')
    web_app_theme_color = fields.Char(related='website_id.web_app_theme_color')
    web_app_display = fields.Selection(related='website_id.web_app_display')
    web_app_code = fields.Text(related='website_id.web_app_code')
    sw_offline = fields.Boolean(related='website_id.sw_offline')
    sw_code = fields.Text(related='website_id.sw_code')
