from model.abstract_precious_stone import AbstractPreciousStone


class Ruby(AbstractPreciousStone):

    def __init__(self, color=None, price_in_usd_dollars=None, country_of_origin=None, chemical_formula=None,
                 weight_in_carats=None, transparency_from_zero_to_one=None, special_precious_stone_id=None,
                 refractive_index=None):
        super().__init__(color, price_in_usd_dollars, country_of_origin, chemical_formula, weight_in_carats,
                         transparency_from_zero_to_one, special_precious_stone_id)
        self.refractive_index = refractive_index

