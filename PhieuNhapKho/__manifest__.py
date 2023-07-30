# -*- coding: utf-8 -*-
{
    'name': "QuanLyQuanCaPhe",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/PhieuNhapKho',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'SanPham','Kho'],

    # always loaded
    'data': [

        'security/phieunhapkho_security.xml',
        'security/ir.model.access.csv',

        "views/phieunhapkho.xml",

    ],
    'sequence':1,
    'application': True,
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
