from odoo import models, fields, api


class SanPham(models.Model):
    _name = 'sanpham'
    _table = "san_pham"
    _description = ''
    # id_sp = fields.Char(string="Mã sản phẩm ", required = True)
    name = fields.Char(string="Tên sản phẩm")
    img_sp = fields.Image(string="Hình ảnh", attachment=True)
    descr = fields.Html(string="Mô tả sản phẩm")
    price = fields.Float(string="Giá sản phẩm")
    id_catesp = fields.Many2one("danhmucsp", string="Loại sản phẩm", required=True)
    id_nhanviencsp = fields.Many2one("nhanvien", string="Tên nhân viên", required=True)
    # kho_id = fields.Char(string="Kho", compute = "_compute_kho", store = True)

    # so_luong_san_pham = fields.Float(string='Số lượng sản phẩm')
    nguyenlieu_ids = fields.One2many('chitietsanpham', 'product_id', string='Nguyên liệu')
    quantity = fields.Integer(string="Số lượng", default=1, readonly= True)

    @api.model
    def create(self, vals):
        if 'name' in vals:
            existing_product = self.search([
                ('name', '=', vals['name'])
            ], limit=1)

            if existing_product:
                existing_product.write({'quantity': existing_product.quantity + 1})
                return existing_product
        return super(SanPham, self).create(vals)

    # @api.depends('quantity')
    # def _compute_soluongsp(self):
    #     for i in self:
    #         quantityproduct = i.nguyenlieu_ids.soluongsanphamduoctao
    #         i.quantity = quantityproduct

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'descr': self.descr,
    #         'price': self.price,
    #         # Add other fields as needed
    #     }

    # soluong

    # @api.depends("id_catesp")
    # def _compute_kho(self):
    #     for i in self:
    #         kho = i.id_catesp.id_kho.name
    #         i.kho_id = kho


# class DanhMucSP(models.Model):
#     _inherit = "danhmucsp"
#     sp_category = fields.One2many("sanpham","id_catesp",string="Sản Phẩm" )

class NhanVien(models.Model):
    _inherit = "nhanvien"
    sp_idnv = fields.One2many("sanpham", "id_nhanviencsp", string="Thông tin sản phẩm")


class ChiTietSanPham(models.Model):
    _name = "chitietsanpham"
    name = fields.Char("Name")
    product_id = fields.Many2one('sanpham', string='Sản phẩm', required=True)
    material_id = fields.Many2one('nguyenlieu', string='Nguyên liệu', required=True)
    quantity = fields.Float(string='Số lượng', required=True)

    # kho_idd = fields.Many2one("kho", string="Kho")

    @api.onchange('quantity')
    def onchange_quantity(self):
        # Lấy số lượng nguyên liệu
        material_quantity = self.quantity

        related_phieunhapkho = self.env['phieunhapkho'].search([
            ('nguyenlieu_id', '=', self.material_id.id)
        ])

        total_stock_quantity = sum(related_phieunhapkho.mapped('soluong'))
        print("total", total_stock_quantity)

        # Kiểm tra xem số lượng sản phẩm cần đặt hàng có lớn hơn
        # số lượng tồn kho thực tế hay không
        if material_quantity > total_stock_quantity:
            # Nếu số lượng sản phẩm cần đặt hàng lớn hơn số lượng tồn kho thực tế
            # thì hiển thị thông báo lỗi và đặt số lượng sản phẩm trong kho là 0
            raise models.ValidationError('Không đủ số lượng sản phẩm trong kho!')
            # self.phieunhapkho_id.soluong = 0
        else:
            for phieunhapkho in related_phieunhapkho:
                phieunhapkho.soluong -= material_quantity

                print("còn lại", phieunhapkho.soluong)




class NguyenLieu(models.Model):
    _inherit = "nguyenlieu"
    product_material_ids = fields.Many2many('product.template', 'product_material_rel', 'material_id', 'product_id',
                                            string='Products Using This Material')


class ShoppingCart(models.Model):
    _name = 'my_shopping_cart.cart'
    _description = 'Shopping Cart'

    name = fields.Char(string='Cart Name', required=True)
    total_price = fields.Float(string='Total Price', compute='_compute_total_price')
    product_ids = fields.Many2many('sanpham', string='Products')

    def _compute_total_price(self):
        for cart in self:
            cart.total_price = sum(cart.product_ids.mapped('price'))
