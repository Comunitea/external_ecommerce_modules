# Copyright 2020 Odoo
# Copyright 2020 Tecnativa - Alexandre Díaz
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api, fields, models


class Menu(models.Model):
    _inherit = "website.menu"

    def _compute_field_is_mega_menu(self):
        for menu in self:
            menu.is_mega_menu = bool(menu.mega_menu_content)

    def _set_field_is_mega_menu(self):
        for menu in self:
            if menu.is_mega_menu:
                if menu.mega_menu_module_name and menu.mega_menu_template_name:
                    mega_menu_template = menu.mega_menu_module_name + '.' \
                               + menu.mega_menu_template_name
                    default_content = self.env["ir.ui.view"].render_template(
                        mega_menu_template,
                        {'menu': menu, 'website': menu.website_id}
                    )
                    menu.mega_menu_content = default_content.decode()
                elif menu.mega_menu_hierarchy \
                        or menu.mega_menu_product_categories \
                        or menu.mega_menu_category_domain \
                        or menu.mega_menu_category_domain_only_child:
                    default_content = self.env["ir.ui.view"].render_template(
                        "website_megamenu_extend.mega_menu_category_products",
                        {'menu': menu, 'website': menu.website_id}
                    )
                    menu.mega_menu_content = default_content.decode()
                if not menu.mega_menu_content:
                    default_content = self.env["ir.ui.view"].render_template(
                        "website_megamenu.s_mega_menu_multi_menus"
                    )
                    menu.mega_menu_content = default_content.decode()
            else:
                menu.mega_menu_content = False
                menu.mega_menu_classes = False

    is_mega_menu = fields.Boolean(
        compute=_compute_field_is_mega_menu, inverse=_set_field_is_mega_menu
    )

    # To compose xmlid of custom mega menu template
    mega_menu_module_name = fields.Char(string="Module Name")
    mega_menu_template_name = fields.Char(string="Template Name")

    # To render mega menus templates
    mega_menu_hierarchy = fields.Boolean(string="Only categories with child")
    mega_menu_product_categories = fields.Boolean(
        string="Show product categories"
    )
    mega_menu_category_domain = fields.Text(string="Category domain")
    mega_menu_category_domain_only_child = fields.Boolean(
        string="Only domain parent categories"
    )
