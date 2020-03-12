# -*- coding: utf-8 -*-
{
    'name': "dimabe_health_care",

    'summary': """
        Module created to keep a record of the health problems each person has.""",

    'description': """
        Module created to keep a record of the health problems each person has
    """,

    'author': "Dimabe",
    'website': "http://www.dimabe.cl/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'Contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/health_stock_picking.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}