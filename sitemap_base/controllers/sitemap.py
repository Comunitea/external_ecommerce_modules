# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import base64
import datetime
from datetime import date
from odoo import http, api, models, fields
from odoo.http import request
from odoo.addons.website.controllers.main import Website
from odoo.addons.http_routing.models.ir_http import slug

CACHE_TIME = datetime.timedelta(seconds=1)


class Sitemap(Website):
    @http.route('/sitemap.xml', type='http', auth="public", website=True, multilang=False)
    def sitemap_generator(self):
        current_website = request.website
        current_company = current_website.company_id
        attachment = request.env['ir.attachment'].sudo()
        view = request.env['ir.ui.view'].sudo()
        mimetype = 'application/xml;charset=utf-8'
        cache_content = None

        def create_sitemap(url, content):
            return attachment.create({
                'datas': base64.b64encode(content),
                'mimetype': mimetype,
                'type': 'binary',
                'name': url,
                'url': url,
            })

        def create_one(loc, lastmod, changefreq, image, priority):
            return view.render_template('sitemap_base.sitemap_tpl', {
                'loc': loc,
                'lastmod': lastmod,
                'changefreq': changefreq,
                'image': image,
                'priority': priority
            })

        # Check of sitemap actual
        dom = [('url', '=', '/sitemap-%d.xml' % current_website.id), ('type', '=', 'binary')]
        sitemap = attachment.search(dom, limit=1)
        if sitemap:
            create_date = fields.Datetime.from_string(sitemap.create_date)
            delta = datetime.datetime.now() - create_date
            if delta < CACHE_TIME:
                cache_content = base64.b64decode(sitemap.datas)

        if not cache_content:
            # Remove all old sitemaps for current website
            sitemaps = attachment.search(dom)
            sitemaps.unlink()

            # Create new sitemap
            today = date.today()
            first_day = date(today.year, today.month, 1)
            root = request.httprequest.url_root

            # Add home page
            image = '%sweb/image/res.company/%s/logo/' % (root, current_company.id)
            sitemap_content = create_one(root, first_day, 'weekly', image, '0.5')

            # Add favicon.ico
            sitemap_content += create_one(root + 'favicon.ico', first_day, 'weekly', root + 'favicon.ico', '0.5')
            #
            favicon_path = '%sweb/image/website/%s/favicon/' % (root, current_website.id)
            sitemap_content += create_one(favicon_path, first_day, 'weekly', favicon_path, '0.5')

            # Add robots.txt
            sitemap_content += create_one(root + 'robots.txt', first_day, 'weekly', '', '0.5')

            # Add static pages
            domain = [('website_indexed', '=', True)]
            domain += [('website_published', '=', True)]
            domain += [('website_ids', '=like', current_website.id)]
            page_ids = request.env['website.page'].sudo().search(domain)

            for r in page_ids:
                loc = '%s%s' % (root, r.url[1:])
                sitemap_content += create_one(loc, r.write_date[:-9], 'weekly', '', '0.5')

            # Add product public categories
            domain = [('website_ids', '=like', current_website.id)]
            category_ids = request.env['product.public.category'].sudo().search(domain)

            for r in category_ids:
                loc = '%sshop/category/%s' % (root, slug(r))
                if r.image_medium:
                    image = '%sweb/image/product.public.category/%s/image_medium/' % (root, r.id)
                else:
                    image = ''
                sitemap_content += create_one(loc, r.write_date[:-9], 'weekly', image, '0.5')

            # Add products

            # Add blog pages

            #
            #

            # Sitemap generation
            content = view.render_template('sitemap_base.sitemap_wrap', {'content': sitemap_content})
            create_sitemap('/sitemap-%d.xml' % current_website.id, content)
        else:
            content = cache_content

        return request.make_response(content, [('Content-Type', mimetype)])
