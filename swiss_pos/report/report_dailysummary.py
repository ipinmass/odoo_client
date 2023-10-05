import logging
from datetime import timedelta
from functools import partial
from itertools import groupby
from collections import defaultdict

import psycopg2
import pytz
import re

from odoo import api, fields, models, tools, _
from odoo.tools import float_is_zero, float_round, float_repr, float_compare
from odoo.exceptions import ValidationError, UserError
from odoo.osv.expression import AND
import base64

_logger = logging.getLogger(__name__)
import traceback


class ReportSaleDetails(models.AbstractModel):

    _name = 'report.swiss_pos.report_dailysummary'
    _description = 'Report Daily Summary'


    @api.model
    def get_sale_details(self, data):
        session_ids = self.env['pos.session'].browse(data.get('form',{}).get('session_ids'))
        payment_ids = self.env['account.payment'].browse(data.get('form', {}).get('payment_ids'))

        receipt_header = session_ids.mapped('config_id.receipt_header')
        receipt_header = receipt_header and receipt_header[0] or 'None'
        paymentlines = {}
        for session in session_ids:
            for pospayment in self.env['pos.payment'].search([('session_id', '=', session.id)]):
                if pospayment.payment_method_id.journal_id.name in paymentlines:
                    paymentlines[pospayment.payment_method_id.journal_id.name][0] += pospayment.amount
                else:
                    paymentlines[pospayment.payment_method_id.journal_id.name] = [pospayment.amount, 0.0]
        for salepayment in payment_ids:
            if salepayment.journal_id.name in paymentlines:
                paymentlines[salepayment.journal_id.name][1] += salepayment.amount
            else:
                paymentlines[salepayment.journal_id.name] = [0.0, salepayment.amount]
        return {
            'report_header': receipt_header,
            'date': data.get('form', {}).get('date'),
            'store': self.env['stock.warehouse'].browse(data.get('form', {}).get('warehouse_id')).display_name,
            'paymentlines': paymentlines
        }

    @api.model
    def _get_report_values(self, docids, data=None):
        data = dict(data or {})

        data.update(self.get_sale_details(data))
        return data
