from odoo import models, fields, api


class SanPham(models.Model):
    _name = 'sanpham'
    _table = "san_pham"
    _description = ''
    name = fields.Char(string="Tên sản phẩm")
    img_sp = fields.Image(string="Hình ảnh", attachment=True)
    descr = fields.Html(string="Mô tả sản phẩm")
    price = fields.Float(string="Giá sản phẩm")
    id_catesp = fields.Many2one("danhmucsp", string="Loại sản phẩm", required=True)


    nguyenlieu_ids = fields.One2many('chitietsanpham', 'product_id', string='Nguyên liệu')
    quantity = fields.Integer(string="Số lượng", default=1, readonly= True)



    @api.model
    def create(self, vals):
        if 'name' in vals:
            existing_product = self.search([
                ('name', '=', vals['name'])
            ], limit=1)

            if existing_product:
                existing_product.write({
                    'img_sp': existing_product.img_sp,
                    'descr': existing_product.descr,
                    'price': existing_product.price,
                    'id_catesp': existing_product.id_catesp,
                    'quantity': existing_product.quantity + 1,
                })
                return existing_product


        return super(SanPham, self).create(vals)


class ChiTietSanPham(models.Model):
    _name = "chitietsanpham"
    name = fields.Char("Name")
    product_id = fields.Many2one('sanpham', string='Sản phẩm', required=True)
    material_id = fields.Many2one('nguyenlieu', string='Nguyên liệu', required=True)
    quantity = fields.Float(string='Số lượng', required=True)





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
