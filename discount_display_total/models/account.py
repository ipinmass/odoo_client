from odoo import models, fields, api


class accountMove(models.Model):
    _inherit = 'account.move'

    total_discount = fields.Monetary('Total Discount', compute='get_total_discount_line', store=True)

    @api.depends('line_ids', 'line_ids.discount', 'line_ids.quantity')
    def get_total_discount_line(self):
        for rec in self:
            rec.total_discount = sum([l.quantity*l.price_unit*l.discount/100 \
                for l in rec.line_ids\
                    .filtered(lambda l: l.display_type == 'product')])
    
