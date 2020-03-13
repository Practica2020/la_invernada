# -*- coding: utf-8 -*-
from odoo import http

# class Fireworks(http.Controller):
#     @http.route('/fireworks/fireworks/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fireworks/fireworks/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fireworks.listing', {
#             'root': '/fireworks/fireworks',
#             'objects': http.request.env['fireworks.fireworks'].search([]),
#         })

#     @http.route('/fireworks/fireworks/objects/<model("fireworks.fireworks"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fireworks.object', {
#             'object': obj
#         })