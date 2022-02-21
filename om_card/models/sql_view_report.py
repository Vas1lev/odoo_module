# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class SqlViewReport(models.AbstractModel):
    _name = 'dep.view.report'
    _auto = False

    dep_name = fields.Char(string="DEPARTMENT")
    amount = fields.Integer(string="NUMBER OF STAFF")
    _rec_name = "dep_name"

    def _select(self):
        select = f"""
                SELECT row_number() OVER () AS id, card_department.name AS dep_name, COUNT(card_info.department) AS amount
                FROM card_department
                LEFT JOIN card_info ON card_department.id = card_info.department
                GROUP BY card_department.name
                """
        return select

    def init(self):
        tools.drop_view_if_exists(self._cr, 'dep_view_report')
        self._cr.execute(f"""
                        CREATE OR REPLACE VIEW dep_view_report AS (
                            {self._select()}
                        )""")
