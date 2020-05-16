# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Management',
    'version' : '12.0.1.0.0',
    'license' : 'AGPL-3',
    'summary': 'Module for managing the hospitals',
    'sequence': '15',

    'category': 'Extra Tools',
    'website': 'https://www.odoo.com/page/billing',

    'depends' : ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'patient.xml',
    ],
    'demo': [

    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}
