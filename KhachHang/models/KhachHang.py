from odoo import models, fields, api

class KhachHang(models.Model):
    _name = 'khachhang'
    _table = "KhachHang"
    _description = ''
    id_khachhang = fields.Char(string="Mã khách hàng ")
    name = fields.Char(string = "Tên khách hàng")
    phone = fields.Char(string="Số điện thoại")
    email = fields.Char(string="Email")