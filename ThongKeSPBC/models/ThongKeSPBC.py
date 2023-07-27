#

from odoo import models, fields, api
from datetime import date, datetime


class ThongkeSPBC(models.Model):
    _name = 'thongkespbc'
    _description = ''

    name = fields.Char(string="Top")
    top_products = fields.Text(string='Sản phẩm bán chạy ', compute='_compute_top_products')
    start_date = fields.Date(string='Ngày bắt đầu')

    end_date = fields.Date(string='Ngày kết thúc')

    @api.depends('start_date', 'end_date')
    def _compute_top_products(self):
        for record in self:


            # Xác định ngày bắt đầu (đầu tháng) và ngày kết thúc (hiện tại) hoặc theo giá trị start_date và end_date)
            today = date.today()
            start_date = record.start_date or date(today.year, today.month, 1)
            end_date = record.end_date or today

            # Tìm các đơn đặt hàng đã xác nhận trong tháng hiện tại
            confirmed_orders = self.env['donhang'].search(
                [('state', '=', 'done'), ('ngaytaodh', '>=', start_date), ('ngaytaodh', '<=', end_date)])

            # Tạo danh sách sản phẩm và số lượng đã bán của từng sản phẩm
            products_sold = {}
            for order in confirmed_orders:
                for line in order.ct_donhang:
                    product = line.product_item_id
                    if product in products_sold:
                        products_sold[product.id]['quantity'] += line.quantity
                    else:
                        products_sold[product.id] = {
                            'name': product.name,
                            'quantity': line.quantity,
                            'image': product.img_sp
                        }


            # Sắp xếp danh sách theo số lượng đã bán và lấy ra top 1 sản phẩm
            top_selling_products = sorted(products_sold.values(), key=lambda x: x['quantity'], reverse=True)[:1]

            # # Ghi kết quả vào trường top_products
            record.top_products = '\n'.join(
                [f"{product['name']} \nĐã bán: {product['quantity']}" for product in top_selling_products])

