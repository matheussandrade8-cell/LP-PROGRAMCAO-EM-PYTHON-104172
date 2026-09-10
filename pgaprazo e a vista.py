import os
os.system("cls")

valor = float(input("Digite o valor do produto: R$ "))
print("==Selecione a forma de pagamento")
print       ("1-Pagamento a vista")
print       ("2-Pagamento a prazo")
opcao = int(input("Digite a opção do pagamento:"))
match opcao:
    case 1:
        Desconto=valor*0.10
        total=valor - Desconto
        print(f"{valor} do produto")
        print("Forma de pagamento: à vista")
        print(f"Valor do {Desconto:} R$ ")
        print(f"{total} a pagar: R$ ")

    case 2:
        Parcelas=int(input("digite a quantidade de parcelas (1 a 6)"))
        if 1 <= Parcelas <= 6:
            valor_parcela = valor / Parcelas
            print(f"{valor} do produto: R$")
            print("forma de pagamento: á prazo")
            print("quantidade de parcelas", Parcelas)
            print(f"valor da parcela:{valor_parcela}")
            print(f"total á prazo: R${valor}")

        else:
            print("Quantidade de parcelas inválida! Escolha de 1 a 6.")
    case _:
        print("opção de pagamento invalido!")
