# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta


class ProductWarranty(models.Model):
    _inherit = 'product.template'
    _description = ' Product '
    date_from = fields.Date("Date from")
    date_to = fields.Date("Date to")
    product_warranty = fields.Char("PW CODE", compute='check_code')
    check_valid_date = fields.Boolean(string='Check Valid' ,compute='check_date')
    total = fields.Float("discount total", compute='check_total')
    discount = fields.Char('Discount', default="")

    @api.constrains('date_release')
    def _check_release_date(self):
        for record in self:
            if record.date_from and record.date_from > fields.Date.today():
                raise models.ValidationError('date from must be in the past or now')
            elif record.date_from < record.date_to:
                raise models.ValidationError('ERrOr')

    @api.depends('date_from', 'date_to')
    def check_code(self):
        for record in self:
            date_from_str = str(record.date_from)
            date_to_str = str(record.date_to)
            code_from = date_from_str.replace('-', '')
            code_to = date_to_str.replace('-', '')
            record.product_warranty = "PWR/" + code_from + "/" + code_to

    @api.depends('product_warranty')
    def check_date(self):
        for record in self:
            if record.product_warranty != "PWR/False/False":
                record.check_valid_date = True
            else:
                record.check_valid_date = False

    @api.depends('total')
    def check_total(self):
        for rec in self:
            if not rec.date_to:
                rec.discount = "10%"
                rec.total += (rec.list_price - rec.standard_price) * 10 / 100 + (rec.list_price - rec.standard_price)
            else:
                rec.discount = ""
                rec.total += rec.list_price - rec.standard_price

    def action_confirm(self):
        for rec in self:
            rec.date_from = fields.Date.today()
            rec.date_to = fields.Date.today() + timedelta(days=365)


class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'
