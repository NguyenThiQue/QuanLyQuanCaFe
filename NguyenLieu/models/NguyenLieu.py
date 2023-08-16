from odoo import models, fields, api

class NguyenLieu(models.Model):
    _name = 'nguyenlieu'
    _description = 'Thông tin nguyên liệu'
    name = fields.Char(string = "Tên nguyên liệu")
    # nguyenlieu_ma = fields.Char(string = " Mã nguyên liệu")
    nguyenlieu_dv_id = fields.Char(string = "Đơn vị tính")
    price = fields.Float(string = "Giá")
    # nguyenlieu_giaxuat = fields.Float(string = "Giá xuất")
    # nguyenlieu_tondinhmuc = fields.Float(string = "Tồn định mức")
    # nguyenlieu_tonthucte = fields.Float(compute = 'get_tonthucte', string = 'Tồn kho', store = True)
    nguyenlieu_hinhanh = fields.Binary(string = "Hình ảnh", attachment = True)
    # nguyenlieu_nsp_id = fields.Char(string="Nhóm nguyên liệu")
    ma_ncc = fields.Many2one("nccnguyenlieu", string = "Mã nhà cung cấp", required = True)

    loainguyenlieu = fields.Many2one("loainguyenlieu", string="Loại nguyên liệu", required = True)
    id_nhanviencsp = fields.Many2one("nhanvien", string="Mã nhân viên", required = True)
    # kho_id = fields.Char(string="Kho", compute = "_compute_kho", store = True)

    # @api.depends("id_catesp")
    # def _compute_kho(self):
    #     for i in self:
    #         kho = i.id_catesp.id_kho.name
    #         i.kho_id = kho