import os
os.system("cls")

print("bem vindo")

print("Cardapio da semana")
print("1=Picanha R$25,00")
print("2=Lasanha R$20,00")
print("3=Strogonoff R$18,00")
print("4=Bife acebolado R$15,00")
print("5=Pão com ovo R$5,00")

cardapio =int(input("digite o numero do cardapio:"))

match cardapio:
    case 1:
        print("Picanha R$25,00")
    case 2:
        print("Lasanha R$20,00")
    case 3:
        print("Strogonoff R$18,00")
    case 4:
        print("Bife acebolado R$15,00")
    case 5:
        print("Pão com ovo R$5,00")
    case _:
        ("Obrigado pela preferencia!")
