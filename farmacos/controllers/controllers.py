# -*- coding: utf-8 -*-
from odoo import http

 class Farmacos(http.Controller):
     @http.route('/farmacos/farmacos/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/farmacos/farmacos/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('farmacos.listing', {
             'root': '/farmacos/farmacos',
             'objects': http.request.env['farmacos.farmacos'].search([]),
         })

     @http.route('/farmacos/farmacos/objects/<model("farmacos.farmacos"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('farmacos.object', {
             'object': obj
         })