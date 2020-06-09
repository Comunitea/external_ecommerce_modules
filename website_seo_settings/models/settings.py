# -*- coding: utf-8 -*-

from odoo import http, api, models, fields, _

from odoo.http import request
from odoo.exceptions import ValidationError


def _default_website(self):
    # Check if website is forced
    if request and request.session.get('force_website_id', False):
        return self.env['website'].browse(request.session['force_website_id'])

    # Check if website is in context
    website_id = self.env.context.get('website_id', False)
    if website_id:
        return self.env['website'].browse(website_id)

    # Search website by host
    domain = []
    host = request and (request.httprequest.host or '').split(':')[0]
    if host:
        domain = [('domain', '=ilike', host)]
    websites = self.env['website'].search(domain)
    if not websites:
        # Find the first company's website, if there is one or first website
        company_id = request and request.env.user.company_id.id or None
        domain = []
        if company_id:
            domain = [('company_id', '=', company_id)]
        websites = self.env['website'].search(domain, limit=1)
    elif len(websites) == 1:
        return websites[0]
    else:
        # > 1 website with the same domain. Find the first website by country groups
        country = request.session.geoip.get('country_code') if request and request.session.geoip else False
        if country:
            country_id = self.env['res.country'].search([('code', '=', country)], limit=1).id
            country_specific_websites = websites.filtered(
                lambda website: country_id in website.country_group_ids.mapped('country_ids').ids)
            return country_specific_websites[0] if country_specific_websites else websites[0]

    return websites and websites[0] or False

