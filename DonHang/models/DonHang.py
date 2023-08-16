import self as self

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError



class DonHang(models.Model):
    _name = 'donhang'

    _table = "DonHang"
    _description = ''
    name = fields.Char(string="Đơn hàng")
<<<<<<< HEAD
    tongdh = fields.Float(compute='_compute_price_total',string="Tổng đơn hàng")
    # id_nv = fields.Many2one("nhanvien", string="Mã nhân viên")
    id_nv = fields.Many2one("nhanvien", string="Mã nhân viên", compute = "_compute_name_nhanvien")


    ct_donhang = fields.One2many("ctdonhang", "hoadon_id", string="Chi tiết đơn hàng")
=======
    # id_donhang = fields.Char(string="Mã đơn hàng")
    tongdh = fields.Float(compute='_compute_price_total',string="Tổng đơn hàng")
    id_nv = fields.Many2one("nhanvien", string="Mã nhân viên")


    ct_donhang = fields.One2many("ctdonhang", "hoadon_id", string="Chi tiết đơn hàng")
    # id_khachhang = fields.Many2one("khachhang", string="Khách hàng", required = True)
>>>>>>> a955c00701b649db70a93d96737b4ca121d43598
    id_khachhang = fields.Many2one("khachhang", string="Khách hàng")
    ngaytaodh = fields.Date(string="Ngày tạo đơn hàng")

    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')
                              ], default='draft', string='Status')


<<<<<<< HEAD


    @api.depends('ct_donhang')
    def _compute_name_nhanvien(self):
        for record in self:
            nhanvien_ids = record.ct_donhang.mapped('id_nhanvien')
            if len(nhanvien_ids) == 1:
                record.id_nv = nhanvien_ids[0]
            else:
                record.id_nv = False  # Set to False or another appropriate value when there's ambiguity
=======
>>>>>>> a955c00701b649db70a93d96737b4ca121d43598

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

<<<<<<< HEAD

=======
    # @api.depends('tongdh', 'ngaytaodh')
    # def update_thongke(self):
    #     month = self.ngaytaodh.strftime("%m")
    #     year = self.ngaytaodh.strftime("%Y")
    #     thongke = self.env['thongke'].search([('month', '=', month), ('year', '=', year)], limit=1)
    #     thongke.revenue = thongke.calculate_revenue(month, year)
    #     thongkesl = self.env['thongkesldh'].search([('month', '=', month), ('year', '=', year)], limit=1)
    #     thongkesl.sldh = thongkesl.compute_sale_order(month, year)
>>>>>>> a955c00701b649db70a93d96737b4ca121d43598

    @api.depends('tongdh', 'ngaytaodh')
    def update_thongke(self):
        for record in self:
            if record.ngaytaodh:
                month = record.ngaytaodh.strftime("%m")
                year = record.ngaytaodh.strftime("%Y")
                thongke = self.env['thongke'].search([('month', '=', month), ('year', '=', year)], limit=1)
                if thongke:
                    thongke.revenue = thongke.calculate_revenue(month, year)
                thongkesl = self.env['thongkesldh'].search([('month', '=', month), ('year', '=', year)], limit=1)
                if thongkesl:
                    thongkesl.sldh = thongkesl.compute_sale_order(month, year)

<<<<<<< HEAD

    def action_confirm(self):
        for line in self.ct_donhang:
            for material in line.product_item_id.nguyenlieu_ids:
                related_phieunhapkho = self.env['phieunhapkho'].search([
                    ('nguyenlieu_id', '=', material.material_id.id)
                ], order='create_date asc')

                remaining_quantity = material.quantity * line.quantity

                for phieunhapkho in related_phieunhapkho:
                    if remaining_quantity <= 0:
                        break

                    if phieunhapkho.soluong >= remaining_quantity:
                        phieunhapkho.soluong -= remaining_quantity
                        remaining_quantity = 0
                    else:
                        remaining_quantity -= phieunhapkho.soluong
                        phieunhapkho.soluong = 0
                        raise models.ValidationError('Không đủ nguyên liệu để tạo sản phẩm ' + line.product_item_id.name)

=======
    #========================================================== Xác nhận số lượng sản phẩm và trừ đí

    @api.onchange('ct_donhang')
    def onchange_order_line(self):
        for line in self.ct_donhang:
            if line.quantity > line.product_item_id.quantity:
                raise models.ValidationError('Không đủ số lượng sản phẩm!')

    def action_confirm(self):
        for line in self.ct_donhang:
            if line.quantity > line.product_item_id.quantity:
                raise models.ValidationError('Không đủ số lượng sản phẩm!')
            line.product_item_id.quantity -= line.quantity
>>>>>>> a955c00701b649db70a93d96737b4ca121d43598
        self.state = 'done'


class NhanVien(models.Model):
    _inherit = "nhanvien"
    sp_idnv = fields.One2many("donhang", "id_nv", string ="Thông tin đơn hàng")


class CTDonHang(models.Model):
    _inherit = "ctdonhang"
    hoadon_id = fields.Many2one("donhang", string="Hoá đơn")

class KhachHang(models.Model):
    _inherit = "khachhang"
    id_kh = fields.One2many("donhang","id_khachhang", string = "Khách hàng")






<<<<<<< HEAD



=======
>>>>>>> a955c00701b649db70a93d96737b4ca121d43598
