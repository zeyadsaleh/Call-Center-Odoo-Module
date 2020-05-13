# -*- coding: utf-8 -*-
# from odoo import http


# class CallCenter(http.Controller):
#     @http.route('/call__center/call__center/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/call__center/call__center/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('call__center.listing', {
#             'root': '/call__center/call__center',
#             'objects': http.request.env['call__center.call__center'].search([]),
#         })

#     @http.route('/call__center/call__center/objects/<model("call__center.call__center"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('call__center.object', {
#             'object': obj
#         })
