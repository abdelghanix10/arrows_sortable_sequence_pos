# POS Product Arrows Sortable Sequence (Odoo 20)

This Odoo 20 module enhances Point of Sale product and category management by adding intuitive **Move to Top**, **Move Up**, **Move Down**, and **Move to Bottom** buttons directly into the list views, along with bulk sorting actions.

## Features

- **Single-Step & Instant Jump Controls**:
  - **Move Up (`arrow_upward`) / Move Down (`arrow_downward`)**: Steps a product or POS category up or down by 1 exact row.
  - **Move to Top (`keyboard_double_arrow_up`) / Move to Bottom (`keyboard_double_arrow_down`)**: Jumps a product or category to the first or last position immediately.
- **Auto-Normalization of Tied Sequences**:
  - Automatically resolves duplicate `pos_sequence` values (such as when multiple products default to `0`) so single-step arrows never jump over tied items.
- **Bulk Sorting Server Actions**:
  - Select multiple products in the list view and open the **Action** menu to:
    - Move Selected to Top / Bottom
    - Sort Selected Alphabetically (A → Z)
    - Sort Selected by Price (Low → High)
    - Normalize All Sequences (10, 20, 30...)
- **POS Category Support**:
  - Also adds arrow buttons to **Point of Sale → Configuration → PoS Product Categories**.
- **Odoo 20 Material Symbols**:
  - Uses Odoo 20's Material Symbols ligature icons.

## License

LGPL-3