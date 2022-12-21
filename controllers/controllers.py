# -*- coding: utf-8 -*-
# from odoo import http


# class Bypassprintview(http.Controller):
#     @http.route('/bypassprintview/bypassprintview', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bypassprintview/bypassprintview/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bypassprintview.listing', {
#             'root': '/bypassprintview/bypassprintview',
#             'objects': http.request.env['bypassprintview.bypassprintview'].search([]),
#         })

#     @http.route('/bypassprintview/bypassprintview/objects/<model("bypassprintview.bypassprintview"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bypassprintview.object', {
#             'object': obj
#         })
