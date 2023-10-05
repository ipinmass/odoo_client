from odoo import models, fields, _, api, Command
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
from datetime import datetime, date
class dailySummary(models.TransientModel):
    _name = 'store.daily.summary'

    date = fields.Date('Date', default=date.today())
    session_ids = fields.Many2many('pos.session', string='PoS Sessions')
    payment_ids = fields.Many2many('account.payment', string='Sales Payments')


    @api.onchange('date')
    def date_change(self):
        if not self.date:
            return
        sessions = self.env['pos.session'].search([
            ('stop_at', '>', self.date.strftime(DF) + ' 00:00:00'),
            ('stop_at', '<', self.date.strftime(DF) + ' 23:59:59')
        ])
        self.payment_ids = self.env['account.payment'].search([('date', '=', self.date)])
        self.session_ids = sessions

    
    def print_report(self):
        self.ensure_one()
        data = {
            'session_ids': self.session_ids.ids,
            'payment_ids': self.payment_ids.ids

        }
        return self.env.ref('swiss_pos.action_report_dailysummary').report_action(None, data=data)
