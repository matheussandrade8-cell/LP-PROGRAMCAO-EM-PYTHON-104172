import os
os.system("cls")
total=0.0
print("bem vindo")
vetor_prato=[]
vetor_preco=[]
while True:
    print("Cardapio da semana")
    print("1 - Picanha = R$25,00")
    print("2 - Lasanha = R$20,00")
    print("3 - Strogonoff = R$18,00")
    print("4 - Bife acebolado = R$15,00")
    print("5 - Pão com ovo = R$5,00")

    cardapio =int(input(" Digite o numero do cardapio:"))

    match cardapio:
        case 1:
            prato=("Picanha")
            preço=25.00
        case 2:
            prato=("Lasanha")
            preço=20.00
        case 3:
            prato=("Strogonoff")
            preço=18.00
        case 4:
            prato=("Bife acebolado")
            preço=15.00
        case 5:
            prato=("Pão com ovo")
            preço=5.00
        case _:
            ("Obrigado pela preferencia!")

    if cardapio >=1 and cardapio <=5:
        vetor_prato.append(prato)
        vetor_preco.append(preço)

    continuar= input("Deseja escolher outro prato? \n Responda com s ou n : ").lower()
    if continuar == "n":
        break
    os.system("cls")

    if  sum(vetor_preco) == 0:
        print("Nenhum prato selecionado.")
    else:
        print(" Prato escolhidos ")
        for i, prato in enumerate(vetor_prato, start=1):
            print(f"{i}° prato: {prato}")
        print(f"total: R$ {sum(vetor_preco)}")
    print(" Volte sempre!")