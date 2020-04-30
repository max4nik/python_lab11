import doctest

from model.Diamond import Diamond
from model.Necklace import Necklace
from model.Pearl import Pearl


class GemstoneInNecklaceManager:

    @staticmethod
    def find_gemstones_with_transparency_between(necklace: Necklace, minimal_transparency: float,
                                                 maximal_transparency: float):
        """
        >>> necklace = Necklace()
        >>> diamond = Diamond(transparency_from_zero_to_one=0.65)
        >>> pearl = Pearl(transparency_from_zero_to_one=0.8)
        >>> pearl1 = Pearl(transparency_from_zero_to_one=0.2)
        >>> necklace.add_gemstone(diamond)
        >>> necklace.add_gemstone(pearl)
        >>> necklace.add_gemstone(pearl1)
        >>> len(GemstoneInNecklaceManager.find_gemstones_with_transparency_between(necklace, 0.5, 0.7))
        1
        """
        result = []
        for gemstone in necklace.gemstones_in_lace:
            if minimal_transparency <= gemstone.transparency_from_zero_to_one <= maximal_transparency:
                result.append(gemstone)
        return result


if __name__ == '__main__':
    doctest.testmod(verbose=True)
