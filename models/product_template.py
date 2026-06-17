# -*- coding: utf-8 -*-
from odoo import models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_pos_sequence_up(self):
        self.ensure_one()
        # Search for products available in POS, ordered by pos_sequence
        # We use the same ordering as the POS product list view
        domain = [('available_in_pos', '=', True)]
        # If we are in a specific category context, we might want to follow that, 
        # but pos_sequence is global for POS.
        products = self.search(domain, order='pos_sequence asc, id asc')
        product_ids = products.ids
        try:
            index = product_ids.index(self.id)
            if index > 0:
                previous_product = products[index - 1]
                # Swap sequences
                current_seq = self.pos_sequence
                prev_seq = previous_product.pos_sequence
                
                if current_seq == prev_seq:
                    self.pos_sequence = prev_seq - 1
                else:
                    self.pos_sequence = prev_seq
                    previous_product.pos_sequence = current_seq
        except ValueError:
            pass
        return True

    def action_pos_sequence_down(self):
        self.ensure_one()
        domain = [('available_in_pos', '=', True)]
        products = self.search(domain, order='pos_sequence asc, id asc')
        product_ids = products.ids
        try:
            index = product_ids.index(self.id)
            if index < len(product_ids) - 1:
                next_product = products[index + 1]
                # Swap sequences
                current_seq = self.pos_sequence
                next_seq = next_product.pos_sequence
                
                if current_seq == next_seq:
                    self.pos_sequence = next_seq + 1
                else:
                    self.pos_sequence = next_seq
                    next_product.pos_sequence = current_seq
        except ValueError:
            pass
        return True
