from odoo import fields, models, _


class Website(models.Model):
    _inherit = 'website'

    revi_api_key = fields.Char(string=_("Revi API key"))
    revi_def_state = fields.Selection([
        ('skip', _("Don't send")),
        ('open', _("Open invoice"))], string=_("When send data"), default='skip',
        help='Establish when send data to Revi or no send data at all')
    # revi_send_back = fields.Boolean(string=_("Use back-end"))
    revi_auto_send = fields.Boolean(string=_("Automatic sending of invitation emails"), default=False)
    revi_url = fields.Selection([
        ('https://test.revi.io', _("Test")),
        ('https://revi.io', _("Production"))], string=_("Environment"),
        default='https://test.revi.io',
        help='Establish the environment url for send data to Revi. '
             'Just use TEST for testing because this send data only to Revi Panel Test: https://test.revi.io')
