# -*- coding: utf-8 -*-
from odoo import models, fields, api

class qualification(models.Model):
     _name = 'qualification'
     _inherit = 'stock.picking'


     starting_date = fields.Date(
         string='Inicio de actividades',
         default=fields.Date.context_today,
     )

     
     efficiency = fields.Float(
         string='Eficacia',
     )
     


     
