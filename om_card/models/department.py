from odoo import fields, models, api


class Department(models.Model):
    _name = "card.department"

    name = fields.Char(string="DEPARTMENT", required=True)
    info = fields.One2many('card.info', 'department', string='INFO')
    manager = fields.Many2one('card.info', domain="[('department.name', '=', name)]")


