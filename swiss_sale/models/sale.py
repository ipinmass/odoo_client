from odoo import models, fields, api, _
from datetime import datetime
import logging
import pytz

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    nota_no = fields.Char('Nota No.')
    order_type = fields.Selection([
        ('shop', _('Shop')),
        ('special', _('Special Order'))
    ], string=_('Order Type'))
    delivery_type = fields.Selection([
        ('self', _('Self-collected')),
        ('delivered', _('Delivered'))
    ], string=_('Delivery Type'))
    description = fields.Text(_('Description'))


    def get_datetime_now(self):
        tz = pytz.timezone(self.env.user.tz or 'Asia/Jakarta')
        lang = self.env['res.lang'].sudo().search([('code', '=', self.env.user.lang)], limit=1)
        _time_format = ' '.join([lang.date_format, lang.time_format])
        return datetime.now(tz).strftime(_time_format)
