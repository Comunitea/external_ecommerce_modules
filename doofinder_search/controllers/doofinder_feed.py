# -*- coding: utf-8 -*-
# © 2019 Comunitea - Pavel Smirnov <pavel@comunitea.com> & Ruben Seijas <ruben@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import re
from odoo import http, api, models, fields
from odoo.http import request
from odoo.addons.website.controllers.main import Website
from odoo.addons.website.models.website import slug


class DoofinderFeed(Website):
    @http.route('/doofinder/feed', type='http', auth="public", website=True, multilang=False)
    def doofinder_feed_generator(self):
        current_website = request.website
        attachment = request.env['ir.attachment'].sudo()
        view = request.env['ir.ui.view'].sudo()
        mimetype = 'text/plain;charset=utf-8'
        root = request.httprequest.url_root
        feed_content = ''

        # File generator
        def create_file(url, content):
            return attachment.create({
                'datas': content.encode('base64'),
                'mimetype': mimetype,
                'type': 'binary',
                'name': url,
                'url': url,
            })

        def get_tags(tag_ids):
            result = ''
            for tag in tag_ids:
                result += '%s/' % tag.name
            return result[:-1]

        def get_parent(object, result):
            parent = object.parent_id
            if parent:
                result += '%s > ' % parent.name
                if parent.parent_id:
                    get_parent(parent, result)
            result += '%s > ' % object.name
            return result

        def get_categories(cat_ids):
            result = ''
            for cat in cat_ids:
                if cat.parent_id:
                    result += get_parent(cat.parent_id, '')
                result += '%s %%%% ' % cat.name
            return result[:-4]

        def create_line(values):
            return view.render_template('doofinder_search.feed_line', {'values': values})

        # Add active and published products
        domain = [('sale_ok', '=', True)]
        domain += [('active', '=', True)]
        domain += [('website_published', '=', True)]
        product_ids = request.env['product.template'].sudo().search(domain)

        for prod in product_ids:

            # Price control
            price = 'N/D'
            if not prod.hide_website_price:
                if prod.website_public_price - prod.website_price > 0.01 and prod.pricelist_id.discount_policy == 'with_discount':
                    price = prod.website_public_price
                else:
                    price = prod.website_price

            values = {
                'id': prod.id,
                'title': prod.name,
                'link': '%sproduct/%s' % (root, prod.slug) if prod.slug else '%sshop/product/%s' % (root, slug(prod)),
                'description': prod.description_short or '',
                # 'alternate_description': '',  # X_x
                # 'meta_keywords': prod.product_meta_keywords or '',
                # 'meta_title': prod.product_meta_title or prod.name,
                # 'meta_description': prod.product_meta_description or prod.description_short,
                'image_link': '%sweb/image/product.template/%s/image/' % (root, prod.id) if prod.image else '',
                'categories': get_categories(prod.public_categ_ids) if prod.public_categ_ids else '',
                'availability': 'out of stock' if prod.availability == 'warning' else 'in stock',
                # 'brand': 'Nostrumsport',
                'mpn': prod.default_code or '',
                # 'extra_title_1': '',  # X_x
                # 'extra_title_2': '',  # X_x
                'tags': get_tags(prod.tag_ids) if prod.tag_ids else '',
                'price': price,  # prod.list_price or '', #  price has price control, list_price has not
                # 'sale_price': '',  # X_x
            }
            # Delete spaces and line breaks
            feed_content += re.sub("^\s+|\n|\r|\s+$", '', create_line(values))
            feed_content += '\n'

        # Add product lines to file template
        content = view.render_template('doofinder_search.feed_wrap', {'content': feed_content})

        # Remove old similar files
        to_remove = attachment.search([
            ('url', '=', '/doofinder-feed-%d.txt' % current_website.id),
            ('type', '=', 'binary')
        ])
        to_remove.unlink()

        # Create file and return it
        create_file('/doofinder-feed-%d.txt' % current_website.id, content)
        return request.make_response(content, [('Content-Type', mimetype)])
