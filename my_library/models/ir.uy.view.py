from odoo import models, fields

class View(models.Model):
    _inherit = 'ir.ui.view'
    type = fields.Selection(selection_add=[('m2m_group', 'M2m Group')])