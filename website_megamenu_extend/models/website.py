# -*- coding: utf-8 -*-
from odoo import models

from odoo.osv import expression


class Website(models.Model):
    _inherit = "website"

    def _get_product_public_categories(self, website=None, category_domain=None,
                                       category_domain_only_child=False,
                                       parent_hierarchy=True,
                                       product_hierarchy=False):
        # Ensure get right website
        if not website:
            website = self.get_current_website()

        # Default search
        category_search = [
            ('website_id', '=', website.id),
            ('website_published', '=', True),
        ]

        # By default only gets parent categories with child_ids
        if parent_hierarchy:
            category_search += [
                ('parent_id', '=', False),
                ('child_id', '!=', False),
            ]

        # Add custom domain
        if category_domain:
            category_domain = eval(category_domain)
            if '|' in category_domain[0]:
                category_domain.remove("|")
                category_search = expression.OR([category_search, category_domain])
            elif '&' in category_domain[0]:
                category_domain.remove("&")
                category_search = expression.AND([category_search, category_domain])
            else:
                category_search = expression.AND([category_search, category_domain])

        # Categories to show
        categories = self.env['product.public.category'].search(category_search)

        # Use only parents categories for category domain
        if category_domain and category_domain_only_child:
            category_child_ids = []
            for category in categories:
                categories_child = self.env['product.public.category'].search([
                    ('parent_id', '=', category.id)
                ])
                for category_child in categories_child:
                    category_child_ids.append(category_child.id)
            if category_child_ids:
                categories = self.env['product.public.category'].browse(
                    category_child_ids
                )

        # Product categories to show under their category
        product_ids = []
        category_ids = []
        products = None
        if product_hierarchy:
            for category in categories:
                cat_products = self.env['product.template'].search([
                    ('public_categ_ids', 'in', category.id)
                ])
                # If not parent_hierarchy avoid categories without products
                if not parent_hierarchy and not cat_products:
                    category_ids.append(category.id)
                for cat_product in cat_products:
                    product_ids.append(cat_product.id)
            if category_ids:
                categories = categories.filtered(
                    lambda x: x.id not in category_ids)
            products = self.env['product.template'].browse(product_ids)
        return (categories, products)
