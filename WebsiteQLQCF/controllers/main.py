from odoo import http, _
from odoo.http import request
from odoo.addons.http_routing.models.ir_http import unslug
import uuid

class Main(http.Controller):



    @http.route('/web/login', type='http', auth='public', website=True)
    def web_login(self, redirect_url=None, **kw):
        if request.httprequest.method == 'POST':
            login = kw.get('login')
            password = kw.get('password')

            # Custom authentication using the nhanvien model
            user = request.env['nhanvien'].sudo().search([('username', '=', login)])
            if user and user.password == password:
                # Đăng nhập thành công, chuyển hướng đến trang chủ
                print("Đăng nhập thành công")
                # Lưu thông tin nhân viên đã đăng nhập vào session
                request.session.uid = user.id

                # Generate a unique session token and set it
                request.session.session_token = str(uuid.uuid4())

                if user.is_admin:
                    # Redirect to admin dashboard or specific admin page
                    return http.request.redirect('/sanpham')
                else:
                    # Redirect to regular employee dashboard or specific employee page
                    return http.request.redirect('/web/database/selector')

                # return http.request.redirect('/web')
            else:
                # Đăng nhập thất bại, hiển thị thông báo lỗi
                return http.request.render('web.login', {'error': _('Invalid username or password')})

        return http.request.render('web.login', {'redirect': redirect_url})

    @http.route('/web/logout', type='http', auth='user', website=True)
    def web_logout(self, redirect_url=None, **kw):
        # Clear the user-specific session data
        request.session.logout()
        return http.request.redirect('/web/login')



