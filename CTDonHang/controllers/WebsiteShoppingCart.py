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

    # @http.route('/add_to_cart', type='http', auth='public', website=True, csrf=False)
    # def add_to_cart(self, **post):
    #     product_item_id = post.get('product_item_id')
    #     quantity = post.get('quantity')
    #     user = request.env.user
    #     nhanvien_model = request.env['nhanvien']
    #     nhanvien = nhanvien_model.sudo().search([('user_id', '=', user.id)], limit=1)
    #
    #     if not product_item_id or not quantity:
    #         return json.dumps({'error': 'Missing product_id or quantity'})
    #
    #     try:
    #         product_item_id = int(product_item_id)
    #         quantity = int(quantity)
    #     except ValueError:
    #         return json.dumps({'error': 'Invalid product_item_id or quantity'})
    #
    #     shopping_cart = request.env['ctdonhang']
    #
    #     try:
    #         cart_item = shopping_cart.sudo().search([('product_item_id', '=', product_item_id)])
    #         if cart_item:
    #             cart_item.write({'quantity': cart_item.quantity + quantity})
    #         else:
    #             shopping_cart.create({
    #                 'product_item_id': product_item_id,
    #                 'quantity': quantity,
    #                 'id_nhanvien': nhanvien.id,
    #             })
    #     except Exception as e:
    #         _logger.error("Error while adding to cart: %s", str(e))
    #         return json.dumps({'error': 'Error while adding to cart'})
    #
    #     return json.dumps({'success': True})

    # @http.route('/add_to_cart', type='http', auth='public', website=True, csrf=False)
    # def add_to_cart(self, **post):
    #     product_item_id = post.get('product_item_id')
    #     quantity = post.get('quantity')
    #     user = request.env.user
    #
    #     if not product_item_id or not quantity:
    #         return json.dumps({'error': 'Missing product_id or quantity'})
    #
    #     try:
    #         product_item_id = int(product_item_id)
    #         quantity = int(quantity)
    #     except ValueError:
    #         return json.dumps({'error': 'Invalid product_item_id or quantity'})
    #
    #     shopping_cart = request.env['ctdonhang']
    #
    #     if user and user.id:  # Kiểm tra người dùng đăng nhập
    #         nhanvien_model = request.env['nhanvien']
    #         nhanvien = nhanvien_model.sudo().search([('user_id', '=', user.id)], limit=1)
    #         order = request.env['donhang'].sudo().create({'name': 'New Order'})
    #
    #         if nhanvien:  # Nếu người dùng là nhân viên
    #             cart_item = shopping_cart.sudo().search([('product_item_id', '=', product_item_id)])
    #             if cart_item:
    #                 cart_item.write({'quantity': cart_item.quantity + quantity})
    #             else:
    #                 shopping_cart.create({
    #                     'hoadon_id': order.id,
    #                     'product_item_id': product_item_id,
    #                     'quantity': quantity,
    #                     'id_nhanvien': request.env.user.id,
    #                 })
    #             return json.dumps({'success': True})
    #         else:
    #             return json.dumps({'error': 'User is not a valid employee'})
    #     else:
    #         return json.dumps({'error': 'User not logged in'})

    @http.route('/add_to_cart', type='http', auth='public', website=True, csrf=False)
    def add_to_cart(self, **post):
        product_item_id = post.get('product_item_id')
        quantity = post.get('quantity')
        user = request.env.user

        if not product_item_id or not quantity:
            return json.dumps({'error': 'Missing product_id or quantity'})

        try:
            product_item_id = int(product_item_id)
            quantity = int(quantity)
        except ValueError:
            return json.dumps({'error': 'Invalid product_item_id or quantity'})

        shopping_cart = request.env['ctdonhang']
        order = None

        if user and user.id:  # Kiểm tra người dùng đăng nhập
            nhanvien_model = request.env['nhanvien']
            nhanvien = nhanvien_model.sudo().search([('user_id', '=', user.id)], limit=1)

            if nhanvien:  # Nếu người dùng là nhân viên
                order = request.env['donhang'].sudo().search([('id_nv', '=', nhanvien.id), ('state', '=', 'draft')],
                                                             limit=1)
                if not order:
                    order = request.env['donhang'].sudo().create(
                        {'id_nv': nhanvien.id, 'ngaytaodh': fields.Date.today()})

                cart_item = shopping_cart.sudo().search(
                    [('hoadon_id', '=', order.id), ('product_item_id', '=', product_item_id)])
                if cart_item:
                    cart_item.write({'quantity': cart_item.quantity + quantity})
                else:
                    shopping_cart.create({
                        'hoadon_id': order.id,
                        'product_item_id': product_item_id,
                        'quantity': quantity,
                        'id_nhanvien': request.env.user.id,
                    })
                return json.dumps({'success': True})
            else:
                return json.dumps({'error': 'User is not a valid employee'})
        else:
            return json.dumps({'error': 'User not logged in'})

    #
    # @http.route('/shop/cart', type='http', auth='public', website=True)
    # def shopping_cart_page(self, **kw):
    #     # Your logic to fetch cart data and pass it to the template
    #     cart_items = http.request.env['ctdonhang'].search(
    #         [])  # Replace 'shopping.cart' with the actual model name
    #
    #     cart_data = {
    #         'shopping_cart': cart_items,
    #     }
    #     return http.request.render('CTDonHang.website_shopping_cart_page', cart_data)
    @http.route('/shop/cart', type='http', auth='public', website=True)
    def shopping_cart_page(self, **kw):
        user = http.request.env.user

        # Fetch cart data based on user's logged in status
        if user and user.id:
            cart_items = http.request.env['ctdonhang'].sudo().search([
                ('hoadon_id.state', '=', 'draft'),  # Chỉ lấy các chi tiết đơn hàng ở trạng thái draft
                ('id_nhanvien', '=', user.id)
            ])
            order_state = 'draft'  # Đang ở trạng thái draft cho đơn hàng mới
        else:
            cart_items = http.request.env['ctdonhang'].search([])
            order_state = ''  # Không cần trạng thái nếu không có đơn hàng

        cart_data = {
            'shopping_cart': cart_items,
            'order_state': order_state,  # Truyền trạng thái đơn hàng vào template
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

    # ================================ đẩy lên model don hàng thông tin từ giỏ hàng
    @http.route('/clear_cart_on_order_confirm', type='json', auth='public', website=True)
    def clear_cart_on_order_confirm(self, order_id):
        order = request.env['donhang'].sudo().browse(order_id)
        if order.state == 'done':
            gio_hang = request.env['ctdonhang'].sudo().search([('id_nhanvien', '=', request.env.user.id)])
            gio_hang.sudo().unlink()  # Xoá giỏ hàng
            return {'success': True}
        else:
            return {'error': 'Order is not in "done" state'}




