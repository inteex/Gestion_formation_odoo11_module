# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class Session(models.Model):
    _name = "session"
    _description = "c'est une session looool"

    name = fields.Char()
    nb_participant = fields.Integer()
    date_debut = fields.Date()
    date_fin = fields.Date()
    duree = fields.Char()
    state = fields.Selection([('a', 'A'), ('b', 'B')])
    formationId = fields.Many2one('formation.formation', ondelete="cascade")
    salle = fields.Many2many('formation.salle')
    candidat = fields.Many2many('formation.candidat')
    formateur = fields.Many2many('formation.formateur')