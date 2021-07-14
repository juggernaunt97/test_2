from odoo import api, fields, models, tools
from odoo.exceptions import UserError, ValidationError


class BatchUpdate(models.TransientModel):
    _name = "product.batch.update.wizard"
    _description = "update product"
    date_from = fields.Date("From")
    date_to = fields.Date("To")

    def multi_update(self):
        ids = self.env.context['active_ids']
        products = self.env["product.template"].browse(ids)
        new_date = {}

        if self.date_to:
            new_date["date_to"] = self.date_to
        if self.date_from:
            new_date["date_from"] = self.date_from

        products.write(new_data)
