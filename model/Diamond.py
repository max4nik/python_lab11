from model.AbstractPreciousStone import AbstractPreciousStone
from model.ChemicalType import ChemicalType


class Diamond(AbstractPreciousStone):

    def __init__(self, color=None, price_in_usd_dollars=None, country_of_origin=None, chemical_formula=None,
                 weight_in_carats=None, transparency_from_zero_to_one=None, special_precious_stone_id=None,
                 chemical_type: ChemicalType = None):
        super().__init__(color, price_in_usd_dollars, country_of_origin, chemical_formula, weight_in_carats,
                         transparency_from_zero_to_one, special_precious_stone_id)
        self.chemical_type = chemical_type

    # def __repr__(self):
    #     dic = super().__repr__()
    #     dic.update({"chemical_type": self.chemical_type})
    #     return str(dic)
