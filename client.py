import IEasterEggs
from EasterEggsFactorys import NestleFactory, GarotoFactory, LactaFactory
def Client(codigo):
    if(codigo == 101):
        OvoDePascoa = NestleFactory().EasterEgg()
        print(f"\n{OvoDePascoa.ShowInfo()}\n")
    elif(codigo == 102):
        NestleFactory.EasterEgg2()
    elif(codigo == 103):
        NestleFactory.EasterEgg3()



if __name__ == '__main__':
    print("\n<<---AQUISIÇÃO DE OVO DE PASCOA--->>\n")
    aux = True
    while aux:
        resposta = int(input(" Se você deseja consultar digite 1\n Se deseja consultar os códigos/catalogo digite 2\n Se deseja sair digite 3\n"))
        if(resposta == 1):
            codigo = int(input("Insira o código do produto:"))
            Client(codigo)
        elif(resposta == 2):
            print("CATOLOGO")
        elif(resposta == 3):
            print("Obrigado por usar a aplicação")
            aux = False
        else:
            print("Insira uma opção válida!")



