from odoo import models, api, fields


class Modifier(models.Model):
    _inherit = 'stock.picking'


    starting_date = fields.Date(
         string='Inicio de actividades',
         default=fields.Date.context_today,
     )

     
    efficiency = fields.Float(
         string='Eficacia',
     )