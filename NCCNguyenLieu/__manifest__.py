# -*- coding: utf-8 -*-
{
    'name': "QuanLyQuanCaPhe",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'sequence':2,
    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/NCCNguyenLieu',
    'version': '16.0.0.1',

    'depends': ['base'],

    # always loaded
    'data': [

        'security/nccnguyenlieu_security.xml',
        'security/ir.model.access.csv',
        "views/nccnguyenlieu.xml",

    ],
    'application': True,

    'demo': [
    ],
}
