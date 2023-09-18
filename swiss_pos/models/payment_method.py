from odoo import models, fields, api, _

class posPaymentMethod(models.Model):
    _inherit = 'pos.payment.method'

    require_card_no = fields.Boolean(_('Require Card Number'))

class posPayment(models.Model):
    _inherit = 'pos.payment'

    card_number = fields.Char(_('Card Number'))
