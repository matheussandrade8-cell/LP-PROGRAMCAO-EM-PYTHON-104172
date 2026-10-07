import os
os.system("cls")


soma_salario = 0
quantidade = 0
maior_idade = 0
menor_idade = 0
mulheres = 0

while True:
    print("1 - Adicionar pessoa")
    print("2 - Exibir resultados")
    print("3 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        idade = int(input("Idade: "))
        sexo = input("Sexo (M/F): ")
        salario = float(input("Salário: "))

        soma_salario = soma_salario + salario
        quantidade = quantidade + 1

        if quantidade == 1:
            maior_idade = idade
            menor_idade = idade
        else:
            if idade > maior_idade:
                maior_idade = idade

            if idade < menor_idade:
                menor_idade = idade

        if sexo == "F" and salario >= 5000:
            mulheres = mulheres + 1

    elif opcao == 2:
        if quantidade > 0:
            media = soma_salario / quantidade

            print(f"Média salarial:{media}")
            print(f"Maior idade:{maior_idade}")
            print(f"Menor idade:{maior_idade}")
            print(f"Mulheres com salário >= 5000: {mulheres}")
        else:
            print("Nenhuma pessoa cadastrada.")

    elif opcao == 3:
        break

    else:
        print("Opção inválida")