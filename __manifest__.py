{
    'name': 'POS Product Arrows Sortable Sequence',
    'version': '20.0.2.0.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Add top, bottom, up, and down arrows and bulk sorting to POS products & categories',
    'description': """
POS Product & Category Arrows Sortable Sequence (Odoo 20)
=========================================================
- Move products Up, Down, to Top, or to Bottom in the POS product list view.
- Automatically normalizes tied `pos_sequence` values so single-step arrows always move by 1 exact row.
- Bulk actions to sort selected POS products alphabetically, by price, or move them to top/bottom.
- Adds Up/Down/Top/Bottom sorting buttons to POS Categories (`pos.category`).
    """,
    'depends': ['point_of_sale'],
    'data': [
        'views/product_template_views.xml',
        'views/pos_category_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}