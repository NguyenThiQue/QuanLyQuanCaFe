from odoo import models, fields, api

class NguyenLieu(models.Model):
    _name = 'nguyenlieu'
    _table = "NguyenLieu"
    _description = 'Thông tin nguyên liệu'
    name = fields.Char(string = "Tên nguyên liệu")
    nguyenlieu_ma = fields.Char(string = " Mã nguyên liệu")
    # sp_dv_id = fields.Many2one(comodel_name = 'donvitinh', string = "Đơn vị tính")
    nguyenlieu_dv_id = fields.Char(string = "Đơn vị tính")
    nguyenlieu_gianhap = fields.Float(string = "Giá nhập")
    nguyenlieu_giaxuat = fields.Float(string = "Giá xuất")
    nguyenlieu_giaxuat1 = fields.Float(string = "Giá xuất 1")
    nguyenlieu_giaxuat2 = fields.Float(string = "Giá xuất 2")
    nguyenlieu_tondinhmuc = fields.Float(string = "Tồn định mức")
    nguyenlieu_tonthucte = fields.Float(compute = 'get_tonthucte', string = 'Tồn kho', store = True)
    nguyenlieu_hinhanh = fields.Binary(string = "Hình ảnh", attachment = True)
    # sp_store_fname = fields.Char(string = 'File Name', type = 'jpg,png')
    # sp_nsp_id = fields.Many2one(comodel_name = 'nhomsanpham', string = 'Nhóm sản phẩm')
    nguyenlieu_nsp_id = fields.Char(string="Nhóm nguyên liệu")
    ma_ncc = fields.Many2one("nccnguyenlieu", string = "Mã nhà cung cấp", required = True)