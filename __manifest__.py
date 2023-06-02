# -*- coding: utf-8 -*-
{
    "name" : "Support Pipeline",
    "author": "Jasmine",
    "summary" : "Support",
    'data': [
        'views/report.xml',
        'security/ir.model.access.csv',
        'data/main_template.xml',
    ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'depends':['base','board','mail','web','web_domain_field']
}