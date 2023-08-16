from odoo import http
from odoo.http import request
import json

class SanPhamController(http.Controller):

    @http.route('/sanpham', type='http', auth='public', website=True)
    def display_product(self, **kw):

        product = http.request.env['sanpham'].search([])
        return http.request.render("SanPham.product_item", {
            'product_list':product,
        })


    @http.route("/sanpham/<model('sanpham'):sanpham_item_id>/", type = "http", auth= "public", website = True)
    def display_product_detail(self, sanpham_item_id):
        return  http.request.render("SanPham.product_item_detail", {
            'product_detail': sanpham_item_id
        })



    # class ShoppingCartController(http.Controller):
    #     @http.route('/add_to_cart', type='http', auth='public', website=True, csrf=False)
    #     def add_to_cart(self, **post):
    #         product_id = post.get('product_id')
    #         quantity = post.get('quantity')
    #
    #         if not product_id or not quantity:
    #             return json.dumps({'error': 'Missing product_id or quantity'})
    #
    #         try:
    #             product_id = int(product_id)
    #             quantity = int(quantity)
    #         except ValueError:
    #             return json.dumps({'error': 'Invalid product_id or quantity'})
    #
    #         # Your logic to add to cart goes here...
    #
    #         return json.dumps({'success': True})
