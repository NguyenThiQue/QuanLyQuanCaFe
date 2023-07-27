#
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api

class ThongkeSLDH(models.Model):
    _name = 'thongkesldh'
    _description = ''

    name = fields.Char(string='Name')
    month = fields.Selection([('01', 'Tháng 1'), ('02', 'Tháng 2'), ('03', 'Tháng 3'), ('04', 'Tháng 4'), ('05', 'Tháng 5'),
                              ('06', 'Tháng 6'), ('07', 'Tháng 7'), ('08', 'Tháng 8'), ('09', 'Tháng 9'), ('10', 'Tháng 10'),
                              ('11', 'Tháng 11'), ('12', 'Tháng 12')], string='Tháng', required=True)
    year = fields.Integer('Năm', required=True)
    sldh = fields.Integer(string='Số lượng đơn hàng')

    @api.model
    def create(self, values):
        result = super(ThongkeSLDH, self).create(values)
        result.sldh = self.compute_sale_order(result.month, result.year)
        return result

    @api.model
    def compute_sale_order(self, month, year):
        # orders = self.env['donhang'].search(
        #     [('ngaytaodh', '>=', f'{year}-{month}-01'), ('ngaytaodh', '<=', f'{year}-{month}-31')])
        orders = self.env['donhang'].search(
            [('state', '=', 'done'),('ngaytaodh', '>=', f'{year}-{month}-01'), ('ngaytaodh', '<=', f'{year}-{month}-30')])

        sldh = len(
            orders
        )

        return sldh