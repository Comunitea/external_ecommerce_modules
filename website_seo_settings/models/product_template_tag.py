# © 2020 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.addons.http_routing.models.ir_http import slug


class ProductTemplateTag(models.Model):

    _inherit = 'product.template.tag'

    slug = fields.Char(
        string="Friendly URL", compute='_compute_tag_slug')
    website_meta_title = fields.Char(string=_("Meta Title"), translate=True)
    website_meta_description = fields.Text(string=_("Meta Description"), translate=True)
    website_meta_keywords = fields.Char(string=_("Meta Keywords"), translate=True)
    website_published = fields.Boolean(string=_('Website Published'), default=True,
                                       help=_("Only published tags are visible on the website"))
    sequence = fields.Integer('Sequence', default=9999)

    @api.multi
    def _compute_tag_slug(self):
        for tag in self:
            tag.slug = slug(tag)