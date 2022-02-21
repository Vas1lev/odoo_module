import json
from odoo import http
from odoo.http import request
from odoo.http import Response
from collections import OrderedDict

# -*- coding: utf-8 -*-
class Card(http.Controller):
    @http.route("/controller/info", website=False, auth='public', type="http")
    def card_info(self, **kwargs):
        data = request.env['card.info'].sudo().search([])

        return Response(json.dumps(OrderedDict([
                                                ('data', [[
                                                    f'first_name: {i.first_name}',
                                                    f'last_name: {i.last_name}',
                                                    f'age: {i.age}',
                                                    f'citizenship: {i.citizenship}',
                                                    f'gender: {i.gender}',
                                                    f'signature: {i.signature}',
                                                    f'issuing_authority: {i.issuing_authority}',
                                                    f'date_of_birth: {i.date_of_birth}',
                                                    f'date_of_expiry: {i.date_of_expiry}',
                                                    f'personal_no: {i.personal_no}',
                                                    f'place_of_birth: {i.place_of_birth}',
                                                    f'date_of_issue: {i.date_of_issue}',
                                                    f'card_no: {i.card_no}',
                                                    f'department: {i.department.name}',
                                                    f'description: {", ".join([each.name for each in i.description])}'
                                                ] for i in data])]), ensure_ascii=False).encode('utf-8'), mimetype='application/json')
