from odoo import models, fields, api

class Kho(models.Model):
    _name = 'kho'
    _description = ''
    name = fields.Char(string="Tên")
    soluong = fields.Integer(string="Số lượng")
    diachi = fields.Char(string="Địa chỉ")
    # cauhinhkho = fields.Char(string="Cấu hình kho hàng")
    category = fields.Many2one("danhmucsp", string="Loại sản phẩm")

    # @api.model
    # def update_stock_quantity(self, ctdonhang):
    #     self.ensure_one()
    #     self.soluong -= ctdonhang.quantity







