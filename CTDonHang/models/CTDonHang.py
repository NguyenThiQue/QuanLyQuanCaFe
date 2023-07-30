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
    # kho_id = fields.Many2one("kho", string="Kho", related="product_item_id.kho_id")
    kho_idd = fields.Many2one("kho", string="Kho")

    phieunhapkho_id = fields.Many2one("phieunhapkho", string="Phiếu nhập kho")


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


    # print("x", total_stock_quantity)
    @api.onchange('quantity')
    def onchange_quantity(self):
        # Lấy số lượng sản phẩm
        product_quantity = self.quantity

        # Lấy số lượng sản phẩm trong kho
        # product_in_stock = self.kho_id.soluong
        #---------------------------------------------------
        # if self.kho_id.phieunhapkho_ids.sanpham_id == self.product_item_id:
        #
        #     product_in_stock = self.kho_id.phieunhapkho_ids.soluong
        #     print("sl", product_in_stock)
            # Lấy số lượng sản phẩm tồn kho thực tế từ các phiếu nhập kho liên quan đến sản phẩm
        # Lấy danh sách phiếu nhập kho liên quan đến sản phẩm và kho hiện tại

        related_phieunhapkho = self.env['phieunhapkho'].search([
            ('sanpham_id', '=', self.product_item_id.id),
            ('kho_id', '=', self.kho_idd.id)
        ])

        # Tính lại giá cho sản phẩm
        # self._compute_price()
        # Tính tổng số lượng thực tế từ các phiếu nhập kho đã lấy
        total_stock_quantity = sum(related_phieunhapkho.mapped('soluong'))
        print("total", total_stock_quantity)

        # Kiểm tra xem số lượng sản phẩm cần đặt hàng có lớn hơn
        # số lượng tồn kho thực tế hay không
        if product_quantity > total_stock_quantity:
            # Nếu số lượng sản phẩm cần đặt hàng lớn hơn số lượng tồn kho thực tế
            # thì hiển thị thông báo lỗi và đặt số lượng sản phẩm trong kho là 0
            raise models.ValidationError('Không đủ số lượng sản phẩm trong kho!')
            # self.phieunhapkho_id.soluong = 0
        else:
            for phieunhapkho in related_phieunhapkho:
                phieunhapkho.soluong -= product_quantity
                print("còn lại", phieunhapkho.soluong)
        #-------------------------------------------------------

        # #Kiểm tra xem số lượng sản phẩm cần đặt hàng có lớn hơn
        # #số lượng sản phẩm trong kho hay không
        # if product_quantity > total_stock_quantity:
        #     # Nếu số lượng sản phẩm cần đặt hàng lớn hơn số lượng sản phẩm trong kho
        #     # thì hiển thị thông báo lỗi và đặt số lượng sản phẩm trong kho là 0
        #     raise models.ValidationError('Không đủ số lượng sản phẩm trong kho!')
        #     self.kho_id.phieunhapkho_ids.soluong = 0
        # else:
        #     # Cập nhật số lượng sản phẩm trong kho
        #     self.kho_id.phieunhapkho_ids.soluong -= product_quantity

        #=----------------------------------------------------------------







class SanPham(models.Model):
    _inherit = "sanpham"
    idctdh = fields.One2many("ctdonhang", "product_item_id", string= "Chi tiết đơn hàng")

class PhieuNhapKho(models.Model):
    _inherit = "phieunhapkho"
    ctdh = fields.One2many("ctdonhang","phieunhapkho_id", string="Chi tiết đơn hàng")



