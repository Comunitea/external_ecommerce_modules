# -*- coding: utf-8 -*-

from odoo import api, models, fields, tools, _


class BlogPost(models.Model):
    _inherit = 'blog.post'

    image = fields.Binary(attachment=True, string=_("Post main image"), help=_("This is image of post preview"))
    introduction = fields.Text(string=_("Short post description"))
