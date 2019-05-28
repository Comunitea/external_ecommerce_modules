# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

from odoo.addons.website.controllers.main import Website


class FaviconRoot(Website):

    @http.route('/favicon.ico', type='http', auth="none", website=True)
    def favicon_redirect(self):
        """
        Redirect favicon url for current website
        """
        current_website = request.website.sudo()
        filename = '/web/image/website/%d/favicon/' % current_website.id
        return request.env['ir.http'].reroute(filename)
