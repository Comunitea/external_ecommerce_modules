# -*- coding: utf-8 -*-

import string
import logging

from random import SystemRandom

from odoo import http
from odoo.tests.common import HttpCase


class RedirectionCase(HttpCase):
    """
    Test slug redirection for products and categories
    """
    def random_string(self):
        """
        Create random string
        """
        return ''.join(SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))

    @classmethod
    def setUpClass(self):
        super(RedirectionCase, self).setUpClass()
        self.product = self.env['product.template'].create(
            {'name': self.random_string(), 'slug': self.random_string()})
        self.category = self.env['product.public.category'].create(
            {'name': self.random_string(), 'slug': self.random_string()})

    def test_product_redirection_with_slug(self):
        """
        Test product redirection with slug
        """

        http.local_redirect("/product/" + self.slug)
        self.assertEqual(http.status, 200, 'Response is not Status 200 but %s' % http.status)

    def test_category_redirection_with_slug(self):
        """
            Test category redirection with slug
        """
        http.local_redirect("/category/" + self.category_slug)
        self.assertEqual(http.status, 200, 'Response is not Status 200 but %s' % http.status)
