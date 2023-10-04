from odoo import models, fields, _, api

class dailySummary(models.TransientModel):
    _name = 'store.daily.summary'

    session_ids = fields.Many2many()

    def print_report(self):
        self.ensure_one()
        data = {'name': self._name}
        return self.env.ref('swiss_pos.action_report_dailysummary').report_action(None, data=data)
