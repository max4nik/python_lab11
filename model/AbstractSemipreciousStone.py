from model.AbstractGemstone import AbstractGemstone


class AbstractSemiPreciousStone(AbstractGemstone):
    def __init__(self, color=None, price_in_usd_dollars=None, country_of_origin=None, chemical_formula=None,
                 weight_in_carats=None, transparency_from_zero_to_one=None, special_semiprecious_stone_id=None):
        super().__init__(color, price_in_usd_dollars, country_of_origin, chemical_formula, weight_in_carats,
                         transparency_from_zero_to_one)
        self.special_semiprecious_stone_id = special_semiprecious_stone_id

    # def __repr__(self):
    #     dic = super().__repr__()
    #     dic.update({"special_semiprecious_stone_id": self.special_semiprecious_stone_id})
    #     return dic
