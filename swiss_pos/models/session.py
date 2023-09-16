from odoo import models, api, fields, _

class posSession(models.Model):
    _inherit = 'pos.session'

    receipt_header = fields.Text(related='config_id.receipt_header')


    def _get_line_report_cashier(self):
        self.ensure_one()

        lines = []
        payments = {}
        for payment in self.env['pos.payment'].search([('session_id', '=', self.id)]):
            if payment.payment_method_id.id in payments:
                payments[payment.payment_method_id.id]['amount'] += payment.amount
            else:
                payments[payment.payment_method_id.id] = {
                    'name': payment.payment_method_id.display_name,
                    'amount': payment.amount,
                    'is_cash': payment.payment_method_id.journal_id.type == 'cash'
                }
        _sequence = 0
        for p in payments:
            _sequence +=1
            _line = {
                'sequence': _sequence,
                'name': payments[p]['name'],
                'deposit': payments[p]['amount'],
                'transaction': payments[p]['amount'],
                'diff': 0.0,
            }
            if payments[p]['is_cash']:
                _line['deposit'] = self.cash_register_balance_end_real - self.cash_register_balance_start
                _line['diff'] = _line['deposit'] - _line['transaction']
            
            lines.append(_line)
        return lines

    def print_report_cashier(self):
        self.ensure_one()   
        return self.env.ref('swiss_pos.action_report_cashier_document')\
            .report_action(self.ids)

            

        