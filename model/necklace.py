from model.abstract_gemstone import AbstractGemstone


class Necklace:

    def __init__(self, price_in_usd_dollars=None, all_weight_in_carats=None, necklace_length_in_meters=None,
                 amount_of_gems: int = None):
        self.price_in_usd_dollars = price_in_usd_dollars
        self.all_weight_in_carats = all_weight_in_carats
        self.necklace_length_in_meters = necklace_length_in_meters
        self.gemstones_in_lace = []
        self.amount_of_gems = amount_of_gems

    def add_gemstone(self, gemstone: AbstractGemstone):
        self.gemstones_in_lace.append(gemstone)
