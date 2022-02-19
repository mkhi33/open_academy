# -*- coding: utf-8 -*-

from email.policy import default
from importlib.metadata import files
import string
from odoo import models, fields, api


class open_academy(models.Model):
    _name = 'open_academy.session'
    _description = 'Sesion'

    name = fields.Char()
    start_date = fields.Date( default= fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer()
    active = fields.Boolean(default=True)

    instructor_id = fields.Many2one('res.partner', string="Instructor", domain=[('instructor', '=', True),('category_id.name', 'ilike', 'Teacher')])
    course_id = fields.Many2one('open_academy.course', ondelete="cascade", string="Curso", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    taken_seats = fields.Float(string="Taken Seats", compute="_taken_seats" )
    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for item in self:
            if not item.seats:
                item.taken_seats = 0.0
            else:
                item.taken_seats = 100.0 * len(item.attendee_ids) / item.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if( self.seats < 0 ):
            return {
                    'warning': {
                        'title': "Incorrect 'seats' value",
                        'message': "The number of available seats may not be negative",
                    },
            }
        if( self.seats < len(self.attendee_ids)):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }