# -*- coding: utf-8 -*-
# © 2019 Comunitea - Pavel Smirnov <pavel@comunitea.com> & Ruben Seijas <ruben@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import datetime
from odoo import http, api, models, fields, _
from odoo.http import request
from odoo.addons.website.models.website import slug


class ExportFeeds(http.Controller):

    def create_file(self, url, content, mimetype):
        attachment = request.env['ir.attachment']
        return attachment.sudo().create({
            'datas': content.encode('base64'),
            'mimetype': mimetype,
            'type': 'binary',
            'name': url,
            'url': url,
        })

    @http.route('/google-merchant/<path:mode>/feed-<int:feed_id>.xml', type='http', auth='public', website=True)
    def export_feeds(self, mode, feed_id):
        attachment = request.env['ir.attachment']
        view = request.env['ir.ui.view']
        mimetype = 'application/xml;charset=utf-8'
        root = request.httprequest.url_root
        path = 'feed-%d.xml' % feed_id

        domain = ['&', ('url', '=', path), ('type', '=', 'binary')]

        # Search export model
        feed = request.env['google_merchant_export.feed'].search([('id', '=', feed_id)])
        if not feed:
            return request.render('website.404')

        # Check if the file already exists
        exist = attachment.search(domain, limit=1)
        if exist:
            exist.sudo().unlink()

        # Set export file data
        now = datetime.datetime.now()
        head = {
            'title': feed.name,
            'link': root,
            'author': feed.author,
            'updated': now.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        values = ''

        # Search categories parents
        def get_parent(object, result):
            parent = object.parent_id
            if parent:
                result += '%s > ' % parent.name
                if parent.parent_id:
                    get_parent(parent, result)
            result += '%s > ' % object.name
            return result

        def get_categories(category, result):
            if category.parent_id:
                result += get_parent(category.parent_id, '')
            result += '%s ' % category.name
            return result

        # Generate product entry
        def new_feed(product):
            return view.render_template('google_merchant_export.feed_wrap', {
                'id': product.id,
                'title': product.name,
                'description': product.description_short or product.website_meta_description or product.name,
                'link': '%sproduct/%s' % (root, product.slug) if product.slug else '%sshop/product/%s' % (root, slug(product)),
                'image_link': '%sweb/image/product.template/%s/image/' % (root, product.id),
                'condition': 'new',
                'availability': 'preorder' if product.sudo().qty_available == 0 else 'in stock',
                'price': '%s EUR' % product.list_price,
                # TODO: Auto calculate of shipping price for current product for Spain, Baleares and Canarias
                # 'shipping': '',
                'product_type': get_categories(product.public_categ_ids[0], '') if product.public_categ_ids else '',
                'barcode': product.barcode,
            })

        # Add products to the XML file
        if feed.export_all:
            domain = [('website_published', '=', True),
                      ('list_price', '>', '0'),
                      ('sale_ok', '=', True),
                      ('image', '!=', '')]
            products = request.env['product.template'].sudo().search(domain)
        else:
            products = feed.product_ids

        for res in products:
            values += new_feed(res)

        # Create export file
        content = view.render_template('google_merchant_export.xml_wrap', {'head': head, 'values': values})
        self.create_file(path, content, mimetype)

        # Set headers
        headers = [('Content-Type', mimetype)]
        if mode == 'download':
            headers.append(('Content-Disposition', 'attachment'))

        return request.make_response(content, headers)
