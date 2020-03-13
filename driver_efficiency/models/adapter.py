from odoo import models, api, fields
from datetime import datetime, timedelta


class Adapter(models.Model):
    _inherit = 'stock.picking'
    _order = 'date desc'

    
    starting_date = fields.Date(
         string='Inicio de actividades',
         default=fields.Date.context_today,
     )

     
    efficiency = fields.Float(
         string='Eficacia',
     )
     
