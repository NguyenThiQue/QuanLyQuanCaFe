from odoo import models, fields, api

class DanhMucSP(models.Model):
    _name = 'danhmucsp'
    _table = "DanhMucSP"
    _description = ''
    id_category = fields.Char(string="Mã loại sản phẩm")
    name = fields.Char(string = "Tên loại sản phẩm")
    id_kho = fields.Many2one("kho", string="Kho")
