# -*- coding: utf-8 -*-

from odoo import models, fields, api

class dimabe_health_care(models.Model):
     _name = 'dimabe_health_care.dimabe_health_care'

     name = fields.Char()
     most_severe_condition = fields.Char()
     emergency_contact = emergency_contact = fields.Many2one(
         string='emergency_contact',         
         comodel_name='res.partner'
         
     )
   
     description = fields.Text()
