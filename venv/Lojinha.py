import datetime

data = datetime.datetime.now()
mes = data.strftime("%B")

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
        print("Obrigado pela preferencia")
        exit()

def menuEscolha(opcao):
   validaOpcaoCompra(opcao)
   print("Qual a quantidade que deseja comprar?")
   quantidade = int(input())
   if(opcao == 1):
       valorCompra = espingarda * quantidade
       venda = "Você comprou " + str(quantidade) + " unidades de Espingarda 22 com o total de R$" + str(valorCompra) + "."
       salvaCompra(venda)
       print(venda)
   elif(opcao == 2):
       valorCompra = arco * quantidade
       venda = "Você comprou " + str(quantidade) + " unidades de Arco e Flecha com o total de R$" + str(valorCompra) + "."
       salvaCompra(venda)
       print(venda)
   elif(opcao == 3):
       valorCompra = batatinha * quantidade
       venda = "Você comprou " + str(quantidade) + " unidades de 38 batatinha com o total de R$" + str(valorCompra) + "."
       salvaCompra(venda)
       print(venda)
   elif (opcao == 4):
       valorCompra = garrucha * quantidade
       venda = "Você comprou " + str(quantidade) + " unidades de Garrucha com o total de R$" + str(valorCompra) + "."
       salvaCompra(venda)
       print(venda)
   elif (opcao == 5):
       valorCompra = doze * quantidade
       venda = "Você comprou " + str(quantidade) + " unidades de  12 com o total de R$" + str(valorCompra) + "."
       salvaCompra(venda)
       print(venda)
   continuarCompra()
   exit()

def imprimeRelatorio():
    print("IMPRIMINDO...")
    arq = open(mes + ".txt", "a")
    arq = open(mes + ".txt", "r")
    texto = arq.readlines()
    print(texto)
    arq.close()
    exit()

def salvaCompra(venda):
    arq = open(mes + ".txt", "a")
    arq.write(venda)
    arq.write("\r")

menu()


