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


class Sitemap(Website):
    @http.route('/sitemap.xml', type='http', auth="public", website=True, multilang=False)
    def sitemap_generator(self):
        current_website = request.website
        current_company = current_website.company_id
        attachment = request.env['ir.attachment'].sudo()
        view = request.env['ir.ui.view'].sudo()
        mimetype = 'application/xml;charset=utf-8'
        cache_content = None

        # Set default values
        freq_def = request.website.map_freq_def or 'weekly'
        prio_def = round(request.website.map_prio_def, 1) or '0.5'

        # Set cache live time
        if request.website.map_cache_time and request.website.map_cache_time == '12hours':
            cache_time = datetime.timedelta(hours=12)
        else:
            cache_time = datetime.timedelta(seconds=1)

        def create_sitemap(url, content):
            return attachment.create({
                'datas': base64.b64encode(content),
                'mimetype': mimetype,
                'type': 'binary',
                'name': url,
                'url': url,
            })

        def create_one(loc, lastmod, changefreq, image, priority):
            return view.render_template('seo_base.sitemap_tpl', {
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
            if delta < cache_time:
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
            sitemap_content = create_one(root, first_day, freq_def, image, prio_def)

            if request.website.map_add_icon:
                # Add favicon.ico
                sitemap_content += create_one(root + 'favicon.ico', first_day, freq_def, root + 'favicon.ico', prio_def)

            if request.website.map_add_robot:
                # Add robots.txt
                sitemap_content += create_one(root + 'robots.txt', first_day, freq_def, '', prio_def)

            if request.website.map_add_pages:
                # Add static pages
                domain = [('website_indexed', '=', True)]
                domain += [('website_published', '=', True)]
                domain += [('website_ids', '=like', current_website.id)]
                page_ids = request.env['website.page'].sudo().search(domain)

                for r in page_ids:
                    loc = '%s%s' % (root, r.url[1:])
                    sitemap_content += create_one(loc, r.write_date[:-9], freq_def, '', prio_def)

            if request.website.map_add_cats:
                # Add product public categories
                domain = [('website_ids', '=like', current_website.id)]
                category_ids = request.env['product.public.category'].sudo().search(domain)

                for r in category_ids:
                    loc = '%sshop/category/%s' % (root, slug(r))
                    if r.image_medium:
                        image = '%sweb/image/product.public.category/%s/image_medium/' % (root, r.id)
                    else:
                        image = ''
                    sitemap_content += create_one(loc, r.write_date[:-9], freq_def, image, prio_def)

            if request.website.map_add_prods:
                # Add active and published products
                domain = [('sale_ok', '=', True)]
                domain += [('active', '=', True)]
                domain += [('website_published', '=', True)]
                domain += [('website_ids', '=like', current_website.id)]
                product_ids = request.env['product.template'].sudo().search(domain)

                for r in product_ids:
                    loc = '%sshop/product/%s' % (root, slug(r))
                    image = '%sweb/image/product.template/%s/image/' % (root, r.id) if r.image else ''
                    sitemap_content += create_one(loc, r.write_date[:-9], freq_def, image, prio_def)

            if request.website.map_add_blog:
                # Add blog pages
                domain = [('website_ids', '=like', current_website.id)]
                blog_ids = request.env['blog.blog'].sudo().search(domain)

                for r in blog_ids:
                    loc = '%sblog/%s' % (root, slug(r))
                    sitemap_content += create_one(loc, r.write_date[:-9], freq_def, '', prio_def)

                # Add post pages
                domain = [('active', '=', True)]
                domain += [('website_published', '=', True)]

                domain += [('blog_id', 'in', blog_ids.ids)]

                post_ids = request.env['blog.post'].sudo().search(domain)

                for r in post_ids:
                    loc = '%sblog/%s/post/%s' % (root, slug(r.blog_id), slug(r))
                    sitemap_content += create_one(loc, r.write_date[:-9], freq_def, '', prio_def)

            # Sitemap generation
            content = view.render_template('seo_base.sitemap_wrap', {'content': sitemap_content})
            create_sitemap('/sitemap-%d.xml' % current_website.id, content)
        else:
            content = cache_content

        return request.make_response(content, [('Content-Type', mimetype)])
