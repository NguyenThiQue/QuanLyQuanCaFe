import hashlib
import uuid

import bcrypt
from werkzeug.utils import redirect

from odoo import http, _
from odoo.exceptions import AccessDenied
from odoo.http import request


class LoginController(http.Controller):
#
#     # @http.route('/login', type='http', auth='public', website=True, csrf=False)
#     # def login(self, **kw):
#     #     if kw.get('username') and kw.get('password'):
#     #         username = kw.get('username')
#     #         password = kw.get('password')
#     #         nhanvien = request.env['nhanvien'].sudo().search([('username', '=', username)])
#     #         if nhanvien and nhanvien.password == password:
#     #             # Xử lý đăng nhập thành công (ví dụ: tạo phiên làm việc, chuyển hướng, ...)
#     #             return request.redirect('http://localhost:8069/web/')
#     #
#     #         else:
#     #             # Xử lý đăng nhập thất bại (ví dụ: hiển thị thông báo lỗi)
#     #             return "Invalid username or password!"
#     #     else:
#     #         # Hiển thị form đăng nhập nếu không có thông tin đăng nhập được gửi lên
#     #         return """<form method="post">
#     #                     Username: <input type="text" name="username" required><br>
#     #                     Password: <input type="password" name="password" required><br>
#     #                     <input type="submit" value="Login">
#     #                 </form>"""
#     #
#     # @http.route('/logout', type='http', auth='user', website=True)
#     # def logout(self, **kw):
#     #     request.session.logout()
#     #     return "Logged out successfully!"
#



    @http.route('/web/login', type='http', auth='public', website=True)
    def web_login(self, **kw):
        return http.request.render('NhanVien.login_template', {})

    @http.route('/nhanvien/login', type='http', auth='public', website=True, csrf=False)
    def nhanvien_login(self, **kw):
        username = kw.get('username')
        password = kw.get('password')

        nhanvien = http.request.env['nhanvien'].sudo().search([('username', '=', username)], limit=1)

        if not nhanvien or not nhanvien.password == password:
            return http.request.render('NhanVien.login_template', {'error': 'Thông tin không hợp lệ'})

        try:
            request.session.authenticate(http.request.session.db, nhanvien.user_id.login, password)
        except AccessDenied:
            return http.request.render('NhanVien.login_template', {'error': ' Bạn không có quyền truy cập'})

        return redirect('/web')


    @http.route('/web/logout', type='http', auth="user")
    def logout(self, redirect='/web'):

        return super(LoginController, self).logout(redirect=redirect)

