# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Gestion de formation',
    'version': '0.1',
    'author': 'reda mekhezzem',
    'category': 'premier module',
    'description': "Ceci est mon prmier module du tp n_3",
    'depends': ['project'],
    'installable': True,
    'application': True,
    'data': [
             'security/ir.model.access.csv',
             'security/users.xml',
             'views/formation.xml',
             'wizard/wizard_attestation.xml',
             'views/session.xml',
             'views/salle.xml',
             'views/formateur.xml',
             'views/candidat.xml',
             'report/attestation_report.xml',
             'views/attestation.xml'
             ],
    'website' :'www.modulen1.com',
    'license' : 'GPL-2',
}
