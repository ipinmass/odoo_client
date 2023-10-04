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
    def get_sale_details(self):


        return {
            'test': 123,
            'report_header': '',
            'date': '',
            'store': '',
            'paymentlines': [{
            }]
        }

    @api.model
    def _get_report_values(self, docids, data=None):
        data = dict(data or {})

        data.update(self.get_sale_details())
        return data
