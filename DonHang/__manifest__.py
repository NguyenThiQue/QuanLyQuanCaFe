# -*- coding: utf-8 -*-
{
    'name': "QuanLyQuanCaPhe",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Coffee shop",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/DonHang',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'NhanVien', 'SanPham', 'CTDonHang', 'KhachHang', 'Kho'],

    # always loaded
    'data': [

        'security/donhang_security.xml',
        'security/ir.model.access.csv',

        "views/donhang.xml",
        "reports/donhang_card.xml",
        "reports/report.xml",
        # "reports/sale_report_inherit.xml",

    ],
    'sequence':1,
    'application': True,
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
