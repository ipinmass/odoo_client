from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    nota_no = fields.Char('Nota No.')
    order_type = fields.Selection([
        ('shop', _('Shop')),
        ('special', _('Special Order'))
    ], string='Order Type')
    delivery_type = fields.Selection([
        ('self', _('Self-collected')),
        ('delivered', _('Delivered'))
    ], string='Delivery')
    description = fields.Text(_('Description'))
