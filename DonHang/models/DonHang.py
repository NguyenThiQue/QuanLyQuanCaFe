import self as self

from odoo import models, fields, api

class DonHang(models.Model):
    _name = 'donhang'

    _table = "DonHang"
    _description = ''
    name = fields.Char(string="Đơn hàng")
    id_donhang = fields.Char(string="Mã đơn hàng", required=True)
    tongdh = fields.Float(compute='_compute_price_total',string="Tổng đơn hàng")
    id_nv = fields.Many2one("nhanvien", string="Mã nhân viên", required=True)


    ct_donhang = fields.One2many("ctdonhang", "hoadon_id", string="Chi tiết đơn hàng")
    id_khachhang = fields.Many2one("khachhang", string="Khách hàng", required = True)
    ngaytaodh = fields.Date(string="Ngày tạo đơn hàng")
    # confirmed = fields.Boolean(string='Xác nhận', default=False)

    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')
                              ], default='draft', string='Status')



    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = "draft"

    def action_cancel(self):
        self.state = "cancel"

    @api.depends('ct_donhang')
    def _compute_price_total(self):
        for record in self:
            price = sum(record.ct_donhang.mapped('tonggiasp'))
            record.tongdh = price

    # ============================= cập nhật thống kê doanh thu =============================
    def write(self, values):
        result = super(DonHang, self).write(values)
        self.update_thongke()
        return result

    @api.model
    def create(self, values):
        result = super(DonHang, self).create(values)
        result.update_thongke()
        return result

    @api.depends('tongdh', 'ngaytaodh')
    def update_thongke(self):
        month = self.ngaytaodh.strftime("%m")
        year = self.ngaytaodh.strftime("%Y")
        thongke = self.env['thongke'].search([('month', '=', month), ('year', '=', year)], limit=1)
        thongke.revenue = thongke.calculate_revenue(month, year)
        thongkesl = self.env['thongkesldh'].search([('month', '=', month), ('year', '=', year)], limit=1)
        thongkesl.sldh = thongkesl.compute_sale_order(month, year)

    #==========================================================


class NhanVien(models.Model):
    _inherit = "nhanvien"
    sp_idnv = fields.One2many("donhang", "id_nv", string ="Thông tin đơn hàng")


class CTDonHang(models.Model):
    _inherit = "ctdonhang"
    hoadon_id = fields.Many2one("donhang", string="Hoá đơn")

class KhachHang(models.Model):
    _inherit = "khachhang"
    id_kh = fields.One2many("donhang","id_khachhang", string = "Khách hàng")


