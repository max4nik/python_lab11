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

    # def __repr__(self):
    #     return {
    #         'color': self.color,
    #         'price_in_usd_dollars': self.price_in_usd_dollars,
    #         'country_of_origin': self.country_of_origin,
    #         'chemical_formula': self.chemical_formula,
    #         'weight_in_carats': self.weight_in_carats,
    #         'transparency_from_zero_to_one': self.transparency_from_zero_to_one
    #     }

    # def __str__(self):
    #     return '\nColor: ' + str(self.color) + \
    #            '\nPrice in USD: ' + str(self.price_in_usd_dollars) + \
    #            '\nCountry of origin: ' + str(self.country_of_origin) + \
    #            '\nChemical formula: ' + str(self.chemical_formula) + \
    #            '\nWeight in carats: ' + str(self.weight_in_carats) + \
    #            '\nTransparency: ' + str(self.transparency_from_zero_to_one)
