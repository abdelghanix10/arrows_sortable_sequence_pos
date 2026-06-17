# POS Product Arrows Sortable Sequence

This Odoo 19 module enhances the Point of Sale product management by adding intuitive "Up" and "Down" arrows to the product list view.

## Features

- **Sequential Control**: Easily move products up or down in the list to change their display order in the POS terminal.
- **Visual Feedback**: Uses standard Odoo icons (`oi-arrow-up`, `oi-arrow-down`) for a seamless UI experience.
- **POS Integration**: Inherit directly from the `point_of_sale.product_template_tree_view_point_of_sale` view.

## Installation

1. Copy the `arrows_sortable_sequence_pos` folder to your Odoo addons directory.
2. Restart your Odoo server.
3. Enable developer mode in Odoo.
4. Go to **Apps** -> **Update Apps List**.
5. Search for `POS Product Arrows Sortable Sequence` and click **Install**.

## Usage

1. Navigate to **Point of Sale** -> **Configuration** -> **Products**.
2. Switch to the List view (if not already there).
3. Use the arrows on the left side of each product row to adjust its position.

## Technical Details

- **Model**: Inherits `product.template`.
- **Fields**: Manipulates the `pos_sequence` field used by the Point of Sale module.
- **Methods**:
  - `action_pos_sequence_up()`: Swaps sequence with the preceding product.
  - `action_pos_sequence_down()`: Swaps sequence with the following product.

## License

LGPL-3
