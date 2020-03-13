# -*- coding: utf-8 -*-
from odoo import http

# class CoronavirusRegister(http.Controller):
#     @http.route('/coronavirus_register/coronavirus_register/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/coronavirus_register/coronavirus_register/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('coronavirus_register.listing', {
#             'root': '/coronavirus_register/coronavirus_register',
#             'objects': http.request.env['coronavirus_register.coronavirus_register'].search([]),
#         })

#     @http.route('/coronavirus_register/coronavirus_register/objects/<model("coronavirus_register.coronavirus_register"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('coronavirus_register.object', {
#             'object': obj
#         })