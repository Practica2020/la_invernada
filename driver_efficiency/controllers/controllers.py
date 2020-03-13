# -*- coding: utf-8 -*-
from odoo import http

# class DimabeModifier(http.Controller):
#     @http.route('/dimabe_modifier/dimabe_modifier/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dimabe_modifier/dimabe_modifier/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dimabe_modifier.listing', {
#             'root': '/dimabe_modifier/dimabe_modifier',
#             'objects': http.request.env['dimabe_modifier.dimabe_modifier'].search([]),
#         })

#     @http.route('/dimabe_modifier/dimabe_modifier/objects/<model("dimabe_modifier.dimabe_modifier"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dimabe_modifier.object', {
#             'object': obj
#         })