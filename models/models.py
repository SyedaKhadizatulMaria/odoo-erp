# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class bjit_erp_test(models.Model):
#     _name = 'bjit_erp_test.bjit_erp_test'
#     _description = 'bjit_erp_test.bjit_erp_test'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
