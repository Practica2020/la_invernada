# -*- coding: utf-8 -*-
# noinspection PyStatementEffect
{
    'name': "My Library",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Dimabe ltda.",
    'website': "http://www.dimabe.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'purchase_requisition',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'stock',
        'mail',
        'purchase_requisition'
    ],

    # always loaded
    'data': [

     
    ],
    # only loaded in demonstration mode
    'demo': [
      
    ],
}