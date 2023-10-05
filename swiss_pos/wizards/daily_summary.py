from odoo import models, fields, _, api, Command
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
from datetime import datetime, date
class dailySummary(models.TransientModel):
    _name = 'store.daily.summary'

    date = fields.Date('Date', default=date.today())
    session_ids = fields.Many2many('pos.session', string='PoS Sessions')
    payment_ids = fields.Many2many('account.payment', string='Sales Payments')
    warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse')


    @api.onchange('date', 'warehouse_id')
    def date_change(self):
        if not all([self.date, self.warehouse_id]):
            return
        sessions = self.env['pos.session'].search([
            ('stop_at', '>', self.date.strftime(DF) + ' 00:00:00'),
            ('stop_at', '<', self.date.strftime(DF) + ' 23:59:59')
        ])
        self.session_ids = sessions.filtered(lambda s:\
            s.config_id.picking_type_id.warehouse_id == self.warehouse_id)

        valid_payments = self.env['account.payment']
        for payment in self.env['account.payment'].search([('date', '=', self.date)]):
            for invoice in payment.reconciled_invoice_ids:
                warehouse = invoice.mapped('line_ids.sale_line_ids.order_id.warehouse_id')
                if self.warehouse_id.id in warehouse.ids:
                    valid_payments |= payment
        self.payment_ids = valid_payments


    def print_report(self):
        self.ensure_one()
        data = {
            'form': {
                'session_ids': self.session_ids.ids,
                'payment_ids': self.payment_ids.ids,
                'date': self.date.strftime(DF),
                'warehouse_id': self.warehouse_id.id
            }
        }
        return self.env.ref('swiss_pos.action_report_dailysummary').report_action(None, data=data)
