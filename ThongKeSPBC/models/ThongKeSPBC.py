#
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api

class ThongkeSPBC(models.Model):
    _name = 'thongkespbc'
    _description = ''

    name = fields.Char(string='Name')
    month = fields.Selection([('01', 'Tháng 1'), ('02', 'Tháng 2'), ('03', 'Tháng 3'), ('04', 'Tháng 4'), ('05', 'Tháng 5'),
                              ('06', 'Tháng 6'), ('07', 'Tháng 7'), ('08', 'Tháng 8'), ('09', 'Tháng 9'), ('10', 'Tháng 10'),
                              ('11', 'Tháng 11'), ('12', 'Tháng 12')], string='Tháng', required=True)
    year = fields.Integer('Năm', required=True)

    # name = fields.Char(string='Month', required=True)
    product_id = fields.Many2one('sanpham', string='Sản phẩm', required=True)
    quantity = fields.Float(string='Số lượng sản phẩm đã bán')



    @api.model
    def update_product_stat(self):
        # Sau mỗi lần bán hàng, gọi phương thức này để cập nhật thống kê sản phẩm
        all_products = self.env['sanpham'].search([])
        for product in all_products:
            month = fields.Datetime.now().strftime('%B %Y')
            quantity_sold = self.env['ctdonhang'].search_count([('product_item_id', '=', product.id)])
            product_stat = self.search([('name', '=', month), ('product_item_id', '=', product.id)])
            if product_stat:
                product_stat.write({'quantity': quantity_sold})
            else:
                self.create({'name': month, 'product_item_id': product.id, 'quantity': quantity_sold})