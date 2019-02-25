# -*- coding: utf-8 -*-

from odoo import http, api, models, fields, _
from odoo.http import request


class WebsiteBlog(models.Model):
    _inherit = 'website'

    @api.multi
    def latest_posts(self, qty, columns, title, read_all):
        # Search blog of current website
        website = self.id
        domain = [('website_ids', 'ilike', website)]
        blog = request.env['blog.blog'].sudo().search(domain, limit=1)

        # Search published posts if blog exists
        post_list = False
        if blog:
            domain = [('blog_id', '=', blog.id), ('active', '=', True), ('website_published', '=', True)]
            post_list = request.env['blog.post'].sudo().search(domain, limit=qty, order='post_date desc')

        # Set bootstrap width class for post div (support from 2 to 4 columns)
        cols_md = {2: 6, 3: 4, 4: 3}
        col_md = cols_md.get(columns, 4)

        # Return of latest posts
        result = {
            'posts': post_list,
            'col_md': col_md,
            'title': title or _("Our latest news"),
            'read_all': read_all or _("Read all our news")
        }
        return result
