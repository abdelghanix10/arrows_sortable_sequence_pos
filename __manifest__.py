# -*- coding: utf-8 -*-
{
    'name': 'POS Product Arrows Sortable Sequence',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Add top and bottom arrows to sort products in POS list view',
    'description': """
This module adds arrows to the product list view in Point of Sale to allow easy sequencing.
    """,
    'depends': ['point_of_sale'],
    'data': [
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
