# -*- coding: utf-8 -*-

import string
from odoo import models, fields, api


class open_academy(models.Model):
    _name = 'open_academy.session'
    _description = 'Sesion'

    name = fields.Char()
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer()

    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('open_academy.course', ondelete="cascade", string="Curso", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
