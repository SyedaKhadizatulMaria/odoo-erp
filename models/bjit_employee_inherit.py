from odoo import models, fields, api


class BjitEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = 'Employee'

    employee_language_line = fields.One2many('bjit.employee.language', 'language_id', string="Language")


class BjitEmployeeLanguage(models.Model):
    _name = 'bjit.employee.language'
    _description = 'Language Skill'

    employee_language = fields.Selection([('bangla', 'Bangla'),
                                          ('english', 'English'),
                                          ('japanese', 'Japanese')
                                          ], string="Language")
    language_id = fields.Many2one('hr.employee', string="Language")
    language_history_line = fields.One2many('bjit.employee.language.history', 'language_history_id',
                                            string='Language History')


class BjitEmployeeLanguageHistory(models.Model):
    _name = 'bjit.employee.language.history'
    _description = 'Language History'

    language_type = fields.Selection([('read', 'Read'),
                                      ('write', 'Write'),
                                      ('talk', 'Talk')])
    grade_level = fields.Selection([('a_grade', 'A'),
                                    ('b_grade', 'B'),
                                    ('c_grade', 'C'),
                                    ('d_grade', 'D')
                                    ])
    language_history_id = fields.Many2one('bjit.employee.language', string="Language History")
