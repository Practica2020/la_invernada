# -*- coding: utf-8 -*-
from odoo import http

# class DimabeHealthCare(http.Controller):
#     @http.route('/dimabe_health_care/dimabe_health_care/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dimabe_health_care/dimabe_health_care/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dimabe_health_care.listing', {
#             'root': '/dimabe_health_care/dimabe_health_care',
#             'objects': http.request.env['dimabe_health_care.dimabe_health_care'].search([]),
#         })

#     @http.route('/dimabe_health_care/dimabe_health_care/objects/<model("dimabe_health_care.dimabe_health_care"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dimabe_health_care.object', {
#             'object': obj
#         })