# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class Formateur(models.Model):
	_name="formation.formateur"
	_description="formateur"

	name = fields.Char()
	matricule = fields.Integer()
	diplome = fields.Char()
	session = fields.Many2many('session')
