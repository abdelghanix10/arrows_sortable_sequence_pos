from odoo import models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def _get_ordered_pos_products(self):
        """Return all POS-enabled products in the exact order displayed in the POS list view."""
        products = self.search(
            [('available_in_pos', '=', True)],
            order='pos_sequence asc, id asc',
        )
        # If duplicate pos_sequence values exist (e.g. multiple products at 0),
        # normalize them first so adjacent swaps always move by 1 exact row.
        sequences = products.mapped('pos_sequence')
        if len(sequences) != len(set(sequences)):
            for idx, prod in enumerate(products, start=1):
                if prod.pos_sequence != idx:
                    prod.pos_sequence = idx
        return products

    def action_pos_sequence_up(self):
        """Move product up by 1 position in the POS sequence."""
        self.ensure_one()
        products = self._get_ordered_pos_products()
        product_ids = products.ids
        try:
            index = product_ids.index(self.id)
            if index > 0:
                previous_product = products[index - 1]
                current_seq = self.pos_sequence
                prev_seq = previous_product.pos_sequence
                self.pos_sequence = prev_seq
                previous_product.pos_sequence = current_seq
        except ValueError:
            pass
        return True

    def action_pos_sequence_down(self):
        """Move product down by 1 position in the POS sequence."""
        self.ensure_one()
        products = self._get_ordered_pos_products()
        product_ids = products.ids
        try:
            index = product_ids.index(self.id)
            if index < len(product_ids) - 1:
                next_product = products[index + 1]
                current_seq = self.pos_sequence
                next_seq = next_product.pos_sequence
                self.pos_sequence = next_seq
                next_product.pos_sequence = current_seq
        except ValueError:
            pass
        return True

    def action_pos_sequence_top(self):
        """Move product(s) to the very top of the POS sequence."""
        products = self._get_ordered_pos_products()
        if not products:
            return True
        min_seq = min(products.mapped('pos_sequence'))
        # Preserve relative order if multiple records are selected
        selected_ordered = products.filtered(lambda p: p.id in self.ids)
        offset = len(selected_ordered)
        for idx, prod in enumerate(selected_ordered):
            prod.pos_sequence = min_seq - offset + idx
        return True

    def action_pos_sequence_bottom(self):
        """Move product(s) to the very bottom of the POS sequence."""
        products = self._get_ordered_pos_products()
        if not products:
            return True
        max_seq = max(products.mapped('pos_sequence'))
        selected_ordered = products.filtered(lambda p: p.id in self.ids)
        for idx, prod in enumerate(selected_ordered, start=1):
            prod.pos_sequence = max_seq + idx
        return True

    def action_pos_sequence_sort_alpha(self):
        """Bulk Action: Sort selected products alphabetically (A -> Z) within their current sequence slots."""
        if len(self) < 2:
            return True
        self._get_ordered_pos_products()
        current_slots = sorted(self.mapped('pos_sequence'))
        sorted_by_name = self.sorted(key=lambda p: (p.name or '').lower())
        for prod, seq_val in zip(sorted_by_name, current_slots):
            prod.pos_sequence = seq_val
        return True

    def action_pos_sequence_sort_price(self):
        """Bulk Action: Sort selected products by Sales Price (Low -> High) within their current sequence slots."""
        if len(self) < 2:
            return True
        self._get_ordered_pos_products()
        current_slots = sorted(self.mapped('pos_sequence'))
        sorted_by_price = self.sorted(key=lambda p: (p.list_price or 0.0, (p.name or '').lower()))
        for prod, seq_val in zip(sorted_by_price, current_slots):
            prod.pos_sequence = seq_val
        return True

    def action_pos_sequence_normalize_step10(self):
        """Bulk Action: Reset and normalize all POS products to clean steps of 10 (10, 20, 30...)."""
        products = self.search(
            [('available_in_pos', '=', True)],
            order='pos_sequence asc, id asc',
        )
        for idx, prod in enumerate(products, start=1):
            prod.pos_sequence = idx * 10
        return True