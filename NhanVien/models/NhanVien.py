from odoo import models, fields, api, exceptions
import bcrypt

class NhanVien(models.Model):
    _name = 'nhanvien'
    _table = "NhanVien"
    _description = ''
    # id_nhanvien = fields.Char(string="Mã nhân viên ")
    name = fields.Char(string = "Tên nhân viên")
    address = fields.Char(string="Địa chỉ")
    male = fields.Char(string="Giới tính")
    date_birthday = fields.Date(string="Ngày sinh")
    phone = fields.Char(string="SĐT")
    username = fields.Char(string="Username", required=True, unique=True)
    password = fields.Char(string="Password", required=True)
    is_admin = fields.Boolean(string="Is Admin")
    user_id = fields.Many2one('res.users', string='User', ondelete='cascade')

    # def authenticate_user(self, password):
    #     return self.env.user.sudo().check_password(password)



    # @api.model
    # def authenticate(self, login, password):
    #     """Xác thực thông tin đăng nhập của nhân viên."""
    #     nhanvien = self.search([('login', '=', login), ('password', '=', password)])
    #     print("nhanvien", nhanvien)
    #     if nhanvien:
    #         return nhanvien.user_id  # Trả về tài khoản người dùng liên kết với nhân viên
    #     return False



    # def name_get(self):
    #     result = []
    #     for group in self:
    #
    #         name = '[' + group.id_nhanvien + ']' + " " + group.name
    #         result.append((group.id, name))
    #     return result





