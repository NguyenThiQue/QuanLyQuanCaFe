from odoo import models, fields

class AccessControl(models.Model):
    _name = 'access_control'
    _description = 'Access Control'

    employee_id = fields.Many2one('nhanvien', string='Nhân viên', required=True)
    # model_id = fields.Many2one('ir.model', string='Model', required=True)
    read_access = fields.Boolean(string='Read Access')
    write_access = fields.Boolean(string='Write Access')
    create_access = fields.Boolean(string='Create Access')
    delete_access = fields.Boolean(string='Delete Access')
    model_id = fields.Many2one(
        'ir.model',
        string='Model',
        ondelete='cascade',  # Change 'restrict' to 'cascade' or another supported mode.
        required=True,
    )
