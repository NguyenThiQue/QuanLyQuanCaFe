from odoo import models, fields, api

class LoaiNguyenLieu(models.Model):
    _name = 'loainguyenlieu'
    _description = ''
    name = fields.Char(string="Tên loai nguyên liệu")

