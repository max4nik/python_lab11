from model.abstract_semiprecious_stone import AbstractSemiPreciousStone


class Nephrite(AbstractSemiPreciousStone):
    impurities = []

    def __init__(self, color=None, price_in_usd_dollars=None, country_of_origin=None, chemical_formula=None,
                 weight_in_carats=None, transparency_from_zero_to_one=None, special_semiprecious_stone_id=None,
                 impurities=None):
        super().__init__(color, price_in_usd_dollars, country_of_origin, chemical_formula, weight_in_carats,
                         transparency_from_zero_to_one, special_semiprecious_stone_id)
        self.impurities = impurities
