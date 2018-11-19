# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class Candidat(models.Model):
    _name = "formation.candidat"
    _description = "candidat"

    name = fields.Char()
    num_ins = fields.Integer()
    session = fields.Many2many('formation.session')
