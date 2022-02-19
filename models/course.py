# -*- coding: utf-8 -*-

from odoo import models, fields, api


class open_academy(models.Model):
    _name = 'open_academy.course'
    _description = 'Course'

    name = fields.Char(string='Course')
    title = fields.Char(string='title')
    description = fields.Text(string='Description')

    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsable", index=True)
    
    session_ids = fields.One2many('open_academy.session', 'course_id', string='Sessions')

    _sql_constraints = [
        ('name_description_check', 'CHECK(name != description)', 'El titulo del curso debe ser diferente a la descripción'),
        ('name_unique', 'UNIQUE(name)', 'El titulo del curso debe ser único' )
    ]