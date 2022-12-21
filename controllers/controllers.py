# -*- coding: utf-8 -*-
# from odoo import http


# class Fiscal(http.Controller):
#     @http.route('/fiscal/fiscal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fiscal/fiscal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fiscal.listing', {
#             'root': '/fiscal/fiscal',
#             'objects': http.request.env['fiscal.fiscal'].search([]),
#         })

#     @http.route('/fiscal/fiscal/objects/<model("fiscal.fiscal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fiscal.object', {
#             'object': obj
#         })
