from odoo import models, fields, api

class NhanVien(models.Model):
    _name = 'nhanvien'
    _table = "NhanVien"
    _description = ''
    id_nhanvien = fields.Char(string="Mã nhân viên ")
    name = fields.Char(string = "Tên nhân viên")
    address = fields.Char(string="Địa chỉ")
    male = fields.Char(string="Giới tính")
    date_birthday = fields.Date(string="Ngày sinh")
    phone = fields.Char(string="SĐT")



    def name_get(self):
        result = []
        for group in self:

            name = '[' + group.id_nhanvien + ']' + " " + group.name
            result.append((group.id, name))
        return result