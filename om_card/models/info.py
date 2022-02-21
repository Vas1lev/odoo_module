from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Info(models.Model):
    _name = "card.info"

    first_name = fields.Char(string="FIRST NAME", required=True)
    last_name = fields.Char("LAST NAME", required=True)
    age = fields.Integer("AGE")
    citizenship = fields.Char(string="CITIZENSHIP")
    gender = fields.Selection([
        ('M', 'M'),
        ('FM', 'FM')
    ], string='GEN')
    signature = fields.Text("SIGNATURE")
    issuing_authority = fields.Text("ISSUING AUTHORITY")
    date_of_birth = fields.Date(string="DATE OF BIRTH")
    date_of_expiry = fields.Date(string="DATE OF EXPIRY")

    personal_no = fields.Char("PERSONAL No", size=11, required=True)

    @api.constrains('personal_no')
    def _check_personal_no(self):
        for val in self:
            if not val.personal_no.isdigit():
                raise ValidationError("Enter only numeric values")
            if len(val.personal_no) != 11:
                raise ValidationError("Length of personal number must be 11")

    place_of_birth = fields.Char("PLACE OF BIRTH")
    date_of_issue = fields.Datetime("DATE OF ISSUE")

    card_no = fields.Char("CARD No", size=9, required=True)
    image = fields.Binary(string="IMAGE")

    department = fields.Many2one('card.department', string='DEPARTMENT', ondelete="set null")
    description = fields.Many2many('card.description', string='DESCRIPTION')

    _rec_name = 'combination'
    combination = fields.Char(string='Combination', compute='_compute_fields_combination')

    @api.depends('last_name', 'first_name')
    def _compute_fields_combination(self):
        for test in self:
            test.combination = test.last_name + ', ' + test.first_name




