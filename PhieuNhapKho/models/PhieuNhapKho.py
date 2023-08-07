from odoo import models, fields, api

class PhieuNhapKho(models.Model):
    _name = 'phieunhapkho'
    _description = 'Phiếu nhập kho'

    name = fields.Char(string="Name")
    # sanpham_id = fields.Many2one('sanpham', string='Sản Phẩm', required=True)
    nguyenlieu_id = fields.Many2one('nguyenlieu', string='Nguyên liệu', required=True)
    ngay_nhap = fields.Date(string='Ngày Nhập', required=True)
    soluongthucte = fields.Float(string="Số lượng thực tế")
    soluong = fields.Float(string="Số lượng hiện có", compute="_compute_sl", store=True)
    loainguyenlieu = fields.Char(string="Loại nguyên liệu", compute = "_compute_loaisp")
    giasp = fields.Float(string= "Giá", compute = "_compute_price")
    kho_id = fields.Many2one("kho", string="Kho")
    # kho_id = fields.Char(string="kho", compute = "_compute_kho", store = True)

    # @api.depends("sanpham_id")
    # def _compute_kho(self):
    #     for i in self:
    #         kho = i.sanpham_id.kho_id
    #         i.kho_id = kho

    @api.depends("soluongthucte")
    def _compute_sl(self):
        for i in self:
            i.soluong = i.soluongthucte





    @api.depends("nguyenlieu_id")
    def _compute_loaisp(self):
        for i in self:
            loaisanpham = i.nguyenlieu_id.loainguyenlieu.name
            i.loainguyenlieu = loaisanpham

    @api.depends("nguyenlieu_id")
    def _compute_price(self):
        for i in self:
            gia = i.nguyenlieu_id.price
            i.giasp = gia

