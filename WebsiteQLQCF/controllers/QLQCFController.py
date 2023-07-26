from odoo import http
from odoo.http import request
class Test(http.Controller):
    @http.route('/loginsp', auth='public')
    # def index(self, **kw):
    #     return request.render('WebsiteQLQCF.login_id', {
    #         'html':"""
    #             <div>
    #                  <link href="/WebsiteQLQCF/static/src/css/bootstrap.css" rel="stylesheet" type="text/css"/>
    #             <div>
    #         """
    #     })
    class MyController(http.Controller):
        @http.route('/module_name/hello', auth='public', type='http')
        def hello(self):
            return {
                'html': """
                    <div>
                        <link href="/WebsiteQLQCF/static/src/css/bootstrap.css" rel="stylesheet">
                        <h1>hello, world</h1>
                    </div> """
            }