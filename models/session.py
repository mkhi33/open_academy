# -*- coding: utf-8 -*-

from ast import Store
from datetime import timedelta
from email.policy import default
from importlib.metadata import files
import string
from odoo import models, fields, api, exceptions, _

class open_academy(models.Model):
    _name = 'open_academy.session'
    _description = 'Sesion'

    name = fields.Char()
    start_date = fields.Date( default= fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer()
    active = fields.Boolean(default=True)
    color = fields.Integer()

    instructor_id = fields.Many2one('res.partner', string="Instructor", domain=[('instructor', '=', True),('category_id.name', 'ilike', 'Teacher')])
    course_id = fields.Many2one('open_academy.course', ondelete="cascade", string="Curso", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    taken_seats = fields.Float(string="Taken Seats", compute="_taken_seats" )

    end_date = fields.Date(string="End Date", Store=True, compute="_get_end_date", inverse="_set_end_date")

    attendees_count = fields.Integer( string="Número de asistentes", compute="_get_attendees_count", store=True)

   

    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for item in self:
            item.attendees_count = len(item.attendee_ids)
    
    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for item in self:
            if not (item.start_date and item.duration):
                item.end_date = item.start_date
                continue
            start = fields.Datetime.from_string(item.start_date)
            duration = timedelta(days=item.duration, seconds=-1)
            item.end_date = start + duration
    
    def _set_end_date(self):
        for item in self:
            if not (item.start_date and item.end_date):
                continue
            start_date = fields.Datetime.from_string(item.start_date)
            end_date = fields.Datetime.from_string(item.end_date)
            item.duration = (end_date - start_date).days + 1


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
                        'title': _("Incorrect 'seats' value"),
                        'message': _("The number of available seats may not be negative"),
                    },
            }
        if( self.seats < len(self.attendee_ids)):
            return {
                'warning': {
                    'title': _("Too many attendees"),
                    'message': _("Increase seats or remove excess attendees"),
                },
            }
    
    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for item in self:
            if item.instructor_id and (item.instructor_id in item.attendee_ids):
                raise exceptions.ValidationError(_("Error: A session's instructor can't be an attendee"))