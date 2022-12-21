# -*- coding: utf-8 -*-
{
    'name': "fiscal",

    'summary': """
        Zambian compliant fiscal receipts""",

    'description': """
        This module extends the POS module to allow
        printing of RevMax compliant fiscal receipts
    """,

    'author': "Rashid Designs",
    'website': "assanisaidi73@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/point_of_sale.assets_common.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_qweb': [
          "fiscal/static/src/xml/pos.xml"
        ],
    }
}
