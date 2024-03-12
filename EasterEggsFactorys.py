from IEasterEggs import IEasterEggs
from IProductFactory import IEasterEggProduct
from ProductEasterEggs import Alpino, Crocante, AoLeite, Classic, KitKat, Talento, BatonAoLeite, Oreo, SonhoDeValsa, Bis, Caribe, OuroBranco, Hersheys1, Hersheys2, Hersheys3, FerreiroRocher1, FerreiroRocher2, FerreiroRocher3

class NestleFactory(IEasterEggs):
    def EasterEgg(self) -> IEasterEggProduct:
        return Alpino()
    def EasterEgg2(self) -> IEasterEggProduct:
        return Classic()
    def EasterEgg3(self) -> IEasterEggProduct:
        return KitKat()
    def EasterEgg4(self) -> IEasterEggProduct:
        return Bis()
class GarotoFactory(IEasterEggs):
    def EasterEgg(self) -> IEasterEggProduct:
        return Crocante()
    def EasterEgg2(self) -> IEasterEggProduct:
        return Talento()
    def EasterEgg3(self) -> IEasterEggProduct:
        return BatonAoLeite()
    def EasterEgg4(self) -> IEasterEggProduct:
        return Caribe()
class LactaFactory(IEasterEggs):
    def EasterEgg(self) -> IEasterEggProduct:
        return AoLeite()
    def EasterEgg2(self) -> IEasterEggProduct:
        return Oreo()
    def EasterEgg3(self) -> IEasterEggProduct:
        return SonhoDeValsa()
    def EasterEgg4(self) -> IEasterEggProduct:
        return OuroBranco()
class HersheysFactory(IEasterEggs):
    def EasterEgg(self) -> IEasterEggProduct:
        return Hersheys1()
    def EasterEgg2(self) -> IEasterEggProduct:
        return Hersheys2()
    def EasterEgg3(self) -> IEasterEggProduct:
        return Hersheys3()

class FerreiroFactory(IEasterEggs):
    def EasterEgg(self) -> IEasterEggProduct:
        return FerreiroRocher1()
    def EasterEgg2(self) -> IEasterEggProduct:
        return FerreiroRocher2()
    def EasterEgg3(self) -> IEasterEggProduct:
        return FerreiroRocher3()