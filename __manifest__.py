# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'product warranty',
    'version' : 'v1.0',
    'summary': 'this app for everyone',
    'sequence': 10,
    'description': """ Alien Software""",
    'category': 'productivity',
    'website': '',
    'images': [],
    'author': "Chau Nguyen",
    'depends': ['sale', 'base'],
    'data': [
        'views/produc_warranty_view.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/templates.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}