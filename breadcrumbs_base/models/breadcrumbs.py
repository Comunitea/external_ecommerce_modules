# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, models, fields, _
from odoo.http import request
from odoo.addons.http_routing.models.ir_http import slug


class Crumb(models.Model):
    _name = 'breadcrumbs_base.crumb'

    name = fields.Text(translate=True)
    url = fields.Text()
    active = fields.Boolean()


def _generate_one(name, url, active):
    crumb = request.env['breadcrumbs_base.crumb'].sudo()
    # Find the current crumb element and create it if it doesn't exist
    exist = crumb.search([('name', '=', name), ('url', '=', url), ('active', '=', active)])
    if exist:
        result = exist
    else:
        result = crumb.create({'name': name, 'url': url, 'active': active})
    return result


class BreadCrumbs(models.Model):
    _inherit = 'website'

    @api.multi
    def generate_breadcrumbs(self, main_object, website):
        breadcrumbs = self.env['breadcrumbs_base.crumb'].sudo()

        def _get_parent(object, result):
            parent = object.parent_id
            if parent:
                result.append(object.id)
                _get_parent(parent, result)
            else:
                result.append(object.id)
            return result

        if main_object._name == 'product.template':
            product = main_object
            # Add shop crumb
            breadcrumbs += _generate_one(_("Products"), '/shop', False)
            # Add parent categories crumb
            if product.public_categ_ids:
                parent_cat = product.public_categ_ids[0]

                if parent_cat:
                    parent_res = _get_parent(parent_cat, [])
                    parent_res.reverse()
                    for res in parent_res:
                        cat = self.env['product.public.category'].sudo().search([('id', '=', res)])
                        cat_url = '/category/%s' % cat.slug if cat.slug else '/shop/category/%s' % slug(cat)
                        breadcrumbs += _generate_one(cat.name, cat_url, False)

            # Add current product crumb
            breadcrumbs += _generate_one(product.name, '', True)
        elif main_object._name == 'product.public.category':
            category = main_object
            # Add shop crumb
            breadcrumbs += _generate_one(_("Products"), '/shop', False)
            # Add parent categories crumb
            parent_cat = category.parent_id

            if parent_cat:
                parent_res = _get_parent(parent_cat, [])
                parent_res.reverse()
                for res in parent_res:
                    cat = self.env['product.public.category'].sudo().search([('id', '=', res)])
                    cat_url = '/category/%s' % cat.slug if cat.slug else '/shop/category/%s' % slug(cat)
                    breadcrumbs += _generate_one(cat.name, cat_url, False)

            # Add current category crumb
            breadcrumbs += _generate_one(category.name, '', True)
        elif main_object._name == 'website.page':
            page = main_object
            if page.parent_id:
                parent_res = _get_parent(page.parent_id, [])
                parent_res.reverse()
                for res in parent_res:
                    parent = self.env['website.page'].sudo().search([('id', '=', res)])
                    breadcrumbs += _generate_one(parent.name, parent.url, False)
            breadcrumbs += _generate_one(page.name, page.url, True)
        elif main_object._name == 'ir.ui.view':
            view = main_object
            # Find the current website page that uses this view
            domain = [('view_id', '=', view.id)]
            domain += [('website_id', '=', website.id)]
            page = self.env['website.page'].sudo().search(domain)
            # If there is no page with current view -> search page with current url
            if not page:
                path = request.httprequest.path
                domain = [('url', '=', path), ('website_id', '=', website.id)]
                page = self.env['website.page'].sudo().search(domain)
            if page:
                if page.parent_id:
                    parent_res = _get_parent(page.parent_id, [])
                    parent_res.reverse()
                    for res in parent_res:
                        parent = self.env['website.page'].sudo().search([('id', '=', res)])
                        breadcrumbs += _generate_one(parent.name, parent.url, False)
                breadcrumbs += _generate_one(page.name, page.url, True)
            else:
                breadcrumbs += _generate_one(view.name, slug(view), True)
        elif main_object._name == 'blog.blog':
            blog = main_object
            breadcrumbs += _generate_one(blog.name, slug(blog), True)
        elif main_object._name == 'blog.post':
            post = main_object
            blog = post.blog_id
            # Add parent blog crumb
            breadcrumbs += _generate_one(blog.name, '/blog/%s' % slug(blog), False)
            # Add post crumb
            breadcrumbs += _generate_one(post.name, slug(post), True)

        return breadcrumbs
