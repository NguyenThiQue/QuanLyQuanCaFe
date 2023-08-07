from odoo import models, fields, api

class BaoCaoTonKho(models.Model):
    _name = "baocaotonkho"
    name = fields.Char(string="Tên báo cáo")
    # nguyenlieu_item_id = fields.Many2one("sanpham", string="Sản phẩm")
    nguyenlieu_item_id = fields.Many2one("nguyenlieu", string="Nguyên liệu")
    # kho_id = fields.Many2one("kho", string="Kho")
    # tenkho = fields.Char(string="Tên kho", compute = "_compute_name_kho", store = True)
    soluongthucte = fields.Integer(string="Số lượng thực tế", compute = "_compute_real_quantity", store = True)
    soluonghienco = fields.Integer(string="Số lượng hiện có", compute = "_compute_pre_quantity", store = True)
    totalprice = fields.Integer(string="Giá trị", compute = "_compute_total_price", store = True)

    phieunhapkho_id = fields.Many2one("phieunhapkho", string="Phiếu nhập kho")




    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done')
                              ], default='draft', string='Status')


    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = "draft"







    # @api.depends('nguyenlieu_item_id')
    # def _compute_name_kho(self):
    #     for item in self:
    #         ten_kho = item.nguyenlieu_item_id.kho_id
    #         print('kho', ten_kho)
    #         item.tenkho= ten_kho

    @api.depends('phieunhapkho_id')
    def _compute_real_quantity(self):
        for item in self:
            related_phieunhapkho = self.env['phieunhapkho'].search([
                ('nguyenlieu_id', '=', self.nguyenlieu_item_id.id),
            ])
            soluong = sum(related_phieunhapkho.mapped('soluongthucte'))
            item.soluongthucte = soluong

    @api.depends('phieunhapkho_id')
    def _compute_pre_quantity(self):
        for item in self:
            related_phieunhapkho = self.env['phieunhapkho'].search([
                ('nguyenlieu_id', '=', self.nguyenlieu_item_id.id),
            ])
            soluong = sum(related_phieunhapkho.mapped('soluong'))
            item.soluonghienco = soluong
    #
    @api.depends('nguyenlieu_item_id','soluongthucte')
    def _compute_total_price(self):
        for i in self:
            tong = i.soluongthucte * i.nguyenlieu_item_id.price
            i.totalprice = tong