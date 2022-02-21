from odoo import fields, models, _
class Partner(models.Model):
    _inherit = 'res.partner'
    instructor = fields.Boolean("Instructor", default=False)
    session_partner = fields.Many2many('open_academy.session', string="Attended Sessions", readonly=True)
