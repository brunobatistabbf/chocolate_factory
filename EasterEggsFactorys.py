from IEasterEggs import IEasterEggs
from IProductFactory import IEasterEggProduct
from ProductEasterEggs import Alpino, Crocante, AoLeite

class NestleFactory(IEasterEggs):
    def EasterEgg(self) -> IEasterEggProduct:
        return Alpino()

class GarotoFactory(IEasterEggs):
    def EasterEgg(self) -> IEasterEggProduct:
        return Crocante()

class LactaFactory(IEasterEggs):
    def EasterEgg(self) -> IEasterEggProduct:
        return AoLeite()