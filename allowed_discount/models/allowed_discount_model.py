# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime


class allowed_discount_model(models.Model):
    _inherit = 'res.partner'

    allowed_discount = fields.Float("Allowed discount",mandatory=False)














