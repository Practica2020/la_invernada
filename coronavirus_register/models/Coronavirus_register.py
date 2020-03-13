# -*- coding: utf-8 -*-

from odoo import models, fields, api

class coronavirus_register(models.Model):
     _name = 'coronavirus_register'

     
     afflicted_contact = fields.Many2one(
         string='afflicted_contact',         
         comodel_name='res.partner',
     )
     
     call_in_sick_date = fields.Date(
         string='call_in_sick_date',
         default=fields.Date.context_today,
     )

     
     observations = fields.Text(
         string='observations',
     )
     
     

