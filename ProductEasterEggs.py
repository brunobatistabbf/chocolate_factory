from IProductFactory import IEasterEggProduct

#NESTLE
class Alpino(IEasterEggProduct):
    def ShowInfo(self):
        print("ALPINO")
        print("Marca: Nestle")
        print("Peso: 337g")
        print("Validade: 8 meses")
        print("Preço: R$ 69,99")
    def CodigoProduto(self):
        return 101

class Classic(IEasterEggProduct):
    def ShowInfo(self):
        print("CLASSIC")
        print("Marca: Nestle")
        print("Peso: 300g")
        print("Validade: 12 meses")
        print("Preço: R$ 59,99")

    def CodigoProduto(self):
        return 102

class KitKat(IEasterEggProduct):
    def ShowInfo(self):
        print("KIT KAT")
        print("Marca: Nestle")
        print("Peso: 312g")
        print("Validade: 6 meses")
        print("Preço: R$ 70,90")

    def CodigoProduto(self):
        return 103

class Bis(IEasterEggProduct):
    def ShowInfo(self):
        print("BIS")
        print("Marca: Nestle")
        print("Peso: 200g")
        print("Validade: 10 meses")
        print("Preço: R$ 39,99")
    def CodigoProduto(self):
        return 110

#GAROTO
class Crocante(IEasterEggProduct):
    def ShowInfo(self):
        print("CROCANTE")
        print("Marca: Garoto")
        print("Peso: 215g")
        print("Validade: 7 meses")
        print("Preço: R$ 68,94")

    def CodigoProduto(self):
        return 104

class Talento(IEasterEggProduct):
    def ShowInfo(self):
        print("Talento")
        print("Marca: Garoto")
        print("Peso: 290g")
        print("Validade: 12 meses")
        print("Preço: R$ 90,00")

    def CodigoProduto(self):
        return 105

class BatonAoLeite(IEasterEggProduct):
    def ShowInfo(self):
        print("BATON AO LEITE")
        print("Marca: Garoto")
        print("Peso: 172g")
        print("Validade: 3 meses")
        print("Preço: R$ 45,00")

    def CodigoProduto(self):
        return 106

class Caribe(IEasterEggProduct):
    def ShowInfo(self):
            print("Caribe")
            print("Marca: Garoto")
            print("Peso: 300g")
            print("Validade: 12 meses")
            print("Preço: R$ 69,90")

    def CodigoProduto(self):
            return 111

#LACTA
class AoLeite(IEasterEggProduct):
    def ShowInfo(self):
        print("AO LEITE")
        print("Marca: Lacta")
        print("Peso: 170g")
        print("Validade: 3 meses")
        print("Preço: R$ 58,90")

    def CodigoProduto(self):
        return 107

class Oreo(IEasterEggProduct):
    def ShowInfo(self):
        print("OREO")
        print("Marca: Lacta")
        print("Peso: 257g")
        print("Validade: 5 meses")
        print("Preço: R$ 60,30")
    def CodigoProduto(self):
        return 108

class SonhoDeValsa(IEasterEggProduct):
    def ShowInfo(self):
        print("SONHO DE VALSA")
        print("Marca: Lacta")
        print("Peso: 277g")
        print("Validade: 6 meses")
        print("Preço: R$ 64,00")

    def CodigoProduto(self):
        return 109

class OuroBranco(IEasterEggProduct):
    def ShowInfo(self):
            print("OURO BRANCO")
            print("Marca: Lacta")
            print("Peso: 310g")
            print("Validade: 8 meses")
            print("Preço: R$ 49,92")

    def CodigoProduto(self):
            return 112

#HERSHEY
class Hersheys1(IEasterEggProduct):
    def ShowInfo(self):
        print("HERSHEYS")
        print("Marca: Hersheys")
        print("Peso: 137g")
        print("Validade: 4 meses")
        print("Preço: R$ 79,98")

    def CodigoProduto(self):
        return 113

class Hersheys2(IEasterEggProduct):
    def ShowInfo(self):
        print("HERSHEYS")
        print("Marca: Hersheys")
        print("Peso: 225g")
        print("Validade: 6 meses")
        print("Preço: R$ 89,30")
    def CodigoProduto(self):
        return 114

class Hersheys3(IEasterEggProduct):
    def ShowInfo(self):
        print("HERSHEYS")
        print("Marca: Hersheys")
        print("Peso: 336g")
        print("Validade: 8 meses")
        print("Preço: R$ 98,90")

    def CodigoProduto(self):
        return 115

#FERREIRO
class FerreiroRocher1(IEasterEggProduct):
    def ShowInfo(self):
        print("FERREIRO ROCHER")
        print("Marca: Ferreiro")
        print("Peso: 137g")
        print("Validade: 5 meses")
        print("Preço: R$ 79,45")

    def CodigoProduto(self):
        return 116

class FerreiroRocher2(IEasterEggProduct):
    def ShowInfo(self):
        print("FERREIRO ROCHER")
        print("Marca: Ferreiro")
        print("Peso: 225g")
        print("Validade: 7 meses")
        print("Preço: R$ 99,30")
    def CodigoProduto(self):
        return 117

class FerreiroRocher3(IEasterEggProduct):
    def ShowInfo(self):
        print("FERREIRO ROCHER")
        print("Marca: Ferreiro")
        print("Peso: 336g")
        print("Validade: 12 meses")
        print("Preço: R$ 105,90")

    def CodigoProduto(self):
        return 118















