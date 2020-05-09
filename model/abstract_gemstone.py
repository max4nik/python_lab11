class AbstractGemstone:

    def __init__(self, color=None, price_in_usd_dollars=None, country_of_origin=None,
                 chemical_formula=None, weight_in_carats=None, transparency_from_zero_to_one=None):
        self.color = color
        self.price_in_usd_dollars = price_in_usd_dollars
        self.country_of_origin = country_of_origin
        self.chemical_formula = chemical_formula
        self.weight_in_carats = weight_in_carats
        self.transparency_from_zero_to_one = transparency_from_zero_to_one

    def __del__(self):
        print(self.__class__.__name__ + " deleted")
