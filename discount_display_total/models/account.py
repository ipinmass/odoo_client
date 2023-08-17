from odoo import models, fields, api


class accountMove(models.Model):
    _inherit = 'account.move'

    total_discount = fields.Monetary('Total Discount', compute='get_total_discount_line', store=True)
    undiscounted_total = fields.Monetary('Subtotal', compute='get_total_discount_line', store=True)

    @api.depends('line_ids', 'line_ids.discount', 'line_ids.quantity', 'tax_totals')
    def get_total_discount_line(self):
        for rec in self:
            rec.total_discount = sum([l.quantity*l.price_unit*l.discount/100 \
                for l in rec.line_ids\
                    .filtered(lambda l: l.display_type == 'product')])
            if rec.tax_totals:
                rec.undiscounted_total = rec.tax_totals.get('amount_untaxed', 0.0) + rec.total_discount
            else:
                rec.undiscounted_total = sum([l.quantity*l.price_unit for l in rec.line_ids\
                    .filtered(lambda ll: ll.display_type == 'product')])
    