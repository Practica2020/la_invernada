# -*- coding: utf-8 -*-
from odoo import http

# class DimabeCvTracking(http.Controller):
#     @http.route('/dimabe_cv_tracking/dimabe_cv_tracking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dimabe_cv_tracking/dimabe_cv_tracking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dimabe_cv_tracking.listing', {
#             'root': '/dimabe_cv_tracking/dimabe_cv_tracking',
#             'objects': http.request.env['dimabe_cv_tracking.dimabe_cv_tracking'].search([]),
#         })

#     @http.route('/dimabe_cv_tracking/dimabe_cv_tracking/objects/<model("dimabe_cv_tracking.dimabe_cv_tracking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dimabe_cv_tracking.object', {
#             'object': obj
#         })