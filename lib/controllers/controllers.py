# -*- coding: utf-8 -*-
from odoo import http

# class Lib(http.Controller):
#     @http.route('/lib/lib/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lib/lib/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lib.listing', {
#             'root': '/lib/lib',
#             'objects': http.request.env['lib.lib'].search([]),
#         })

#     @http.route('/lib/lib/objects/<model("lib.lib"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lib.object', {
#             'object': obj
#         })