# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime


class account_settings(models.TransientModel):
    _inherit = 'res.config.settings'

    #allowed_discount_account = fields.Many2one('account.account')
    #allowed_discount_product = fields.Many2one('product.product')

    # My custom fields
    my_custom_field11_id = fields.Many2one('account.account', config_parameter='base.my_custom_field11_id')
    my_custom_field12_id = fields.Many2one('product.product', config_parameter='base.my_custom_field12_id',  domain="[('type','=','service')]")

