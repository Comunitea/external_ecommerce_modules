# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import base64
import datetime
from odoo import http, api, models, fields
from odoo.http import request
from odoo.addons.website.controllers.main import Website


class ProgressiveWebApp(Website):

    def _auto_create(self, name, mimetype):
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
                'description': website.web_app_description or '%s web app' % website.domain,
                'start_url': '%s?homescreen=1' % (website.web_app_start_url or '/'),
                'background_color': website.web_app_background_color or '#ffffff',
                'theme_color': website.web_app_theme_color or '#7c7bad',
                'display': website.web_app_display or 'browser',
                'icon_id': app_icon.id,
                'lang': website.default_lang_code,
                'content': website.web_app_code or ''
            }
            # Write content to template
            content = view.render_template('seo_base.web_app_manifest_template', {'values': values})

            # Create new file
            create_file(name, content, mimetype)
        else:
            content = cache_content

        return request.make_response(content, [('Content-Type', mimetype)])

    @http.route('/manifest.json', type='http', auth="none", website=True)
    def manifest_redirect(self):
        current_website = request.website.sudo()
        return self._auto_create('/manifest-%d.json' % current_website.id, 'application/json;charset=utf-8')
