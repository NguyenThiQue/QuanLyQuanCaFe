from odoo import models, fields, api

class NCCNguyenLieu(models.Model):
    _name = 'nccnguyenlieu'
    _table = "NCCNguyenLieu"
    _description = 'Thông tin nhà cung cấp nguyên liệu'
    # ma_ncc = fields.Char(string="Mã nhà cung cấp")
    name = fields.Char(string="Tên nhà cung cấp")
    # nguyenlieu_ma = fields.Char(string=" Mã nguyên liệu")