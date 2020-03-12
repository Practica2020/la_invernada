# -*- coding: utf-8 -*-
from odoo import models, fields, api

class dimabe_health_care(models.Model):
     _name = 'dimabe_health_care.dimabe_health_care'

    
     most_severe_condition = fields.Char()

   
     description = fields.Text()
