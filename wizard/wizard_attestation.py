from odoo import api,fields,models, _
from datetime import datetime


class Wizard_attestation(models.TransientModel):
    _name="foramtion.wizard_attestation"

    date=fields.Date()
    description=fields.Text()

    def action_done(self):
        print('cc')