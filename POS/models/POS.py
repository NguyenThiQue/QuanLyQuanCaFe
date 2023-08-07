from odoo import models, fields, api
class POS(models.Model):
    _name = "pos"
    name = fields.Char(string="Name")