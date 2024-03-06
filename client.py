import IEasterEggs
from EasterEggsFactorys import NestleFactory, GarotoFactory, LactaFactory
def Client(factory: IEasterEggs) -> None:
    if isinstance(factory, NestleFactory):
        OvodePascoa = factory.EasterEgg()
        print(f"{OvodePascoa.ShowInfo()}")
    elif isinstance(factory, GarotoFactory):
        OvodePascoa = factory.EasterEgg()
        print(f"{OvodePascoa.ShowInfo()}")
    elif isinstance(factory, LactaFactory):
        OvodePascoa = factory.EasterEgg()
        print(f"{OvodePascoa.ShowInfo()}")
    else:
        print("ERROR")


if __name__ == '__main__':
    print("<<---AQUISIÇÃO DE OVO DE PASCOA--->>")
    print("Primeira Fabrica: Nestle")
    Client(NestleFactory())
    print("Segunda Fabrica: Garoto")
    Client(GarotoFactory())
    print("Terceira Fabrica: Lacta")
    Client(LactaFactory())