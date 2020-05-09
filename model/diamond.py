from model.abstract_precious_stone import AbstractPreciousStone
from model.chemical_type import ChemicalType


class Diamond(AbstractPreciousStone):

    def __init__(self, color=None, price_in_usd_dollars=None, country_of_origin=None, chemical_formula=None,
                 weight_in_carats=None, transparency_from_zero_to_one=None, special_precious_stone_id=None,
                 chemical_type: ChemicalType = None):
        super().__init__(color, price_in_usd_dollars, country_of_origin, chemical_formula, weight_in_carats,
                         transparency_from_zero_to_one, special_precious_stone_id)
        self.chemical_type = chemical_type
