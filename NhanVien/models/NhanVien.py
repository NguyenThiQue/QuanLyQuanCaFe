from odoo import models, fields, api, exceptions
import bcrypt
<<<<<<< HEAD

from odoo.exceptions import ValidationError

=======
>>>>>>> a955c00701b649db70a93d96737b4ca121d43598

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
<<<<<<< HEAD
    user_id = fields.Many2one('res.users', string='User', ondelete='cascade')


    @api.constrains('date_birthday')
    def _check_valid_birth_date(self):
        for record in self:
            if record.date_birthday > fields.Date.today():
                raise ValidationError("Birth date cannot be in the future.")

    @api.model
    def authenticate(self, username, password):
        """Xác thực thông tin đăng nhập của nhân viên."""
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        nhanvien = self.search([('username', '=', username), ('password', '=', hashed_password)])

        if nhanvien:
            return nhanvien.user_id  # Trả về tài khoản người dùng liên kết với nhân viên
        return False
=======
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


>>>>>>> a955c00701b649db70a93d96737b4ca121d43598

    # def name_get(self):
    #     result = []
    #     for group in self:
    #
    #         name = '[' + group.id_nhanvien + ']' + " " + group.name
    #         result.append((group.id, name))
    #     return result
<<<<<<< HEAD
=======

>>>>>>> a955c00701b649db70a93d96737b4ca121d43598




