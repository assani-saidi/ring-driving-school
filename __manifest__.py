# -*- coding: utf-8 -*-
{
    'name': "order.pos name on receipt",

    'summary': """
        This module allows you to reference the pos.order name on the receipt and some extra fields""",

    'description': """
        This module allows you to reference the pos.order name on the receipt. It can 
        be used with the booking module. It has been coupled with ring contacts also.
    """,

    'author': "Rashid Designs",
    'website': "assanisaidi73@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_qweb': [
            "booking-ref-receipt/static/src/xml/pos.xml",
            # "booking-ref-receipt/static/src/xml/point.xml",
        ],
    },
}
