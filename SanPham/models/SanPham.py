
from odoo import models, fields, api

class SanPham(models.Model):
    _name = 'sanpham'
    _table = "san_pham"
    _description = ''
    id_sp = fields.Char(string="Mã sản phẩm ", required = True)
    name = fields.Char(string = "Tên sản phẩm")
    img_sp = fields.Image(string = "Hình ảnh", attachment = True)
    descr = fields.Html(string="Mô tả sản phẩm")
    price = fields.Float(string="Giá sản phẩm")
    id_catesp = fields.Many2one("danhmucsp", string="Loại sản phẩm", required = True)
    id_nhanviencsp = fields.Many2one("nhanvien", string="Mã nhân viên", required = True)
    kho_id = fields.Char(string="Kho", compute = "_compute_kho")

    @api.depends("id_catesp")
    def _compute_kho(self):
        for i in self:
            kho = i.id_catesp.id_kho.name
            i.kho_id = kho


class DanhMucSP(models.Model):
    _inherit = "danhmucsp"
    sp_category = fields.One2many("sanpham","id_catesp",string="Sản Phẩm" )

class NhanVien(models.Model):
    _inherit = "nhanvien"
    sp_idnv = fields.One2many("sanpham", "id_nhanviencsp", string ="Thông tin sản phẩm")

