from odoo import models, api


class PosCategory(models.Model):
    _inherit = 'pos.category'

    @api.model
    def _get_ordered_pos_categories(self):
        categories = self.search([], order='sequence asc, id asc')
        sequences = categories.mapped('sequence')
        if len(sequences) != len(set(sequences)):
            for idx, cat in enumerate(categories, start=1):
                if cat.sequence != idx:
                    cat.sequence = idx
        return categories

    def action_category_sequence_up(self):
        self.ensure_one()
        categories = self._get_ordered_pos_categories()
        cat_ids = categories.ids
        try:
            index = cat_ids.index(self.id)
            if index > 0:
                prev_cat = categories[index - 1]
                self.sequence, prev_cat.sequence = prev_cat.sequence, self.sequence
        except ValueError:
            pass
        return True

    def action_category_sequence_down(self):
        self.ensure_one()
        categories = self._get_ordered_pos_categories()
        cat_ids = categories.ids
        try:
            index = cat_ids.index(self.id)
            if index < len(cat_ids) - 1:
                next_cat = categories[index + 1]
                self.sequence, next_cat.sequence = next_cat.sequence, self.sequence
        except ValueError:
            pass
        return True

    def action_category_sequence_top(self):
        self.ensure_one()
        categories = self._get_ordered_pos_categories()
        if categories:
            self.sequence = min(categories.mapped('sequence')) - 1
        return True

    def action_category_sequence_bottom(self):
        self.ensure_one()
        categories = self._get_ordered_pos_categories()
        if categories:
            self.sequence = max(categories.mapped('sequence')) + 1
        return True