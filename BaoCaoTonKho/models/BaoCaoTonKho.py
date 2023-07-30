from odoo import models, fields, api

class BaoCaoTonKho(models.Model):
    _name = "baocaotonkho"
    name = fields.Char(string="Tên")
    sanpham_item_id = fields.Many2one("sanpham", string="Sản phẩm")
    # kho_id = fields.Many2one("kho", string="Kho")
    # tenkho = fields.Char(string="Tên kho", compute = "_compute_name_kho", store = True)
    # soluongthucte = fields.Integer(string="Số lượng thực tế", compute = "_compute_real_quantity", store = True)
    # soluonghienco = fields.Integer(string="Số lượng hiện có", compute = "_compute_pre_quantity", store = True)
    # totalprice = fields.Integer(string="Giá trị", compute = "_compute_total_price", store = True)

    tenkho = fields.Char(string="Tên kho", store=True)
    soluongthucte = fields.Integer(string="Số lượng thực tế", store=True)
    soluonghienco = fields.Integer(string="Số lượng hiện có", store=True)
    totalprice = fields.Integer(string="Giá trị", store=True)

    # @api.depends('sanpham_item_id')
    # def _compute_name_kho(self):
    #     for item in self:
    #         ten_kho = item.sanpham_item_id.kho_id.name
    #         print('kho', ten_kho)
    #         item.tenkho= ten_kho
    #
    # @api.depends('sanpham_item_id')
    # def _compute_real_quantity(self):
    #     for item in self:
    #         soluong = item.sanpham_item_id.kho_id.soluongthucte
    #         item.soluongthucte = soluong
    #
    # @api.depends('sanpham_item_id')
    # def _compute_pre_quantity(self):
    #     for item in self:
    #         soluong = item.sanpham_item_id.kho_id.soluong
    #         item.soluonghienco = soluong
    #
    # @api.depends('sanpham_item_id')
    # def _compute_total_price(self):
    #     for i in self:
    #         tong = i.sanpham_item_id.kho_id.soluongthucte * i.sanpham_item_id.price
    #         i.totalprice = tong