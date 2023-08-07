# from odoo import http
from odoo.exceptions import ValidationError
from odoo.http import request
#

from odoo import models, fields, api

import json
import logging
from odoo import http

_logger = logging.getLogger(__name__)


class ShoppingCartController(http.Controller):

    @http.route('/add_to_cart', type='http', auth='public', website=True, csrf=False)
    def add_to_cart(self, **post):
        product_item_id = post.get('product_item_id')
        quantity = post.get('quantity')

        if not product_item_id or not quantity:
            return json.dumps({'error': 'Missing product_id or quantity'})

        try:
            product_item_id = int(product_item_id)
            quantity = int(quantity)
        except ValueError:
            return json.dumps({'error': 'Invalid product_item_id or quantity'})

        shopping_cart = request.env['ctdonhang']

        try:
            cart_item = shopping_cart.sudo().search([('product_item_id', '=', product_item_id)])
            if cart_item:
                cart_item.write({'quantity': cart_item.quantity + quantity})
            else:
                shopping_cart.create({
                    'product_item_id': product_item_id,
                    'quantity': quantity,
                    # 'id_nhanvien': request.env.user.id_nhanvien.id,
                })
        except Exception as e:
            _logger.error("Error while adding to cart: %s", str(e))
            return json.dumps({'error': 'Error while adding to cart'})

        return json.dumps({'success': True})

    #
    @http.route('/shop/cart', type='http', auth='public', website=True)
    def shopping_cart_page(self, **kw):
        # Your logic to fetch cart data and pass it to the template
        cart_items = http.request.env['ctdonhang'].search(
            [])  # Replace 'shopping.cart' with the actual model name
        cart_data = {
            'shopping_cart': cart_items,
        }
        return http.request.render('CTDonHang.website_shopping_cart_page', cart_data)

    @http.route('/remove_from_cart', type='http', auth='public', website=True, csrf=False)
    def remove_from_cart(self, **post):
        product_item_id = post.get('product_item_id')

        if not product_item_id:
            return json.dumps({'error': 'Missing product_item_id'})

        try:
            product_item_id = int(product_item_id)
        except ValueError:
            return json.dumps({'error': 'Invalid product_item_id'})

        # Your logic to remove the item from the cart goes here...
        shopping_cart = request.env['ctdonhang']
        cart_item = shopping_cart.sudo().search([('product_item_id', '=', product_item_id)])
        if not cart_item:
            return json.dumps({'error': 'Item not found in cart'})

        cart_item.unlink()

        return json.dumps({'success': True})

    @http.route('/update_cart_item', type='http', auth='public', website=True, csrf=False)
    def update_cart_item(self, **post):
        product_item_id = post.get('product_item_id')
        quantity = post.get('quantity')

        if not product_item_id or not quantity:
            return json.dumps({'error': 'Missing product_item_id or quantity'})

        try:
            product_item_id = int(product_item_id)
            quantity = int(quantity)
        except ValueError:
            return json.dumps({'error': 'Invalid product_item_id or quantity'})

        # Your logic to update the cart item quantity goes here...
        # For example, you can fetch the cart item and update its quantity
        shopping_cart = request.env['ctdonhang']
        cart_item = shopping_cart.sudo().search([('product_item_id', '=', product_item_id)])
        if cart_item:
            cart_item.write({'quantity': quantity})

        return json.dumps({'success': True})

    # @http.route('/gio_hang/confirm_order', type='http', auth='user', website=True)
    # def confirm_order(self):
    #     # Lấy thông tin giỏ hàng của nhân viên đăng nhập
    #     gio_hang = request.env['ctdonhang'].sudo().search([('id_nhanvien', '=', request.env.user.id)])
    #
    #     if not gio_hang:
    #         return http.request.redirect('/gio_hang')  # Chuyển hướng nếu giỏ hàng trống
    #
    #     # Lấy thông tin khách hàng của nhân viên từ model `donhang`
    #     donhang_model = request.env['donhang']
    #     nhanvien_id = request.env.user.id
    #     donhang = donhang_model.sudo().search([('id_nv', '=', nhanvien_id)], limit=1)
    #
    #     # Tạo đơn hàng nếu chưa có
    #     if not donhang:
    #         # return http.request.redirect('/create_nv')  # Chuyển hướng đến trang tạo thông tin nhân viên
    #         return False
    #
    #     # Tạo chi tiết đơn hàng dựa trên thông tin từ giỏ hàng
    #     for item in gio_hang:
    #         donhang.ct_donhang = [(0, 0, {
    #             'product_item_id': item.product_item_id.id,
    #             'quantity': item.quantity,
    #             'gia': item.gia,
    #             'tonggiasp': item.tonggiasp,
    #         })]
    #
    #     # Tính tổng đơn hàng
    #     donhang.tongdh = sum(item.tonggiasp for item in gio_hang)
    #
    #     # Xóa giỏ hàng sau khi tạo đơn hàng
    #     gio_hang.unlink()
    #
    #     return http.request.redirect('/my/orders')  # Chuyển hướng đến trang đơn hàng của nhân viên
    #

    # @http.route('/gio_hang/confirm_order', type='http', auth='user', website=True)
    # def confirm_order(self):
    #     # Lấy giỏ hàng của người dùng đang đăng nhập
    #     # gio_hang = request.env['ctdonhang'].sudo().search([('id_nhanvien', '=', request.env.user.id_nhanvien.id)])
    #     gio_hang = request.env['ctdonhang'].sudo().search([])
    #
    #     if not gio_hang:
    #         return http.request.redirect('/gio_hang')  # Chuyển hướng về trang giỏ hàng nếu giỏ hàng rỗng
    #
    #     # Tạo đơn hàng từ giỏ hàng
    #     created_order = gio_hang.create_donhang_from_giohang()
    #
    #     if created_order:
    #         # Đơn hàng đã được tạo thành công, chuyển hướng đến trang xác nhận đơn hàng
    #         return http.request.redirect('/order_confirmation')
    #     else:
    #         # Có lỗi xảy ra khi tạo đơn hàng, xử lý và chuyển hướng tùy theo trường hợp
    #         return http.request.redirect('/gio_hang')  # Chẳng hạn, chuyển hướng về trang giỏ hàng
    #

    #


#
    @http.route('/api/get_cart', type='json', auth='public', methods=['GET'], csrf=False)
    def get_cart_api(self, **kwargs):
        try:
            # Gọi hàm để lấy thông tin giỏ hàng từ database
            cart_data = self.get_cart_data()

            return json.dumps(cart_data)
        except Exception as ex:
            return json.dumps({'error': str(ex)})

    @staticmethod
    def get_cart_data():
        # Lấy thông tin giỏ hàng từ database (sử dụng model "CTDONHANG" trong Odoo)
        cart = request.env['ctdonhang'].search([('your_filter_field', '=', 'your_filter_value')])
        if not cart:
            return {'products': []}

        cart_data = {
            'products': [],
        }

        for product in cart:
            cart_data['products'].append({
                'product_item_id': product.product_item_id.id,
                'quantity': product.quantity,
            })

        return cart_data
