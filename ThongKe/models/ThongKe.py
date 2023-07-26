#
from odoo import models, fields, api

class Thongke(models.Model):
    _name = 'thongke'
    _description = ''
    name = fields.Char(string='Name')

    month = fields.Selection([('01', 'Tháng 1'), ('02', 'Tháng 2'), ('03', 'Tháng 3'), ('04', 'Tháng 4'), ('05', 'Tháng 5'),
                              ('06', 'Tháng 6'), ('07', 'Tháng 7'), ('08', 'Tháng 8'), ('09', 'Tháng 9'), ('10', 'Tháng 10'),
                              ('11', 'Tháng 11'), ('12', 'Tháng 12')], string='Tháng', required=True)
    year = fields.Integer('Năm', required=True)
    revenue = fields.Float('Doanh thu')

    @api.model
    def create(self, values):
        result = super(Thongke, self).create(values)
        result.revenue = self.calculate_revenue(result.month, result.year)
        return result



    @api.model
    def calculate_revenue(self, month, year):
        # orders = self.env['donhang'].search(
        #     [('ngaytaodh', '>=', f'{year}-{month}-01'), ('ngaytaodh', '<=', f'{year}-{month}-31')])
        orders = self.env['donhang'].search(
            [('ngaytaodh', '>=', f'{year}-{month}-01'), ('ngaytaodh', '<=', f'{year}-{month}-30')])

        revenue = sum(order.tongdh for order in orders)

        return revenue



