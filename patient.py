# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api, _


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Records'
    _rec_name = 'patient_name'
    # to add chatter to form view
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_name = fields.Char(string='Name', Required=True)
    patient_age = fields.Integer('Age')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')
    # copy=false means field's values shouldn't be copied when the records are duplicated
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    # overriding the create method to create sequence

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _("New")) == _("New"):
            # here hospital.patient.sequence <-- is the code in sequence.xml file
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _("New")
        result = super(HospitalPatient, self).create(vals)
        return result