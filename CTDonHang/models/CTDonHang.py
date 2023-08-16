from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.http import request


class CTDonHang(models.Model):
    _name = 'ctdonhang'

    _table = "CTDonHang"
    _description = ''

    gia = fields.Float(compute='_compute_price', string="Giá")
    quantity = fields.Integer(string="Số lượng")
    tonggiasp = fields.Float(compute='_compute_price_total', string="Tổng giá cho sản phẩm")

    product_item_id = fields.Many2one("sanpham", string="Sản phẩm")

    kho_idd = fields.Many2one("kho", string="Kho")

    phieunhapkho_id = fields.Many2one("phieunhapkho", string="Phiếu nhập kho")

    id_nhanvien = fields.Many2one("nhanvien", string="Nhân viên", readonly=True)

    @api.model
    def create(self, vals):
        # Tìm thông tin người dùng đăng nhập
        user = self.env.user
        nhanvien_model = self.env['nhanvien']
        nhanvien = nhanvien_model.sudo().search([('username', '=', user.login)], limit=1)
        print("nhân viên", nhanvien.id)

        if nhanvien:
            vals['id_nhanvien'] = nhanvien.id
        return super(CTDonHang, self).create(vals)







    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if request.env.user:
                nhanvien_model = self.env['nhanvien']
                nhanvien = nhanvien_model.sudo().search([('user_id', '=', request.env.user.id)], limit=1)
                if nhanvien:
                    vals['id_nhanvien'] = nhanvien.id



        return super(CTDonHang, self).create(vals_list)



    @api.depends('product_item_id')
    def _compute_price(self):
        for record in self:
            price_item = record.product_item_id.price
            record.gia = price_item

    @api.depends('quantity', 'gia')
    def _compute_price_total(self):
        for record in self:
            record.tonggiasp = record.gia * record.quantity


# -----------------------------------------


class SanPham(models.Model):
    _inherit = "sanpham"
    idctdh = fields.One2many("ctdonhang", "product_item_id", string="Chi tiết đơn hàng")


class PhieuNhapKho(models.Model):
    _inherit = "phieunhapkho"
    ctdh = fields.One2many("ctdonhang", "phieunhapkho_id", string="Chi tiết đơn hàng")


class NhanVien(models.Model):
    _inherit = "nhanvien"
    idnhanvien = fields.One2many("ctdonhang", "id_nhanvien", string="Chi tiết đơn hàng")
