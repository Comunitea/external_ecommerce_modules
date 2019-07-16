# -*- coding: utf-8 -*-

from odoo import http, api, models, fields, _

from odoo.http import request


class WebsiteBlog(models.Model):
    _inherit = 'website'

    @api.multi
    def blogs(self):
        """
        :return: all active blogs for current website
        """
        website = self.id
        domain_blog = [('website_ids', '=', website), ('active', '=', True)]
        blogs = request.env['blog.blog'].sudo().search(domain_blog)

        return blogs

    @api.multi
    def latest_posts(self, qty, columns, title, read_all):
        """
        Set data for generate post list to all blogs of current website.

        :param qty: number of posts to show: integer
        :param columns: number of columns: integer (from 2 to 4)
        :param title: section H2 title: string, may be empty
        :param read_all: title of button "Read all news": string, may be empty
        :return: result dict with the last post of all blogs of current website ordered by date desc..
        """
        # Search blog of current website
        website = self.id
        domain_blog = [('website_ids', '=', website)]
        blogs = request.env['blog.blog'].sudo().search(domain_blog)

        # Search published posts if blog exists
        posts = []
        if blogs:
            for blog in blogs:
                domain = [('blog_id', '=', blog.id), ('active', '=', True), ('website_published', '=', True)]
                post = request.env['blog.post'].sudo().search(domain, limit=qty, order='post_date desc')
                if post and post not in posts:
                    posts += post

        # Set bootstrap width class for post div (support from 2 to 4 columns)
        cols_md = {2: 6, 3: 4, 4: 3}
        col_md = cols_md.get(columns, 4)

        # Return of latest posts
        result = {
            'posts': posts,
            'col_md': col_md,
            'title': title or _("Our latest news"),
            'read_all': read_all or _("Read all our news")
        }
        return result

    @api.multi
    def access_to_blog(self, blog):
        """
        Check user permission access for one blog
        :param blog: blog to check
        :return: True if user has access to this blog, false otherwise
        """
        user = request.env.user
        access = False

        user_b2b = user.has_group('sale.group_show_price_subtotal')
        user_b2c = user.has_group('sale.group_show_price_total') or user.has_group('base.group_public')
        user_admin = user.has_group('website.group_website_publisher') or user.has_group('base.group_user')

        if (blog.for_retailers and user_b2b) or (blog.for_customers and user_b2c) or user_admin:
            access = True

        return access

    @api.multi
    def access_to_blogs(self, blogs):
        """
        Check user permission access for all blogs
        :param blogs: blogs to check
        :return: True if user has access to all blogs, false otherwise
        """
        user = request.env.user
        access = False

        user_b2b = user.has_group('sale.group_show_price_subtotal')
        user_b2c = user.has_group('sale.group_show_price_total') or user.has_group('base.group_public')
        user_admin = user.has_group('website.group_website_publisher') or user.has_group('base.group_user')

        for blog in blogs:
            if (blog.for_retailers and user_b2b) or (blog.for_customers and user_b2c) or user_admin:
                access = True

        return access
