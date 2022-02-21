from odoo import models


class InfoCardXls(models.AbstractModel):
    _name = 'report.om_card.report_info_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet("Info Card")

        sheet.write(0, 0, 'FIRST NAME')
        sheet.write(1, 0, lines.first_name)

        sheet.write(0, 1, 'LAST NAME')
        sheet.write(1, 1, lines.last_name)

        sheet.write(0, 2, 'AGE')
        sheet.write(1, 2, lines.age)

        sheet.write(0, 3, 'CITIZENSHIP')
        sheet.write(1, 3, lines.citizenship)

        sheet.write(0, 4, 'GEN')
        sheet.write(1, 4, lines.gender)

        sheet.write(0, 5, 'SIGNATURE')
        sheet.write(1, 5, lines.signature)

        sheet.write(0, 6, 'ISSUING AUTHORITY')
        sheet.write(1, 6, lines.issuing_authority)

        sheet.write(0, 7, 'DATE OF BIRTH')
        sheet.write(1, 7, lines.date_of_birth)

        sheet.write(0, 8, 'DATE OF EXPIRY')
        sheet.write(1, 8, lines.date_of_expiry)

        sheet.write(0, 9, 'PERSONAL No')
        sheet.write(1, 9, lines.personal_no)

        sheet.write(0, 10, 'PLACE OF BIRTH')
        sheet.write(1, 10, lines.place_of_birth)

        sheet.write(0, 11, 'DATE OF ISSUE')
        sheet.write(1, 11, lines.date_of_issue)

        sheet.write(0, 12, 'CARD No')
        sheet.write(1, 12, lines.card_no)

        sheet.write(0, 13, 'DEPARTMENT')
        sheet.write(1, 13, lines.department.name)

        sheet.write(0, 14, 'DESCRIPTION')
        desc = ", ".join([each.name for each in lines.description])
        sheet.write(1, 14, desc)








        # arr = [
        #     'first_name', 'last_name', 'age', 'citizenship', 'gen', 'signature', 'issuing_authority',
        #     'date_of_birth', 'date_of_expiry', 'personal_no', 'place_of_birth', 'date_of_issue',
        #     'card_no', 'department', 'description'
        # ]

        # sheet.write(0, 0, 'FIRST NAME')
        #
        # sheet.write(0, 1, 'LAST NAME')
        #
        # sheet.write(0, 2, 'AGE')
        # x = 0
        # y = 0
        # for _ in range(len(arr)):
        #     sheet.write(0, x, arr[y])
        #     sheet.write(1, x, ", ".join([each.name for each in lines.description]))
        #     x += 1
        #     y += 1