class Website(models.Model):
    _inherit = 'website'

    # General Settings
    cache_mode = fields.Selection(
        selection=[
            ("1second", _("Developer mode")),
            ("12hours", _("Normal mode"))
        ], string="Cache mode: ", default="12hours"
    )
    console_mode = fields.Selection(
        selection=[
            ("dev", _("Developer mode")),
            ("user", _("Normal mode"))
        ], string=_("Console mode: "), default="user"
    )
    slug_length = fields.Integer(_("Friendly URL max length"), default=40)
    web_public_shop = fields.Boolean(string=_("Public shop"), default=True)
    shop_access_rules = fields.Selection(selection=[('b2c', _("Only users B2C")),
                                                    ('b2b', _("Only users B2B"))],
                                         string=_("Shop access rules:"), default='b2b')

    # Sitemap Settings
    map_add_icon = fields.Boolean('Favicon.ico', default=False)
    map_add_robot = fields.Boolean('Robots.txt', default=False)
    map_add_pages = fields.Boolean(_("Static pages"), default=False)
    map_add_cats = fields.Boolean(_("Product public categories"), default=False)
    map_add_prods = fields.Boolean(_("Published products"), default=False)
    map_add_blog = fields.Boolean(_("Blog pages"), default=False)
    map_freq_def = fields.Selection(
        selection=[
            (_("daily"), _("Daily")),
            (_("weekly"), _("Weekly")),
            (_("monthly"), _("Monthly"))
        ], string=_("Frequency update"), default="weekly"
    )
    map_prio_def = fields.Float(_("URL priority"), default=0.5, help=_("Between 0,1 and 1,0"))

    # Web App Progressive Settings
    web_app_icon = fields.Binary(_("App icon"))
    web_app_name = fields.Char(_("App name"), help=_("Icon name on the homescreen of device"))
    web_app_cache_name = fields.Char(_("App cache name"),
                                     help=_("Change this name let refresh cache when new resources are available"))
    web_app_short_name = fields.Char(_("App short name"))
    web_app_description = fields.Char(_("App short description"))
    web_app_start_url = fields.Char(_("App start URL"))
    web_app_background_color = fields.Char(_("App background color"), help=_("In the HEX format, ex: #7c7bad"))
    web_app_theme_color = fields.Char(_("App theme color"), help=_("In the HEX format, ex: #7c7bad"))
    web_app_display = fields.Selection(selection=[("standalone", _("Native App")),
                                                  ("fullscreen", _("Fullscreen")),
                                                  ("minimal-ui", _("Minimal")),
                                                  ("browser", _("Browser"))],
                                       string=_("Display mode"), default="standalone")
    web_app_orientation = fields.Selection(selection=[("portrait", _("Portrait")),
                                                  ("landscape", _("Landscape"))],
                                       string=_("Orientation mode"), default="portrait")
    web_app_code = fields.Text(_("Manifest additional code"))
    sw_offline = fields.Boolean(_("Use service worker offline cache"), default=False)
    sw_code = fields.Text(_("Service worker cache list"))

    # Analytics Settings
    facebook_pixel_key = fields.Char(_("Facebook Pixel key"))

    # Robots Settings
    robots_txt_content = fields.Text(_("Robots.txt content"))

    @api.multi
    def unlink(self):
        for r in self:
            domain = [('website_id', '=', r.id)]
            # Remove website settings with a website delete
            if r.env.get('res.config.settings', False):
                r.env['res.config.settings'].sudo().search(domain).unlink()
            if r.env.get('sitemap_base.settings', False):
                r.env['sitemap_base.settings'].sudo().search(domain).unlink()
            if r.env.get('robots_txt.settings', False):
                r.env['robots_txt.settings'].sudo().search(domain).unlink()
            if r.env.get('seo_general.settings', False):
                r.env['seo_general.settings'].sudo().search(domain).unlink()
            if r.env.get('web_app.settings', False):
                r.env['web_app.settings'].sudo().search(domain).unlink()
            return super(Website, r).unlink()


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # General Settings
    website_id = fields.Many2one('website', string="website", default=_default_website, required=True)
    slug_length = fields.Integer(related='website_id.slug_length', default=40, readonly=False)
    cache_mode = fields.Selection(related='website_id.cache_mode', readonly=False,
                                  selection=[(_("1second"), _("Developer mode")), (_("12hours"), _("Normal mode"))],
                                  string="Cache mode: ",
                                  default="12hours")
    console_mode = fields.Selection(related='website_id.console_mode', readonly=False,
                                    selection=[(_("dev"), _("Developer mode")), (_("user"), _("Normal mode"))],
                                    string=_("Browser console mode: "),
                                    default="user")
    web_public_shop = fields.Boolean(related='website_id.web_public_shop', default=True, readonly=False)
    shop_access_rules = fields.Selection(related='website_id.shop_access_rules', readonly=False,
                                         selection=[('b2c', _("Only users B2C")),
                                                    ('b2b', _("Only users B2B"))],
                                         string=_("Shop access rules:"), default='b2b')

    @api.constrains('slug_length')
    def _check_slug_length_value(self):
        for r in self:
            if r.slug_length < 20 or r.slug_length > 99:
                raise ValidationError(_("Friendly URL max length must be between 20 and 99"))

    # Sitemap Settings
    map_add_icon = fields.Boolean(related='website_id.map_add_icon', readonly=False)
    map_add_robot = fields.Boolean(related='website_id.map_add_robot', readonly=False)
    map_add_pages = fields.Boolean(related='website_id.map_add_pages', readonly=False)
    map_add_cats = fields.Boolean(related='website_id.map_add_cats', readonly=False)
    map_add_prods = fields.Boolean(related='website_id.map_add_prods', readonly=False)
    map_add_blog = fields.Boolean(related='website_id.map_add_blog', readonly=False)
    map_freq_def = fields.Selection(related='website_id.map_freq_def', readonly=False)
    map_prio_def = fields.Float(related='website_id.map_prio_def', readonly=False)

    @api.constrains('map_prio_def')
    def _check_priority_value(self):
        for r in self:
            if r.map_prio_def < 0.1 or r.map_prio_def > 1:
                raise ValidationError(_("URL priority must be between 0,1 and 1,0"))

    # Web App Progressive Settings
    web_app_icon = fields.Binary(related='website_id.web_app_icon', readonly=False)
    web_app_name = fields.Char(related='website_id.web_app_name', readonly=False)
    web_app_cache_name = fields.Char(related='website_id.web_app_cache_name', readonly=False)
    web_app_short_name = fields.Char(related='website_id.web_app_short_name', readonly=False)
    web_app_description = fields.Char(related='website_id.web_app_description', readonly=False)
    web_app_start_url = fields.Char(related='website_id.web_app_start_url', readonly=False)
    web_app_background_color = fields.Char(related='website_id.web_app_background_color', readonly=False)
    web_app_theme_color = fields.Char(related='website_id.web_app_theme_color', readonly=False)
    web_app_display = fields.Selection(related='website_id.web_app_display', readonly=False)
    web_app_orientation = fields.Selection(related='website_id.web_app_orientation', readonly=False)
    web_app_code = fields.Text(related='website_id.web_app_code', readonly=False)
    sw_offline = fields.Boolean(related='website_id.sw_offline', readonly=False)
    sw_code = fields.Text(related='website_id.sw_code', readonly=False)

    # Analytics Settings
    facebook_pixel_key = fields.Char(related='website_id.facebook_pixel_key', readonly=False)

    # Robots Settings
    robots_txt_content = fields.Text(related='website_id.robots_txt_content', readonly=False)
