from odoo import models, fields, api, _


class posConfig(models.Model):
    _inherit = 'pos.config'
    receipt_logo = fields.Binary('Receipt Logo')


class resConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    pos_receipt_logo = fields.Binary('Receipt Logo', related='pos_config_id.receipt_logo')