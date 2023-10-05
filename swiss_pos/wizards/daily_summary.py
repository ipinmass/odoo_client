from odoo import models, fields, _, api

class dailySummary(models.TransientModel):
    _name = 'store.daily.summary'

    session_ids = fields.Many2many('pos.session', string='PoS Sessions')
    payment_ids = fields.Many2many('account.payment', string='Sales Payments')


    @api.model
    def default_get(self, fields_list):
        res = super(dailySummary, self).default_get(fields_list)
        
        return res

    def print_report(self):
        self.ensure_one()
        data = {'name': self._name}
        return self.env.ref('swiss_pos.action_report_dailysummary').report_action(None, data=data)
