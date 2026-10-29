import os
os.system("cls")

lista_serie= []
while True:
    #LIMPA O TERMINAL.
    os.system("cls")
    #menu do programa
    print("=Cinema=")
    print("1- cadastrar series")
    print("2- lista de series")
    print("3- sair")

    opcao=int(input("Escolha uma opção:"))
    match opcao:
        case 1:
            print("=Cadastrar filme=")
            nome=input("Novo filme:").strip().upper()
            if nome == "":
                print("o nome não pode fica vazio.")
            elif nome in lista_serie:
                print(f"{nome} ja esta cadastrado")
            #append()adiciona o produto na lista.
            else:
                lista_serie.append(nome)
                print("filme cadastrado com sucesso")
            input("pressione uma tecla para cutinuar")

        case 2:
            print("\n =Lista todos os filmes=")
            if len(lista_serie)==0:
                print("estoque vazio")
            for i, filmes in enumerate(lista_serie):
                print(f"{i+1}. {filmes}")
                #len(lista_filmes) mostra a quantidade de filmes na lista
                print(f"total de filmes: {len(lista_serie)}")
            input("pressione uma tecla para cutinuar")

        case 0:
            print("fim do progama")
            input("pressione uma tecla para cutinuar")
            break
        case _:
            print=("opção invalida")
            input("pressione uma tecla para cutinuar")

