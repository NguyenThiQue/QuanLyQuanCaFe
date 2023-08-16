from odoo import models, fields, api
from odoo.exceptions import ValidationError


class KhachHang(models.Model):
    _name = 'khachhang'
    _table = "KhachHang"
    _description = ''
    # id_khachhang = fields.Char(string="Mã khách hàng ")
    name = fields.Char(string = "Tên khách hàng")
    phone = fields.Char(string="Số điện thoại")
    email = fields.Char(string="Email")

    @api.constrains('email')
    def _check_valid_email(self):
        for record in self:
            if record.email and '@' not in record.email:
                raise ValidationError("Định dạng email không hợp lệ. Vui lòng nhập đúng định dạng email.")