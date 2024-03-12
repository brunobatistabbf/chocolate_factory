import IEasterEggs
from EasterEggsFactorys import NestleFactory, GarotoFactory, LactaFactory, HersheysFactory, FerreiroFactory


def Client(codigo):
    if(codigo == 0):
        print("---------- Códigos Disponiveis ------------")
        print("\nNestle:")
        print(NestleFactory().EasterEgg().CodigoProduto())
        print(NestleFactory().EasterEgg2().CodigoProduto())
        print(NestleFactory().EasterEgg3().CodigoProduto())
        print(NestleFactory().EasterEgg4().CodigoProduto())
        print("\nGaroto:")
        print(GarotoFactory().EasterEgg().CodigoProduto())
        print(GarotoFactory().EasterEgg2().CodigoProduto())
        print(GarotoFactory().EasterEgg3().CodigoProduto())
        print(GarotoFactory().EasterEgg4().CodigoProduto())
        print("\nLactea:")
        print(LactaFactory().EasterEgg().CodigoProduto())
        print(LactaFactory().EasterEgg2().CodigoProduto())
        print(LactaFactory().EasterEgg3().CodigoProduto())
        print(LactaFactory().EasterEgg4().CodigoProduto())
        print("\nHershey:")
        print(HersheysFactory().EasterEgg().CodigoProduto())
        print(HersheysFactory().EasterEgg2().CodigoProduto())
        print(HersheysFactory().EasterEgg3().CodigoProduto())
        print("\nFerreiro:")
        print(HersheysFactory().EasterEgg().CodigoProduto())
        print(HersheysFactory().EasterEgg2().CodigoProduto())
        print(HersheysFactory().EasterEgg3().CodigoProduto())
        print("-----------------------------------------")
    elif(codigo == 101):
        OvoDePascoa = NestleFactory().EasterEgg()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    elif(codigo == 102):
        OvoDePascoa = NestleFactory().EasterEgg2()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    elif(codigo == 103):
        OvoDePascoa = NestleFactory().EasterEgg3()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    elif(codigo == 110):
        OvoDePascoa = NestleFactory().EasterEgg4()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    #garoto
    elif(codigo == 104):
        OvoDePascoa = GarotoFactory().EasterEgg()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    elif(codigo == 105):
        OvoDePascoa = GarotoFactory().EasterEgg2()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    elif(codigo == 106):
        OvoDePascoa = GarotoFactory().EasterEgg3()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    elif(codigo == 111):
        OvoDePascoa = GarotoFactory().EasterEgg4()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    #Lactea
    elif(codigo == 107):
        OvoDePascoa = LactaFactory().EasterEgg()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    elif(codigo == 108):
        OvoDePascoa = LactaFactory().EasterEgg2()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    elif(codigo == 109):
        OvoDePascoa = LactaFactory().EasterEgg3()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    elif(codigo == 112):
        OvoDePascoa = LactaFactory().EasterEgg4()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    #Hershey
    elif(codigo == 113):
        OvoDePascoa = HersheysFactory().EasterEgg()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    elif(codigo == 114):
        OvoDePascoa = HersheysFactory().EasterEgg2()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    elif(codigo == 115):
        OvoDePascoa = HersheysFactory().EasterEgg3()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    #Ferreiro
    elif(codigo == 116):
        OvoDePascoa = FerreiroFactory().EasterEgg()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    elif(codigo == 117):
        OvoDePascoa = FerreiroFactory().EasterEgg2()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    elif(codigo == 118):
        OvoDePascoa = FerreiroFactory().EasterEgg3()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    else:
        print("Insira uma opção válida\n")



if __name__ == '__main__':
    print("\n<<---AQUISIÇÃO DE OVOS DE PASCOA--->>\n")
    aux = True
    while aux:
        resposta = int(input(" Se você deseja consultar digite 1\n Se deseja consultar os códigos/catalogo digite 2\n Se deseja sair digite 3\n"))
        if(resposta == 1):
            codigo = int(input("Insira o código do produto:"))
            Client(codigo)
        elif(resposta == 2):
            print("CATOLOGO")
            Client(codigo=0)
        elif(resposta == 3):
            print("Obrigado por usar a aplicação!")
            aux = False
        else:
            print("Insira uma opção válida!")



