from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.http import request


class CTDonHang(models.Model):
    _name = 'ctdonhang'

    _table = "CTDonHang"
    _description = ''
    # id_ctdonhang = fields.Char(string="Mã chi tiết đơn hàng")

    gia = fields.Float(compute='_compute_price',string="Giá")
    quantity = fields.Integer(string="Số lượng")
    tonggiasp = fields.Float(compute = '_compute_price_total',string="Tổng giá cho sản phẩm")



    product_item_id = fields.Many2one("sanpham", string="Sản phẩm")

    kho_idd = fields.Many2one("kho", string="Kho")

    phieunhapkho_id = fields.Many2one("phieunhapkho", string="Phiếu nhập kho")

    id_nhanvien  = fields.Many2one("nhanvien", string="Nhân viên")

    # def create_donhang_from_giohang(self):
    #     # gio_hang = self.env['ctdonhang'].sudo().search([('id_nhanvien', '=', self.env.user.id_nhanvien.id)])
    #     gio_hang = self.env['ctdonhang'].sudo().search([])
    #     if not gio_hang:
    #         return False
    #
    #     donhang_model = self.env['donhang']
    #     donhang = donhang_model.sudo().create({
    #         # 'id_nv': self.env.user.id_nhanvien.id,
    #         'id_khachhang': False,  # Gán id_khachhang là False hoặc bạn có thể nhập thông tin khách hàng mong muốn
    #         'ngaytaodh': fields.Date.today(),
    #     })
    #
    #     for item in gio_hang:
    #         donhang.ct_donhang = [(0, 0, {
    #             'donhang_id': donhang.id,
    #             'product_item_id': item.product_item_id.id,
    #             'quantity': item.quantity,
    #         })]
    #
    #
    #     donhang.tongdh = sum(item.tonggiasp for item in gio_hang)
    #
    #     gio_hang.unlink()
    #
    #     return True

    # @classmethod
    # def create_order_from_cart(cls, cart_data):
    #     try:
    #         # Tạo đơn hàng mới
    #         order = request.env['donhang'].create({})
    #
    #         # Lấy danh sách sản phẩm và số lượng từ giỏ hàng
    #         products = cart_data.get('products', [])
    #
    #         # Tạo các sản phẩm trong đơn hàng
    #         for product_data in products:
    #             product_item_id = product_data.get('product_item_id')
    #             quantity = product_data.get('quantity')
    #
    #             # Kiểm tra nếu sản phẩm tồn tại
    #             product = request.env['ctdonhang'].browse(int(product_item_id))
    #             if product:
    #                 product.create({
    #                     'name': product.name,
    #                     'quantity': int(quantity),
    #                     'donhang_id': order.id,
    #                 })
    #
    #         return {'success': True, 'order_id': order.id}
    #     except ValidationError as e:
    #         return {'error': str(e)}
    #     except Exception as ex:
    #         return {'error': str(ex)}

    @api.depends('product_item_id')
    def _compute_price(self):
        for record in self:
            price_item = record.product_item_id.price
            record.gia = price_item

    @api.depends('quantity', 'gia')
    def _compute_price_total(self):
        for record in self:
            record.tonggiasp = record.gia * record.quantity



    #-----------------------------------------











class SanPham(models.Model):
    _inherit = "sanpham"
    idctdh = fields.One2many("ctdonhang", "product_item_id", string= "Chi tiết đơn hàng")

class PhieuNhapKho(models.Model):
    _inherit = "phieunhapkho"
    ctdh = fields.One2many("ctdonhang","phieunhapkho_id", string="Chi tiết đơn hàng")




