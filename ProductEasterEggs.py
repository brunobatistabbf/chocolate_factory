from IProductFactory import IEasterEggProduct

#NESTLE
class Alpino(IEasterEggProduct):
    def ShowInfo(self):
        print("ALPINO")
        print("Marca: Nestle")
        print("Peso: 337g")
        print("Validade: 8 meses")
        print("Preço: R$ 69,99")

class Clasic(IEasterEggProduct):
    def ShowInfo(self):
        print("CLASSIC")
        print("Marca: Nestle")
        print("Peso: 300g")
        print("Validade: 12 meses")
        print("Preço: R$ 59,99")

class KitKat(IEasterEggProduct):
    def ShowInfo(self):
        print("KIT KAT")
        print("Marca: Nestle")
        print("Peso: 312g")
        print("Validade: 6 meses")
        print("Preço: R$ 70,90")

#GAROTO
class Crocante(IEasterEggProduct):
    def ShowInfo(self):
        print("CROCANTE")
        print("Marca: Garoto")
        print("Peso: 215g")
        print("Validade: 7 meses")
        print("Preço: R$ 68,94")

class Talento(IEasterEggProduct):
    def ShowInfo(self):
        print("Talento")
        print("Marca: Garoto")
        print("Peso: 290g")
        print("Validade: 12 meses")
        print("Preço: R$ 90,00")

class BatonAoLeite(IEasterEggProduct):
    def ShowInfo(self):
        print("BATON AO LEITE")
        print("Marca: Garoto")
        print("Peso: 172g")
        print("Validade: 3 meses")
        print("Preço: R$ 45,00")
#LACTA
class AoLeite(IEasterEggProduct):
    def ShowInfo(self):
        print("AO LEITE")
        print("Marca: Lacta")
        print("Peso: 170g")
        print("Validade: 3 meses")
        print("Preço: R$ 58,90")

class Oreo(IEasterEggProduct):
    def ShowInfo(self):
        print("Oreo")
        print("Marca: Lacta")
        print("Peso: 257g")
        print("Validade: 5 meses")
        print("Preço: R$ 60,30")

class SonhoDeValsa(IEasterEggProduct):
    def ShowInfo(self):
        print("Sonho de Valsa")
        print("Marca: Lacta")
        print("Peso: 277g")
        print("Validade: 6 meses")
        print("Preço: R$ 64,00")
#HERSHEY

#FERREIRO