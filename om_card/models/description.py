from odoo import fields, models


class Description(models.Model):
    _name = "card.description"

    name = fields.Char(string="DESCRIPTION", required=True)
