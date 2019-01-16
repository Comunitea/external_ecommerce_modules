# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website


class FaviconRoot(Website):

    @http.route('/favicon.ico', type='http', auth="none", website=True)
    def favicon_redirect(self):
        current_website = request.website.sudo()
        filename = '/web/image/website/%d/favicon/' % current_website.id
        return request.env['ir.http'].reroute(filename)
