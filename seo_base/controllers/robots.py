# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import base64
import datetime
from odoo import http, api, models, fields
from odoo.http import request
from odoo.addons.portal.controllers.web import Home


class Robots(Home):
    @http.route(['/robots.txt'], type='http', auth="public", website=True)
    def robots(self):
        current_website = request.website.sudo()
        attachment = request.env['ir.attachment'].sudo()
        view = request.env['ir.ui.view'].sudo()
        mimetype = 'text/plain;charset=utf-8'
        cache_content = None

        # Set cache live time
        if request.website.cache_mode and request.website.cache_mode == '12hours':
            cache_time = datetime.timedelta(hours=12)
        else:
            cache_time = datetime.timedelta(seconds=1)

        def create_file(url, content):
            return attachment.create({
                'datas': base64.b64encode(content),
                'mimetype': mimetype,
                'type': 'binary',
                'name': url,
                'url': url,
            })

        # Check of robots.txt actual
        dom = [('url', '=', '/robots-%d.txt' % current_website.id), ('type', '=', 'binary')]
        robots = attachment.search(dom, limit=1)

        if robots:
            create_date = fields.Datetime.from_string(robots.create_date)
            delta = datetime.datetime.now() - create_date
            if delta < cache_time:
                cache_content = base64.b64decode(robots.datas)

        if not cache_content:
            # Remove all old robots.txt for current website
            robots_to_remove = attachment.search(dom)
            robots_to_remove.unlink()

            # Create new robots.txt
            content = view.render_template('seo_base.robots_txt_wrap', {'content': request.website.robots_txt_content})
            create_file('/robots-%d.txt' % current_website.id, content)
        else:
            content = cache_content

        return request.make_response(content, [('Content-Type', mimetype)])
