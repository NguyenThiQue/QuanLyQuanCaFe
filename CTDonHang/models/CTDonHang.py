from odoo import models, fields, api

class CTDonHang(models.Model):
    _name = 'ctdonhang'

    _table = "CTDonHang"
    _description = ''
    id_ctdonhang = fields.Char(string="Mã chi tiết đơn hàng")
    # id_donhang = fields.Char(string = "Mã đơn hàng")
    # id_masp = fields.Char(string="Mã sản phẩm")
    gia = fields.Float(compute='_compute_price',string="Giá")
    quantity = fields.Integer(string="Số lượng")
    tonggiasp = fields.Float(compute = '_compute_price_total',string="Tổng giá cho sản phẩm")


    # product_list = fields.Many2many("sanpham", "product_order_detail_re", "id_ctdonhang", "id_sp", string="Sản Phẩm")

    product_item_id = fields.Many2one("sanpham", string="Sản phẩm")
    # hoadon_id = fields.Many2one("donhang", String = "Hoá đơn")
    kho_id = fields.Many2one("kho", string="Kho", related="product_item_id.kho_id")

    @api.depends('product_item_id')
    def _compute_price(self):
        for record in self:
            price_item = record.product_item_id.price
            record.gia = price_item

    @api.depends('quantity', 'gia')
    def _compute_price_total(self):
        for record in self:
            record.tonggiasp = record.gia * record.quantity

    @api.onchange('quantity')
    def onchange_quantity(self):
        # Lấy số lượng sản phẩm
        product_quantity = self.quantity

        # Lấy số lượng sản phẩm trong kho
        product_in_stock = self.kho_id.soluong
        print("sl", product_in_stock)

        # Kiểm tra xem số lượng sản phẩm cần đặt hàng có lớn hơn
        # số lượng sản phẩm trong kho hay không
        if product_quantity > product_in_stock:
            # Nếu số lượng sản phẩm cần đặt hàng lớn hơn số lượng sản phẩm trong kho
            # thì hiển thị thông báo lỗi và đặt số lượng sản phẩm trong kho là 0
            raise models.ValidationError('Không đủ số lượng sản phẩm trong kho!')
            self.kho_id.soluong = 0
        else:
            # Cập nhật số lượng sản phẩm trong kho
            self.kho_id.soluong -= product_quantity




class SanPham(models.Model):
    _inherit = "sanpham"
    idctdh = fields.One2many("ctdonhang", "product_item_id", string= "Chi tiết đơn hàng")



