# -*- coding: utf-8 -*-

import base64
import datetime

from odoo import api, fields, http, models

from odoo.http import request

from odoo.addons.website.controllers.main import Website


class ProgressiveWebApp(Website):

    def _auto_create(self, name, type, mimetype):
        attachment = request.env['ir.attachment'].sudo()
        view = request.env['ir.ui.view'].sudo()
        cache_content = None
        website = request.website

        # Set cache live time
        if website.cache_mode and website.cache_mode == '12hours':
            cache_time = datetime.timedelta(hours=12)
        else:
            cache_time = datetime.timedelta(seconds=1)

        def create_file(url, content, mimetype):
            return attachment.create({
                'datas': base64.b64encode(content),
                'mimetype': mimetype,
                'type': 'binary',
                'name': url,
                'url': url
            })

        # Check of an attachment in cache
        dom = [('name', '=', name), ('type', '=', 'binary')]
        file = attachment.search(dom, limit=1)

        if file:
            # Check if it's still real
            create_date = fields.Datetime.from_string(file.create_date)
            delta = datetime.datetime.now() - create_date
            if delta < cache_time:
                cache_content = base64.b64decode(file.datas)

        if not cache_content:
            # Remove all old files
            to_remove = attachment.search(dom)
            to_remove.unlink()

            if type == 'manifest':
                icon_name = 'web-app-icon-%d' % website.id
                # Remove all old icons
                dom = [('name', '=', icon_name), ('type', '=', 'binary')]
                to_remove = attachment.search(dom)
                to_remove.unlink()

                # Generate new icon
                app_icon = attachment.create({
                    'datas': website.web_app_icon or website.favicon,
                    'mimetype': 'image/png',
                    'type': 'binary',
                    'public': 'true',
                    'name': icon_name,
                    'url': icon_name
                })

                # Set content for manifest.json
                values = {
                    'name': website.web_app_name or website.name,
                    'short_name': website.web_app_short_name or website.name,
                    'description': website.web_app_description or '%s Progressive Web App' % website.name,
                    'start_url': '%s' % (website.web_app_start_url or ''),
                    'background_color': website.web_app_background_color or '#ffffff',
                    'theme_color': website.web_app_theme_color or '#7c7bad',
                    'display': website.web_app_display or 'standalone',
                    'orientation': website.web_app_orientation or 'portrait',
                    'icon_id': app_icon.id,
                    'lang': website.default_lang_code,
                    'content': website.web_app_code or ''
                }
                # Write content to template
                content = view.render_template('website_seo_settings.web_app_manifest', {'values': values})

            elif type == 'sw':
                # Set content for sw.json
                values = {
                    'name': website.web_app_name or website.name,
                    'console_mode': website.console_mode or 'user',
                    'start_url': '%s' % (website.web_app_start_url or ''),
                    'content': website.sw_code or '',
                    'cache_name': website.web_app_cache_name or website.name.split()[0].lower()
                }
                # Write content to template
                content = view.render_template('website_seo_settings.web_app_sw', {'values': values})

            else:
                content = ''

            # Create new file
            create_file(name, content, mimetype)
        else:
            content = cache_content

        return request.make_response(content, [('Content-Type', mimetype)])

    @http.route('/manifest.json', type='http', auth="none", website=True)
    def manifest_redirect(self):
        current_website = request.website.sudo()
        return self._auto_create('/manifest-%d.json' % current_website.id,
                                 'manifest', 'application/json;charset=utf-8')

    @http.route('/sw.js', type='http', auth="none", website=True)
    def sw_redirect(self):
        current_website = request.website.sudo()
        return self._auto_create('/sw-%d.js' % current_website.id, 'sw', 'application/javascript;charset=utf-8')
