# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime


class sale_order_dimension(models.Model):
    _inherit = 'sale.order.line'

    account = fields.Many2one('account.account')
    product_id = fields.Many2one('product.product')
    testest = fields.Float(compute='_check_discount')
    product_uom_qty = fields.Float()
    price_unit = fields.Float()


    def _prepare_invoice_line(self,**optional_values):
        res = super(sale_order_dimension, self)._prepare_invoice_line(**optional_values)
        res.update({'account_id': self.account})
        return res

    @api.onchange('order_id.partner_id')
    def _check_discount(self):
        if self.order_id.partner_id.allowed_discount > 0:
            self.testest = self.order_id.partner_id.allowed_discount
            self.product_uom_qty = 1
            self.price_unit = self.testest * -1
            self.account = self.env['ir.config_parameter'].get_param('base.my_custom_field11_id')

            #self.product_id = self.env['ir.config_parameter'].get_param('base.my_custom_field12_id')
        else:
            self.testest = 0

    def create_line(self):
        self.ensure_one()
        vals = {}
        SaleOrderLine = self.env['sale.order.line']
        self.testest = self.order_id.partner_id.allowed_discount
        if self.order_id.partner_id.allowed_discount > 0:
            vals = {
                'sequence': 10000,
                'product_id': self.company_id.sales_discount_product,
                'product_uom': self.company_id.sales_discount_product.uom_id,
                'product_uom_qty': 1,
                'price_unit': self.amount_discount * -1,
                'name': self.company_id.sales_discount_product.name,
                'order_id': self.id,
                'tax_id': [(6, 0, self.company_id.sales_discount_product.taxes_id.ids)],
            }
        sol = SaleOrderLine.sudo().create(vals)
        return sol

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def custom_function(self):
        if self.partner_id.allowed_discount > 0:
            accountcon = self.env['ir.config_parameter'].sudo().get_param('base.my_custom_field11_id')
            product_idcon = self.env['ir.config_parameter'].sudo().get_param('base.my_custom_field12_id')
            order_lines = []
            val =  (0, 0, {
                'sequence': 10000,
                'product_id': int(product_idcon),
                'account': int(accountcon),
                'product_uom_qty': 1,
                'price_unit': self.partner_id.allowed_discount * -1,
            })
            order_lines.append(val)
            self.update({'order_line': order_lines})

















