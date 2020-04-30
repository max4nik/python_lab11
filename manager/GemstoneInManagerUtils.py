import doctest

from model.Diamond import Diamond
from model.Necklace import Necklace
from model.Pearl import Pearl
from model.TypeOfSorting import TypeOfSorting


class GemstoneInNecklaceManagerUtils:

    @staticmethod
    def sort_gemstones_in_necklaces_by_all_weight_in_carats(necklace: Necklace, type_of_sorting: TypeOfSorting):
        """
        >>> necklace = Necklace()
        >>> diamond = Diamond(weight_in_carats=0.65)
        >>> pearl = Pearl(weight_in_carats=0.8)
        >>> pearl1 = Pearl(weight_in_carats=0.2)
        >>> necklace.add_gemstone(diamond)
        >>> necklace.add_gemstone(pearl)
        >>> necklace.add_gemstone(pearl1)
        >>> gems_desc = GemstoneInNecklaceManagerUtils.sort_gemstones_in_necklaces_by_all_weight_in_carats(necklace, TypeOfSorting.DESCENDING.value)
        >>> for gem in gems_desc: print(gem.weight_in_carats)
        0.8
        0.65
        0.2
        >>> gems_asc = GemstoneInNecklaceManagerUtils.sort_gemstones_in_necklaces_by_all_weight_in_carats(necklace, TypeOfSorting.ASCENDING.value)
        >>> for gem in gems_asc: print(gem.weight_in_carats)
        0.2
        0.65
        0.8
        """
        sorted_necklaces = sorted(necklace.gemstones_in_lace, key=lambda gem: gem.weight_in_carats)
        if type_of_sorting == TypeOfSorting.ASCENDING.value:
            return sorted_necklaces
        elif type_of_sorting == TypeOfSorting.DESCENDING.value:
            return sorted_necklaces[::-1]
        else:
            return sorted_necklaces

    @staticmethod
    def sort_gemstones_in_necklaces_by_price_in_usd_dollars(necklace: Necklace, type_of_sorting: TypeOfSorting):
        """
        >>> necklace = Necklace()
        >>> diamond = Diamond(price_in_usd_dollars=100)
        >>> pearl = Pearl(price_in_usd_dollars=50)
        >>> pearl1 = Pearl(price_in_usd_dollars=75)
        >>> necklace.add_gemstone(diamond)
        >>> necklace.add_gemstone(pearl)
        >>> necklace.add_gemstone(pearl1)
        >>> gems_desc = GemstoneInNecklaceManagerUtils.sort_gemstones_in_necklaces_by_price_in_usd_dollars(necklace, TypeOfSorting.DESCENDING.value)
        >>> for gem in gems_desc: print(gem.price_in_usd_dollars)
        100
        75
        50
        >>> gems_asc = GemstoneInNecklaceManagerUtils.sort_gemstones_in_necklaces_by_price_in_usd_dollars(necklace, TypeOfSorting.ASCENDING.value)
        >>> for gem in gems_asc: print(gem.price_in_usd_dollars)
        50
        75
        100
        """
        sorted_necklaces = sorted(necklace.gemstones_in_lace, key=lambda gem: gem.price_in_usd_dollars)
        if type_of_sorting == TypeOfSorting.ASCENDING.value:
            return sorted_necklaces
        elif type_of_sorting == TypeOfSorting.DESCENDING.value:
            return sorted_necklaces[::-1]
        else:
            return sorted_necklaces


if __name__ == '__main__':
    doctest.testmod(verbose=True)
