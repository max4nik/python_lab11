from model.AbstractSemipreciousStone import AbstractSemiPreciousStone


class Pearl(AbstractSemiPreciousStone):

    def __init__(self, color: str = None, price_in_usd_dollars: float = None, country_of_origin: str = None,
                 chemical_formula: str = None,
                 weight_in_carats: float = None, transparency_from_zero_to_one: float = None,
                 special_semiprecious_stone_id: str = None):
        super().__init__(color, price_in_usd_dollars, country_of_origin, chemical_formula, weight_in_carats,
                         transparency_from_zero_to_one, special_semiprecious_stone_id)

    # def __repr__(self):
    #     dic = super().__repr__()
    #     return str(dic)
