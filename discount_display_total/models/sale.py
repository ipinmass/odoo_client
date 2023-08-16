from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_discount = fields.Monetary('Total Discount', compute='get_total_discount_line', store=True)

    @api.depends('order_line', 'order_line.discount')
    def get_total_discount_line(self):
        for rec in self:
            rec.total_discount = sum([l.product_uom_qty*l.price_unit*l.discount/100 for l in rec.order_line])
    

            

