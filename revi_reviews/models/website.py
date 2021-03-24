from odoo import fields, models, _


class Website(models.Model):
    _inherit = 'website'

    revi_api_key = fields.Char(string="Revi API key")
    revi_def_state = fields.Selection([
        ('skip', "Don't send"),
        ('open', "Open invoice")], string="When send data", default='skip',
        help='Establish when send data to Revi or no send data at all')
    revi_auto_send = fields.Boolean("Automatic sending of invitation emails")
    revi_url = fields.Selection([
        ('https://test.revi.io', "Test"),
        ('https://revi.io', "Production")], string="Environment",
        default='https://test.revi.io',
        help='Establish the environment url for send data to Revi. '
             'Just use TEST for testing because this send data only to Revi '
             'Panel Test: https://test.revi.io')
