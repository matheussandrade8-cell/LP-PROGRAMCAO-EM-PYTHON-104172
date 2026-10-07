import os
os.system("cls")

total_familias = 0
soma_salarios = 0
soma_filhos = 0
maior_salario = 0
menor_salario = 0

while True:
    print("\n   Menu   ")
    print("1 - Adiconar familia")
    print("2 - Sair e exebir resultado")

    opcao=int(input("digite uma opoção: "))

    if opcao ==1:
        salario=float(input("digite o salario: "))
        filhos=int(input("digite o numero de filhos: "))

        total_familias += 1
        soma_salarios += salario
        soma_filhos += filhos

        # Primeira família
        if total_familias == 1:
            maior_salario = salario
            menor_salario = salario

        else:
            if salario > maior_salario:
                maior_salario = salario

            if salario < menor_salario:
                menor_salario = salario

    elif opcao == 2:
        if total_familias == 0:
            print("\nNenhuma família foi cadastrada.")
        else:
            media_salario = soma_salarios / total_familias
            media_filhos = soma_filhos / total_familias

            print("\n--- RESULTADOS ---")
            print(f"Total de famílias:{total_familias}")
            print(f"Média dos salários: R${media_salario}")
            print("Média de filhos:", media_filhos)
            print("Maior salário: R$", maior_salario)
            print("Menor salário: R$", menor_salario)

        break

    else:
        print("Opção inválida!")