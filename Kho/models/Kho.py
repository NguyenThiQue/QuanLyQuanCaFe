from odoo import models, fields, api

class Kho(models.Model):
    _name = 'kho'
    _description = ''
    name = fields.Char(string="Tên")
    diachi = fields.Char(string="Địa chỉ")
    donvi = fields.Char(string="Đơn vị")
#     phieunhapkho_ids = fields.One2many("phieunhapkho", "idkho", string="Sản phẩm")
#
#
#
# class PhieuNhapKho(models.Model):
#     _inherit = "phieunhapkho"
#     idkho = fields.Many2one("kho", string="Kho")




