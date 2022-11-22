# © 2019 Comunitea - Pavel Smirnov <pavel@comunitea.com> & Ruben Seijas <ruben@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import logging
import requests
from odoo import api, fields, models
from odoo.http import request

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.multi
    def revi_product_rating(self):
        website = request.env['website'].get_current_website()
        avg_rating = 0
        if website and website.revi_api_key:
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'X-API-KEY': website.revi_api_key
            }

            # Set API URL with product id
            revi_product_info = 'https://revi.io/api/v1/product_info?id_product=%d' % self.id

            # Post call to Revi
            hello_call = requests.get(revi_product_info, headers=headers)

            rating = {}
            if hello_call.status_code and hello_call.status_code in [200, 201]:
                try:
                    response = hello_call.json().get('data')
                except Exception as e:
                    _logger.error('Unable to decode json data: {}'.format(hello_call.content))
                    response = False
                if response:
                    avg_rating = response['product']['avg_rating'][:3]
                    num_ratings = int(response['product']['num_ratings'])
                    if num_ratings < 1:
                        avg_rating = 0
                        plural = False
                    else:
                        plural = False if num_ratings in [1, 11, 21, 31, 41, 51, 61, 71, 81, 91] else True

                    rating = {'avg': avg_rating, 'num': num_ratings, 'plural': plural}

            return rating
