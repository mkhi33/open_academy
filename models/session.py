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
