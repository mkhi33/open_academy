# -*- coding: utf-8 -*-
from email.policy import default
from odoo import models, fields, api
class Wizard(models.TransientModel):
    _name = "open_academy.wizard"

    def _default_session(self):
        return self.env['open_academy.session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2many('open_academy.session', string="Sessions", required=True, default=_default_session)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids

        return {}