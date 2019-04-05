


espingarda = 100
arco = 50
batatinha = 80
garrucha = 75
doze = 150

def menu():
     print("Olá, o que deseja comprar?")
     print("1 - Espingarda 22 R$100,00")
     print("2 - Arco e Flecha R$50,00")
     print("3 - 38 batatinha R$80,00")
     print("4 - Garrucha R$75,00")
     print("5 - 12 R$150,00")
     print("6 - Relatório de compras")
     print("0 - Sair")
     opcao = int (input())
     menuEscolha(opcao)

def validaOpcaoCompra(opcao):
    if (opcao < 0 or opcao > 6):
        print("Opcão inválida ,digite novamente")
        opcao = int(input())
        menuEscolha(opcao)
    elif (opcao == 6):
        imprimeRelatorio()
    elif (opcao == 0):
        print("Obrigado pelas compras")
        exit()

def continuarCompra():
    continuarCompra = int(input("Deseja continuar comprando? 1 - SIM    2 - NÃO "))
    if (continuarCompra == 1):
        menu()
    else:
        exit()

def menuEscolha(opcao):
   validaOpcaoCompra(opcao)
   print("Qual a quantidade que deseja comprar?")
   quantidade = int(input())
   valorCompra = opcao * quantidade
   continuarCompra()
   exit()

def imprimeRelatorio():
    print("IMPRIMINDO...")
    exit()


menu()


