from odoo import api,fields,models, _
from datetime import datetime


class Wizard_attestation(models.TransientModel):
    _name="foramtion.wizard_attestation"

    date=fields.Date()
    description=fields.Text()

    @api.multi
    def action_done(self):
        session_id = self.env.context.get('active_id')
        session = self.env['session'].browse(session_id)
        for candidat in session.candidat_ids:
            self.env['formation.attestation'].create({
                'date' : self.date,
                'description' : self.description,
                'candidat' : candidat.id,
                'formation' : session.formationId.id,
            })

