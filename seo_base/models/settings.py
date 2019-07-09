# -*- coding: utf-8 -*-

from odoo import http, api, models, fields, _
from odoo.http import request
from odoo.exceptions import ValidationError


def _default_website(self):
    domain = []
    host = request and request.httprequest.host.split(':')[0]
    if host:
        domain = [('domain', '=ilike', host)]
    website = self.env['website'].search(domain, limit=1)
    if not website:
        website = self.env['website'].search([], limit=1)
    return website


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
        ], string=_("Browser console mode: "), default="usr"
    )
    map_add_icon = fields.Boolean('Favicon.ico', default=False)
    map_add_robot = fields.Boolean('Robots.txt', default=False)
    map_add_pages = fields.Boolean(_("Static pages"), default=False)
    map_add_cats = fields.Boolean(_("Product public categories"), default=False)
    map_add_prods = fields.Boolean(_("Published products"), default=False)
    map_add_blog = fields.Boolean(_("Blog pages"), default=False)
    map_freq_def = fields.Selection(
        selection=[
            ("daily", "Daily"),
            ("weekly", "Weekly"),
            ("monthly", "Monthly")
        ], string=_("Change frequently"), default="weekly"
    )
    map_prio_def = fields.Float(_("URL priority"), default=0.5, help=_("Between 0,1 and 1,0"))
    robots_txt_content = fields.Text(_("Robots.txt content"))
    slug_length = fields.Integer(_("Friendly URL max length"), default=40)
    web_app_icon = fields.Binary(_("App icon"))
    web_app_name = fields.Char(_("App name"), help=_("Icon name on the homescreen of device"))
    web_app_short_name = fields.Char(_("App short name"))
    web_app_description = fields.Char(_("App short description"))
    web_app_start_url = fields.Char(_("App start URL"))
    web_app_background_color = fields.Char(_("App background color"), help=_("In the HEX format, ex: #7c7bad"))
    web_app_theme_color = fields.Char(_("App theme color"), help=_("In the HEX format, ex: #7c7bad"))
    web_app_display = fields.Selection(selection=[
        ("standalone", _("Standalone native app")),
        ("fullscreen", "Fullscreen"),
        ("browser", "Standart")
    ], string=_("App display mode"), default="browser")
    web_app_code = fields.Text(_("Manifest additional code"))
    sw_offline = fields.Boolean(_("Use service worker offline cache"), default=False)
    sw_code = fields.Text(_("Service worker cache list"))
    google_tag_manager_key = fields.Char(_("Google tag manager key"))
    facebook_pixel_key = fields.Char(_("Facebook Pixel key"))
    web_public_shop = fields.Boolean(string=_("Public shop"), default=True)
    shop_access_rules = fields.Selection(selection=[
        ('b2c', _("Only portal users logged with B2C")),
        ('b2b', _("Only portal users logged with B2B"))
    ], string=_("Store access rules:"), default='b2b')

    @api.multi
    def unlink(self):
        for r in self:
            domain = [('website_id', '=', r.id)]
            # Remove website settings with a website delete
            r.env['res.config.settings'].sudo().search(domain).unlink()
            r.env['sitemap_base.settings'].sudo().search(domain).unlink()
            r.env['robots_txt.settings'].sudo().search(domain).unlink()
            r.env['seo_general.settings'].sudo().search(domain).unlink()
            r.env['web_app.settings'].sudo().search(domain).unlink()
            return super(Website, r).unlink()


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
                raise ValidationError(_("URL priority must be between 0,1 and 1,0"))


class RobotsConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'robots_txt.settings'

    website_id = fields.Many2one('website', string="website", default=_default_website, required=True)
    robots_txt_content = fields.Text(related='website_id.robots_txt_content')


class SeoGeneralConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'seo_general.settings'

    website_id = fields.Many2one('website', string="website", default=_default_website, required=True)
    slug_length = fields.Integer(related='website_id.slug_length', default=40)
    cache_mode = fields.Selection(related='website_id.cache_mode',
                                  selection=[("1second", "Developer mode"), ("12hours", "Normal mode")],
                                  string="CACHE_TIME: ",
                                  default="12hours")
    console_mode = fields.Selection(related='website_id.console_mode',
                                    selection=[("dev", "Developer mode"), ("usr", "Normal mode")],
                                    string=_("Browser console mode: "),
                                    default="usr")
    web_public_shop = fields.Boolean(related='website_id.web_public_shop', default=True)
    shop_access_rules = fields.Selection(related='website_id.shop_access_rules',
                                         selection=[('b2c', _("Only portal users logged with B2C")),
                                                    ('b2b', _("Only portal users logged with B2B"))],
                                         string=_("Store access rules:"), default='b2b')

    @api.constrains('slug_length')
    def _check_slug_length_value(self):
        for r in self:
            if r.slug_length < 20 or r.slug_length > 99:
                raise ValidationError(_("Friendly URL max length must be between 20 and 99"))


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


class AnalyticsConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'seo_analytics.settings'

    website_id = fields.Many2one('website', string="website", default=_default_website, required=True)
    google_tag_manager_key = fields.Char(related='website_id.google_tag_manager_key')
    facebook_pixel_key = fields.Char(related='website_id.facebook_pixel_key')
