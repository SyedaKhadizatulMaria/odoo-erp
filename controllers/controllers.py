# -*- coding: utf-8 -*-
# from odoo import http


# class BjitErpTest(http.Controller):
#     @http.route('/bjit_erp_test/bjit_erp_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bjit_erp_test/bjit_erp_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bjit_erp_test.listing', {
#             'root': '/bjit_erp_test/bjit_erp_test',
#             'objects': http.request.env['bjit_erp_test.bjit_erp_test'].search([]),
#         })

#     @http.route('/bjit_erp_test/bjit_erp_test/objects/<model("bjit_erp_test.bjit_erp_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bjit_erp_test.object', {
#             'object': obj
#         })
